import random

"""creates a hash of any length. I chose 256, and 256 hash is the most common.
starts at 0, and uses random function as well as a loop to generate the hash"""
def createHash(hashList=""):
    for index in range(16):
        hashList += str(random.randint(0,1))
        index+=1
    return hashList #return the hashList

def hashProtocol(hashContents, hashList):
    for index in range(len(hashContents)):
        """Used for troubleshooting
        #print(binaryInput)
        #print("")"""
        """Program checks the value of hashlist at each index value
        if that index value is 1, then the program flips the bit of
        corresponding binaryInputList index value"""
        if hashList[index] == '1':
            """Used for troubleshooting
            #print("flip")"""
            """Checks to see if the index value is 1 or 0. If 1 set to 0
            if 0 set to 1"""
            if hashContents[index] == '1':
                hashContents[index]='0'
            else:
                hashContents[index]='1'
        index+=1 #increment index
    return hashContents #once the loop is finished, return the binaryInputList
    return
"""Function for encrypting entire files of information
Open the file, save to fileContents, encrypt fileContents and then
save to a new file"""
def encryptFile(hashList, fileName, fileContents=""):
    """Open, read, and close the given file"""
    f=open(fileName, 'r')
    fileContents=list(f.read())
    f.close()
    """Used for troubleshooting purposes
    print(fileContents)"""
    fileContents = hashProtocol(fileContents,hashList)  #hash the file contents
    fileContents=valueCompression(fileContents) #compress the list back into a useable string
    """open (or create), write and close an encrypted version of the file"""
    f=open(("encrypt"+fileName),'w')
    f.write(fileContents)
    f.close()
    """Save the hash sequence so you can decrypt later"""
    f=open("Hash sequence.txt", 'w')
    f.write(hashList)
    f.close()
    """used for troubleshooting
    print(fileContents)"""
    return fileContents

"""Function encryptString is used to encrypt any data that is user
inputed manually. The input is given, then returned as an ouput list."""
def encryptString(hashList, binaryInputList):
    binaryInputList=hashProtocol(binaryInputList,hashList)
    return binaryInputList #once the loop is finished, return the binaryInputList

"""This function compresses the list down to a useable and readable string"""
def valueCompression(listChoice,string=""):
    """compress binaryOutput to a string using an empty string"""
    listChoice=string.join(listChoice)  
    return listChoice     #return binaryOutput

def main():
    hashList=createHash()   #create out hashList
    binaryInput=createHash()
    binaryInputList=list(str(binaryInput))
    #Used for troubleshooting
    print("Hash List     ",hashList)
    #print(binaryInput)
    binaryOutput=encryptString(hashList, binaryInputList)
    """used for troubleshooting
    print("---------------------------------------------------------")
    #print(binaryOutput)"""
    binaryOutput=valueCompression(binaryOutput)
    print("Binary Input  ",binaryInput)
    print("Binary Output ",binaryOutput)

def main2():
    hashList=createHash()
    encryptFile(hashList, "sample.txt")
    
    
