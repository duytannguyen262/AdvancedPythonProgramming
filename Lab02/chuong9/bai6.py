text=""

while text.lower() != "quit":
     text = input("What's Your Name(or 'quit' to exit):")
     if text.lower() == "quit":
         print("_exiting program")
     else: print("Welcome",text)
    