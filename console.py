#!/usr/bin/python3
"""
    This module contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """The main cmd of the program for testing and adminstrative purposes"""

    prompt = "(hbnb) "

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id

        Usage:
            create <class name>
        """
        args = line.split()  # splitting by whitespace by default
        if not args:
            print("** class name missing **")
            return

        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        obj = BaseModel()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id

        Usage:
            show <class name> <instance id>
        """
        args = line.split()  # splitting by whitespace by default
        if not args:
            print("** class name missing **")
            return

        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        try:
            id_key = args[0] + '.' + args[1]
            desired_obj = (storage.all())[id_key]
        except KeyError:
            print("** no instance found **")
            return

        print(desired_obj)

    def do_destroy(self, line):
        """
        Deletes an instance from the JSON file
        based on the class name and id

        Usage:
            destroy <class name> <instance id>
        """
        args = line.split()  # splitting by whitespace by default
        if not args:
            print("** class name missing **")
            return

        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        try:
            id_key = args[0] + '.' + args[1]
            removing_obj = (storage.all())[id_key]
        except KeyError:
            print("** no instance found **")
            return

        storage.destroy(removing_obj)

    def do_EOF(self, line):
        """
        Exiting the program by pressing Ctrl+D
        """
        return True

    def do_quit(self, line):
        """
        Exiting the program by typing 'quit'
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
