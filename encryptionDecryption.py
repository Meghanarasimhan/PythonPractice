from cryptography.fernet import Fernet

key= Fernet.generate_key() # Generating key using fernet library
print(f"generated key is {key}")
cipher=Fernet(key) #creating cipher object using generated key

data="Meghashree Badri Lakshmi Narasimhan"
data_bytes=data.encode() #converting string to bytes
encrypted_data=cipher.encrypt(data_bytes)
print(f"encrypted data is {encrypted_data}")
decrypted_data=cipher.decrypt(encrypted_data)
print(f"decrypted data is {decrypted_data.decode()}")


