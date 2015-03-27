'''game page of chess.fallenofftheedge.com'''
if __name__ == '__main__':
    import library as lib
else:
    import webapp.library as lib

lib.print_header()
html = lib.get_html(lib.HTML_DIR + 'game.html')
print(html)
