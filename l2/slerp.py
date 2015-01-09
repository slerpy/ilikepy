__author__ = 'shaden'
###
# my new slerping code, hope it works in the end!
###
# from urllib.request import urlopen
# def get_page(url):
#    try:
#        return str(urlopen(url).read())
#    except:
#        return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

url, endpos = get_next_target('page test <a href="http://www.test.com">linkage</a>')
print url


def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break
# print_all_links('this is a test. it is only a test <a href="http://www.test.com">test 1</a><a href="http://www.test2.com">test 2</a><a href="http://test3.com">test 3</a>')
#print_all_links(get_page('http://xkcd.com/353'))



