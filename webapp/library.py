'''This is the library files for all used code that needs to be
used multi times'''
import binascii
import cgi
import hashlib
import http.cookies
import os
import sqlite3
import time
import cgitb
cgitb.enable()

HTML_DIR = 'html\\'
REDIRECT_DIR = 'redirect\\'
DB_DIR = 'db\\'
COOKIE_MAX_AGE = 300
# COOKIE_DOMAIN = 'applequest.fallenofftheedge.com'
COOKIE_PATH = '/'


def open_conn(database):
    '''Open SQL Connection to a given sqlite databsase'''
    conn = sqlite3.connect(database)
    c = conn.cursor()
    return (conn, c)


def save_conn(conn):
    '''Savesthe conn'''
    conn.commit()


def save_close_conn(conn):
    '''Saves and closes the conn'''
    conn.commit()
    conn.close()


def close_conn(conn):
    '''Closes the database conn'''
    conn.close()


def add_user(username, pword, email, c):
    '''For a givven username and pasword and maybe an e-mail. Adds the user to
    the database. If the user is allready there then it returns false. if it
    added the database it sends True'''
    display = username[:]
    username = username.lower()

    salt = binascii.hexlify(os.urandom(64))  # 64 bytes = 512 bits
    utf8pword = pword.encode("utf-8")
    utf8pword_salt = utf8pword + salt

    hashed_salted_password = hashlib.sha512(utf8pword_salt)
    enchexpass = hashed_salted_password.hexdigest()
    try:
        c.execute("INSERT INTO logon VALUES (?, ?, ?, ?, ?)", (username,
                                                               display,
                                                               enchexpass,
                                                               salt, email))
    except sqlite3.IntegrityError:
        return 'exists'

    except:
        return 'sqlerror'

    return True


def issue_session_id(username, pword, c):
    '''issues a session id for a given username, checks the user and pass
    agenst the db then sends back a sessionif, epx, and theusername it is sent
    agenst | noauth means username and password is wrrong | sqlerror means the
    server is haveing issues'''
    username = username.lower()
    authuser = check_user(username, pword, c)
    if authuser is True:

        sqlretry = 0
        sqlgood = False
        while sqlgood is False:
            # c.execute("SELECT * FROM logon WHERE username = ?", [username])
            # dbdata = c.fetchone()
            # db_username = dbdata[0]
            # db_display = dbdata[1]

            exp = int(time.time()) + 300
            # seconds till this is expired | 300 = 5 min | 1 = 1 sec
            sessionid = binascii.hexlify(os.urandom(16)).decode("utf-8")

            try:
                c.execute("DELETE FROM sessions WHERE username = ?",
                          [username])
                c.execute("INSERT INTO sessions VALUES (?, ?, ?)",
                          [sessionid, exp, username])
                sqlgood = True
            except:
                sqlretry += 1
                if sqlretry == 10:
                    return ('sqlerror', 'sqlerror', 'sqlerror')

        return (sessionid, exp, username)

    return ('noauth', 'noauth', 'noauth')


def renew_session_id(old_id, username, c):
    '''givven the old session id and username it checks that the session is
    is still good then send a newone if OK, else it sends out a "s qlerror" in
    the case the server is erroring and a "expired" if the session is old'''
    username = username.lower()
    c.execute("SELECT * FROM sessions WHERE username =  ? AND id = ?",
              [username, old_id])
    dbdata = c.fetchone()
    if dbdata is None:
        return False
    db_exp = int(dbdata[1])

    if int(time.time()) > db_exp:
        return 'expired'
    elif int(time.time()) <= db_exp:
        sqlgood = False
        sqlretry = 0
        while sqlgood is False:
            exp = int(time.time()) + 300
            # secontill this is expired | 300 = 5 min | 1 = 1 sec
            sessionid = binascii.hexlify(os.urandom(16)).decode("utf-8")
            try:
                c.execute("DELETE FROM sessions WHERE username = ?",
                          [username])
                c.execute("INSERT INTO sessions VALUES (?, ?, ?)",
                          [sessionid, exp, username])
                sqlgood = True
            except sqlite.Error:
                sqlretry += 1
                if sqlretry == 10:
                    return 'sqlerror'

        return (sessionid, exp, username)


def delete_session(sessionid, username, c):
    '''deletes a session from the database in the case the client wants to
    "logoff"'''
    username = username.lower()
    c.execute("SELECT * FROM sessions WHERE username = ? OR id = ?",
              [username, sessionid])
    dbdata = c.fetchone()
    if dbdata is None:
        return False

    c.execute("DELETE FROM sessions WHERE username = ? OR id = ?",
              [username, sessionid])
    return True


def check_user(username, pword, c):
    '''checks the username and password agenst the data base loaded with the
    open_conn(), returns True is they are correct'''
    username = username.lower()
    c.execute("SELECT username, password, salt FROM logon WHERE username = ?",
              [username])
    dbdata = c.fetchone()

    if dbdata is None:
        return None

    enchexpassdb = dbdata[1]

    salt = dbdata[2]
    utf8pword = pword.encode('utf8')
    utf8pword_salt = utf8pword + salt

    hashed_salted_password = hashlib.sha512(utf8pword_salt)
    enchexpass = hashed_salted_password.hexdigest()

    if slow_equal(enchexpassdb, enchexpass):
        return True
    else:
        return False


def slow_equal(hexstrA, hexstrB):
    '''TODO : make the compair bit for bit in binary using XNOR OR SOMETHING
    Instead of comparing the string with == it checkes each part on at a
    time, this makes it slower and therefor harder to crack.'''
    length = 0
    errors = 0

    a = ''.join(format(ord(char), 'b') for char in hexstrA)
    b = ''.join(format(ord(char), 'b') for char in hexstrB)

    if len(a) == len(b):
        length = len(a)
    else:
        time.sleep(1)
        length = 0
        errors = 1000

    for i in range(length):
        errors += int(a[i]) ^ int(b[i])

    if errors == 0:
        return True
    else:
        return False


def cookie_wright(sessionid, exp, username):
    '''give the imput data it returns a session cookie ment to be placed in the
    print_header function to send to the client'''
    cookie = http.cookies.BaseCookie()
    cookie['id'] = sessionid
    cookie['exp'] = exp
    cookie['username'] = username
    for morsel in cookie:
        cookie[morsel]['max-age'] = COOKIE_MAX_AGE
        # cookie[morsel]['domain'] = COOKIE_DOMAIN
        cookie[morsel]['path'] = COOKIE_PATH
    return cookie


def get_cookies():
    '''returns a cookie opject of the request header sent to the server from
    the client'''
    cookie = http.cookies.BaseCookie()
    if 'HTTP_COOKIE' in os.environ:
        cookie.load(os.environ['HTTP_COOKIE'])
        return cookie
    return None


def print_header(cookie=''):
    '''Prints the standard HTTP header needed by CGI along with any cookie data
    sent to the function - cookie must be a cookie object'''
    print('Content-type: text/html')
    print('Status: 200 OK')
    print(cookie)
    if not cookie == '':
        print()


def get_html(filepath):
    '''For the given path it returns a str of all the data in that file.
    \n and all'''
    file = open(filepath)
    txt = file.read()
    return txt


def print_me(filename):
    '''prints file to screen - use for redirects'''
    file = open(filename)
    txt = file.read()
    print(txt)


def get_cgi_data():
    '''gets the cgi data from the last form the client summited'''
    cgidata = cgi.FieldStorage()
    return cgidata
