def choose_practicum():
    some_string = input("sign up for a practicum")
    if some_string == "Lighting": 
        return some_string 
    if some_string == "Scenery":
        return some_string
    if some_string == "Costumes":
       return some_string
    if some_string == "Sound":
        return some_string
    return choose_practicum()

name = input("what is your name?")
choice = choose_practicum()
print (f"Congratulations{name} you are signed up for {choice} ")