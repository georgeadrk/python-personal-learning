words: dict = {}

class FlashcardTrainer():
    def showOptions(self) -> None:
        print("1. Add new word")
        print("2. Practice (random word quiz)")
        print("3. View all words")
        print("4. Quit")

    def addWord(self) -> None:
        word: str = input('Word: ')
        defi: str = input('Definition: ')
        words[word] = defi
