# - All code should be written in .py files.
# - Homework should be submitted via a Pull Request on GitHub.
# - Your files should have appropriate names and be organized in 
#   a clear structure.
# - Your code should adhere to the Python PEP8 code guidelines. 
#   You can use the flake8, black, and isort libraries to achieve this.


# 1. Create add method to add two countries together. 
#    This method should create another country object with the name of
#    the two countries combined and the population of the two countries
#    added together.


# bosnia = Country('Bosnia', 10_000_000)
# herzegovina = Country('Herzegovina', 5_000_000)

# bosnia_herzegovina = bosnia.add(herzegovina)
# bosnia_herzegovina.population -> 15_000_000
# bosnia_herzegovina.name -> 'Bosnia Herzegovina'

class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    @classmethod
    def double_counries(cls, country1, country2):
        new_country = f'{country1.name} {country2.name}'
        new_population = country1.population + country2.population
        return new_country, new_population


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

double_country = Country.double_counries(bosnia, herzegovina)
print(double_country)

# Implement the previous method with a magic method

class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population
 
    def __add__(self, other):
        new_country2 = f'{self.name} {other.name}'
        new_population2 = self.population + other.population
        return new_country2, new_population2


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

double_country2 = bosnia + herzegovina
print(double_country2)