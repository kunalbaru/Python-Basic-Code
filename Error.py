#!/usr/bin/python2.6 #Path for Binaries
file=raw_input('Enter File Name:') #this is for taking input from user
try: #try and except is used to verify something
 fhand=open(file)
except:
 print 'This is not the right file',file
 exit()
count=0
for line in fhand:
 if 'Error' in line: # Error is the keyword which we are searching in the text file, we can change the Keyword as per our requirement.
  count=count+1
print 'Required word comes',count, 'times'
