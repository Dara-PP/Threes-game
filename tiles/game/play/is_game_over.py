def is_game_over(plateau):
    t=plateau['tiles']
    to=plateau['nombres_de_case_libres']
    if to > 0 :
        return False 
    else : 
        i=0
        while i < len(t):
            if t[i]+t[i+1] % 3 == 0 or t[i]+[i+4]%3 == 0 or t[i]+t[i-1]%3 == 0 or t[i]+t[i-4]%3 == 0 :
                return False 
            elif t[i] == t[i+1] or t[i+4] == t[i] or t[i-1] == t[i] or t[i] == t[i-4] :
                return False 
            elif t[i] == 0 :
                return False
            else : 
                return False   
            i+=1
        return True  
                
