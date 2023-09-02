user = {
    "id": 4170,
    "uid": "9sjskd8gjs9qa2751aldjj",
    "password": "SyUpfo1ljm",
    "first_name": "David",
    "last_name": "Cohen",
    "username": "david.cohen",
    "email": "david.cohen@gmail.com",
    "gender": "male",
    "phone_number": "1122334455",
    "social_insurance_number": "98765432",
    "date_of_birth": "1988-12-30"
}

user["surname"] = user.pop("last_name")
user['secret'] = user.pop('password')
print(user)
