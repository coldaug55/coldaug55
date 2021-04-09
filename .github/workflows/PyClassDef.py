class Animals(object):
    def __init__(self, breed):
        self.breed = breed
        self.age = None
        self.name = None
    def get_breed(self):
        return self.breed
    def get_age(self):
        return self.age
    def set_age(self, newAge):
        self.age = newAge
    def get_name(self):
        return self.name
    def set_name(self, newName):
        self.name = newName
    def set_breed(self, newBreed):
        self.breed = newBreed
    
    def __str__(self):
        return "< Animal: " + str(self.breed) + ", " + str(self.age) + " >"
    
class Dogs(Animals):
    def speak(self):
        if len(self.breed) < 8:
            return "woof"
        elif len(self.breed) > 8:
            return "bork"
        else:
            return "bark"
    def __str__(self):
        return "< Dog: " + str(self.breed) + ", " + str(self.name) + " , " + str(self.age) + " >"
    
class Cats(Animals):
    def speak(self):
        print("meow")
    def personality(self):
        if self.age > 5:
            return "Grumpy old cat vibes"
        else: 
            return "Playful and mischevious"
        
    def name_length(self):
        return len(self.name)
    
    def __str__(self):
        return "< Cat: " + str(self.name) + ", " + str(self.age) + " >"
