from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES


class Encryption:
    def __init__(self, password):
        self.salt = get_random_bytes(32)
        self.key = PBKDF2(password, self.salt, dkLen=32)

    def generate_aes_encrypted_file_cbc(self, inputFile, outputFile):
        with open(inputFile, "r") as file:
            bytesData = file.read()
        bytesData = bytes(bytesData.encode('utf-8'))
        cipher = AES.new(self.key, AES.MODE_CBC)
        data = cipher.encrypt(pad(bytesData, AES.block_size))
        with open(outputFile, "wb") as file:
            file.write(self.salt)  # 32 bytes
            file.write(cipher.iv)  # 16 bytes
            file.write(data)
