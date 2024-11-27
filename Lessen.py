"""ООП - объектно ориентированное програмирование"""
"""Полиморфизм"""
"""
*Полиморфизм* (грекче «түрдүү форма») ар кандай объекттерди белгилүү бир 
көз караштан алганда окшош болушу үчүн кароого мүмкүндүк берет. 
Окшоштук деп бул жерде бир эле жүрүм-турумду, башкача айтканда,
 бир эле кыймыл-аракетти жасоо жөндөмүн айтып жатам."""

"""Абстракнно - это претставить"""

"""1. Абстракция
Абстракция ишке ашыруунун чоо-жайын жашырууга жана 
объекттерди интерфейстери аркылуу көрсөтүүгө мүмкүндүк берет.
 Биз базалык абстракттуу Транспорт классын түзөбүз, 
андан башка класстар мурасталат."""

# string1 = "Hello"
# string2 = "geeks"
# print(string1 + string2) #Конкатинация строк


# # class PublicExample: 
# #      def __init__(self, value): #Конструктор
          
# class Cat:
#      def __init__(self,name, preferences):
#           self.name = name
#           self.preferences = preferences
#      def info(self):
#        print(f"Я кот. Меня зовут {self.name}.Мне {self. preferences} года")
#      def make_sound(self):
#          print("Мяу!")

# class Dog:
#      def __init__(self,name, preferences):
#           self.name = name
#           self.preferences = preferences
#      def info(self):
#        print(f"Я собака. Меня зовут {self.name}.Мне {self. preferences} года")
#      def make_sound(self):
#          print("Гаф!")

# cat = Cat("васька", 2)
# dog = Dog("мухтар", 3)
# cat.info()
# dog.info()
# cat.make_sound()
# dog.make_sound

# for animal in (cat, dog):
#     animal.info()
#     animal.make_sound()

# class PaymentMethod:
#     def pay(self, amount):
#         pass

# class CreditCard(PaymentMethod):
#     def pay(self, amount):
#         return f"Сумма {amount}, оплачивается по кридитной карте"
    

# class PayPal(PaymentMethod):
#     def pay(self, amount):
#         return f"Сумма {amount}, оплачивается по PayPal"
    
# class BankTransfer(PaymentMethod):
#     def pay(self, amount):
#         return f"Сумма {amount}, оплачивается по банковскому переводу"
    
# payments = [CreditCard(), PayPal(), BankTransfer()]
    
# for payments in payments:
#     print(payments.pay(100))

class Employee:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def calculate_salary(self):
        print (f"Имя - {self.name}, Зп-{self.amount}")

    def display_info(self):
        print(f"Имя сотрудника-{self.name}")

class FullTimeEmployee(Employee):
    def __init__(self, name, amount):
        super().__init__(name, amount)
    def calculate_salary(self):
        print(f"Имя - {self.name}, Зп - {self.amount * 1.2}")

class ParttimeEmployee(Employee):
    def __init__(self, name, amount, time):
        super().__init__(name, amount)
        self.time = time
    def calculate_salary(self):
        return f"Имя - {self.amount}, Зп - * 0.5 * {self.time}"
    

def process_salary(employee):
    employee.display_info()
    salari = employee.calculate_salary()
    print (f"Зп: {salari}")

full_time = FullTimeEmployee("Султан", 20000)
part_time = ParttimeEmployee ("Аслан", 5000 , 20)

process_salary(full_time)
process_salary(part_time)

