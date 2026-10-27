white = 0
oolong = 0
green = 0
herbal = 0

name = input ("I heard you want tea, so tell me, what's your name?: ")
print ()
print ("So you're name is", str(name) + ".")
print ()
print ("I'm going to ask you a series of questions to find out what kind of tea you like. Answer with 'Y' or 'N'.")
print ()

# question 1

q1 = input ("1. Do you prefer a slow and quiet morning over a fast and lively routine? (Y/N): ")
if q1 == "Y":
    white += 1
elif q1 == "N":
    herbal += 1

if q1 != "Y" or q1 != "N":
    print ("Please answer with 'Y' or 'N'.")
print ()

# question 2
q2 = input ("Do you like going with the flow over following a strict plan? (Y/N): ")
if q2 == "Y":
    herbal += 1
elif q2 == "N":
    oolong += 1

if q2 != "Y" or q2 != "N":
    print ("Please answer with 'Y' or 'N'.")
print ()

# question 3
q3 = input ("3. Do you think you are more of an extrovert over an introvert? (Y/N): ")
if q3 == "Y":
    green += 1
elif q3 == "N":
    herbal += 1

if q3 != "Y" or q3 != "N":
    print ("Please answer with 'Y' or 'N'.")
print ()

# question 4
q4 = input ("When you are stressed, do you like to unplug completely rather than venting to others? (Y/N): ")
if q4 == "Y":
    white += 1
elif q4 == "N":
    green += 1

if q4 != "Y" or q4 != "N":
    print ("Please answer with 'Y' or 'N'.")
print ()

# question 5
q5 = input ("Do you consider yourself more of a night owl than a morning lark? (Y/N): ")
if q5 == "Y":
    green += 1
elif q5 == "N":
    oolong += 1

if q5 != "Y" or q5 != "N":
    print ("Please answer with 'Y' or 'N'.")
print ()

# question 6
q6 = input ("Do you like solving and analyzing complex problems? (Y/N): ")
if q6 == "Y":
    oolong += 1
elif q6 == "N":
    herbal += 1

if q6 != "Y" or q6 != "N":
    print ("Please answer with 'Y' or 'N'.")
print ()

# print ("Oolong:", oolong)
# print ("Green:", green)
# print ("White:", white)
# print ("Herbal:", herbal)

pref = max(oolong, green, white, herbal)

if pref == oolong:
    pref = "oolong tea"
    pers = "You are calm, nurturing, and empathetic, often acting as the soothing peacekeeper in your social circle"
elif pref == green:
    pref = "green tea"
    pers = "You are patient, open-minded, and health-conscious, possessing a refined appreciation for life's complex and layered moments."
elif pref == white:
    pref = "white tea"
    pers = "You are gentle, intuitive, and harmonious, often seeking balance and tranquility in your daily life."
elif pref == herbal:
    pref = "herbal tea"
    pers = "You are a minimalist and a deep thinker who values gentle simplicity, purity, and meaningful connections."

print ("Based on your answers, you must like", pref + ".")
print ()
print (pers)
print ()
# sweetness
sweetness = input ("Do you like your tea sweet? (Y/N): ")
if sweetness == "Y":
    print ("So you'resweet?")
    numsweet = input ("How sweet do you like your tea? (1-10): ")
elif sweetness == "N":
    print ("So you're bitter? (Nothing wrong with that, I like my tea bitter too.)")
if sweetness != "Y" or sweetness != "N":
    print ("You're not getting anything. Please answer with 'Y' or 'N'.")
print ()

print ("You'd like your", pref, "to have", numsweet, "sugar cubes.")

print ("Thank you for taking the tea preference quiz, " + name + ". I hope you like your tea!")
