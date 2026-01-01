# def table(n):
# 	for x in range(11):
# 		print(f"{n} * {x} = {n*x}")
# n = int(input("which table you may to check: "))
# print(table(n))

def pettorn(n):
	for x in range(0,n): #EH 0 TE LEY KE END VALUE HAA
		p = n-x # X KEYA HAI PTA LAGG GEYA X NU USE KITA VALUE LAI X RANGE LIKE1,2,3,

		if x==0:
			print(" "*p,"*" , end="")# JE VALUE 0 HOI FR PHER 1 * 
		print(" "*p, "*"*x, end="") ,print("*"*x, end=""),print("*"*x)# EH LINE DA MTLB 
		'''
		" "*p SPACE DEna jini p ch value ani oh space nal * ho jani
		"*"*x star increase hone x di value nal * ho ke
		end="" next LINE BREAK KARNA 
		print("*"*x, end="") SAME INCREACE STAR BREAK LINE
		print("*"*x)# THEN IN CREATE STAR KAR KE DEKHDI AA 
		'''
		print("")
n = int(input("which formate you may to drow: "))
print(pettorn(n))

'''
      *

     **

    ****

   ******

  ********
'''