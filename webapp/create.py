''''Create users from this page and add them to the data base'''
if __name__ == '__main__': import library as lib
else: import webapp.library as lib

enable_script = 0

# import os
# os.environ["REQUEST_METHOD"] = "GET"
# os.environ["QUERY_STRING"] = "key=create_user"

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
        username = form.getvalue('username')
        password = form.getvalue('password')
        confirm = form.getvalue('confirm')
        email = form.getvalue('email')

        if username is None or password is None or confirm is None or\
        email is None:
            resp = 'NoneError'
        elif password == confirm:
            resp = lib.add_user(username, password, email, c)
        else:
            resp = 'pwerror'

        if resp == 'NoneError':
            lib.print_header()
            error = 'Please fill in all the fields'
            html_print(error)

        elif resp == 'exists':
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
    if enable_script == False:
        lib.print_header()
        print("Script Offline! Email 'servgud777@gmail.com' for info.")
    else:
        main()
