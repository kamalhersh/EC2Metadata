from flask import Flask
import requests

x= requests.get("https://container0-cxckasqe4a-uc.a.run.app/")
y = x.content
z = str(y)
z = z.splitlines()
print (z)

