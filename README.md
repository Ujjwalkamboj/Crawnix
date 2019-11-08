# Crawnix

Crawnix is a python tool designed to crawl all the web pages from the website. Cranix uses [Beautiful Soup]() to crawl web pages. It only crawl those webpages which are matching with base url. Crawnix uses url.netloc function for extract the base url and using regular expression it will check for the urls with base url and show on the display. 

# Screenshot
![alt text](https://github.com/Mehra1998/Crawnix/blob/master/screenshot/Screenshot.png)
# Installation

```sh
git clone http://github.com/Mehra1998/Crawnix.git
```

# Recomended Python Version :

Crawnix currently supported Python3.x.
  - The recommended version for Python3 is 3.x

# Dependencies :
Crawnix depends on the [colorama](), [subprocess](), [codecs](), [Beautiful Soup](), [lxml]() python modules.

These dependencies can be installed using the requirements file:
- Installation in Windows:
```sh
c:\python27\python.exe -m pip install -r requirements.txt
```

- Installation on Linux:
```sh
$ sudo pip install -r requirements.txt
```

# Features :
* Crawl all Web Pages with in scope urls.

# Usage :
```sh
$ python3 crawnix.py
```

# License :
Crawnix is licensed under the GNU GPL license. take a look at the  [LICENSE](https://github.com/Mehra1998/Crawnix/blob/master/LICENSE) for more information
