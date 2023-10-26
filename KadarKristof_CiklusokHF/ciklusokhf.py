'''
Minden feladathoz külön eljárást készíts! 
'''


# 1. Készíts eljárást, mely a paramterében kap egy számot.
# Az eljárás írja ki a hárommal osztható számokat eddig a számig vesszővel elválasztva.
# Az utolsó szám után ne legyen jel! 

def Harommal(szam):
	i=0
	while i!=szam:
		i+=1
		if i%3==0:
			if i==szam or i==szam-1 or i==szam-2:
				print(i,end="")
			else:
				print(i,end=", ")










# Készíts eljárást, mely a paraméterében kap egy pozitív egész számot.
# Az eljárás írja ki a számokat a képernyőre ;-vel elválasztva csökkenő sorrendben 1-ig!
# Az utolsó szám után ne legyen pontosvessző!  
# Pl.: ha a szám 5 --> 5; 4; 3; 2; 1 


def Csokkeno(szam):
	while szam!=0:
		if szam==1:
			print(szam,end="")
		else :
			print(szam,end="; ")
		szam-=1

#Csokkeno()












# Kérjünk be a felhasználótól 5-tel osztható számot!
# A számot addig kérjük be, amíg nem sikerül 5-tel oszthatót beírnia!  

def Ottel(szam):

	if szam%5==0:
		print("Siker")
	else:
		while szam!="Siker":
			szam=int(input("5-tel osztható számot kérek: "))
			if szam%5==0 and szam>0:
				szam="Siker"

#Ottel()








# Készíts eljárást, mely a paramterében kap egy számot.
# Az eljárás írja ki a számokat eddig a számig,  ha a szám 3-mal osztható,
# akkor ne a számot írja ki, hanem írja helyette, hoyg BUMM.
# Az utolsó szám után ne legyen vessző! Pl, ha a szam=7 
# 1, 2, BUMM, 4, 5, BUMM, 7 

# Egészítsd ki a feladatot, hogy ha páros szám, akkor BAM-ot írjon,
# és ha 3-mal és 2-vel is osztható, akkor BUMMBAM-ot írjon! 
# 1, BAM, BUMM, BAM, 5, BUMMBAM, 7 

# Készíts teszteseteket az előző feladathoz!	:,(

def Bumm(szam):


	def Keplet():
		if i!=szam:
			if i%3==0 or i%2==0:
				if i%3==0 and i%2==0:
					print("BUMMBAM",end=", ")
				elif i%3==0:
					print("BUMM",end=", ")
				elif i%2==0:
					print("BAM",end=", ")
			else:
				print(i,end=", ")
		else:
			if i%3==0 or i%2==0:
				if i%3==0 and i%2==0:
					print("BUMMBAM")
				elif i%3==0:
					print("BUMM")
				elif i%2==0:
					print("BAM")
			else:
				print(i)




	i=0
	while i!=szam:
		if szam>0:
			i+=1
			Keplet()
		elif szam<0:
			i-=1
			Keplet()
		elif szam==0:
			print("A játékhoz nem lehet nullát megadni!")



#Bumm()





