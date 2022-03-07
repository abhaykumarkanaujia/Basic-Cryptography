# Basic-Cryptography
Basic Cryptography can Encrypt or Decrypt text files. 

To Encrypt:
-> Run main.py in command line
-> Enter File Location you wish to Encrypt.
-> Create a Password. (save it somewhere as you will need when decypting)
-> Encryption Complete.

To Decrypt:
-> Run main.py in command line
-> Enter Encrypted File Location.
-> Enter Password You Created at time of Encryption.
-> Decryption Complete.

Note: run "pip install pycryptodome" and install PyCryptodome module before running main.py

# How it Works
Basic-Cryptography is Created using python and uses pycryptodome library.
the encryption protocol used is AES 256 bits Cipher Block Chaining.
In CBC mode, each block of plaintext is XORed with the previous ciphertext block before being encrypted.
This way, each ciphertext block depends on all plaintext blocks processed up to that point.

