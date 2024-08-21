def initialUserJson(*, userName: str, userAge: int, userNationality: str, userDNI: int, id: int):

    jsonData = {
        'id': id,
        'name': userName,
        'age': userAge,
        'nationality': userNationality,
        'dni': userDNI
    }
    return jsonData
