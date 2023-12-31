import csv

INDEX_CHAMPION_NAME = 2
INDEX_CHAMPION_COUNTRY = 1


def main():
    """Take in a list of Wimbledon final matches, then process and display the winners"""
    champion_to_wins = {}
    wimbledon_finals = []  # Unnecessary to declare here make this
    get_match_results(wimbledon_finals)
    winning_countries = compile_winners(champion_to_wins, wimbledon_finals)
    display_winners(champion_to_wins, winning_countries)


def get_match_results(wimbledon_finals):
    """Open a csv file, read and then append to a list"""
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        rows = csv.reader(in_file, delimiter=",")
        for row in rows:
            wimbledon_finals.append(row)


def compile_winners(champion_to_wins, wimbledon_finals):
    """Take empty lists and dictionary then add winning countries to a list and add to count of a key or set a key's
    value"""
    countries = []
    for match in wimbledon_finals:
        try:
            countries.append(match[INDEX_CHAMPION_COUNTRY])
            champion_to_wins[match[INDEX_CHAMPION_NAME]] += 1
        except KeyError:
            champion_to_wins[match[INDEX_CHAMPION_NAME]] = 1
    return set(countries)


def display_winners(champion_to_wins, winning_countries):
    """Take a dictionary of winners and a list of winning countries and display formatted"""
    print("Wimbledon Champions:")
    for champion, count in champion_to_wins.items():
        print(f"{champion} : {count}")
    print(f"These {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(winning_countries)))


main()
