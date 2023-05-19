from phrases_choice import food, sport, book
import random

if __name__ == "__main__":
    phrase_choosed = random.choice([food, sport, book])
    phrase_choosed.madlib()
