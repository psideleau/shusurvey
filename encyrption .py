from Question import answer 
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate public and private key
pubkey = key.publickey() # pub key export for exchange

print ("\n")

#Encrypt the string provided  and print the encrypted value  
encrypted = pubkey.encrypt( answer  , 32)
print ("\n The Encrypted Value : ") , encrypted #ciphertext

#write the Encrypted string in file 
writefile = open ('encryption.txt', 'w')
writefile.write(str(encrypted)) #write ciphertext to file
writefile.close()

#read from the Encrypted file
readfile = open('encryption.txt', 'r')
message = readfile.read()

print ("\n")
#asking the admin if he wants to the answers to be revealed 
R_S = raw_input("Do you want the answer to be revealed (yes / no)?   ")
if R_S == "yes":
    #print the answers message 
    decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
    
    print (" The Decrypted answers  : "), decrypted
else:
    print ("\t End of the program ")


#the answers will be in the text file 
#write the decrypted answers in test file 
writefile=open('decrypted.txt','w')
writefile.write(decrypted)
writefile.close()






