from cryptography.fernet import Fernet
class Decrypt:
    def __init__(self,address_of_the_file,key):
        self.address_of_the_file=address_of_the_file
        self.key=key
        fernet_object=Fernet(self.key)
        file_to_decrypt=open(self.address_of_the_file,"rb")
        content_of_file_to_decrypt=file_to_decrypt.read()
        decrypted_content=fernet_object.decrypt(content_of_file_to_decrypt)
        file_to_decrypt.close()

        file_to_decrypt=open(self.address_of_the_file,"wb")
        file_to_decrypt.write(decrypted_content)
        file_to_decrypt.close()