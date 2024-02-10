def store_inputs(count: int):
    """
    Storing the *count* number of purchased products from stdin.
    :rtype: list[str]
    """
    products = []
    for i in range(count):
        product = input("Enter the name of the purchased product: \n")
        products.append(product)
    return products


def load_from_file(path: str):
    """
    In case you do not want to redirect the input from a file to stdin and
    load the products from a file directly, you may use this method.
    :param path: The path to the file that stores the products.
    :return:
    :rtype: list[str]
    """
    products = []
    with open(path) as file:
        # Reading the number of products from the first line
        count = int(file.readline())
        # Reading lines the same number of times as there are products
        for i in range(count):
            # Stripping the \n from the end of the current line
            products.append(file.readline().strip())
    return products


def featuredProduct(products: list[str]):
    """
    Return the featured product of tomorrow.

    The product that is purchased the most one day is the featured product
    for the following day. If there is a tie for the product
    purchased most frequently, those product names are ordered
    alphabetically ascending and the last name in the list is chosen.
    :param products: Products that were previously purchased.
    :return: The feature popular product.
    :rtype: str
    """

    # Creating a dictionary where the frequency of the products is stored
    prod_dict = {}
    for p in products:
        if p in prod_dict:
            prod_dict[p] += 1
        else:
            prod_dict[p] = 1

    # The highest frequency of a product
    highest_count = max(prod_dict.values())

    # Find the most popular products (those that occurred the most in the list)
    most_popular = []
    for key in prod_dict.keys():
        if prod_dict[key] == highest_count:
            most_popular.append(key)

    most_popular.sort()
    # From the most popular products return the last one in alphabetic order
    return most_popular[-1]


number_of_products = int(input("How many products would you like to enter? "))
products = store_inputs(number_of_products)
print(featuredProduct(products))
