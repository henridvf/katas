from urllib.parse import urlparse

def domain_name(url):
    if '//' in url:
        parsed = urlparse(url).hostname.split('.')
        return parsed[1] if 'www' in url else parsed[0]
    else:
        split = url.split('.')
        return split[1] if 'www' in url else split[0]

print(domain_name('http://google.com'))