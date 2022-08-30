# Introduction to string concatenation (how to put strings together)
# suppose we want to create a string that says "subscribe to _____"
#youtuber = "Javier_is_awsome" # some string variable

# a few ways to do this
#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

adj = input('Insert an adjective :')
adj2 = input('Insert an adjective :')
verb = input('Insert a verb :')

madlib = f"Programming is so {adj}. It makes me feel {adj2}, while programming, my mid and brain {verb} to a 100%"

print(madlib)