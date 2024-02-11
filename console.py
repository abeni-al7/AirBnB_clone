#!/usr/bin/python3
"""Entry point of command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter"""

    prompt = "(hbnb) "
    def do_quit(self, line):
        """quit: quits the interpreter"""
        return True
    
    def do_EOF(self, line):
        """EOF: quits the interpreter"""
        return True
    
    def emptyline(self):
        """Empty line: does nothing"""
        pass

    def help_quit(self):
        """Help for quit"""
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        """Help for EOF"""
        print("EOF: quits the interpreter")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
