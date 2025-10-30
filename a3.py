# repl.py
import code

## define banner and exit messages
bannerMsg = "COMP3005 A3!"
exitMsg = "bye!"


class Repl(code.InteractiveConsole):
    def runsource(self, source, filename="<input>", symbol="single"):
        match source:
            case "help":
                print("help incoming...")
            case _:
                print("command not recognized:", source)


## create an interactive console
repl = Repl()
repl.interact(banner=bannerMsg, exitmsg=exitMsg)
