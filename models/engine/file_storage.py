#!/usr/bin/python3
"""
This script defines a class for serializing and deserializing Python objects:
Instance <-> Dictionary <-> JSON string <-> file

Classes:
    FileStorage
"""


class FileStorage:
    """A class for serializing and deserializing Python objects"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary containing all objects"""

        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the dictionary"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to JSON and saves to a file"""

        import json

        file_name = FileStorage.__file_path
        to_json = {}
        for key, obj in FileStorage.__objects.items():
            to_json[key] = obj.to_dict()

        with open(file_name, "w", encoding="UTF-8") as f:
            json.dump(to_json, f)

    def reload(self):
        """Deserializes objects from a JSON file"""

        import json
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.city import City
        from models.review import Review
        from models.state import State

        file_name = FileStorage.__file_path

        try:
            with open(file_name, "r", encoding="UTF-8") as f:
                from_json = json.load(f)
                for key, value in from_json.items():
                    cls_name, obj_id = key.split(".")
                    if cls_name == "BaseModel":
                        cls = BaseModel
                    elif cls_name == "User":
                        cls = User
                    elif cls_name == "Amenity":
                        cls = Amenity
                    elif cls_name == "Place":
                        cls = Place
                    elif cls_name == "City":
                        cls = City
                    elif cls_name == "Review":
                        cls = Review
                    elif cls_name == "State":
                        cls = State
                    else:
                        continue

                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
