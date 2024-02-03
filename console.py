#!/usr/bin/python3
"""HBNBCommand console
"""


import cmd
import os
import shlex
from cmd import sys

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """A console to interact with my database
    """
    prompt = "(hbnb) "

    def do_create(self, args):
        """Creates a new instance of BaseModel
        """
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            cls_object = globals().get(args[0], None)
            if cls_object:
                instance = cls_object()
                instance.save()
                print(instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        """
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key in all_objects:
                print(all_objects.get(key))
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        """
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation of all instances
        """
        my_list = list()

        args = shlex.split(args)
        if len(args) == 0:
            for val in storage.all().values():
                my_list.append(str(val))
            print('[', end="")
            print(', '.join(my_list), end="")
            print(']')

        elif args[0] in classes:
            for arg_id in storage.all():
                if args[0] in arg_id:
                    my_list.append(str(storage.all()[arg_id]))

            print('[', end="")
            print(', '.join(my_list), end="")
            print(']')

        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id
        """
        int_lst = [
            "number_rooms", "number_bathrooms", "max_guest", "price_by_night"
        ]

        float_lst = ["latitude", "longitude"]

        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return False

        elif args[0] in classes:
            if len(args) > 1:
                arg_id = "{}.{}".format(args[0], args[1])
                if arg_id in storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "place":
                                if args[2] in int_lst:
                                    try:
                                        args[3] = int(args[3])
                                    except Exception:
                                        args[3] = 0.0
                                elif args[2] in float_lst:
                                    try:
                                        args[3] = float(args[3])
                                    except Exception:
                                        args[3] = 0.0
                            setattr(
                                storage.all()[arg_id], args[2], args[3]
                            )
                            storage.all()[arg_id].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_shell(self, shellcmd):
        "Run a shell command"
        os.system(shellcmd)

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Exits the console
        """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
