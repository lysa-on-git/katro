from os import system
from time import sleep

import pygame

class BoardCLI :
       
       pygame.init()
       _fictive_board = '''
              ╔══════╦══════╦══════╦══════╗
              ║  @@  ║  @@  ║  @@  ║  @@  ║
              ╠══════╬══════╬══════╬══════╣
              ║  @@  ║  @@  ║  @@  ║  @@  ║
              ╚══════╩══════╩══════╩══════╝        
              ╠═══════════════════════════╣
              ╔══════╦══════╦══════╦══════╗
              ║  @@  ║  @@  ║  @@  ║  @@  ║
              ╠══════╬══════╬══════╬══════╣
              ║  @@  ║  @@  ║  @@  ║  @@  ║
              ╚══════╩══════╩══════╩══════╝   
       
       '''

       _format_string_board = _fictive_board.replace('@@' , '{:2d}')

       def __init__(self) -> None:
              system('@echo off')
              system('cls')

       def show(cls, pits : list[list[int]]) -> None:
              BOARD = cls._format_string_board.format(
                     pits[0][4], pits[0][5], pits[0][6], pits[0][7] ,
                     pits[0][3], pits[0][2], pits[0][1], pits[0][0] , 

                     pits[1][0], pits[1][1], pits[1][2], pits[1][3] , 
                     pits[1][7], pits[1][6], pits[1][5], pits[1][4]
              )
              BOARD = BOARD.replace('   0  ' , '      ')
              cls.clear()
              print(BOARD);
       
       def prompt(self) -> int :
              pit = int(input("Choose one PIT to start sowing: "))
              return pit

       def clear(self) -> None :
              system('cls')

if __name__ == '__main__' :
       pass