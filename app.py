import sys
import feedparser

from colorama import init
from colorama import Back, Style


init(autoreset=True)


def rss_print(title, link):
    print(Back.RED + "Title:" + Style.RESET_ALL + " " + title)
    print(Back.YELLOW + "Link :" + Style.RESET_ALL + " " + link)

    
def get_rss(limit):
    """
    Get rss data from url,
    print single entry to show latest news, else give index number
    """
    rss_data = feedparser.parse(URL)
    if limit == 1:
        title = rss_data.entries[0].title
        link = rss_data.entries[0].link
        rss_print(title, link)
    else:
        for i in range(0, limit):
            title = rss_data.entries[i].title
            link = rss_data.entries[i].link

            print(Back.CYAN + str(i + 1) + "\t")
            rss_print(title, link)


def menu():
    print("""What do you wish to do now? \n1. Get the latest issue.
          \n2. Get the titles of the latest 5 issues.""")
    opt = input('opt: ')
    if opt == "1":
        get_rss(1)
    elif opt == "2":
        get_rss(5)
    else:
        print("Not a valid choice")
        exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify some rss link")
    else:
        URL = sys.argv[1]
        menu()
