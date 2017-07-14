import urllib

def read_text():
     quotes = open("/Users/pawan/Documents/Udacity/Python/movie_quotes/movie_quotes.txt")
     content_of_file  = quotes.read()
     print content_of_file
     quotes.close()
     check_profanity(content_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print "Profanity alert!"
    elif "false" in output:
        print "This document has not curse words!"
    else:
        print "Could not scan the document properly"


read_text()
