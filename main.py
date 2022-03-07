from getpass import getpass
from cipher import Encrypt
from cipher import Decrypt
import os



if __name__ == "__main__":

    print("Enter File Location: ")
    inputFile = input()
    print('')

    if os.path.exists(inputFile):
        if inputFile[-4:] == ".bin":
            """Decrypt if file at entered location is a binary file means encrypted by this script. """
            outputFile = inputFile[:-4] + '.txt'
            print("Enter Password to Decrypt file: ")  # password used to encrypt file at time of .
            password = getpass()
            decrypter = Decrypt.Decryption(password)  # creates object of decryption class
            decrypter.decrypt_aes_cbc(inputFile, outputFile)  # generates decrypted text file.
            os.remove(inputFile)  # delete initial encrypted file.
        elif inputFile[-4:] == ".txt":
            """Encrypt if file is a normal text file. """
            outputFile = inputFile[:-4] + '.bin'
            print("Enter Password to Encrypt File: ")  # password to encrypt file
            p1 = getpass()
            print("Re-Enter Password to Encrypt File: ")  # re-check password
            password = getpass()
            while p1 != password:
                print("password not matched!!!")
                print("Enter Password to Encrypt File: ")
                p1 = getpass()
                print("Re-Enter Password to Encrypt File: ")
                password = getpass()
            encypter = Encrypt.Encryption(password)  # creates object of encryption class
            encypter.generate_aes_encrypted_file_cbc(inputFile, outputFile)  # generates encrypted text file.
            os.remove(inputFile)
        else:
            print("File Not Supported.")
    else:
        print("File does not exist.")
