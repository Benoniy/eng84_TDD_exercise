

def make_dough(ingredient1, ingredient2):
    if ingredient1 == "water" or ingredient2 == "water":
        if ingredient1 == "flour" or ingredient2 == "flour":
            return "dough"

    return ingredient1 + "y " + ingredient2


def bake_dough(ingredient1):
    if ingredient1 == "dough":
        return "naan bread"
    return "unknown"


def run_factory(ingredient1, ingredient2):
    dough = make_dough(ingredient1, ingredient2)
    naan = bake_dough(dough)
    return naan
