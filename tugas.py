import string
import os

def encrypt(chrt, msg, key):
    encrypted = ''
    total_key = sum([chrt.find(k) for k in key])

    for i in msg:
        if i in chrt:
            position = chrt.find(i)
            newposition = (position + total_key) % len(chrt)
            encrypted += chrt[newposition]
        else:
            encrypted += i

    return encrypted

def decrypt(chrt, msg, key):
    decrypted = ''
    total_key = sum([chrt.find(k) for k in key])

    for i in msg:
        if i in chrt:
            position = chrt.find(i)
            newposition = (position - total_key) % len(chrt)
            decrypted += chrt[newposition]
        else:
            decrypted += i

    return decrypted

def main():
    alp = string.ascii_letters
    out = True
    while out:
        select = input("Menu :\n1. Encrypt\n2. Decrypt\n3. Exit\nSelect : ")
        if select == '3':
            out = False
        elif select == '1':
            Private_key = input("Input Key: ")  
            message = input('Masukkan teks untuk dienkripsi: ')
            result = encrypt(alp, message, Private_key)
            print(f'Pesan Terenkripsi: {result}')
        elif select == '2':
            message = input('Masukkan teks untuk didekripsi: ')
            Private_key = input("Key? ")
            result = decrypt(alp, message, Private_key)
            print(f'Pesan Terdekripsi: {result}')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Tidak Tersedia")
            continue

main()
