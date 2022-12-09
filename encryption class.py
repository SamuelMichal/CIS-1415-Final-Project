import random
class encryption:
    def __init__(self, plainText, cipherText, encrypt,hashList):
        self.p=plainText
        self.c=cipherText
        self.e=encrypt
        self.h=hashList
    """This will set up the encryption based on wether encrypt is true
    false"""
    def encrypt(self):
        if self.e==True:    #if true call the encryption program
            self.c=self.hashProtocol(self, plainText, cipherText, hashList)
        elif self.e==False: #if false call the decryption program
            self.p=self.hashProtocol(self, cipherText, plainText, hashList)
        """I should note that because of the nature of hash arguements,
        The true or false will call the same function, with two different arguements.
        The hash program is a two way algorithm, so the same steps are used
        for encryption as decryption"""
        return

    def hashProtocol(self, plainText, cipherText, hashList):
        for index in range(len(plainText)):
        """Used for troubleshooting
        #print(plainText)
        #print("")"""
        """Program checks the value of hashlist at each index value
        if that index value is 1, then the program flips the bit of
        corresponding binaryInputList index value"""
        if hashList[index] == '1':
            """Used for troubleshooting
            #print("flip")"""
            """Checks to see if the index value is 1 or 0. If 1 set to 0
            if 0 set to 1"""
            if cipherText[index] == '1':
                cipherText[index]='0'
            else:
                cipherText[index]='1'
        index+=1 #increment index
    return cipherText #once the loop is finished, return the cipherText


def createHash(hashList = ""):
    for index in range(16):
        hashList += str(random.randint(0,1))
        index+=1
    return hashList #return the hashList
hashList = createHash()
plainText = createHash()

x=encryption(plainText, "Hello World", True)
y=encryption("Test", "Hello World", False)
