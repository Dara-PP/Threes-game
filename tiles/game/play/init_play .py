def init_play():
    plateau={}
    plateau["n"]=4
    plateau["nombre_case_libres"]=16
    tiles=[]
    i=0
    while i < 4:
        j=0
        while j < 4:
            tiles.append(0)
            j+=1
        i+=1
    plateau["tiles"]=tiles 
    return plateau 



