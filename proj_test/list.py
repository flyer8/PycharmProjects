# List generator
list_name = ["EC","ec","ECh","ech","Es","es","Ches","ches","Esc","esc","Esch","esch","Churikova","churikova","Echurikova","echurikova","Cantabile","cantabile"]
list_sym = ["!", "@", "#", "$"]
list_date = ["1105", "110581", "11051981", "1981","81"]
list = [n+s+d for n in list_name for s in list_sym for d in list_date]
list2 = [n+d for n in list_name for d in list_date]
#print('\n'.join(list))
f = open("chur.txt","w")
f.write('\n'.join(list))
f.write('\n'.join(list2))
f.close()