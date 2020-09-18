
print("Input 'help' if you are unable to do anything.")
Command = ''
while Command.lower() != "quit":
    Command = input("> ").lower()
    if Command == "start":
        print("The car has started and is running.")
    elif Command == "stop":
        print("The car has stopped.")
    elif Command == "help":
        print("""
      start-the car starts.
      stop-the car stops.
      quit-you quit the game.
      """)
    elif Command == "quit":
        break
else:
    print("I don't know what this command means.")

