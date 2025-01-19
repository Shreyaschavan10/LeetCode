#Write a solution to find the name, population, and area of the big countries.

#Return the result table in any order.

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    new_area=world['area'] >=3000000
    new_population = world['population'] >=25000000
    big_countries= world[new_population | new_area ][['name','population', 'area']]
    return big_countries
