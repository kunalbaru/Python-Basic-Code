#!/usr/bin/python2.6
file=raw_input('Enter File Name:')
try:
 fhand=open(file)
except:
 print 'This is not the right file',file
 exit()
count=0
for line in fhand:
 if 'Error' in line:
  count=count+1
print 'Required word comes',count, 'times'
