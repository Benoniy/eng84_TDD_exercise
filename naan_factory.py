
class NaanFactory:
    #  Returns dough only if the ingredients are correct
    def make_dough(self, ingredient1, ingredient2):
        if ingredient1 == "water" or ingredient2 == "water":
            if ingredient1 == "flour" or ingredient2 == "flour":
                return "dough"

        return ingredient1 + "y " + ingredient2

    # Returns naan bread only if the dough is correct
    def bake_dough(self, ingredient1):
        if ingredient1 == "dough":
            return "naan bread"
        return "unknown"

    # Runs the factory to make naan bread out of the ingredients provided
    def run_factory(self, ingredient1, ingredient2):
        dough = self.make_dough(ingredient1, ingredient2)
        naan = self.bake_dough(dough)
        return naan


#  User input if this file is being run
if __name__ == "__main__":
    factory = NaanFactory()  # Instantiate NaanFactory
    while True:
        user_input = input("Would you like to make naan today? (y or n): ")  # gives the user an option to exit

        if user_input.lower() == "n":  # exit if no
            break

        # Collect information about ingredients
        ing1 = input("What is the first ingredient for the dough?: ").lower().strip()
        ing2 = input("What is the second ingredient for the dough?: ").lower().strip()

        # Get the result and print it
        result = factory.run_factory(ing1, ing2)
        print(f"You made {result}")
