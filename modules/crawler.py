from urllib.request import urlopen, urlparse
from bs4 import BeautifulSoup
import codecs, lxml, os
from modules import helper
import win_unicode_console , colorama

width = os.get_terminal_size().columns

# Windows deserves coloring too :D
G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\33[97m'  # white

try:
    pages = set()
    url = input("%s\t\t\tExample :- %szugtech.com (or) http://zugtech.com/%s\n\n\n[*] Enter the URL >> %s"%(Y,G,W,R))
    print('%s_'%(W) * width)

    def getLinks(pageUrl):
        global pages
        clean = helper.clean(url)
        domain = helper.get_domain(clean)
        html = urlopen(clean)
        bsObj = BeautifulSoup(html, "lxml")
        for link in bsObj.findAll("a"):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                #We have encountered a new page
                    newPage = link.attrs['href']
                    if helper.valid(newPage, domain):
                        pages.add(newPage)
                        print("%s>> %s"%(W,G), newPage)

                        os.chdir('.')
                        file = codecs.open("directory/links.txt", "w", "utf-8")
                        for result in pages:
                            file.write(result)
                            file.write("\n")
                        file.close()

                        getLinks(newPage)

    getLinks("")

except Exception as e:
    print("%s[-] Something gonna wrong! Please Restart the application."%(R))