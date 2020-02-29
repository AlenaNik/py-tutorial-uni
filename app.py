command = ""
while command.lower() != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Ready to go")
    elif command == "stop":
        print("Stoppint the car")
    elif command == "help":
        print("""
        start - to start,
        stop - top stop,
        quit - to quit
        """)
    elif command == "quit":
        exit()
    else:
        print("Sorry no command recognized")


