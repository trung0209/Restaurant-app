class Order_list():
    def __init__(self,id):
        self.id = id
        self.list_of_order = {}

    def add_to_order(self,dish, amount):
        self.list_of_order[dish] = amount

    def add_existed_to_order(self,dish, amount):
        self.list_of_order[dish] += amount

    def check(self,dishe):
        if dishe not in self.list_of_order:
            return False
        else:
            return True

    def get_dict(self):
        return self.list_of_order

    def get_lenght(self):
        return len(self.list_of_order)

    def get_id(self):
        return self.id


