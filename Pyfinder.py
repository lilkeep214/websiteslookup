import pyprog
from pyprog import random_links_twitter

def finder():
    while True:
        choice = input("github finder = 1, facebook finder = 2, twitter finder = 3 / twitter publication finder  = 4 -> ")

        if choice == "1":

            name = input("[N]: ")
            find = f"https://github.com/{name}"
            print(find)
            input("")
        
        if choice == "2":

            name = input("[N]: ")
            find = f"https://www.facebook.com/{name}"
            print(find)
            input("")

        if choice == "3":

            name = input("[N]: ")
            find = f"https://twitter.com/{name}"
            print(find)
            input("")
        
        if choice == "4":
            random_links_twitter()