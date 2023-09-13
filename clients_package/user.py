class User:

    def __init__(self, name, last_name, age, email):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email

    def __str__(self):
        return f"Name: {self.name} {self.last_name}, Age: {self.age}, Email: {self.email}"

    def change_email(self, new_email):
        self.email = new_email
