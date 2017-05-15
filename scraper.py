#Given the citation list traverse through list and retrieve data
#e.g. given http://scholar.google.com/scholar?cites=3358877064191775708&as_sdt=2005&sciodt=0,5&hl=en
from scholar import ScholarArticleParser

def main():

print ScholarArticleParser.article()

if __name__ == "__main__":
    sys.exit(main())

