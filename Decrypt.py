from cryptography.fernet import Fernet

key = Fernet.generate_key()
file = open("encryption_key.txt", 'wb')
file.write(key)
file.close()

Wifi_passwords = 'Informations.txt'



encrypted_files = [Wifi_passwords]
count = 0


for decrypting_files in encrypted_files:

    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open("decryption.txt", 'ab') as f:
        f.write(decrypted)

    count += 1
