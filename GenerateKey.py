from os import name
from cryptography.fernet import Fernet
import os
class GenerateKey:
    def __init__(self,name_of_file):
        self.name_of_file=name_of_file
        current_dir=os.getcwd()
        location_to_save=current_dir+"\\"+self.name_of_file+".txt"
        key=Fernet.generate_key()
        file=open(location_to_save,"wb")
        file.write(key)
        file.close()
        print(location_to_save)