def medium_display(plateau):
    eto=''
    j=0
    while j < 21:
        eto+='*'
        j+=1

    tab='* '
    l1=0
    print(eto)
    while l1 <=3:
        tab+=str(plateau[l1]).rjust(2)+' * '
        l1+=1
    print(tab)

    tab='* '
    l2=4
    print(eto)
    while l2<=7:
        tab+=str(plateau[l2]).rjust(2)+' * '
        l2+=1
    print(tab)

    tab='* '
    l3=8
    print(eto)
    while l3<=11:
        tab+=str(plateau[l3]).rjust(2)+' * '
        l3+=1
    print(tab)

    tab='* '
    l4=12
    print(eto)
    while l4<=15:
        tab+=str(plateau[l4]).rjust(2)+' * '
        l4+=1
    print(tab)
    print(eto)
