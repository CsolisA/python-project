class Purchase:

    def __init__(self, id_purchase, products, client, admin):
        self.id_purchase = id_purchase,
        self.products = products,
        self.client = client
        self.admin = admin

    def __str__(self):
        return f"Products: {self.products} by Client: {self.client.name} & Served by: {self.admin.name}"
