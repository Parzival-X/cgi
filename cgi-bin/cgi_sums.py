#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-Type: text/plain")
print("")

form = cgi.FieldStorage()
vals = form.getlist("operand")
try:
    result = sum(int(val) for val in vals)
except Exception:
    print("Unable to add values. Please try again.")

print("Total is: {}".format(str(result)))
