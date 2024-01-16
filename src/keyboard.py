from src.item import Item


class MixinKeyboard:
    """
    Миксин для класса Keyboard.
    """
    def __init__(self) -> None:
        self.__language = "EN"

    def change_lang(self) -> None:
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

    @property
    def language(self) -> str:
        return self.__language


class Keyboard(Item, MixinKeyboard):
    """
    Класс Keyboard.
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        MixinKeyboard.__init__(self)

    def __repr__(self) -> str:
        return f"{super().__repr__()} {self.language}"
