import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate public and private key
pubkey = key.publickey() # pub key export for exchange

print ("\t Hello Profssor Foss Welcome to my program ")
print ("\n")
# take the user input 
X= raw_input(" Enter the string that you want to Encrypt =  ")

#Encrypt the string provided  and print the encrypted value  
encrypted = pubkey.encrypt( X , 32)
print ("\n The Encrypted Value : ") , encrypted #ciphertext

#write the Encrypted string in file 
writefile = open ('encryption.txt', 'w')
writefile.write(str(encrypted)) #write ciphertext to file
writefile.close()

#read from the Encrypted file
readfile = open('encryption.txt', 'r')
message = readfile.read()

print ("\n")

#Decrypt the the encrypted value and print the decrypted value 
decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
#ast.literal_eval was used used for safely evaluating strings
#containing Python values from untrusted source
#without the need to parse the values oneself
print (" The Decrypted Value  : "), decrypted

#write the decrypted string in file 
writefile=open('decrypted.txt','w')
writefile.write(decrypted)
writefile.close()

#end of progam 
print ("\n End of program ")





