from random import * 
import sys
sys.path.append("jeu_du_threes/tiles/game/play")
from is_game_over import *
import sys
sys.path.append("jeu_du_threes/tiles/tiles_acces")
from is_room_empty import *

def get_next_alea_tiles(plateau,mode):
    tiles={}
    tiles['mode']=mode
    t1={}
    t2={}
    if is_game_over(plateau)==True :
        tiles['check'] = True
        if mode == init :
            t1['val']=1
            t2['val']=2
            lig=randint(0,3)
            col=randint(0,3)
            while is_room_empty(plateau,lig,col) != True :
                lig=randint(0,3)
                col=randint(0,3)
                if is_room_empty(plateau,lig,col) == True :
                    t1['lig']=lig
                    t1['col']=col
                    lig2=randint(0,3)
                    col2=randint(0,3)
                    while is_room_empty(plateau,lig2,col2) != True :
                        lig2=randint(0,3)
                        col2=randint(0,3)   
                        if is_room_empty(plateau,lig,col) == True :
                            t2['lig']=lig2
                            t2['col']=col2
                            tiles['t1']=t1
                            tiles['t2']=t2  
                            return tiles
        else :
            t1['val']=randint(1,3)
            lig=randint(0,3)
            col=randint(0,3)
            while is_room_empty(plateau,lig,col) != True :
                lig=randint(0,3)
                col=randint(0,3)
                t1['lig']=lig
                t1['col']=col
                tiles['t1']=t1
                return tiles
    else:
        print('Game over')   
