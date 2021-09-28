from flask import Flask
import requests
import string
import os
import urllib 

# reinitialising my file

f = open("listing.txt", "w")
f.write("")
f.close()

# request the list of metadata and convert it to string then split the content in to list 

resp= requests.get("https://container0-cxckasqe4a-uc.a.run.app/")
getcont = resp.content
strcont = str(getcont)
splitcont = strcont.split('\\n')

# initializing my variables 

conttodic = {1 :""}
indx=1

# printing the list on the screen and saving it to dictionary (converting it from list)

for item in splitcont:
    conttodic [indx] = item
    print(str(indx) + conttodic[indx])
    indx +=1


# saving the list in to a file (optinal)
i=1
for wrtcont in splitcont:
    f = open("listing.txt", "a")
    f.write(str(i) + wrtcont + "\n")
    i +=1
f.close()
    