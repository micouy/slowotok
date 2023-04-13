import requests
from random import choice
from bs4 import BeautifulSoup


DICTIONARY_PAGE_URL = "https://sjp.pl/{word}"
GOOGLE_QUERY_URL = "https://www.google.com/search?q={query}"


with open("slowa.txt", "r") as f:
    words = [w for w in f]

while True:
    word = choice(words)

    response = requests.get(DICTIONARY_PAGE_URL.format(word=word))
    soup = BeautifulSoup(response.content, "html.parser")

    basic_form = soup.find("a", { "class": "lc"})
    # p > b > a
    definition = basic_form.parent.parent.find_next_sibling("p")

    # No definition.
    if definition.get_text() == "KOMENTARZE":
        continue

    basic_form = basic_form.get_text()

    print(basic_form.upper())
    print("-" * len(basic_form))
    print()
    print(definition.get_text(separator="\n"))
    print()
    print(GOOGLE_QUERY_URL.format(query=basic_form))

    # If Ctrl+C/Ctrl+D is pressed, it raises an error.
    _ = input("")
