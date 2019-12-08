import requests

from model import db, Player, User

from bs4 import BeautifulSoup


def offense_scrape(html):
    soup = BeautifulSoup(html, 'html.parser')
    names = soup.select("td.name-col")
    info = soup.select("table.data-table__scrollable.data-table__forwards > tbody > tr")

    offense = []
    for row in names:
        player = create_player(row, names, info)
        offense.append(player)

    return offense


def defense_scrape(html):
    soup = BeautifulSoup(html, 'html.parser')
    names = soup.select("td.name-col")
    info = soup.select("table.data-table__scrollable.data-table__defensemen > tbody > tr")

    defense = []
    for row in names:
        player = create_player(row, names, info)
        defense.append(player)

    return defense


def goalie_scrape(html):
    soup = BeautifulSoup(html, 'html.parser')
    names = soup.select("td.name-col")
    info = soup.select("table.data-table__scrollable.data-table__goalies > tbody > tr")

    goalies = []
    for row in names:
        player = create_player(row, names, info)
        goalies.append(player)

    return goalies


def create_player(row, names, info):
    player = {}
    player["first"] = names[row].select("span.name-col__firstName")[0].text
    player["last"] = names[row].select("span.name-col__lastName")[0].text
    player["special"] = names[row].select("span.name-col__special")[0].text.strip()
    player["number"] = info[row].select("td.number-col")[0].text
    player["position"] = info[row].select("td.position-col")[0].text
    player["shoots"] = info[row].select("td.shoots-col")[0].text
    player["height"] = info[row].select("td.height-col > span.xs-sm-md-only")[0].text
    player["weight"] = info[row].select("td.weight-col")[0].text
    return player


if __name__ == "__main__":
    html = requests.get("https://www.nhl.com/capitals/roster").text

    players = {}
    players["offense"] = offense_scrape(html)
    players["defense"] = defense_scrape(html)
    players["goalies"] = goalie_scrape(html)

    for list in players:
        for player in list:
            db.session.add(Player(
                first = player["first"],
                last = player["last"],
                special = player["special"],
                number = player["number"],
                position = player["position"],
                shoots = player["shoots"],
                height = player["height"],
                weight = player["weight"]
            ))
    db.session.add(User(username="Ken", email="kgreen7@umbc.edu"))
    db.session.commit()