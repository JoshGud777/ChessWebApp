''''Create users from this page and add them to the data base''' 
if __name__ == '__main__': import library as lib 
else: import webapp.library as lib

import sqlite3

# import os
# os.environ["REQUEST_METHOD"] = "GET"
# os.environ["QUERY_STRING"] = "key=create_user&username=s&password=s&confirm=s&email=joshgud777@gmail.com"
import cgitb
cgitb.enable()

def html_print(returndata='<!--returndata-->'):
    html = lib.get_html(lib.HTML_DIR + 'create.html')
    html = html.replace('$$returndata$$',  returndata)
    print(html)

def main():
    conn, c = lib.open_conn(lib.DB_DIR + 'ChessApp.db')
    form = lib.get_cgi_data()
    if form.getvalue('key') == 'create_user':
        username = form['username'].value
        password = form['password'].value
        confirm = form['confirm'].value
        email = form['email'].value

        if password == confirm:
            resp = lib.add_user(username, password, email, c)
        else:
            resp = 'pwerror'


        if resp == 'exists':
            lib.print_header()
            error = '!!! Invalid Username, User Exists !!!'
            html_print(error)

        elif resp == 'pwerror':
            lib.print_header()
            error = 'Passwords did not match!'
            html_print(error)

        elif resp == 'sqlerror':
            lib.print_header()
            error = 'Internal SQL error. </br> '\
                    'Please e-mail servgud777@gmail.com!'
            html_print(error)

        elif resp is True:
            lib.print_header()
            returndata = '!!! User Created !!!'
            html_print(returndata)

        else:
            lib.print_header()
            error = 'Internal SERVER error. </br> '\
                    'Please e-mail servgud777@gmail.com!'
            html_print(error)

    else:
        lib.print_header()
        html_print()

    lib.save_close_conn(conn)


if __name__ == '__main__':
    main()
