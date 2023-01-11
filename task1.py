from datetime import datetime as dt

class Ticket():
    def __init__(self, uid,  event_name, date, basic_price):
        
        self.uid = uid
        self.event_name = event_name
        self.date = date
        self.ticket_type = 'квиток'
        self.price = basic_price
        self.discount = 0

    def __str__(self):
        return '''{} на "{}", що відбудеться {}\nБазова ціна складає {}, знижка {},\nдо сплати {}'''\
        .format(self.ticket_type, self.event_name, self.date, self.price, self.discount, (self.price - self.discount) )    

    def get_price(self):
        return self.price - self.discount

class StudTicket(Ticket):
    def __init__(self, uid,  event_name, date, basic_price):
        super().__init__(uid,  event_name, date, basic_price)
        self.discount = self.price * 0.5
        self.ticket_type = 'Студентський ' + self.ticket_type

class LateTicket(Ticket):
    def __init__(self, uid,  event_name, date, basic_price):
        super().__init__(uid,  event_name, date, basic_price)
        self.discount = -self.price * 0.1
        self.ticket_type = 'Пізно куплений ' + self.ticket_type

class EarlyTicket(Ticket):
    def __init__(self, uid,  event_name, date, basic_price):
        super().__init__(uid,  event_name, date, basic_price)
        self.discount = self.price * 0.4
        self.ticket_type = 'Зазделегідь куплений ' + self.ticket_type

def get_ticket(uid: int,  event_name: str, date=str, basic_price=float, stud: bool=False):
    delta = (dt.strptime(date, '%d.%m.%y') - dt.now()).days

    if stud:
        return StudTicket(uid,  event_name, date, basic_price)
    if delta < 10:
        return LateTicket(uid,  event_name, date, basic_price)
    elif delta >  60:
         return EarlyTicket(uid,  event_name, date, basic_price)   
    return Ticket(uid,  event_name, date, basic_price)
