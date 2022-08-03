from constructions import *

# This list shows what places gain which features.
# A chasm would require a bridge over it to be liveable.

global roomTransformations
roomTransformations = [
    ["entrance", "trap"],
    ["lavapit", "bridge"],
    ["river", "bridge"],
]

# This ordered wishlist makes the elves make one alcove into a kitchen,
# then one cavern into a library.

wishList = [
    ["alcove", "kitchen", 1],
    ["cavern", "library", 1],
    ["alcove", "forge", 1],
    ["fungus", "garden", 1],
    ["cavern", "musicHall", 1],
    ["alcove", "bedroom", 20],
    ["lake", "boats", 20],
]

def fixRooms(dungeon):
    for x in range(len(dungeon) - 1, 1, -1):
        for pair in range(len(roomTransformations)):
            if dungeon[x]["name"] == roomTransformations[pair][0]:
                dungeon[x]["constructions"].append(roomTransformations[pair][1])

def makeRooms(dungeon):
    for x in range(len(dungeon) - 1, 1, -1):
        for pair in range(len(wishList)):
            if wishList[pair][2] > 0 and dungeon[x]["name"] == wishList[pair][0]:
                dungeon[x]["constructions"].append(wishList[pair][1])
                wishList[pair][2] -= 1
                break

