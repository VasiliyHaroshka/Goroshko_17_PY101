class Tomato:
    """
    Class for describe tomato. Class has two attributes: index and state which describe stage life of tomato.
    Objects of this class can grow (change stage of development) and method for checking its ripe
    (the last stage of tomato's life).
    """
    states: list = ["seed", "little_plant", "green_tomatoes", "red_tomatoes"]
    _index: int
    _state: list

    def __init__(self, index=0) -> None:
        self._index = index
        self._state = self.states[self._index]

    def grow(self) -> None:
        """
        When you call this method object of Tomato class changes its stage of development (grows).
        This method limit stage of tomato's development.
        :return: None
        """
        try:
            self._index += 1
            self._state = self.states[self._index]
        except IndexError:
            print("Tomato can not grow more")
            self._index -= 1

    def is_rape(self) -> bool:
        """
        Checking is tomato reach its last stage of development. Returns True if it is and False otherwise.
        :return: Returns True if tomato has stage "red_tomatoes" and False otherwise.
        """
        if self.states[self._index] == "red_tomatoes":
            return True
        else:
            return False


class TomatoBush:
    """
    Class for description some tomatoes on one bush.
    Class has methods for growing all tomatoes on the bush, check if they are ripe or not
    and clear the bush from tomatoes.
    """
    tomatoes: list

    def __init__(self, quantity_tomatoes) -> None:
        self.tomatoes = [Tomato() for _ in range(quantity_tomatoes)]

    def grow_all(self) -> None:
        """
        Method calls method grow from class Tomato for each tomato on the bush
        :return: None
        """
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self) -> bool:
        """
        Method calls method is_rape from class Tomato for each tomato on the bush
        :return: True if all tomatoes on the last stage of their development and False if it is not
        """
        for i in self.tomatoes:
            if not i.is_rape():
                return False
        return True

    def give_away_all(self) -> None:
        """
        Defines index = 0 for stage of development all tomatoes on the bush.
        Returns all tomatoes on the bush to the first stage of development (seed)
        :return: None
        """
        for i in self.tomatoes:
            i._index = 0


class Gardener:
    """
    Class describe gardener who has name and amout of his tomatoes.
    Class has methods: work that enhance stage of tomato's development,
    harvest that check if tomatoes are ripe and gather them from the bush if they are
    and knowledge_base that contains information about growing and harvesting tomatoes
    """
    name: str
    _plant: TomatoBush

    def __init__(self, name) -> None:
        self.name = name
        self._plant = TomatoBush(n)

    def work(self):
        """
        All tomatoes grow and change their stage of development to next
        Call method plant.grow_all for all gardener's tomatoes
        :return:
        """
        self._plant.grow_all()

    def harvest(self):
        """
        Method checks if all tomatoes are ripe and, if it is, harvest them for the bush
        Prints inform messages for cases if tomatoes ready to harvest or not
        :return: None
        """
        if self._plant.all_are_ripe():
            print(f"Let's go harvest.\nHarvest was gathered. {self.name.title()}, good work.")
            self._plant.give_away_all()
        else:
            print(f"There is no time to harvest. {self.name.title()}, continue working.")

    @staticmethod
    def knowledge_base() -> None:
        """
        Method shows description how to plant and harvest tomatoes
        :return:None
        """
        print("This is description how to plant and harvest tomatoes\n"
              "Call method work several times to growtomatoes and they will change their stage of life "
              "from seed to little_plant, from little_plant to green tomatoes, from green tomatoes to red tomatoes.\n"
              "Call method harvest to harvest your crop if your tomatoes are ripe.\n"
              "Have a good time!\n")


if __name__ == "__main__":
    Gardener.knowledge_base()
    n = int(input("Input amount of tomatoes on the bush: "))
    bush1 = TomatoBush(n)
    red_neck = input("Input name of a gardener: ")
    gardener = Gardener(red_neck)
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
