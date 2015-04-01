'''game page of chess.fallenofftheedge.com'''
if __name__ == '__main__':
    import library as lib
else:
    import webapp.library as lib

enable_script = 1

# import os
# os.environ["REQUEST_METHOD"] = "GET"
# os.environ["QUERY_STRING"] = "key=create_user"

def html_print(userlist):
    html = lib.get_html(lib.HTML_DIR + 'game.html')
    optionlist = ''
    for user in userlist:
        username = user[0]
        display = user[1]

        option = '<option value="' + username + '">' + display + '</option>\n'
        optionlist += option

    html = html.replace('$$users$$$', optionlist)
    print(html)

def main():
    conn, c = lib.open_conn(lib.DB_DIR + 'ChessApp.db')

    html = lib.get_html(lib.HTML_DIR + 'game.html')
    c.execute("SELECT username, display FROM logon")
    dbdata = c.fetchall()

    lib.print_header()
    html_print(dbdata)

    lib.close_conn(conn)

if __name__ == '__main__':
    if enable_script == False:
        lib.print_header()
        print("Script Offline! Email 'servgud777@gmail.com' for info.")
    else:
        main()
