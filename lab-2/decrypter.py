import os
import pyaes

key = b"diocybersecurity"
file_name = "file.txt"
crypt_name = file_name + ".cry"

crypt_file = open(crypt_name, "rb")
crypt_data = crypt_file.read()
crypt_file.close()
os.remove(crypt_name)

file_data = pyaes.AESModeOfOperationCTR(key).decrypt(crypt_data)
file = open(file_name, "wb")
file.write(file_data)
file.close()
