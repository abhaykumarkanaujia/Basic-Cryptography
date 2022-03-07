from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


class Decryption:
    def __init__(self, password):
        self.password = password

    def decrypt_aes_cbc(self, inputFile, outputFile):
        with open(inputFile, "rb") as file:
            salt = file.read(32)
            iv = file.read(16)
            data = file.read()
        key = PBKDF2(self.password, salt, dkLen=32)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decryptedData = unpad(cipher.decrypt(data), AES.block_size)
        with open(outputFile, "w") as file:
            file.write(decryptedData.decode('utf-8'))
