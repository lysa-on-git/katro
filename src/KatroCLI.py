from enum import Enum
from src.BoardCLI import BoardCLI

class states (Enum) :
    OPENING   : int = 0x0A
    SOWING    : int = 0x0B
    LAST_SEED : int = 0x0C
    GAME_OVER : int = 0x0D

class KatroCLI :
    def __init__(self) -> None:
        self.pit  : int = 0
        self.player : int = 0
        self.Board = BoardCLI()
        self.seeds_to_sow : int = 0
        self.players : list[list[int]] = [ [2]*8, [2]*8 ]

        self.PITS    = len(self.players[0])
        self.COLUMNS = len(self.players[0]) // 2
    
    def play(self) :
        state = states.OPENING
        while True :
            match state :
                case states.OPENING :
                    self.Board.show(self.players)
                    self.pit = self.Board.prompt()
                    state = states.SOWING

                case states.SOWING :
                    self.seeds_to_sow = self.players[self.player][self.pit]
                    self.players[self.player][self.pit] = 0
                    
                    while self.seeds_to_sow > 1 : 
                        self.pit = (self.pit + 1) % self.PITS
                        self.seeds_to_sow -= 1
                        self.players[self.player][self.pit] += 1

                        self.Board.show(self.players); 
                        print(self.seeds_to_sow); input()
                        self.Board.clear()

                    state = states.LAST_SEED
                
                case states.LAST_SEED :
                    self.pit = (self.pit + 1) % self.PITS

                    if not self.players[self.player][self.pit] == 0 :
                        self.seeds_to_sow -= 1
                        self.players[self.player][self.pit] += 1
                        state = states.SOWING
                    else :
                        if self.pit not in range(self.COLUMNS) :
                            state = states.OPENING
                            print("HERE GOES THE A.I")
                            break
                        else :
                            if all(self.players[self.player][i] == 0 for i in range(self.COLUMNS)) :
                                opponent_pit = self.pit + self.COLUMNS
                            else :
                                opponent_pit =  (self.COLUMNS-1) - self.pit
                            
                            opponent_player = (self.player + 1) % 2
                            
                            self.seeds_to_sow -= 1
                            self.players[self.player][self.pit] += self.players[opponent_player][opponent_pit] + 1
                            self.players[opponent_player][opponent_pit] = 0

                            if all(i == 0 for i in self.players[0]) or all(i == 0 for i in self.players[1]) :
                                state = states.GAME_OVER
                            else :
                                if self.players[self.player][self.pit] > 1 :
                                    state = states.SOWING
                                else :
                                    state = states.OPENING
                                    print("HERE GOES THE A.I")
                                    break
                        self.Board.show(self.players); 
                        print(self.seeds_to_sow); input()
                        self.Board.clear()
                case states.GAME_OVER :
                    break