# Given a variable page which contains the contents of a web page( the HTML code )
# Find the first link

page = "<html><head><title>EL</title></head><body><a href='www.google.com'>Google</a><br/><a href='www.fb.com'>Facebook</a></body></html>"
linkString = "<a href="
startLink = page.find( linkString ) + 9
endLink = page.find( "'>" )
link = page[ startLink : endLink ]
print link
