# encoding

import json
import re

class BrailleTranslator:
    """This class provides a basic latin to braille translator.
    It need a json file that is used as a dictionnary.
    """
    def __init__(self, json_filename: str='chars.json'):
        """Initializes the BrailleTranslator Object.

        Args:
            json_filename (str): The relative path to the json braille dictionnary.
            Here is an example of a file:
            ```json
            {
              " ": "⠀",
              "a": "⠁",
              "b": "⠃",
              "c": "⠉",
              "d": "⠙"
            }
            ```
        Example:
        ```python
            translator = BrailleTranslator('chars.json')
            text = "Hello World!"
            
        ```
        """
        self.chars = self.get_braills_chars(json_filename)

    def get_braills_chars(self, filename: str) -> dict:
        """Opens a chars file json file and returns its content.
        The chars file contains the tranlation of characters in braille.

        Args:
            filename (str): file name

        Returns:
            dict: python json equivalent.
        """
        with open(filename) as file:
            chars: dict = json.load(file)
        return chars

    def char_to_braille(self, char: str) -> str:
        """Returns the braille char of a text char.

        Args:
            char (str): the text char to translate.
            braille_chars (dict): the text to braille dictionnary.

        Returns:
            str: the braille char
        """
        if char in self.chars:
            return self.chars[char]
        return char

    def text_to_braille(self, text: str, spacing:str="") -> str:
        """Translates a string to braille. You can add a delimiter char between all chars.
        Unkown chars will appear as is.

        Args:
            text (str): text to translate
            spacing (str, optional): string that will be between all braille char
            for better readability. Defaults to " ".

        Returns:
            str: texty translated to braille.
        """
        braille = spacing.join(list(map(self.char_to_braille, text)))
        return braille

    def interactive(self, spacing:str=" ") -> None:
        """Interactive shell that translates all user inputs.
        """
        print('Type some text to translate and press [Enter]:\n')
        while True:
            text = input()
            # Add spaces between letters and before upper and number.
            prompt = re.sub(pattern=r'([A-Z0-9])', repl=r' \1', string=spacing.join(text))
            print(prompt)
            print(self.text_to_braille(text, spacing))

if __name__ == '__main__':

    text = 'Hello World!'
    translator = BrailleTranslator()
    braille_text = translator.text_to_braille(text)
    print(braille_text)

    translator.interactive(spacing=" ")
