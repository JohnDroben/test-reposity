
class Store():
    def __init__(self,name,adress):
        self.name = name
        self.adress = adress
        self.item = {

        }

    def add_item(self, item_product, item_price):
        """Добавляет товар в ассортимент магазина"""
        self.item [item_product]= item_price

    def remove_item(self, item_product):
        """Удаляет товар из ассортимента, если он существует"""
        if item_product in self.item:
                      del self.item [item_product]

    def get_price(self, item_product):
        """Возвращает цену товара по его названию, иначе None"""
        return self.item.get(item_product, None)

    def update_item_price(self, item_product, new_price):
        """Обновляет цену товара, если он существует"""
        if item_product in self.item:
            self.item[item_product] = new_price


store1 = Store ("Магазин у дома", "Улица Пушкина,15")
store2 = Store ("Супермаркет", "Улица Ленина, 25")
store3 = Store ("Эко-магазин", "Улица Зеленая, 30")

# Добавление товаров в ассортимент магазинов
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2.add_item("молоко", 1.2)
store2.add_item("хлеб", 0.6)

store3.add_item("орехи", 2.5)
store3.add_item("фрукты", 1.0)

# Тестирование методов на первом магазине
print(f"Товары в магазине '{store1.name}': {store1.item}")

# Добавление нового товара
print("\nДобавление нового товара 'груши' за 0.80...")
store1.add_item("груши", 0.8)
print(f"Обновленный ассортимент: {store1.item}")

# Обновление цены товара
print("\nОбновление цены на 'яблоки' до 0.6...")
store1.update_item_price("яблоки", 0.6)
print(f"Обновленный ассортимент: {store1.item}")

# Удаление товара
print("\nУдаление товара 'бананы'...")
store1.remove_item("бананы")
print(f"Обновленный ассортимент: {store1.item}")

# Запрос цены товара
item_product = "груши"
price = store1.get_price(item_product)
if price is not None:
    print(f"Цена '{item_product}' в магазине '{store1.name}': {price} руб.")
else:
    print(f"Товар '{item_product}' отсутствует в магазине '{store1.name}'.")



