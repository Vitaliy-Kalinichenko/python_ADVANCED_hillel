# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить
from validate_email import validate_email


class EmailDescriptor:
    def __get__(self, instance, owner):
        # your code here
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not validate_email(value):
            raise ValueError('email is incorrect')
        instance.__dict__[self.__name] = value

    def __set_name__(self, owner, name):
        self.__name = name


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()
my_class.email = "validemail@gmail.com"
print(my_class.email)
# my_class.email = "novalidemail"
# Raised Exception
print(my_class.email)


# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


c = MyClass()
b = MyClass()
assert id(c) == id(b)


# Задача-3
# реализовать дескриптор IngegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен

class IngegerField:
    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    def __set_name__(self, owner, name):
        self.__name = name


class Data:
    number = IngegerField()


data_row = Data()
new_data_row = Data()

data_row.number = 5
new_data_row.number = 10

assert data_row.number != new_data_row.number


# Задача4
# Необходимо создать модели работы со складскими запасами товаров и процесса оформления заказа этих товаров.
# Cписок требований:
# 1) Создайте товар с такими свойствами, как имя(name), подробные сведения(description or details),
# количество на складе(quantity), доступность(availability), цена(price).
# 2) Добавить товар на склад
# 3) Удалить товар со склада
# 4) Распечатать остаток товара по его имени
# 5) Распечатать остаток всех товаров
# 6) Товар может принадлежать к категории
# 7) Распечатать список товаров с заданной категорией

# Добавить к этой задаче дескриптор для аттрибута цена.
# При назначении цены товара будет автоматически добавлен НДС 20%
# При получении цены товара, цена возврщается уже с учетом НДС
class PriceDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Cannot be negative.')
        instance.__dict__[self.__name] = value * 1.2

    def __set_name__(self, owner, name):
        self.__name = name


class MyWarehouse:
    price = PriceDescriptor()
    warehouse = {}

    def __init__(self, name, description_or_details, quantity, price, category, availability=True):
        self._name = name.lower()  # имя будет идентификатором товара
        self._description_or_details = description_or_details
        self._quantity = quantity
        self.price = price
        self._category = category.lower()
        self._availability = availability

    def __repr__(self):
        return self._name

    # 2) Добавить товар на склад
    def add_item_to_warehouse(self):
        """This method adds an item to the warehouse"""
        if self._name in MyWarehouse.warehouse:  # если товар с таким именем уже есть на складе добовляем ему кол-во
            MyWarehouse.warehouse[self._name]['_quantity'] += self._quantity
        else:
            MyWarehouse.warehouse[self._name] = self.__dict__

    # 3) Удалить товар со склада
    def remove_item_from_warehouse(self):
        """This method removes the item from the warehouse."""
        del MyWarehouse.warehouse[self._name]

    # 4) Распечатать остаток товара по его имени
    @classmethod
    def remainder_goods_by_name(cls, name):
        """This method prints the remainder goods by its name."""
        if name.lower() in cls.warehouse:
            print(f"{cls.warehouse[name.lower()]['_name']} - "
                  f"remainder {cls.warehouse[name.lower()]['_quantity']} pieces")
        else:
            print('The goods is out of stock')

    # 5) Распечатать остаток всех товаров
    @classmethod
    def remainder_goods(cls):
        """This method prints the remainder of all goods."""
        if not cls.warehouse:
            print('The goods is out of stock')
        else:
            for goods in cls.warehouse.values():
                print(f"{goods['_name']} - remainder {goods['_quantity']} pieces")

    # 7) Распечатать список товаров с заданной категорией
    @classmethod
    def get_goods_from_category(cls, category):
        print(*[goods['_name'] for goods in cls.warehouse.values() if goods['_category'] == category.lower()], sep=', ')

    @classmethod
    def _get_availability_for_order(cls, name):
        """This method returns the availability of an item for an order."""
        if name.lower() in cls.warehouse:
            return cls.warehouse[name.lower()]['_quantity']

    @classmethod
    def _get_price_for_order(cls, name):
        """This method returns the price of an item for an order."""
        return cls.warehouse[name.lower()]['price']

    @classmethod
    def _reduce_quantity_goods(cls, name, quantity):
        cls.warehouse[name.lower()]['_quantity'] -= quantity


# 8) Корзина для покупок, в которой может быть много товаров с общей ценой.
# 9) Добавить товары в корзину (вы не можете добавлять товары, если их нет в наличии)
# 10) Распечатать элементы корзины покупок с ценой и общей суммой
# 11) Оформить заказ и распечатать детали заказа по его номеру
# 12) Позиция заказа, созданная после оформления заказа пользователем.
# Он будет иметь идентификатор заказа(order_id), дату покупки(date_purchased), товары(items), количество(quantity)
# 13) После оформления заказа количество товара уменьшается на количество товаров из заказа.
from datetime import date


class ShoppingBag(MyWarehouse):
    order_id = 0

    def __init__(self):
        self._bag = {}

    # 9) Добавить товары в корзину (вы не можете добавлять товары, если их нет в наличии)
    def add_goods_to_bag(self, name, quantity):
        availability = super()._get_availability_for_order(name)  # получаем наличие товара на складе
        if availability >= quantity:  # если остаток товара больше заказа, доб в корзину
            self._bag[name] = quantity
        elif availability:
            print(f'Only {availability} available')
        else:
            print('Out of stock')

    # 10) Распечатать элементы корзины покупок с ценой и общей суммой
    def get_composition_bag(self):
        """This method prints the composition of the shopping bag with price and total"""
        if self._bag:
            for name, quantity in self._bag.items():
                price = super()._get_price_for_order(name)  # получаем цену на товар
                print(f'{name}, price - {price:.2f}, quantity - {quantity}, total amount - {price * quantity:.2f}')
        else:
            print('Shopping bag is empty')

    # 11) Оформить заказ и распечатать детали заказа по его номеру
    def place_order(self):
        if self._bag:
            date_purchased = date.today()
            print(f'Order - {ShoppingBag.order_id}, purchase date - {date_purchased}')
            self.get_composition_bag()
            data_order = {  # 12) Позиция заказа, созданная после оформления заказа пользователем.
                'order id': ShoppingBag.order_id,
                'purchase date': date_purchased,
                'composition bag': self._bag
            }
            for name, quantity in self._bag.items():  # 13) После оформления заказа количество товара уменьшается
                # на количество товаров из заказа.
                super()._reduce_quantity_goods(name, quantity)
            self._bag = {}  # обнуляем корзину
            ShoppingBag.order_id += 1
        else:
            print('Shopping bag is empty')


t_shirt = MyWarehouse('T-shirt', 'L', 20, 300, 'clothes')
print(t_shirt.price)  # цена с учетом ндс
t_shirt.add_item_to_warehouse()  # добовляем товр на склад
print(MyWarehouse.warehouse)  # содержимое склада
t_shirt1 = MyWarehouse('T-shirt', 'L', 20, 300, 'clothes')  # новый экзем, тот же товар
t_shirt1.add_item_to_warehouse()  # добовляем товр на склад
print(MyWarehouse.warehouse)  # содержимое склада
jeans = MyWarehouse('Jeans', 'M', 50, 700, 'clothes')  # новый экзем, новый товар
jeans.add_item_to_warehouse()  # добовляем товр на склад
# jeans.remove_item_from_warehouse()
jeans.remainder_goods_by_name('jeans')  # Распечатать остаток товара по его имени
jeans.remainder_goods()  # 5) Распечатать остаток всех товаров
MyWarehouse.get_goods_from_category('clothes')  # 7) Распечатать список товаров с заданной категорией

order1 = ShoppingBag()  # создаем заказ
order1.add_goods_to_bag('T-shirt', 10)  # добавляем товар в корзину
order1.add_goods_to_bag('Jeans', 5)  # добавляем товар в корзину
# print(order1._bag)
order1.get_composition_bag()  # 10) Распечатать элементы корзины покупок с ценой и общей суммой
order1.place_order()  # 11) Оформить заказ и распечатать детали заказа по его номеру

MyWarehouse.remainder_goods()  # 5) Распечатать остаток всех товаров
