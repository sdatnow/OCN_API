
# OCN code snippet for customer server
# Must be hosted on customer web server
# Retrieves a PDF from customer's account
# Version 1.3

import cgi, cgitb
import sys
import os
import urllib
import urllib2

def main():
    result = None
    pdffilename = None
    directory = None

    form = cgi.FieldStorage()
    pdffilename = form.getvalue('filename')
    directory = form.getvalue('directory')

    try:
        # Link to server where customer's tenant is located
        url = 'http://localhost:82/ServerSide/OCN_GetPDFFile.py'
             # Specify user, MD5(password) and org name
        values = {'org' : 'acme', 'user' : 'sdatnow', 'pass' : 'cc03e747a6afbbcbf8be7668acfebee5' }
   
        # If PDF file name not specified via URL Parameter
        if (pdffilename == None):
            pdffilename = 'testpdf.pdf'
        if (directory == None):
            directory = 'Portal'

        values['filename'] = pdffilename
        values['directory'] = directory
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        result = response.read()
        imagetype = 'application/pdf'
        contentType = "Content-Type:" + imagetype + "\r"
        print contentType
        print "Content-Disposition: inline; filename=\"" + pdffilename + "\"\r" #attachment
        print "Content-length: " + str(len(result)) + "\r\n"
        sys.stdout.write(result)
    except:
        print "Status: 404 Not Found", "\n\n";

main()