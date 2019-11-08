from urllib.request import urlparse
import re

def clean(url):
    # Deal with "http(s)://"
    if url[0:4] != "http":
        url = "http://" + url

    # Deal with "#"
    idx = url.find('#')
    if idx != -1:
        url = url[:idx]

    # Deal with last "/"
    l = len(url)
    if url[l - 1] == '/':
        url = url[:l - 1]

    return url

def get_domain(url):
    parsed_url = urlparse(url)
    return "{url.netloc}".format(url=parsed_url)


def valid(url, domain):
    if re.match(r'^https?://([\w-]*\.)?' + domain + r'.*$', url, re.M|re.I):
        return True
    else:
        return False
