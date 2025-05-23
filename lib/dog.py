#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    
    def __init__(self, name=None, breed=None):
        if name is not None:
            self.name = name

        if breed is not None:
            self.breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if value and isinstance(value, str) and 1 < len(value) < 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)


    def get_breed(self):
        return self._breed
    
    def set_breed(self, value):
        if value not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value

    breed = property(get_breed, set_breed)

        
