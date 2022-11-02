#!/bin/python3
import subprocess
import sys

path = "/tmp/player"
def init():
    args = sys.argv
    if "-n" in args: nextPlayer()
    if "-p" in args: prevPlayer()
    if "-q" not in args: print(readFile())

def readFile(): return open(path,"r").read().strip()
def writeFile(input): return open(path,"w").write(input.strip())

def getPlayers():
    playerctlOutput = subprocess.run(["playerctl", "-l", "-s"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return playerctlOutput.splitlines() 

def currentPlayerIndex(): return getPlayers().index(readFile())
def setPlayer(index): return writeFile(getPlayers()[index])

def nextPlayer(): 
    index = currentPlayerIndex() + 1
    if index == len(getPlayers()): index = 0

    return setPlayer(index)

def prevPlayer():
    index = currentPlayerIndex() - 1
    if index == -1: index=len(getPlayers())-1

    return setPlayer(index)

init();
