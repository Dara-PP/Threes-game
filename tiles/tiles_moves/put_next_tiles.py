def put_next_tiles(p,tiles):
    lig=tiles[t1]['lig']
    col=tiles[t1]['col']
    val=tiles[t1]['val']
        
    lig2=tiles[t2]['lig']
    col2=tiles[t2]['col']
    val2=tiles[t2]['val']
    tab=p['tiles']
    
    if tiles['mode']==init:
        tab[(4*lig)+col]==val 
        tab[(4*lig2)+col2]==val2 
        return p           
    else : 
        tab[(4*lig)+col]==val
        return p
        
        
