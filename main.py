#!/usr/bin/python

# phase1 deals with stage 1: making the space
from phase1 import *
from phase2 import *
from graph import *

maxDungeonSize = 15
setting = random.choice(["mine", "deep"])

dungeon = makeDunList(setting)

dungeon = joinDun(dungeon)

fixRooms(dungeon)

graph = graph(dungeon)

for x in range(len(graph)):
    print(graph[x])
