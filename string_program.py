name="Megha shree Badri Lakshmi Narasimhan"
count=0
for char in name:
    count+=1
print(count)

#String methods
name="amrutha"
print(name.capitalize())
print(name.count("a"))
print(name.endswith("a"))

# Q1. Swap the case of the string without using swapcase
# inbuilt method for string
#
# Input:- Programming Is Easy
# Output:- pROGRAMMING iS eASY

inputString="Programming Is Easy"
outputString=""
for char in inputString:
    if char.isupper():
        outputString+=char.lower()
    else:
        outputString+=char.upper()
print(outputString)

#FETCHING IP ADDRESS FROM STRING
input='''"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2/file_path/teams/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path/teams/bin/test1.csv",
"/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22/file_path/data/bin/test1.csv",
"/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2/file_path//usr/bin/test1.csv",
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31/file_path/worklog/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path//tmp/bin/test1.csv"
]"'''
cleaned_str=input.strip(']"')
paths=[p.strip().strip('"') for p in cleaned_str.split(",")]
print(paths)
for path in paths:
    every_path=path.split("/")
    if "server" in every_path:
        idx=every_path.index("server")
        if idx+1<len(every_path): #Making sure index-out-of-bounds error won't occur
            print(every_path[idx+1])

#Masking Email
input=["mverma625@gmail.com","ramesh02@hotmail.com",
       "sohansingh@gmail.com","swatirahane@outlook.com"]
masked_email=[]
for email in input:
    username,domain=email.split("@")
    if len(username)>2:
        masked_mail=username[0]+"*" * (len(username)-2)+username[-1]
    else:
        masked_mail=username[0]+"*"

    masked_mail=masked_mail + "@"+ domain
    masked_email.append(masked_mail)
print(masked_email)

