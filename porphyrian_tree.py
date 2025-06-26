#Porphyrian Tree: made to tinker with inheritance, while also implementing the Factory design pattern.

class Substance:
    def __init__(self, is_material=None, **bad_predicates):
        self.is_material = is_material
        #in case any absurd combination of predicates is provided, program throws this error
        if bad_predicates:
            raise TypeError(
                f"WARNING! Illogical predicates entered: {list(bad_predicates.keys())}. Being cannot be generated.\n\n"
            )
#It works quite simply: 
#The first child class should consume its arguments (predicates);
#Parent classes do the same when super() is called, iteratively;
#If any arguments are left when Substance level is reached, something innapropriate was predicated.
#(e.g. predicating of an Immaterial that it's True that it is_animate, or even False; the predicate simply doesn't apply.)
#Those left arguments will be stored in the **bad_predicates kwargs dictionary.
#With it not being empty, error is thrown.

class Immaterial(Substance):
    def __init__(self, **inherited):
        super().__init__(**inherited)
        print("\nWe've got an angel!\n")
class Material(Substance):
    def __init__(self, is_animate=None, **inherited):
        self.is_animate = is_animate
        super().__init__(**inherited)

class Inanimate(Material):
    def __init__(self, **inherited):
        super().__init__(**inherited)
        print("\nWe've got a rock!\n")
class Animate(Material):
    def __init__(self, is_sentient=None, **inherited):
        self.is_sentient = is_sentient
        super().__init__(**inherited)

class Unsentient(Animate):
    def __init__(self, **inherited):
        super().__init__(**inherited)
        print("\nWe've got a plant!\n")
class Sentient(Animate):
    def __init__(self, is_rational=None, **inherited):
        self.is_rational = is_rational
        super().__init__(**inherited)

class Irrational(Sentient):
    def __init__(self, **inherited):
        super().__init__(**inherited)
        print("\nWe've got a beast!\n")
class Rational(Sentient):
    def __init__(self, **inherited):
        super().__init__(**inherited)
        print("\nWe've got a human!\n")
    

#this is our factory of beings
def generate_being(**predicates):

    if 'is_material' not in predicates:
        return Substance(**predicates)
    elif predicates['is_material'] == False:
        return Immaterial(**predicates)
    else: pass

    if 'is_animate' not in predicates:
        return Material(**predicates)
    elif predicates['is_animate'] == False:
        return Inanimate(**predicates)
    else: pass
    
    if 'is_sentient' not in predicates:
        return Animate(**predicates)
    elif predicates['is_sentient'] == False:
        return Unsentient(**predicates)
    else: pass

    if 'is_rational' not in predicates:
        return Sentient(**predicates)
    elif predicates['is_rational'] == False:
        return Irrational(**predicates)
    
    else: return Rational(**predicates)

def main():

    Gabriel_predicates = {
        "is_material":False
    }
    Gabriel_seed = generate_being(**Gabriel_predicates)

    diamond_predicates = {
        "is_material":True,
        "is_animate":False
    }
    diamond_seed = generate_being(**diamond_predicates)

    oak_predicates = {
        "is_material":True,
        "is_animate":True,
        "is_sentient":False
    }
    oak_seed = generate_being(**oak_predicates)

    dog_predicates = {
        "is_material":True,
        "is_animate":True,
        "is_sentient":True,
        "is_rational":False
    }
    dog_seed = generate_being(**dog_predicates)

    socrates_predicates = {
        "is_material":True,
        "is_animate":True,
        "is_sentient":True,
        "is_rational":True
    }
    socrates_seed = generate_being(**socrates_predicates)

if __name__ == "__main__":
    main()