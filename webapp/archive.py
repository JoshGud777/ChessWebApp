if __name__ == '__main__': import library as lib
else: import webapp.library as lib

enable_script = 1

# import os
# os.environ["REQUEST_METHOD"] = "GET
# os.environ["QUERY_STRING"] = "data=data"

import cgitb
cgitb.enable()


def print_html(dbdata):
    html = lib.get_html(lib.HTML_DIR + 'archive.html')
    tabledata = ''
    for row in dbdata:
        tabledata += '<tr>\n'
        for item in row:
            if item == None:
                item = ''
            tabledata += '  ' + '<td>' + str(item) + '</td>\n'
        tabledata  += '</tr>\n'
    html = html.replace('$$tabledata$$', tabledata)
    print(html)



def main():
    conn, c = lib.open_conn(lib.DB_DIR + 'ChessApp.db')
    c.execute("SELECT timestamp, userwin, userloss,\
commentwin, commentloss,draw FROM archive")
    data = c.fetchall()

    lib.print_header()
    print_html(data)

    lib.close_conn(conn)






if __name__ == '__main__':
    if enable_script is False:
        lib.print_header()
        print("Script Offline! Email 'servgud777@gmail.com' for info.")
    else:
        main()
