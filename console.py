#!/usr/bin/python3
"""HBNBCommand console
"""


import cmd
import os
import shlex
import ast

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

    def _args_spliter(self, args):
        """Helper method to help split arguments."""
        return shlex.split(args)
    
    def _get_instance_key(self, cls_name, instance_id):
        """Helper method to get the instance key in the storage."""
        return f"{cls_name}.{instance_id}"

    def do_create(self, args):
        """Creates a new instance of BaseModel
        """
        args = self._args_spliter(args)
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
        args = self._args_spliter(args)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = self._get_instance_key(args[0], args[1])
            if key in all_objects:
                print(all_objects.get(key))
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        """
        args = self._args_spliter(args)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = self._get_instance_key(args[0], args[1])
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation of all instances
        """
        args = self._args_spliter(args)
        if args[0] not in classes:
            print("** class doesn't exist **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            all_objects = storage.all()
            objects_list = []
            for key, value in all_objects.items():
                if args[0] in key:
                    objects_list.append(str(value))
            print(objects_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id
        """

        args = self._args_spliter(args)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = self._get_instance_key(args[0], args[1])
            if key in all_objects:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    try:
                        converted_val = ast.literal_eval(args[3])
                    except (ValueError, SyntaxError):
                        converted_val = args[3]
                    setattr(
                        all_objects[key], args[2], converted_val
                    )
                    storage.save()

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
