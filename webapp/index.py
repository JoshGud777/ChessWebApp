'''index page of applequest.fallenofftheedge.com'''
if __name__ == '__main__':
    import library as lib
else:
    import webapp.library as lib


def html_p():
    '''docstring'''
    html = lib.get_html(lib.HTML_DIR + 'index.html')
    print(html)


def main():
    '''docstring'''
    lib.print_header()
    html_p()


if __name__ == '__main__':
    main()
