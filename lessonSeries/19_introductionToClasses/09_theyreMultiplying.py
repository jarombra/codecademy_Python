class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        print self.name
        print self.age

hippo = Animal("Ront", 21)
sloth = Animal("Jed", 41)
ocelot = Animal("Femo", 14)

print hippo.health
print sloth.health
print ocelot.health
