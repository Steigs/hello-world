players=["judge","soto","ohtani","betts","cole"]
print(players[0:3])
print(players[:3])
print(players[2:])
print(players[-4:])
print(players[0:5:2])


#for loop in with list slicing

print("Here are the first three players on my team:")
for player in players[0:3]:
    print(player.title())