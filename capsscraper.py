import requests
from bs4 import BeautifulSoup
from app import db, Player, User


def offense_scrape(html):
    soup = BeautifulSoup(html, 'html.parser')
    names = soup.select("table.data-table__pinned.data-table__forwards > tbody > tr > td.name-col")
    info = soup.select("table.data-table__scrollable.data-table__forwards > tbody > tr")
    offense = []
    for row in range(len(names)):
        player = create_player(row, names, info)
        offense.append(player)
    return offense


def defense_scrape(html):
    soup = BeautifulSoup(html, 'html.parser')
    names = soup.select("table.data-table__pinned.data-table__defensemen > tbody > tr > td.name-col")
    info = soup.select("table.data-table__scrollable.data-table__defensemen > tbody > tr")
    defense = []
    for row in range(len(names)):
        player = create_player(row, names, info)
        defense.append(player)
    return defense


def goalie_scrape(html):
    soup = BeautifulSoup(html, 'html.parser')
    names = soup.select("table.data-table__pinned.data-table__goalies > tbody > tr > td.name-col")
    info = soup.select("table.data-table__scrollable.data-table__goalies > tbody > tr")
    goalies = []
    for row in range(len(names)):
        player = create_player(row, names, info)
        goalies.append(player)
    return goalies


def create_player(row, names, info):
    db.session.add(Player(
        first = names[row].select("span.name-col__firstName")[0].text,
        last = names[row].select("span.name-col__lastName")[0].text,
        special = names[row].select("span.name-col__special")[0].text.strip(),
        number = info[row].select("td.number-col")[0].text,
        position = info[row].select("td.position-col")[0].text,
        shoots = info[row].select("td.shoots-col")[0].text,
        height = info[row].select("td.height-col > span.xs-sm-md-only")[0].text,
        weight= info[row].select("td.weight-col")[0].text
    ))
    return player


if __name__ == "__main__":
    html = requests.get("https://www.nhl.com/capitals/roster").text
    players = {}
    players["offense"] = offense_scrape(html)
    players["defense"] = defense_scrape(html)
    players["goalies"] = goalie_scrape(html)
    db.session.add(User(username="Ken", email="kgreen7@umbc.edu"))
    db.create_all()
    db.session.commit()