class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

store1 = Store("Пятерочка", "Кировоградская, 42")
store2 = Store("Колумбус", "Кировоградская, 13А")
store3 = Store("ВкусВилл", "Кировоградская, 23")

store1.add_item("яблоки", 250)
store1.add_item("бананы", 105)

store2.add_item("монитор MSI", 25000)
store2.add_item("Клавиатура ASUS", 1500)

store3.add_item("суп том-ям", 500)
store3.add_item("креветки охлажденные", 1000)

store1.update_price("яблоки", 205)

print(f"Цена на яблоки {store1.name}: ${store1.get_price('яблоки')}")

store2.remove_item("Клавиатура ASUS")

for store in [store1, store2, store3]:
    print(f"Магазин: {store.name}, Адрес: {store.address}, Товары: {store.items}")