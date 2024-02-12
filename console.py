#!/usr/bin/python3
"""Entry point of command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter"""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
    }
    def do_quit(self, line):
        """quit: quits the interpreter"""
        return True
    
    def do_EOF(self, line):
        """EOF: quits the interpreter"""
        return True
    
    def do_create(self, line):
        """Create command for BaseModel instance"""
        args = line.split()
        if len(args) < 2:
            print("** class name missing **")
        elif args[1] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[1])().id)
            storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()
        obj_dict = storage.all()
        if len(args) < 2:
            print("** class name missing **")
        elif args[1] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 3:
            print("** instance id missing **")
        elif "{}.{}".format(args[1], args[2]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict("{}.{}".format(args[1], args[2])))

    def do_destroy(self, line):
        """Destroy an instance"""
        args = line.split()
        obj_dict = storage.all()
        if len(args) < 2:
            print("** class name missing **")
        elif args[1] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 3:
            print("** instance id missing **")
        elif "{}.{}".format(args[1], args[2]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict[".".join(args[1], args[2])]
            storage.save()

    def do_all(self, line):
        """Prints the string representation of all instances"""
        args = line.split()
        if len(args) > 1 and args[1] not in HBNBCommand.__classes:
            print("** class doesn't exist")
        else:
            objects = []
            for object in storage.all().values():
                if len(args) > 1 and args[1] == object.__class__.__name__:
                    object.append(object.__str__())
                elif len(args) == 0:
                    object.append(object.__str__())
            print (object)

    def do_update(self, line):
        """Updates an instance"""
        args = line.split()
        obj_dict = storage.all()
        if len(args) == 1:
            print("** class name missing **")
            return False
        if args[1] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 2:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[1], args[2]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(args) == 3:
            print("** attribute name missing **")
            return False
        if len(args) == 4:
            try:
                type(eval(args[3])) != dict
            except NameError:
                print("** value missing **")
                return False    
        if len(args) == 5:
            obj = obj_dict["{}.{}".format(args[1], args[2])]
            if args[3] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[3]])
                obj.__dict__[args[3]] = valtype(args[4])
            else:
                obj.__dict__[args[3]] = args[4]
        elif type(eval(args[3])) == dict:
            obj = obj_dict["{}.{}".format(args[1], args[2])]
            for k, v in eval(args[3]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

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
