name = input("What is your name? ").strip()

if name[-1] == "!":
    print(f"HELLO {name.upper()} WHY ARE WE YELLING?")
else:
    print(f"Hello {name}.")