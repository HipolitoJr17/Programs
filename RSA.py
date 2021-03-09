import os

import binascii
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#MENU
def menu():

    print("[+] Bienvenido/a al cifrador RSA HEA, ¿Que desea realizar? \n")

    print("[1] Encriptar un archivo con clave asimetrica")
    print("[2] Desencriptar un archivo con clave asimetrica")

    print("[0] Salir del sistema \n")


menu()
option = int(input("[+] Introduzca la seleccion: "))

while option != 0:
   
    if option == 1:

        random_generator = Crypto.Random.new().read

        private_key = RSA.generate(2048, random_generator)
        public_key = private_key.publickey()



        #CREAR ARCHIVO DE LLAVE PRIVADA
        private_key = private_key.exportKey("PEM")

        with open ("PrivateKey.pem", "wb") as pfile:
            pfile.write(private_key)

        private_key = RSA.importKey(open("PrivateKey.pem", "rb").read())


        #CREAR ARCHIVO DE LLAVE PUBLICA
        public_key = public_key.exportKey("PEM")

        with open ("PublicKey.pem", "wb") as pfile:
            pfile.write(public_key)

        public_key = RSA.importKey(open("PublicKey.pem", "rb").read())    

        #ENCRIPTACION
        filename = input("[+] Introduzca el nombre del archivo que desea encriptar: ")
        
        with open (filename, "rb") as file:
            info = file.read()

        message = info

        cipher = PKCS1_OAEP.new(public_key)
        encryptmessage = cipher.encrypt(message)

        with open (filename, "wb") as file:
            file.write(encryptmessage)

        print("[+] El archivo fue encriptado con exito")
        input("[+] Presione enter para continuar...")

        pass

    elif option == 2:


        filename = input("[+] Introduzca el nombre del archivo que desea desencriptar: ")

        with open (filename, "rb") as file:
            encrypinfo = file.read()

        cipher = PKCS1_OAEP.new(private_key)
        message = cipher.decrypt(encrypinfo)

        with open (filename, "wb") as file:
            file.write(message)

        print("[+] El archivo fue desencriptado con exito")
        input("[+] Presione enter para continuar...")


        pass

    else:
        print("Opcion invalida")
        input("[+] Presione enter para continuar...")
    
    os.system("cls")
    menu()
    option = int(input("[+] Introduzca la seleccion: "))

print ("\nGracias por usar nuestro sistema")
