
import os
import errno
 
def Encrypt(filename, key):
    
    if os.path.isfile(filename):
        
        file = file = open(filename, "rb")
        data = file.read()
        file.close()
    
    
        data = bytearray(data)
    
        for index, value in enumerate(data):
            data[index] = value ^ key

        file = open("cc-" + filename, "wb")
        file.write(data)
        os.remove(filename)
        print("encryption successful")
        file.close()
    else:
        print("File not Found")
    
   



def Decrypt(filename, key):
    
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    
    data = bytearray(data)
    
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open(filename, "wb")
    file.write(data)
    print("decryption successful")
    file.close()



print("encrypt - execute encryption feature ")
print("decrypt - execute decryption feature ") 
print("")
print("-enter command-")
choice = ""
while choice != "quit" or "end" or "end" or "close":
    
    choice = input()
    
    if choice == "x":
        print("hello")
        
    
    if choice == "encrypt":
        key = int (input("Enter key 1 - 255: "))
        filename = input ("Please enter a file name: ")
        Encrypt(filename, key)
    if choice == "decrypt":
       
        
        key = int (input("Enter key 1 - 255: "))
        filename = input ("Please enter a file name: ")
        Decrypt(filename, key)
    
  
   
        
    
    
##Reading and printing the file byte by byte and storing it into data file
##Retrieves each index value and changes it using the exclusive or on the key used changing the array to the encrypted version
##Print(f"index: {index} value: {value}") Print the Index and the value of the index       
##Enumerate gives back index value and  the position
##Reading the file and writing the contents byte by byte into new file with CC appended as an indicator for the copied version