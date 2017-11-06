"""
Vocalizator class
- Vocalize string
"""

import pyttsx3;

class Vocalizator:
    """ Vocalizator class """
    def __init__(self):
        """ init class """
        self.engine = pyttsx3.init()

    def voice(self, str):
        """ voice the string """
        self.engine.say(str)
        self.engine.runAndWait()

if __name__ == "__main__":
    vocalizator = Vocalizator()
    vocalizator.voice("Hello World!")
    