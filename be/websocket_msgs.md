# What types of messages do we need between client and server?

## socket

### join room

user sends in a room id with request
server sends err if the room doesnt exist
otherwise adds that player and their id to the room

### set room's problem settings
[comment]: # TODO: find lc available problem settings

host should be able to change the settings for 
 - problem difficulty
 - problem types

### generate bracket

once all settings are set and people join
we can create bracket
should decide
 - matches
 - who gets a bye (if player count != power of 2)

### toggle player is ready

players set themselves to ready
once both players are ready in a match
 - we generate a problem 
 - send the problem,
 - store on server

### validate problem is submitted
[comment]: # find lc api for testing submit

if a player presses "solved" we
 - check if they solved it
 - update room state accordingly
 - send message to client (AC / ERR)

## Internal helpers

### generate problem
[comment]: # find lc api for random problem

given 2 players find a problem that
 - is within the problem settings for the room
 - is solved by neither contestant

### find room

see if a room exists, given the room id

