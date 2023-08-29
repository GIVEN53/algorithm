from sys import stdin

_ = int(stdin.readline())
cards = set(stdin.readline().split())
_ = int(stdin.readline())

print(" ".join("1" if num in cards else "0" for num in stdin.readline().split()))

##########################
#    memory: 125648KB    #
#    time:   380ms       #
##########################
