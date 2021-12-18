import GenerateKey
import LoadKey
import Encrypt
import Decrypt
if __name__=="__main__":
    g=GenerateKey.GenerateKey("Password")
    l=LoadKey.LoadKey("C:\\Users\\SAMEE\\Documents\\Programming\\Password.txt")
    print(l.key())
    Encrypt.Encrypt("C:\\Users\\SAMEE\\Documents\\Programming\\Sam.txt",l.key())
    Decrypt.Decrypt("C:\\Users\\SAMEE\\Documents\\Programming\\Same.txt",l.key())
