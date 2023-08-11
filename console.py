#!/usr/bin/python3
"""This module contains the entry point of the command
    interpreter
"""
import cmd
import shlex

from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """simple command processor

    Args:
        cmd (class): command line class
    """
    prompt = "(hbnb) "

    my_classes = ["BaseModel"]

    def do_quit(self, line):
        """The exit method

        Args:
            line: current input line

        Returns:
            Boolean: True
        """
        return True

    def do_EOF(self, line):
        """Checks end of file

        Args:
            line: current input line

        Returns:
            Boolean: True
        """
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel and prints the id

        Args:
            arg (str): Class name
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return
        class_dict = {"BaseModel": BaseModel}

        instance = class_dict[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance

        Args:
            arg (str): Class name and instance id
        """
        args = arg.split(" ")
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_objects = storage.all()
        for key, value in all_objects.items():
            object_name = value.__class__.__name__
            object_id = value.id
            if object_name == args[0] and object_id == args[1].strip("''"):
                print(value)
                return

        print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
         Args:
         arg (str): Class name and instance id
        """
        args = arg.split(" ")
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_objects = storage.all()
        for key, value in all_objects.items():
            object_name = value.__class__.__name__
            object_id = value.id
            if object_name == args[0] and object_id == args[1].strip("''"):
                del value
                del storage._FileStorage__objects[key]
                storage.save()
                return

        print("** no instance found **")

    def do_all(self, arg):
        """Prints string representations of all instances

        Args:
            arg (str): Optional class name

        """
        args = arg.split(" ")
        if args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return
        all_objects = storage.all()
        list_all = []
        for key, value in all_objects.items():
            object_name = value.__class__.__name__
            if object_name == args[0]:
                list_all += [value.__str__()]
        print(list_all)

    def do_update(self, arg):
        """Updates an instance based on class name and id

        Args:
            arg (str): Class name, instance id, attribute name,
            and attribute value

        """
        if not arg:
            print("** class name missing **")
            return

        # my_string = ""
        # for token in arg.split(','):
        #     my_string += token

        command_arg = shlex.split(arg)

        if command_arg[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        elif len(command_arg) == 1:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            for key, value in all_objects.items():
                object_name = value.__class__.__name__
                object_id = value.id
                if object_name == command_arg[0] and \
                        object_id == command_arg[1].strip('"'):
                    if len(command_arg) == 2:
                        print("** attribute name missing **")
                    elif len(command_arg) == 3:
                        print("** value missing **")
                    else:
                        setattr(value, command_arg[2], command_arg[3])
                        storage.save()
                    return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
