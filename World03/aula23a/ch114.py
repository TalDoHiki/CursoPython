import urllib.request
try:
    urllib.request.urlopen('http://pudim.com.br')
except:
    print('\033[31mCould not access the site.\033[m')
else:
    print('\033[32mConnection established\033[m')
