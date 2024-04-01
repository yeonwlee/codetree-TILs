class Product():
    def __init__(self, product_name: str = "codetree", product_code: int = 50):
        self.product_name = product_name
        self.product_code = product_code

    def print_data(self):
        print(f"product {self.product_code} is {self.product_name}")


product_name, product_code = input().split()
product1 = Product()
product1.print_data()

product2 = Product(product_name, int(product_code))
product2.print_data()