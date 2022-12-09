# CIS 1415 Final Project
 My encryption decryption final project

This is my final project for CIS 1415 Intro to Programming
The project is a program to encrypt and decrypt data.
You can either choose between a 256 bit hash, or RSA 2 key encryption
As of right now, the hash and RSA are both somewhat functional.
The RSA encryption can't load external keys, but I'm working on it.
The hash encryption works by checking input data with a generated hash.
If the hash has a 1, the bit in the input data is flipped. 
If the hash has a 0, the bit in the input data is unchanged.
It isn't what you might call a true hash, as it is very easy to decrypt with the proper cipher.
The RSA encryption uses a standard private public key to encrypt and decrypt data.
As of right now, the program will generate the private and public keys, but I'm working on it.
When the project is finished, the interface will be GUI based
You will be able to choose various text files for encryption and decryption.
You will also be able to choose wether to generate keys and ciphers, or provide them
