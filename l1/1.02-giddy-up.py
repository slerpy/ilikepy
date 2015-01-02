# __author__ = 'shaden'
#
# #
# # getting into doing actual stuff. maybe it'll hold my adhd ridden interests :D
# # slerping links from pages.
# #
# page=('<div id="top_bin"><div id="top_content" class="width960">''<div class="udacity float-left"><a href="http://udacity.com">')
# start_link=page.find("<a href=")
# end_link=page.find('>',start_link)
# link=page[start_link:end_link]
# link=link[9:]
# link=link[:-1]
# print start_link
# print end_link
# print link
#
# #above works, seems they want a different method so ill play along.
# #
# page=('<div id="top_bin"><div id="top_content" class="width960">''<div class="udacity float-left"><a href="http://udacity.com">')
# start_link=page.find("<a href=")
# start_quote=page.find('"',start_link)
# end_quote=page.find('"',start_quote+1)
# print start_quote
# print end_quote
# url=page[start_quote+1:end_quote]
# print url

# above worked as well, commented out so i dont lose it.
#

page=('<html xmlns="http://www.w3.org/1999/xhtml"><head><title>Udacity</title></head><body><h1>Udacity</h1><p><b>Udacity</b> is a private institution of<a href="http://www.wikipedia.org/wiki/Higher_education">higher education founded by</a> <a href="http://www.wikipedia.org/wiki/Sebastian_Thrun">Sebastian Thrun</a>, David Stavens, and Mike Sokolsky with the goal to provide university-level education that is "both high quality and low cost".</p>  <p> It is the outgrowth of a free computer science class offered in 2011 through Stanford University. Currently, Udacity is working on its second course on building a search engine. Udacity was announced at the 2012 <a href="http://www.wikipedia.org/wiki/Digital_Life_Design">Digital Life Design</a> conference.</p>     </body></html>')

start_link=page.find("<a href=")
start_quote=page.find('"',start_link)
end_quote=page.find('"',start_quote+1)
url=page[start_quote+1:end_quote]
print url

start_link=page.find("<a href=",end_quote)
start_quote=page.find('"',start_link)
end_quote=page.find('"',start_quote+1)
url=page[start_quote+1:end_quote]
print url

start_link=page.find("<a href=",end_quote)
start_quote=page.find('"',start_link)
end_quote=page.find('"',start_quote+1)
url=page[start_quote+1:end_quote]
print url

#
# round and round we go. i totally cheaterfaced and looked up the .5 part.
# all code after lightbulbing on the rounding bits totally did not cheat.
# p.s. the dopamine shot from lightbulbing on a concept is quite lovely.
#

x = 5.64159
y = str(x + .5)
dec = y.find(".")
x = y[:dec]
print x

#
# and that my friends is the end of the first chapter of many in our adventures.
#
# fin
