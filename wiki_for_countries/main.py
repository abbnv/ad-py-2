
import json
import urllib.parse

class getWiki:
    WIKI_URL = 'https://wikipedia.org/wiki/'

    def __init__(self, countries_path, result_path):
        self.countries_path = countries_path
        self.result_path = result_path

    def __iter__(self):
        return self

    def __next__(self):
        with(open(self.countries_path, encoding="utf-8")) as countries:
            countries = json.load(countries)
            countries_with_links = []
            for country in countries:
                wiki_link = urllib.parse.quote(self.WIKI_URL + country['name']['official'], safe='://')
                countries_with_links.append(f"{country['name']['official']} — {wiki_link}\n")
        print(countries_with_links)

        with(open(self.result_path, "w", encoding="utf-8")) as result_file:
            for country_with_link in countries_with_links:
                result_file.write(country_with_link)
        print("Done!")
        raise StopIteration


if __name__ == '__main__':
    for countries_links in getWiki('countries.json', 'result.txt'):
        print(countries_links)

