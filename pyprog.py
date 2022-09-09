import random
import string

def random_links_twitter():
    name = input("[N]: ")
    publication_ID = "" + "".join(random.choices(string.digits, k=19))
    publication_link_compiler = f"https://twitter.com/{name}/status/{publication_ID}/photo/1"
    print(publication_link_compiler)
    input("")