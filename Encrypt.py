from cryptography.fernet import Fernet
class Encrypt:
    def __init__(self,address_of_the_file,key):
        self.address_of_the_file=address_of_the_file
        self.key=key
        fernet_object=Fernet(self.key)

        file_to_encrypt=open(self.address_of_the_file,"rb")
        content_of_file_to_encrypt=file_to_encrypt.read()
        encrypted_content=fernet_object.encrypt(content_of_file_to_encrypt)
        file_to_encrypt.close()

        file_to_encrypt=open(self.address_of_the_file,"wb")
        file_to_encrypt.write(encrypted_content)
        file_to_encrypt.close()