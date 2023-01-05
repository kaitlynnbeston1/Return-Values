def city_country(city, country):
    """Returns a country and city, neatly formatted."""
    fullCity = f"{city}, {country}"
    return fullCity.title()


# calling functions
city1 = city_country("london", "england")
city2 = city_country("toronto", "canada")
city3 = city_country("berlin", "germany")


# printing
print(city1)
print(city2)
print(city3)