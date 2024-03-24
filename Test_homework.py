
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