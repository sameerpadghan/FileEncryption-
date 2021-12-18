class LoadKey:
    def __init__(self,address_of_the_file):
        self.address_of_the_file=address_of_the_file

    def key(self):    
        file=open(self.address_of_the_file,'rb')
        text=file.read()
        file.close()
        return text
