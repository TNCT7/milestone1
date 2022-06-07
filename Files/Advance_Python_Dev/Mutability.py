def addAccount(name : str, holder : str, acountholder = None ):
    if not acountholder:
        acountholder = []
    else:
        acountholder.append(holder)

    return {
        'name' : name,
        'holder' : holder,
        'acountholder' : acountholder
            }


a1=addAccount('saving','Tejas',['Jen'])
print(a1)
a2=addAccount('saving','Amruta')
print(a2)


