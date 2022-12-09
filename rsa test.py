import math
import random

"""Needed information
RSA Key generation
2 large primes, P & Q
N = P*Q
E (must be greater than 1, less than (p-1)(q-1), must be prime

public key=(n,e)
private key: 1=ed mod (p-1)(q-1)

RSA Encryption
P is plaintext
C is encrypted Cipher

C = P^E mod n
Plaintext = C^D mod n
"""

"""Please note that this part of the application is currently broken.
The encryption works just fine, but the decryption returns a value of 1"""

"""List of prime numbers to use"""
primeList = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,
                   73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,
                   151,157,163,167,173,179,181,191,193,197,199,211,223,227,
                   229,233,239,241,251,257,263,269,271,277,281,23,293,307,311,
                   313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,
                   409,419,421,431,433,439,443,449,457,461,463,467,479,487,
                   491,499,503,509,521,523,541,547,557,563,569,571,577,587,
                   593,599,601,607,613,617,619,631,641,643,647,653,659,661,
                   673,677,683,691,701,709,717,727,733,739,743,751,757,761,
                   769,773,787,787,809,811,821,823,827,829,839,853,857,859,
                   856,877,881,883,887,907,911,919,929,937,941,947,953,967,
                   971,977,983,991,997]
"""This variable isn't used directly, I use it for reference later"""
primeLength = 167
"""Initialize the encryptionKeys dict"""
encryptionKeys = {
    "P" : 0,
    "Q" : 0,
    "N" : 0,
    "E" : 0,
    "D": 0
    }

"""The RSA formula is the same both ways, just switch out E for D"""
def encryptDecrypt(P, ED, N, C = 0):
    C = (P**ED)%N    #I call ED for the exponent. ED could either be E for
                    #encryption or D for decryption
    return C


"""Generate Keys for small sizes"""
def keyGenerator(primeList, encryptionKeys,index =1,x=2):
    encryptionKeys["P"]=primeList[random.randint(0,10)] 
    encryptionKeys["Q"]=primeList[random.randint(0,10)] 
    #Set values for P and Q using the first 10 prime numbers in primeList
    while encryptionKeys["P"] == encryptionKeys["Q"]:   #Make sure P and Q aren't the same
        encryptionKeys["Q"]=primeList[random.randint(0,10)] 
        #Randomize Q again until they aren't
    encryptionKeys["N"]=encryptionKeys["P"]*encryptionKeys["Q"]
    #Set value for N
    encryptionKeys["E"]=primeList[random.randint(0,10)]
    while (encryptionKeys["E"]>((encryptionKeys["P"]-1)*(encryptionKeys["Q"]-1))
    or encryptionKeys["E"]<1 or encryptionKeys["E"]== encryptionKeys["P"]
    or encryptionKeys["E"]==encryptionKeys["Q"]):
        encryptionKeys["E"]=primeList[random.randint(0,10)]
    """This mess creates E. I start by giving E some value, then check to make
    sure that 1<E<(p-1)(Q-1). From there I make sure E doesn't equal P or Q."""
        
    encryptionKeys["D"]=0
    while x!=1:
        #print(encryptionKeys["D"])
        encryptionKeys["D"]=encryptionKeys["D"]+1
        x = ((encryptionKeys["E"]*encryptionKeys["D"])
        %((encryptionKeys["P"]-1)*(encryptionKeys["Q"]-1)))
        """print(x)
        print(encryptionKeys["D"], encryptionKeys["P"],encryptionKeys["Q"]
              ,encryptionKeys["E"])""" #used for troubleshooting
    """Set value for D. ED%(P-1)(Q-1)=1. Since we already know the rest we can
    increment D until the mod equals 1"""
    print(encryptionKeys["P"],encryptionKeys["Q"],encryptionKeys["N"]
          ,encryptionKeys["E"], encryptionKeys["D"])#used for troubleshooting
    return encryptionKeys

def main(encryptionKeys):
    encryptionKeys = keyGenerator(primeList, encryptionKeys)
    plainText = 10
    cipherText = encryptDecrypt(plainText, encryptionKeys["E"],encryptionKeys["N"])
    testText = encryptDecrypt(cipherText, encryptionKeys["D"],encryptionKeys["N"])

    print(plainText, cipherText, testText)
