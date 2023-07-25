import  re

sentence =input()
pattern = r'(www\.[a-zA-Z0-9-\.]+(\.[a-z]+))'
valid_links = []

while sentence:
    valid_link = re.search(pattern, sentence)
    if valid_link:
        valid_links.append(valid_link.group(1))
    sentence = input()

for url in valid_links:
    print(url)


"""
tests:
Join WebStars now for free, at www.web-stars.com
You can also support our partners:
Internet - www.internet.com
WebSpiders - www.webspiders101.com
Sentinel - www.sentinel.-ko     ->  www.web-stars.com
                                    www.internet.com
                                    www.webspiders101.com
                                    
Need information about cheap hotels in London?
You can check us at www.london-hotels.co.uk !
We provide the best services in London.
Here are some reviews in some blogs:
London Hotels are awesome! - www.indigo.bloggers.com
I am very satisfied with their services - ww.ivan.bg
Best Hotel Services! - www.rebel21.sedecrem.moc     ->  www.london-hotels.co.uk
                                                        www.indigo.bloggers.com
                                                        www.rebel21.sedecrem.moc
"""