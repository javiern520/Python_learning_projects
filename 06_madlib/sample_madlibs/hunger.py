def madlib():
    
    name = input("Name: ")
    num = input("Number: ")
    gb = input("Girl or boy: ")
    land = input("Country name: ")
    land2 = input("Country name: ")
    verb = input("Verb in past tense: ")
    noun = input("Noun in plural: ")
    noun2 = input("Living thing: ")
    noun3 = input("Living thing: ")
    event = input("Event name: ")
    verb2 = input("Verb: ")
    verb3 = input("Verb in past tense: ")
    
    madlib = f"{name} is a {num}-year-old {gb} living with her mother and younger sister in the poorest district of {land}, the remains of what used be the {land2}. Long ago the districts waged war on the Capitol and were {verb}. As part of the surrender {noun}, each district agreed to send one {noun2} and one {noun3} to appear in an annual televised event called, {event}. The terrain, rules, and level of audience participation may change but one thing is constant: {verb2} or be {verb3}. When {name}'s {noun3} is chosen by lottery, {name} steps up to go in its place."
    
    print(madlib)