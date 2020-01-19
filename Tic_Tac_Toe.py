#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
import pygame
from enum import Enum


### 16/01/2020
### Tic Tac Toe game implemented with a basic IA using MinMax Algorithm (pseudo code found on internet)



SIZE = 900

class Player (Enum) :
    X = 1
    O = 0

def play (x, y, board, screen, isMaxPlayer) :
    pos = x * 300 + SIZE  / 6, y * 300 + SIZE / 6
    yellow = 255, 211, 0
    if isMaxPlayer :
        board[x][y] = 1
        start = pos[0] - 150, pos[1] - 150
        end = pos[0] + 150, pos[1] + 150
        pygame.draw.line (screen, yellow,start, end )
        start = pos[0] - 150, pos[1] + 150
        end = pos[0] + 150, pos[1] - 150
        pygame.draw.line (screen, yellow,start, end)
    else :
        board[x][y] = 0
        pygame.draw.circle (screen, yellow, pos, 80)

def checkFinish(board) :
    test = evaluation (board)
    if test == 1 :
        print "You win !"
        return 0
    elif test == -1 :
        print "You lose !"
        return 0
    return 1



#DRAWING FUNCTONS
def draw_lines (screen) :
    blue = 0, 0, 255
    point1 = 0, 0
    point2 = 0, SIZE
    point3 = point1
    point4 = SIZE, 0
    for i in range (5) :
        pygame.draw.line (screen, blue, point3, point4)
        pygame.draw.line (screen, blue, point1, point2)
        point1 = i*SIZE/3, 0
        point2 = i*SIZE/3, SIZE
        point3 = 0, i*SIZE/3
        point4 = SIZE, i*SIZE/3

def game():
    board = [[-1 for x in range (3)]for y in range(3)]
    pygame.init()
    screen = pygame.display.set_mode ((SIZE, SIZE))
    flag = True
    isMaxPlayer = True
    while flag :
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                flag = False
            elif event.type == pygame.QUIT :
                flag = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                ok = False
                if board[event.pos[0]/300][event.pos[1]/300] == -1 :
                    play( event.pos[0]/300, event.pos[1]/300, board, screen, True)
                    ok = True
                    flag = checkFinish (board)
                elif flag:
                    print "Incorrect play, try again !"

                if ok and flag and isMoveLeft (board):
                    ia = findOptimalMove (board)
                    play (ia[0], ia[1], board, screen, False)
                    flag = checkFinish (board)
                if not isMoveLeft (board) and flag:
                    print "Draw !"
                    flag = 0

            draw_lines(screen)
        pygame.display.flip()
    pygame.quit()


#IA FUNCTIONS

# Find victory and return a value depending on which player win
def evaluation (board) :
    #checking  rows X or O victory
    for i in range (3) :
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] :
            if board[i][0] == Player.X.value :
                return 1
            elif board[i][0] == Player.O.value :
                return -1

    #checking Columns for X or O victory
    for i in range (3) :
            if board[0][i] == board[1][i] and board[1][i] == board[2][i] :
                if board[0][i] == Player.X.value :
                    return 1
                elif board[0][i] == Player.O.value :
                    return -1

    #checking Diagonals for X or O victory
    if board[0][0] == board [1][1] and board [1][1] == board [2][2] :
        if board [0][0] == Player.X.value :
            return 1
        elif board [0][0] == Player.O.value :
            return -1
    if board[0][2] == board [1][1] and board[1][1] ==  board [2][0]:
        if board [0][2] == Player.X.value :
            return 1
        elif board [0][2] == Player.O.value :
            return -1

    return 0


# Check if there are moves possible
def isMoveLeft (board) :
    for i in range(3):
        for j in range (3) :
                if board [i][j] == -1 :
                    return True
    return False


# Evaluate every plays and return the value
def minmax (board, depth, isMaxPlayer) :
    score = evaluation (board)

    if score == 1 :
        return score - depth
    if score == -1 :
        return score + depth
    if not isMoveLeft (board) or depth == 0:
        return 0
    if isMaxPlayer :
        optimal = float ('inf')

        for i in range (3) :
            for j in range (3) :
                if board [i][j] == -1 :
                    board [i][j] = Player.X.value
                    optimal = min (optimal, minmax (board, depth - 1, not isMaxPlayer))
                    board [i][j] = -1
    else :
        optimal =  -float ('inf')
        for i in range (3) :
            for j in range (3) :
                if board[i][j] == -1 :
                    board [i][j] = Player.O.value
                    optimal = max (optimal, minmax (board, depth - 1, not isMaxPlayer))
                    board [i][j] = -1
    return optimal



# Main function, return the best move for the IA
def findOptimalMove (board) :
    best = - float ('inf')
    move =-1, -1

    for i in range (3) :
        for j in range (3) :
            if board [i][j] == -1 :
                board [i][j] = Player.X.value
                val = minmax (board, 0, False)
                board [i][j] = -1

                if val > best :
                    best = val
                    move = i, j
    return move

if __name__ == "__main__" :
    game()

