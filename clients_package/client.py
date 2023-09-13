from clients_package.user import User


class Client(User):
    def __init__(self, name, last_name, age, email, client_id):
        super().__init__(name, last_name, age, email)
        self.client_id = client_id

    def show_client_id(self):
        print("Client ID: ", self.client_id)
