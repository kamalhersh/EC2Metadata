from flask import Flask
import requests
import string
import os
import urllib 
import urllib.request as r

f = open("listing.txt", "w")
f.write("")
f.close()

resp= requests.get("https://container0-cxckasqe4a-uc.a.run.app/")
getcont = resp.content
strcont = str(getcont)
splitcont = strcont.split('\\n')
for wrtcont in splitcont:
    f = open("listing.txt", "a")
    f.write(wrtcont + "\n")
f.close()
    