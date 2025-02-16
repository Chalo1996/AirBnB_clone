The AirBnB Clone Project One<br/>
What is it?
This is the console(terminal) used to execute tasks, including CRUD operations. The storage engine is the file storage—JSON.<br/>
The Console<br/>
Commands to interact with the console:<br/>

- Clone the repository.
- Navigate to the base directory of the AirBnB clone project.
- Run: `./console.py` to launch it in interactive mode or `echo "help" | ./console.py` in non-interactive mode.

To create an instance:
```bash
create <classname>
# Example:
create BaseModel
```
To print the string representation of an instance:
```bash
show <classname> <instance_id>
# Example:
show BaseModel 1234-1234-1234
```
To delete an instance:
```bash
destroy <classname> <instance_id>
# Example:
destroy BaseModel 1234-1234-1234
```
To print all instances:
```bash
all
# OR
all <classname>
# Example:
all BaseModel
```
To update an instance:
```bash
update <classname> <instance_id> <attribute_name> <attribute_value>
# Example:
update BaseModel 1234-1234-1234 email "aibnb@mail.com"
```
Additional commands:
```bash
help or ? - Get help about all available commands
Shell commands (preceded by '!'): !pwd, !ls, !clear
echo $last - Run the previous command
quit or EOF - Exit the console
```

Packages
```text
The models package handles all creation of objects and their serialization and deserialization.
The tests package handles the testing of the models.
```
Contributors

- Emmanuel Chalo - [email](mailto:emusyoka759@gmail.com)
- Chizoba Ugwuoke - [email](mailto:upc4you@gmail.com)
