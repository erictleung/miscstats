"""This module defines the basic class for all distributions"""

class BaseDist:
    """Common base class for all probability distributions"""

    def __init__(self, name):
        self.name = name

    def display_name(self):
        """Print out name of distribution"""
        print(self.name)

    def __str__(self):
        return str(f"{self.__class__.__name__} class str")
