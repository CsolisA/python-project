from clients_package.user import User


class Administrator(User):
    def __init__(self, name, last_name, age, email, admin_type):
        super().__init__(name, last_name, age, email)
        self.admin_type = admin_type

    def show_admin_type(self):
        print("Admin Type: ", self.admin_type)
