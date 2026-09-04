from cryptography.fernet import fernet

key = fernet.generate_key()
cypher = fernet(key)

encoded_text = cypher.encrypt(b"Hello, World!")
print("Encoded text:", encoded_text)
decoded_text = cypher.decrypt(encoded_text)
print("decoded text:", decoded_text)