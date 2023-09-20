# List of dictionaries of predefined food items
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


spicy_food = {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10}

def get_names(spicy_foods):
    '''
    Returns a list containing the names of all the food items in the given list

    Parameters
    ----------
    spicy_foods : list
        A list of dictionaries, with keys "name", "cuisine",
        "heat_level". Each dictionary corresponds to a food item.

    Returns
    -------
    x : list
        A list of strings

    '''
    # Use list comprehension for brevity. Only keep the names of the foods
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    '''
    Returns a list containing the details of the food items in the given list
    whose heat_level is above 5

    Parameters
    ----------
    spicy_foods : list
        A list of dictionaries, with keys "name", "cuisine",
        "heat_level". Each dictionary corresponds to a food item.

    Returns
    -------
    x : list
        A list of dictionaries. This is a subset of the given list.

    '''
    # Use list comprehension for brevity.
    # Only keep a food item (dictionary) if its heat_level is above 5
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    '''
    Displays the details of all the food items in the given list

    Parameters
    ----------
    spicy_foods : list
        A list of dictionaries, with keys "name", "cuisine",
        "heat_level". Each dictionary corresponds to a food item.

    Returns
    -------
    None

    '''
    for food in spicy_foods:
        # Using f-strings to format the output as required
        print(f'{food["name"]} ({food["cuisine"]}) | {"🌶" * int(food["heat_level"])}')


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    '''
    Returns a dictionary containing the details of the (first) food item whose
    cuisine value is specified by the user

    Parameters
    ----------
    spicy_foods : list
        A list of dictionaries, with keys "name", "cuisine",
        "heat_level". Each dictionary corresponds to a food item.
    cuisine : string
        The type of cuisine to keep

    Returns
    -------
    x : dictionary
        This is an element of the given list.

    '''
    for food in spicy_foods:
        # Only keep a food item (dictionary) if its cuisine-type
        # matches the one specified by the user
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    '''
    Displays the details of the food items in the given list
    whose heat_level is above 5

    Parameters
    ----------
    spicy_foods : list
        A list of dictionaries, with keys "name", "cuisine",
        "heat_level". Each dictionary corresponds to a food item.

    Returns
    -------
    None

    '''
    # Use a previous function to loop through only those foods
    # whose heat_level is high enough
    for food in get_spiciest_foods(spicy_foods):
        # Use f-strings to format the output as specified in the brief
        print(f'{food["name"]} ({food["cuisine"]}) | {"🌶" * int(food["heat_level"])}')


def get_average_heat_level(spicy_foods):
    '''
    Computes the average heat level of all the food items
    present in the given list.

    Parameters
    ----------
    spicy_foods : list
        A list of dictionaries, with keys "name", "cuisine",
        "heat_level". Each dictionary corresponds to a food item.

    Returns
    -------
    x : float
        The average of all the heat_level values

    '''
    # Initialise the sum of all the heat levels to zero
    total = 0
    for food in spicy_foods:
        total += food["heat_level"]
    # Divide the sum of the heat levels with the number of food items
    # to get the average value
    return total / len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    '''
    Computes the average heat level of all the food items
    present in the given list.

    Parameters
    ----------
    spicy_foods : list
        A list of dictionaries, with keys "name", "cuisine", and
        "heat_level". Each dictionary corresponds to a food item.
    spicy_food : dictionary
        A dictionary with keys "name", "cuisine", and "heat_level",
        corresponding to a new food item.

    Returns
    -------
    spicy_foods : list
        A list of dictionaries. This is the extension of the original list.

    '''
    # Append the new food item (dictionary) at the end of the original list
    spicy_foods.append(spicy_food)
    return spicy_foods


def main():
    # Call each function with the appropriate input(s) to inspect the output(s)
    print("Calling all the functions in main")
    print(get_names(spicy_foods))
    print(get_spiciest_foods(spicy_foods))
    print_spicy_foods(spicy_foods)
    print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))
    print_spiciest_foods(spicy_foods)
    print(get_average_heat_level(spicy_foods))
    print(create_spicy_food(spicy_foods, spicy_food))


# Call the main() function if running this file as a script
if __name__=="__main__":
    main()