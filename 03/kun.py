rychlost = float(input('jak rychle jede kůň? '))

if rychlost < 0:
	print("couvá")
	
elif rychlost == 0:
	print("stojí")
	
elif rychlost <= 8:
	print("krok")
	
elif rychlost <= 15:
	print("klus")
	
elif rychlost <= 30:
	print("cval")
	
elif rychlost <= 2000:
	print("trysk")
	
elif rychlost <= 5000:
	print("concorde")
	
else:
	print("raketa")