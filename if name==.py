
#import LOOPsSTATEMENTS # here if you just import this and run, there wil be some codes that will be executed automatically

 #if there are set of codes that are executed just by importing the file, it could be problematic if we didn't need them
 # so the syntax:
 # if __name__=="__main__":
 #    callTheFunction


 #this syntax is used before writing the code that are being automatically executed after importing them in another file
 #note that this is used in the file that will be imported

 # for example Check what are the codes that are being executed automatically in LOOPsSTATEMENTS, and write if__ name syntax
 #before those codes, that code will only be executed if they are run in the same file, and won't be executed if the file is imported somewhere else