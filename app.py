import sys
import feedparser


from colorama import init
from colorama import Back, Style
init(autoreset=True)

# print(Fore.RED + 'some red text')
# print('automatically back to default color again')

url = sys.argv[1]


def latest():
    d = feedparser.parse(url)
    print (Back.RED + "Title:") + (Style.RESET_ALL + " " + d.entries[0].title)
    print (Back.YELLOW + "Link:") + (Style.RESET_ALL + " " + d.entries[0].link)


def latest_five():
    d = feedparser.parse(url)
    i = 0
    for i in range(0, 5):
        # Prevent IndexError if less than five aricles in feed
        try:
            d.entries[i]
        except IndexError:
            break
        print (Back.CYAN + "\t" + str(i + 1) + "\t")
        print (Back.RED + "Title:") + \
            (Style.RESET_ALL + " " + d.entries[i].title)
        print (Back.YELLOW + "Link:") + \
            (Style.RESET_ALL + " " + d.entries[i].link)
        # print "Content: " + d.entries[i]['content']


def show(title, link, desc):
    print str(title)
    # print str(date)
    print str(link)
    print str(desc)


def menu():
    print """What do you wish to do now? \n1. Read the latest issue.
          \n2. Get the titles of the latest 5 issues."""
    opt = int(raw_input('opt: '))
    if opt == 1:
        latest()
    elif opt == 2:
        latest_five()
    else:
        print "Not a valid choice"
        exit(0)


if __name__ == "__main__":
    # parse(sys.argv[1])
    url = sys.argv[1]
    menu()
