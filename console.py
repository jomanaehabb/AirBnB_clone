#!/usr/bin/python3
"""
    This module contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """The main cmd of the program for testing and adminstrative purposes"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exiting the program by pressing Ctrl+D
        """
        return True

    def do_quit(self, line):
        """Exiting the program by typing 'quit'
        """
        return True

    def emptyline(self):
        """Do nothing when pressing Enter"""
        pass

    # def postcmd(self, stop, line):
    #     if stop:
    #         if line.strip().lower() == "quit":
    #             print("Exiting with 'quit' command...")
    #         elif line.strip() == "":
    #             print("Exiting with Ctrl+D (EOF)...")
    #         else:
    #             print("Exiting for an unknown reason.")
    #     return stop


if __name__ == '__main__':
    HBNBCommand().cmdloop()
