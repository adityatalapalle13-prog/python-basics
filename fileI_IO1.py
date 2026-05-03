f=open('neededforIO.txt', 'r') #'r' for reading,'w' for writing and 'a' for appending
#remember to make a replit account to access his notes later
print(f)
text=f.read()# it's only possible since f= ~~'r'
print(text) #'r' is a default mode
f.close()

g=open('myfile.txt','w')# 'w' creates a new file even if it didn't exist before

