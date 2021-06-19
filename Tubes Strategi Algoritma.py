# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 10:53:52 2021

@author: Deril
"""
board = [['.' for i in range(8)]for i in range(8)]
movement=0
inputKnight=[0,0]
displayBoard=board
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]
          



def aman(x, y):
    '''
        A utility function to check if i,j are valid indexes
        for N*N chessboard
    '''
    if(x >= 0 and y >= 0 and x < 8 and y < 8):
        return True
    return False



def posisiPionCorrect(posisi):
    if len(posisi)==2:
        if posisi[0]>='a' and posisi[0]<='h' and int(posisi[1])>=2 and int(posisi[1])<=7:
            return True
        else:
            return False



def posisiCorrect(posisi, board):
    x = int(posisi[1])-1
    y = ord(posisi[0])-(ord('a')-1)-1
    if posisi[0]>='a' and posisi[0]<='h' and int(posisi[1])>=1 and int(posisi[1])<=8 and board[x][y]=='.':
        return True
    else:
        return False    



def backtrack(new_x, new_y, move_x, move_y):
    # Try all next moves from the current coordinate x, y
        global koordinatKnight
        global movement
        global board
        if movement==3:
            return False        
        prevX=new_x
        prevY=new_y
        movement+=1
        for i in range(8):     
            new_x += move_x[i]
            new_y += move_y[i]
            if aman(new_x, new_y):
                if board[new_x][new_y]=='x':
                    if movement!=0:
                         movement-=1                 
                    return False  
                else:
                    if board[new_x][new_y]=='P':
                        board[prevX][prevY]='.'
                        board[new_x][new_y]='K'                        
                        return True
                    elif (backtrack(new_x, new_y, move_x, move_y)):
                        board[prevX][prevY]='.'
                        board[new_x][new_y]='K'                        
                        return True
        return False




def inputPion():
    jmlPion=0
    posisiPion=' '
    
    while jmlPion<4 and posisiPion!='':
        print(('Masukan posisi pion ke-'+str(jmlPion+1)+': '))
        posisiPion=input()
        
        if posisiPionCorrect(posisiPion):
            x = int(posisiPion[1])-1
            y = ord(posisiPion[0])-(ord('a')-1)-1
            board[x][y]='P'
            
            if (y-1<0):
                board[x-1][y+1]='x'
            elif (y+1==8):
                board[x-1][y-1]='x'
            else:
                board[x-1][y+1]='x'
                board[x-1][y-1]='x'
                
            ShowBoard(board)
            jmlPion+=1



def inputKnight():
    while True:
        posisiKnight=input('Masukan posisi Knight: ')  
        if posisiCorrect(posisiKnight, board):
            x = int(posisiKnight[1])-1
            y = ord(posisiKnight[0])-(ord('a')-1)-1
            board[x][y]='K'
            global koordinatKnight
            koordinatKnight=[x, y]
            break
    
def ShowBoard(board):
    print('a b c d e f g h')
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=' ')
        print(i+1)
    print(" ")    
    
'''
MAIN
'''

ShowBoard(board)

inputPion()

koordinatKnight=[0,0]

inputKnight()
#print(koordinatKnight)

ShowBoard(board)

current_x = koordinatKnight[0]
current_y = koordinatKnight[1]

print(current_x, current_y)
x=input()
status=backtrack(current_x, current_y, move_x, move_y)
ShowBoard(board)
if (status==True):
    print("Solusi ditemukan")
else:
    print("Tidak ada solusi")