class Human:
    default_name = "Alex"
    default_age = 18

    def __init__(self, money, house, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    def info(self):
        print(self.name, self.age, self.__money, self.__house, sep="\n")

    @staticmethod
    def default_info(self):
        print(self.default_name, self.default_age, sep="\n")

    def earn_money(self, income):
        self.__money += income
        print(self.__money)

    def __make_deal(self, house, house_price):
        self.house = house
        self.__money -= house_price

    def buy_house(self, house, discount):
        if self.__money >= house.final_price(discount):
            print("Congratulations! You bought this house.")
        else:
            print("You don't have enough money.")


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        self._price = self._price * ((100 - discount) / 100)
        return self._price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == "__main__":
    p = Human(700, "no house")
    sh = SmallHouse(900)
    p.buy_house(sh, 10)
    p.earn_money(200)
    p.buy_house(sh, 10)
