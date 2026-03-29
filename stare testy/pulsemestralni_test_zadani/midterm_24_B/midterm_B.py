def main():
    """
    Recommend nutrients and genetic modifications for cell cultures
    :param list cell_sizes: measured cell sizes of cell cultures
    :param dict nutrient_modification_map: genetic modifications based on nutrients
    :rtype: list
    :return: For each cell culture: (growth rate, nutrients, genetic modification)
    """
    ...
    return cultures


if __name__ == "__main__":
    # Test data
    cell_sizes = [
        [10, 15, 20, 25, 30],
        [12, 18, 24, 30, 36],
        [8, 16, 24, 32, 40],
        [11, 15.5, 20, 24.5, 29],
        [3, 6, 9, 12, 15]
    ]
    nutrient_modification_map = {
        "Glucose": "Gene Overexpression",
        "Amino Acids": "Gene Knockout",
        "Minerals": "Gene Editing"
    }

    cultures = main(
        cell_sizes,
        nutrient_modification_map
    )
    print("Cultures:", cultures)
