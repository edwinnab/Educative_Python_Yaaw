# Player class
class Player:
   def __init__(self,ID,name,teamName):
       self.ID = ID
       self.name = name
       self.teamName = teamName


# Team class contains a list of Player
# Objects
class Team:
    def __init__(self,name):
        self.name = name
        self.players = []

    def getNumberOfPlayers(self):
        return len (self.players)
    def addPlayer(self,player):
        self.players.append(player)


# School class contains a list of Team
# objects.
class School:
    def __init__(self,name):
        self.teams = []
        self.name = name
    def addTeam(self,team):
        self.teams.append(team)
    def getTotalPlayersInSchool(self):
        length = 0
        for n in self.teams:
            length = length + (n.getNumberOfPlayers())
        return length

# code to test the implementation
p1 = Player("Harris", 1, "Red")
p2 = Player("Carol", 2, "Red")

p3 = Player("Johnny", 1, "Blue")
p4 = Player("Sarah", 2, "Blue")

red_team=Team("Red Team")
red_team.players.append(p1)
red_team.players.append(p2)

blue_team=Team("Blue Team")
blue_team.players.append(p2)
blue_team.players.append(p3)

mySchool=School("My School")
mySchool.teams.append(red_team)
mySchool.teams.append(blue_team)

print("Total players in my school:", mySchool.getTotalPlayersInSchool())
print("Complete the challenge.")
