# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from clients_package.administrator import Administrator
from clients_package.client import Client
from clients_package.purchase import Purchase

first_admin = Administrator('Carlos', 'Solis', 25, 'carlos@email.com', 'main')
first_client = Client('Juno', 'Araya', 14, 'Juno@email.com', 1)
first_purchase = Purchase(1, ['Jabon, Coca Cola', 'Jarabe','Hielo'], first_client, first_admin)

print(first_purchase)