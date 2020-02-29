command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print('Car is already started')
        else:
            started = True
            print("Ready to go")
    elif command == "stop":
        if not started:
            print('Car is already stopped')
        else:
            started = False
            print("Stopping the car")
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


