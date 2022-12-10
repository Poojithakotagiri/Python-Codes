#trying to open a file, which does not exist
try:
    #trying to open a file in read mode
    fo = open("myfile.txt","r")
    print("file")
except FileNotFoundError:
    print("File does not exist")
except:
    print("other error")

print("ta ta")
