#Código que modifica una colección mientras se itera sobre la misma colección puede ser complejo de hacer bien. Sin embargo, suele ser más directo iterar sobre una copia de la colección o crear una nueva colección
users = {'Hans':'active', 'Eleonore': 'inactive', '景太郎': 'active' }
for user, status in users.copy().items():
    if status =='inactive':
        del users[user]
active_users ={}
for users, status in users.items():
    if status == 'active':
        active_users[user]= status
print (active_users[user])
