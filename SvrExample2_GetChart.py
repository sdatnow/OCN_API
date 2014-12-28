
# OCN code snippet for customer server
# Must be hosted on customer web server
# Get a URL to launch a live version of OCN
# Version 1.0

import cgi, cgitb
import sys
import os
import urllib
import urllib2

def main():
    result = None
    filename = None
    directory = None

    form = cgi.FieldStorage()
    filename = form.getvalue('filename')
    directory = form.getvalue('directory')
    mode = form.getvalue('mode')
 
    try:
        # Link to server where customer's tenant is located
        url = 'http://localhost:82/ServerSide/OCN_GetChart.py'
        # Specify user, MD5(password) and org name
        values = {'org' : 'acme', 'user' : 'sdatnow', 'pass' : 'cc03e747a6afbbcbf8be7668acfebee5' }
        
        # If PDF file name not specified via URL Parameter
        if (filename == None):
            filename = 'test.oc5'
        if (directory == None):
            directory = 'Portal'
        if (mode == None):
            mode = 'portal'

        values['filename'] = filename
        values['directory'] = directory
        values['mode'] = mode
         
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        result = response.read()
        
        print "Status: 302" 
        print "Location: " + result
        print
        #print "Status: 200 OK" 
        #print "Content-Type: text/html;charset=utf-8" 
        #print
        #sys.stdout.write(result)
    except:
        print "Status: 404 Not Found", "\n\n";

main()