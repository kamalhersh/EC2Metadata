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

resp= requests.get("http://169.254.169.254/latest/meta-data/")

getcont = resp.content
getcont =getcont.decode('utf-8')
splitcont = getcont.split('\n')

# initializing my variables 

conttodic = {1 :""}
indx=1

# printing the list on the screen and saving it to dictionary (converting it from list)

for item in splitcont:
    conttodic [indx] = item
    print(str(indx) + "-" + conttodic[indx])
    indx +=1


# saving the list in to a file (optinal)
i=1
for wrtcont in splitcont:
    f = open("listing.txt", "a")
    f.write(str(i) + " "  + wrtcont + "\n")
    i +=1
f.close()

while True:
    try :
        
        metaindex = int(input("Please enter the number of the Metadata that you wish to fetch from the list above or ctrl+c to exit: "))
        if metaindex > 0 and metaindex <= len(splitcont):
            temp = conttodic[metaindex]
            fulurl = "http://169.254.169.254/latest/meta-data/{}"
            print(fulurl.format(temp))
            resp2= requests.get("http://169.254.169.254/latest/meta-data/")
            getcont2 = resp2.content
            getcont2 = getcont2.decode('utf-8')
	        
        else:
            print( metaindex , "is out of the index range ")   
    except KeyboardInterrupt:
        print('\n')
        break
    except:
        print ("please enter an integer or ctrl+c to exit: ")

 


