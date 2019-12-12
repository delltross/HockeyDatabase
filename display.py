from app.model import Player


def get_players():
    playerdict = {}
    players = Player.query.all()
    offenselist = []
    defenselist = []
    goalielist = []
    for player in players:
        statlist = [0,0,0,0,0,0,0,0]
        statlist[0] = player.first
        statlist[1] = player.last
        statlist[2] = player.special
        statlist[3] = player.number
        statlist[4] = player.position
        statlist[5] = player.shoots
        statlist[6] = player.height
        statlist[7] = player.weight

        if player.position == "C" or player.position == "LW" or player.position == "RW":
            offenselist.append(statlist)

        elif player.position == "D":
            defenselist.append(statlist)

        else:
            goalielist.append(statlist)

    playerdict["offense"] = offenselist
    playerdict["defense"] = defenselist
    playerdict["goalies"] = goalielist

    return playerdict


if __name__ == "__main__":
    get_players()