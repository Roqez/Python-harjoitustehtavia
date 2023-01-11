leiviska = float((input)("Syötä leiviskät "))
naula = float((input("Syötä naulat ")))
luoti = float((input)("Syötä luodit "))
naulat = (leiviska*20)+naula
luodit = (naulat*32)+luoti
paino = luodit*13.3
kilogrammat = paino//1000
grammat = paino%1000
print(f"Massa nyky mittojen mukaan: {kilogrammat:2.0f} kiloa ja "f"{grammat:5.2f} grammaa.")