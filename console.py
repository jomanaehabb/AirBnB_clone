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
            storage.destroy(removing_obj)
            del removing_obj
        except KeyError:
            print("** no instance found **")
            return

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name

        Usage:
            all
            all <class name>
        """
        objs_list = []
        args = line.split()  # splitting by whitespace by default
        if args:
            if args[0] in ["BaseModel"]:
                class_name = args[0]
                objs_dict = storage.all()
                for key in objs_dict.keys():
                    if objs_dict[key].__class__.__name__ == class_name:
                        objs_list.append(str(objs_dict[key]))
                print(objs_list)
                return
            else:
                print("** class doesn't exist **")
                return

        objs_dict = storage.all()
        for key in objs_dict.keys():
            objs_list.append(str(objs_dict[key]))
        print(objs_list)

    def do_update(self, line):
        """
        Updates an instance in the JSON file
        based on the class name and id, updating
        only one key-value pair, so any more key-value
        pairs coming after first one will be ignored

        Usage:
            update <class name> <instance id> <attribute name> <value>

        Pre-Conditions and Assumptions:
            id, created_at, upated_at cannot't be passed as arguments
            attribute value must be formatted as "<value>"
            attribute name will always be existed (valid) for the instance
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

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        try:
            id_key = args[0] + '.' + args[1]
            desired_obj = (storage.all())[id_key]
        except KeyError:
            print("** no instance found **")
            return

        setattr(desired_obj, args[2], (args[3])[1:-1])
        desired_obj.save()

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
