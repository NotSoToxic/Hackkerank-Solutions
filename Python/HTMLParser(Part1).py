from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        [print(f'-> {i[0]} > {i[1]}') for i in attrs]
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        [print(f'-> {i[0]} > {i[1]}') for i in attrs]

parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
    