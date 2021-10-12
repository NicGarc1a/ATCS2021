elev = {'Everest': '8848','K2': '8611','Kangchenjunga': '8585','Lhotse': '8516','Cho Oyu': '8188'}

for mtn in elev.keys():
    print(mtn)

for i in elev.values():
    print(i)

for a in elev.keys():
    print("%s is %s meters tall." % (a, elev[a]))