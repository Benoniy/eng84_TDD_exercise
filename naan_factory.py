
class NaanFactory:

    def make_dough(self, ingredient1, ingredient2):
        if ingredient1 == "water" or ingredient2 == "water":
            if ingredient1 == "flour" or ingredient2 == "flour":
                return "dough"

        return ingredient1 + "y " + ingredient2

    def bake_dough(self, ingredient1):
        if ingredient1 == "dough":
            return "naan bread"
        return "unknown"

    def run_factory(self, ingredient1, ingredient2):
        dough = self.make_dough(ingredient1, ingredient2)
        naan = self.bake_dough(dough)
        return naan


if __name__ == "__main__":
    while True:
        user_input = input("Would you like to make naan today?  (y or n)")

        if user_input.lower() == "n":
            break

        ing1 = input("What is the first ingredient for the dough?: ")
        ing2 = input("What is the second ingredient for the dough?: ")

        print(f"You made {NaanFactory.run_factory(ing1, ing2)}")
