# La funzione type vi dice di che tipo sia un oggetto

def count_leaves(input_list):
    # 🚨 CASO BASE
    if len(input_list) == 0:
        return 0
    else:
        counter = 0
        for element in input_list:
            if type(element) == list: # Se ciò su cui sto lavorando è una lista di Python
                # 🚨 MANTENIMENTO DELLO STATO: Ritorno il conteggio al piano superiore
                counter = counter + count_leaves(element)
            else:
                counter+=1 # counter = counter + 1 
        return counter


names = ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
print(names)
c = count_leaves(names)
print(c)
