# TDD Bread Factory! :bread:

## Tasks:
TDD bread factory is the latest bread brand in Py Land. It always produces the best bread because it has the best testing strategy!

What they do is before they make any new bread, they make a test to make sure the end ouput is correct. Then they adjust the recipe until it's just right!

You are going to do the same with bread! This is called Test Driven Development.



This exercise is going to bring together lots of concepts.

### Learning Outcomes:
Learning outcomes include:
- git
- github
- functions
- TDD
- Separation of concerns - this is important do not ignore!
- DRY code
- DOD


## Naan factory:
To run the naan factory do the following:

```python
import naan_factory
run_factory()
```
### User stories for Naan Factory:

1. As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.

2. As a user, I can use the bake dough with dough to get naan.

3. As a user, I can use run_factory with water and flour and get naan.


## Naan factory tests:  
You should write unit tests for naan_factory to ensure that everything has worked as intended

## Acceptance Criteria:

* you have written tests
* test pass
* you have written more test to make sure everything works as indented
* all user stories are satisfied
* code does not break
* code has exit condition
* DOD if followed  

## Solution:  

1. I created tests for naan_factory.py in test_unittest_naan_factory.py.
```python
import unittest
import naan_factory


class NaanTest(unittest.TestCase):
    factory_naan = naan_factory.NaanFactory()  # Instantiate NaanFactory

    # Checks if correct input for make_dough returns "dough"
    def test_make_dough(self):
        self.assertEqual(self.factory_naan.make_dough("flour", "water"), "dough")

    # Checks if correct input for bake_dough returns "naan bread"
    def test_bake_dough(self):
        self.assertEqual(self.factory_naan.bake_dough("dough"), "naan bread")

    # Checks if correct input for run_factory returns "naan bread"
    def test_run_factory(self):
        self.assertEqual(self.factory_naan.run_factory("flour", "water"), "naan bread")
```


2. I created naan factory in naan_factory.py to fulfill the tests.  
```python
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

```


3. I created additional tests to ensure that incorrect input was dealt with.  
```python
    # Checks if incorrect input for make_dough returns the correct mistake
    def test_make_dough_wrong(self):
        self.assertEqual(self.factory_naan.make_dough("water", "salt"), "watery salt")

    # Checks if incorrect input for bake_dough returns "unknown"
    def test_bake_dough_wrong(self):
        self.assertEqual(self.factory_naan.bake_dough("salt"), "unknown")

    # Checks if incorrect input for run_factory returns "unknown"
    def test_run_factory_wrong(self):
        self.assertEqual(self.factory_naan.run_factory("batter", "water"), "unknown")  

```


4. I created a user interface with an exit clause to allow naan_factory.py to be used, not just tested.  
```python
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

```

