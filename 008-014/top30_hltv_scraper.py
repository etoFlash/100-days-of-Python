import cfscrape
import os
import calendar
from bs4 import BeautifulSoup as Soup

# get by URL will be redirect to address like https://www.hltv.org/ranking/teams/2019/november/4
TOP_LINK = "https://www.hltv.org/ranking/teams"
file_exists = False

scraper = cfscrape.create_scraper()
r = scraper.get(TOP_LINK)
r.raise_for_status()
url_parts = scraper.get(TOP_LINK).url.split("/")[-3:]  # ex result: ['2019', 'november', '4']
url_parts[1] = str(list(calendar.month_name).index(url_parts[1].title()))  # ex: convert "november" to "11"
url_parts[2] = url_parts[2].rjust(2, "0")
file_name = os.path.join("top30_results", "_".join(url_parts) + ".txt")
s = Soup(r.content, "html.parser")
teams = s.select(".ranked-team .name")
assert len(teams) == 30, "Teams count should be equal 30"
result = "\n".join(f"{i}. {team.getText()}" for i, team in enumerate(teams, 1))

if not os.path.isfile(file_name):
    with open(file_name, "w") as f:
        f.write(result)


for line in result.splitlines():
    print(line)
