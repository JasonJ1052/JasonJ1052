class Pig:
    def __init__(self, name, material):
        self.name = name
        self.material = material
        self.house = None
    def __str__(self):
        result = self.name + " "+self.material+" "+self.house.__str__()
        return result
    
    def build_house(self):
        strength = {"straw":1, "sticks":2, "bricks":3}[self.material]
        self.house = (self.material, strength)
    def squeal():
        print("Squeal!")
        
class House:
    def __init__(self, material, strength):
        self.material = material
        self.strength = strength
    def __str__(self):
        result = "house:"+self.material+" "+self.strength.__str__()
        return result

pigs = [
    Pig("Pig 1","straw"),
    Pig("Pig 2","sticks"),
    Pig("Pig 3","bricks")
]

for p in pigs:
    p.house=House(p.material,1)
    print(p)
    
        
        
pig1 = ("Pig 1", "straw")
pig2 = ("Pig 2", "sticks")
pig3 = ("Pig 3", "bricks")
pigs = [pig1, pig2, pig3]
def build_house(pig):
    name, material = pig
    strength = {"straw":1, "sticks":2, "bricks":3}[material]
    return (material, strength)
