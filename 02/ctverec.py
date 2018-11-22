strana = float(input('Zadej stranu čtverce v centimetrech: '))

if strana >= 0:
	print("Obvod čtverce se stranou", strana, "cm je", 4 * strana, "cm")
	print("Obsah čtverce se stranou", strana, "cm je", strana * strana, "cm2")
else:
	print("neumim to di do haje")