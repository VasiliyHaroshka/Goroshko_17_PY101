from string import ascii_lowercase


class Alphabet:
    """
    Class Alphabet is used for storage letters and their amount certain language.
    """
    lang: str
    letters: list

    def __init__(self, lang, letters) -> None:
        self.lang = lang
        self.letters = list(letters)

    def print(self) -> None:
        """
        Print list of letters
        :return: None
        """
        print(*self.letters)

    def letters_num(self):
        """
        Return length of letter's list
        :return: int
        """
        return len(self.letters)


class EngAlphabet(Alphabet):
    """
    Class EngAlphabet is inherited from class Alphabet.
    It is contains letters of English alphabet
    """
    __letters_num: int = 26

    def __init__(self):
        super().__init__(lang="En", letters=ascii_lowercase)

    def is_en_letter(self, latter: str) -> None:
        """
        Method takes a letter and checks if it from english alphabet. Prints necessary message
        :param latter: letter for checking
        :return: None
        """
        if latter.lower() in self.letters:
            print("This letter exists in English alphabet.")
        else:
            print("This letter is not in English alphabet.")

    def letters_num(self) -> int:
        """
        Reads private attribute 'letters_num' of class and return it
        :return: attribute 'letters_num'
        """
        return self.__letters_num

    @staticmethod
    def example() -> str:
        """
        Contains a sample of English text and return it
        :return: a sample of English text
        """
        return "The quick brown fox jumps over the lazy dog."


if __name__ == "__main__":
    eng_alph = EngAlphabet()
    eng_alph.print()
    print(eng_alph.letters_num())
    eng_alph.is_en_letter("F")
    eng_alph.is_en_letter("ш")
    print(eng_alph.example())
