list_name = ["Es","Ches","es","ches"]
list_sym = ["!", "@", "#", "$"]
list_date = ["110581", "11051981"]
list = [n+s+d for n in list_name for s in list_sym for d in list_date]
#print('\n'.join(list))
f = open("chur.txt","w")
f.write('\n'.join(list));
f.close()