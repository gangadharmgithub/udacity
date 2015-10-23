from urllib.request import urlencode
from urllib.request import urlopen
from urllib.request import getproxies
def read_text():
    f_handle =  open(r"C:\prank\move_quotes.txt.txt", "r")
    quotes = f_handle.read()
    check_profanity(quotes)
    print(quotes)
    f_handle.close();
               
def check_profanity(qu):
    print(getproxies())
    connection = urlopen(r"http://www.wdyl.com/profanity?q="+ urlencode(str(qu)))
    output = connection.read()
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print("This document has no curse words!");
    else:
        print("Please mannualy check for Profanity");
    connection.close()

read_text()
