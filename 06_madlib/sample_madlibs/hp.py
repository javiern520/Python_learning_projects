def madlib():
    mon = input("month with capital letter: ")
    adj = input("adjective: ")
    noun = input("noun in plural: ")
    noun2 = input("noun in singular: ")
    char = input("Harry potter character: ")
    prof = input("Profession: ")
    potion = input("name of potion: ")
    verb = input("verb in present continuous: ")
    body_p = input("body part: ")
    time = input("time noun plural: ")
    char2 = input("Harry Potter character: ")
    f = input("is a female character? ")
    if f == "yes":
        pro ="her"
    else:
        pro ="his"
    char3 = input("Harry Potter character: ")
    body_p2 = input("body part: ")
    body_p3 = input("body part: ")
    noun3 = input("singular noun: ")
    
    madlib = f"{mon} arrived, spreading a damp {adj} over the {noun} and into the {noun2}. {char}, the {prof}, was kept busy by a sudden spate of colds among the staff and students. Her {potion} potion worked instantly, though it left the drinker {verb} at the {body_p} for several {time} afterward. {char2}, who had been looking pale, was bullied into taking some by {char3}. The steam pouring from under {pro} vivid {body_p2} gave the impression that {pro} whole {body_p3} was on fire."
    
    print(madlib)
    