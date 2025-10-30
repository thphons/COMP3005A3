##  Cal McLelland
#   Assignment 3
##  COMP 3005 Fall 2025

# a3.py
import code

## define banner and exit messages
bannerMsg = "COMP3005 A3!"
exitMsg = "bye!"


# create a read-eval-print loop
class Repl(code.InteractiveConsole):
    def runsource(self, source, filename="<input>", symbol="single"):
        tokens = source.split()
        command = tokens[0]
        args = tokens.pop(0)
        match command:
            case "help":
                print("help incoming...")
            case "listStudents":
                print("listing all students...")
            case "addStudent":
                print("adding new student...")
            case "updateStudentEmail":
                print("updating student email")
            case "deleteStudent":
                print("deleting student")
            case "exit" | "close" | "quit":
                print(exitMsg)
                exit(0)
            case _:
                print("command not recognized:", source)


## create an interactive console
repl = Repl()
repl.interact(banner=bannerMsg, exitmsg=exitMsg)
