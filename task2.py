from datetime import datetime as dt

class Client:
    def __init__(self, uid: int,  client_name: str, tnum: str):
        self.uid = uid
        self.client_name = client_name
        self.tnum = tnum
        self.orders = []
    def __str__(self) -> str:
        return self.client_name + " " + self.tnum

class Pizza:
      def __init__(self, ingredients = ['a', 'b', 'c', 'd'], add=[]):
          self.ingredients = ingredients + add
          self.name = 'Pizza'
      def __str__(self):
        return self.name + '\n' + ' '.join(self.ingredients)

class MonPizza(Pizza, Client):
    def __init__(self, add, ingredients = ['a', 'b', 'c', 'd'] ):
        super().__init__(ingredients, add)
        self.name = 'Monday' + self.name
        self.ingredients += ['Monday special ingredient']
      
class TuePizza(Pizza):
    def __init__(self, add, ingredients = ['a', 'b', 'c', 'd'] ):
        super().__init__(ingredients, add)
        self.name = 'Tuesday' + self.name
        self.ingredients += ['Tuesday special ingredient']    

class WedPizza(Pizza):
    def __init__(self, add, ingredients = ['a', 'b', 'c', 'd'] ):
        super().__init__(ingredients, add)
        self.name = 'Wednsday' + self.name
        self.ingredients += ['Wednsday special ingredient']    

class ThuPizza(Pizza):
    def __init__(self, add, ingredients = ['a', 'b', 'c', 'd'] ):
        super().__init__(ingredients, add)
        self.name = 'Thursday' + self.name
        self.ingredients += ['Thursday special ingredient']    

class FriPizza(Pizza):
    def __init__(self, add, ingredients = ['a', 'b', 'c', 'd'] ):
        super().__init__(ingredients, add)
        self.name = 'Friday' + self.name
        self.ingredients += ['Friday special ingredient']    

class Order(Client):
    def __init__(self, uid,  client: Client, date: str, price: int, add=[]):
        self.uid = uid
        self.client = client
        self.date = date
        self.price = price
        self.add = add 
        weekday = dt.weekday(dt.strptime(date, '%d.%m.%y'))
        if weekday ==  0:
           client.orders +=  [MonPizza(add)]
        elif weekday ==  1:
           client.orders +=  [TuwPizza(add)]           
        elif weekday ==  2:
           client.orders +=  [WedPizza(add)]
        elif weekday ==  3:
           client.orders +=  [ThuPizza(add)]
        elif weekday ==  4:
           client.orders +=  [FriPizza(add)]
        else:
            raise Exception('У вихідні дні замовлення бізнес-ланчу неможливе')
            return None
 
    def __str__(self):
        return '''Замовлення №{} на {}
        Ціна складає {} грн
        Замовник: {}'''\
        .format(self.uid, self.date,  self.price, self.client)    

    def get_price(self):
        return self.price
