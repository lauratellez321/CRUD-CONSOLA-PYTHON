import csv
import os
import time
from user.user import initialUserJson
listUsers = [{'id': 0, 'name': 'Wolfang', 'age': '23',
              'nationality': 'Colombiano', 'dni': '1000974167'}, {'id': 2, 'name': 'Rambo', 'age': '1',
                                                                  'nationality': 'Colombiano', 'dni': '1001'}]


# def ReadFileOrCreateIfNotExist(*, fileName: str):
#     if os.path.isfile(fileName):
#         pass
#     else:
#         with open(fileName, mode='w', newline='') as file_csv:
#             writer = csv.writer(file_csv)
#             writer.writerows(listUsers)
#         pass


def CRUD():
    while True:
        os.system('clear')
        print('1. Crear Usuario')
        print('2. Consultar Usuario')
        print('3. Actualizar Usuario')
        option = input('Escribe la opcion:')

        if option == '1':
            userName = input('Escribe tu nombre:')
            userAge = input('Escribe tu edad:')
            userNationality = input('Escribe tu nacionalidad:')
            userDNI = input('Escribe tu DNI:')
            listUsers.append(initialUserJson(id=len(listUsers), userName=userName, userAge=userAge,
                                             userNationality=userNationality, userDNI=userDNI))
            print('Usuario creado exitosamente')
            print(listUsers)
            time.sleep(2)

        if option == '2':
            userFound = False
            validateUserDNI = True
            while validateUserDNI:
                userDNI = input('Escribe DNI a consultar:')
                for user in listUsers:
                    # VALIDA SI EXISTE EL USUARIO
                    if userDNI == user['dni']:
                        # SI EXISTE
                        userFound = True
                        validateUserDNI = False
                        print('DATA DEL USUARIO')
                        print(
                            f"ID del usuario: {user['id']} \nNombre del usuario: {user['name']} \nEdad del usuario: {user['age']} \nNacionalidad del usuario: {user['nationality']} \nDNI del usuario: {user['dni']}")
                        time.sleep(5)
                        continue
                if not userFound:
                    print('Usuario no existe, digite nuevamente')
                    time.sleep(5)

        if option == '3':
            userDNI = input('Escribe DNI a actualizar')
            flagContar = 0
            for user in listUsers:
                flagContar = flagContar + 1
                # VALIDA SI EXISTE EL USUARIO, Y SI NO EXISTE. QUE?
                if userDNI == user['dni']:
                    print('DATA DEL USUARIO')
                    print(
                        f"1. Nombre del usuario: {user['name']} \n2. Edad del usuario: {user['age']} \n3. Nacionalidad del usuario: {user['nationality']}")
                    time.sleep(5)

                    print('1. Actualizar Nombre')
                    print('2. Actualizar Edad')
                    print('3. Actualizar Nacionalidad')
                    optionUpdate = input(
                        'Elige cual opcion quieres actualizar')

                    if optionUpdate == '1':
                        user['name'] = input('Nombre: ')
                    listUsers.pop()
                    listUsers.append(user)


if __name__ == '__main__':
    # file = 'database.csv'
    # ReadFileOrCreateIfNotExist(fileName=file)
    CRUD()
