# Python program to write JSON
# to a file


import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

with open("file.csv", "w") as outfile:
    (dictionary, outfile)