'''index page of applequest.fallenofftheedge.com'''
if __name__ == '__main__':
    import library as lib
else:
    import webapp.library as lib


def html():
    html = lib.get_html(lib.HTML_DIR + 'index.html')
    print(html)


def main():
    lib.print_header()
    html()


if __name__ == '__main__':
    main()
