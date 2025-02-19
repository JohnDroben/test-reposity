# Разработай систему управления учетными записями пользователей для небольшой компании.
# Требования:
# 1.Класс User*: Этот класс должен инкапсулировать данные о пользователе: ID,
#  имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка
# (представь, что это просто список экземпляров User).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа
# и модификации снаружи. Предоставь доступ к необходимым атрибутам
# через методы (например, get и set методы).


class User():
    def __init__(self, name,identification):
        self._name = name
        self._status = 'user'
        self._identification = identification

    def get_name(self):
        return self._name

    def get_status(self):
        return self._status

    def get_id(self):
        return self._identification

    def set_name(self, new_name):
        self._name = new_name



class Admin(User):
    __user_list = []
    def __init__(self, name, identification):
        super().__init__(name, identification)
        self._status = 'admin'

    def add_user(self,user):
        if isinstance(user, User):
            Admin.__user_list.append(user)
        else:
           raise ValueError ("Ошибка! Пользователь не может быть добавлен в список экземпляров User")


    def remove_user(self, identification):
        for user in Admin.__user_list:
            Admin.__user_list.remove(user)
            return

    @classmethod  # Добавлен декоратор
    def get_info_user(cls):
           return cls.__user_list.copy()



# Проверяем:

# Создаем администратора
admin = Admin("Алиса",1 )

# Создаем обычных пользователей
user1 = User("Алексей", 2)
user2 = User("Иван", 3)
user3 = User("Наталья", 4)

# Администратор добавляет пользователей
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

# Выводим список пользователей
for user in Admin.get_info_user():
    print (f"ID: {user.get_id()}, Имя: {user.get_name()}, Access: {user.get_status()}")

# Администратор удаляет пользователя
admin.remove_user(2)

# Выводим список пользователей
for user in Admin.get_info_user():
    print (f"ID: {user.get_id()}, Имя: {user.get_name()}, Access: {user.get_status()}")