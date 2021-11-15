import sys, random

print("Random gamertag generator. '\n")

# where the first names are from https://www.findnicknames.com/cool-gamer-tags/#Cool_Gamertags
first = ('EatBullets', 'PR0_GGRAM3D', 'TheSickness', 'Shoot2Kill', 'Overkill', 'Killspree', 'MindlessKilling', 'Born2Kill', 'TheZodiac', 'ZodiacKiller', 'ToySoldier', 'MilitaryMan', 'DeathSquad', 'Veteranofdeath', 'Angelofdeath', 'MustardGas', 'Knuckles', 'KnuckleBreaker', 'KnuckleDuster', 'BloodyKnuckles ', 'JackTheRipper', 'TedBundyHandsome', 'Necromancer', 'SmilingSadist', 'ManicLaughter', 'Tearsofjoy', 'ShowMeUrguts', 'KnifeInGutsOut', 'Talklesswinmore', 'Guillotine', 'Decapitator', 'TheExecutor', 'BigKnives', 'SharpKnives', 'LocalBackStabber', 'BodyParts', 'BodySnatcher', 'TheButcher', 'meat cleaver', 'ChopChop', 'ChopSuey', 'TheZealot', 'VagaBond', 'LoneAssailant','9mm', 'SemiAutomatic', '101WaysToMeetYourMaker', 'Dudemister', 'HellNBack', 'SmashDtrash','Sl4ught3r', 'RiotStarter', 'SweetPoison', '3D Waffle', '44', '57 Pixels','Accidental Genius', 'Acid Gosling', 'Admiral Tot', 'Airport Hobo', 'Alpha', 'Angel', 'AngelsCreed', 'Arsenic Coo', 'Back Bett', 'Bad Bunny', 'Bitmap', 'Blitz', 'Bonzai', 'Bowie', 'Bowler', 'Bug Blitz', 'Bug Fire', 'Bugger', 'Cabbie', 'Capital F', 'Chew Chew', 'Chuckles', 'CobraBite', 'Cocktail', 'CommandX', 'Commando', 'Crash Test', 'Cupid Dust', 'Dangle','Criss Cross')

# where the last names are from https://one-name.org/surnames_A-Z
last = ('Zacksfield', 'Zionzee', 'Zittlau', 'Zealand', 'Zeeland', 'Zogg', 'Zehntner', 'Zentner', 'Zion Zee', 'Naden', 'Nadin', 'Naggs', 'Nailer', 'Nation', 'Jack', 'Jacke', 'Janson', 'Jayne', 'Jecks', 'Joiner', 'Jub', 'Fall', 'Fancote', 'Farmarie', 'Farmilo', 'Farrants', 'Fassom', 'Fawl', 'Feakes', 'Feavyour', 'Ferdy', 'Field', 'Filce', 'Fields', 'Filce', 'Fillybrown', 'Finedon', 'Fishwick', 'Flux', 'Fogg', 'Foil', 'Flemming', 'Foat', 'Foxhole', 'Fur', 'Fury', 'Fyndorne', 'Futty', 'Foxell', 'Van Der Belt', 'Vawse', 'Vik', 'Vitty', 'Voss', 'Van Der Vord', 'Vyze', 'Vanderbilt', 'Maczula', 'Maishment', 'Marke', 'Marshall', 'Maxam', 'Maybury', 'Melly', 'Merryman', 'Milo', 'Moist', 'Moon', 'Muskett', 'Myst', 'Munny', 'Muskett', 'Munay', 'Munday', 'Munny', 'Sackitt', 'Saint', 'Smee', 'Squirrel', 'Stanley', 'Sturdy',)

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)

    print("\n\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n\n")

    try_again = input("\n\nTry Again? (Press Enter for new name or 'Ctrl + C' to quit.)\n ")
    if try_again.lower() == "n":

     input("\nPress Enter to exit")