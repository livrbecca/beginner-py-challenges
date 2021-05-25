def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}") # dont forget f to formatt


greet("Olivia", "Rebecca") # good practice to have 2 line breaks before calling

print(round(1.9))

# not tied to printing something, returns a vaklue which you can then do whatever with
def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Liv")