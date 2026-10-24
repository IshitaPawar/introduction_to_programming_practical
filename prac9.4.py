def greet(name, message="Hello"):
    print(message, name)

greet("Asha")                         # Uses the default message
greet("Ravi", "Good morning")         # Positional arguments
greet(message="Welcome", name="Meera")  # Keyword arguments
