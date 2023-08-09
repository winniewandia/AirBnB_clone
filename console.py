#!/usr/bin/python3
"""This module contains the entry point of the command
    interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """simple command processor

    Args:
        cmd (class): command line class
    """
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
