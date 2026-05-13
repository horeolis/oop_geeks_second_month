
# __init__

class Test:

    # Class_Name()
    def __init__(self, value):
        self.value = value

    # print()
    def __str__(self):
        return f"{self.value}"

    # +
    def __add__(self, other):
        print(self.value)
        print(other.value)
    # -
    # def __sub__(self, other):
    # *
    # def __mul__(self, other):
    # /
    # def __truediv__(self, other):

    # ==
    # def __eq__(self, other):

    def __getitem__(self, item):
        return self.value[item]

obj_1 = Test(12)
obj_2 = Test(21)

# my_sum = obj_1 + obj_2
# print(my_sum)

# my_list = [1,2,3,4,5]
#
# obj_3 = Test([1,2,3,4,5])
# test_1 = obj_3[2]
# print(test_1)


class Money:

    def __init__(self, value, currency):
        self.value = value
        self.currency = currency
        self.view_count = 0

    def __add__(self, other):
        return self.value + other.value

    # def __eq__(self, other):
    #     if self.currency != other.currency:
    #

    def __call__(self, *args, **kwargs):
        print("View")

# {
#   "str": 123
#   123: 123
# }


# news_1 = Money(5, "USD")
# news_2 = Money(250, "SOM")
# news_3 = Money(250, "SOM")

# if tran_1 == tran_2:
#     # soncert_to_som(usd)


# if tran_1 != tran_2:
    # soncert_to_som(usd)

# news_3()

class BankAccount:
    # Атрибута класса
    bank_name = "Simba"

    def __init__(self, first_name, last_name, balance):
        # Атрибута экземпляра класса
        self.first_name = first_name
        self._last_name = last_name
        self.__balance = balance


    def get_name(self):
        return self.first_name

    @staticmethod
    def add(a ,b):
        return a + b

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    @property
    def full_name(self):
        return f"{self.first_name} {self._last_name}"

    @property
    def my_balance(self):
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        if self.__balance == 0 or value < 0:
            print("Ошибка!!")
        else:
            self.__balance = value


ardager1 = BankAccount("Ardager", "Kartanbekov", 100)
ardager = BankAccount(ardager1, "Kartanbekov", 100)

# print(BankAccount.add(12, 13))
print(ardager.my_balance)
ardager.my_balance = -100
print(ardager.my_balance)

print(type(ardager1))
print(type(ardager))