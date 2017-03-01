from lxml import html
import requests
#Campaign URL goes here
page = requests.get('http://www.ppaction.org/site/TR?px=9693618&fr_id=1160&pg=personal')
tree = html.fromstring(page.content)
#This will find the goal amount
goal = tree.xpath('//span[@class="amount-raised-value"]/text()')
goal = [item.replace("\n", "") for item in goal]
#This prints the currently raised amount out of the total goal
with open("donation.txt", "w") as text_file:
    print(goal,'/$10000', sep="", file=text_file)
