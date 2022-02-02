#!/usr/bin/python3
'''
Defines the class Base
'''

import json
import csv


class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        lo = []
        if list_objs is not None:
            for i in list_objs:
                lo.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(lo))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        lm = []
        try:
            with open(filename, 'r') as f:
                lm = cls.from_json_string(f.read())
            for i, e in enumerate(lm):
                lm[i] = cls.create(**lm[i])
        except:
            pass
        return lm

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves to csv file
        Args
           cls - class
           list_objs - list objects
        """
        if cls.__name__ is "Rectangle":
            names = ['width', 'height', 'x', 'y', 'id']
        else:
            names = ['size', 'x', 'y', 'id']

        filename = '{}.csv'.format(cls.__name__)

        with open(filename, 'w', newline='') as f:
            if list_objs:
                writer = csv.DictWriter(f, fieldnames=names)
                writer.writeheader()
                for x in list_objs:
                    writer.writerow(x.to_dictionary())
            else:
                writer.writerow([[]])

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of instances of cls
        Args
           cls - class
        """
        my_list = []
        filename = '{}.csv'.format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    for key, val in row.items():
                        row[key] = int(val)
                    my_list.append(row)
            return([cls.create(**x) for x in my_list])
        except FileNotFoundError:
            return([[]])
