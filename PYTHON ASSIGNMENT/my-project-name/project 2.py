name = input("what is your name?:")
print("Hello", name, "! Nice to meet you.")
feeling = input("How are you feeling today?")
if feeling.lower() == "good":
    print("That's nice to hear!")
elif feeling.lower() == "bad":
    print("I'm sorry to hear that. I hope you feel better soon.")
else:
    print("Thank you for sharing how you feel.")