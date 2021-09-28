from flask import Flask
import requests
import string
import os
import urllib 
import urllib.request as r

f = open("listing.txt", "w")
f.write("")
f.close()

resp= requests.get("http://169.254.169.254/latest/meta-data/")
getcont = resp.content
strcont = str(getcont)
splitcont = strcont.split('\\n')
for wrtcont in splitcont:
    f = open("listing.txt", "a")
    f.write(wrtcont + "\n")
f.close()
    
