'''function for aesthetic display the available options'''
def choser(listname):
    rang = (range(len(listname)))
    ranglist = []
    for x in rang:
        ranglist.append(x+1)
    stries = str(ranglist)
    return stries.replace(',','/').replace(' ','')

'''module controlling migration of resources'''
def do_order(stock):
    your_summary = {}
    used_resources = {}
    while True: 
        availables = []
        for keyy in stock.keys():
            if (stock[keyy]) > 0:
                availables.append(keyy)
        print("Available:","\n\t",availables)
        
        que = "Enter item's number from list "
        que += choser(availables)
        que += "\n[ Enter 'end' to display summary ]"
        print(que)
        ans = input()
        if not ans:
            continue
        if ans == 'end':  
            break
        if ans in choser(availables):
        
            single_item = availables[int(ans)-1]
            stock[single_item] = (int(stock[single_item]-1))
            if single_item not in your_summary:
                your_summary[single_item] = 1
            else:
                your_summary[single_item] += 1
            if single_item not in used_resources:
                used_resources[single_item] = 1
            else:
                used_resources[single_item] += 1
            print("You've added "+str(single_item)+"!")
        
        else:
            continue

    '''summary'''
    print('Your summary', your_summary)    
    print('\n' 'stock:',stock,'\nused:', used_resources)

