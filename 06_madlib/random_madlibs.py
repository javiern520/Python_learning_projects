from sample_madlibs import hp, hunger, twilight, davinci
import random

if __name__ == "__main__":
    m = random.choice([hp, hunger, twilight, davinci])
    m.madlib()