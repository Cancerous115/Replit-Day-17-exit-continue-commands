from getpass import getpass as input

print("Rock,Paper scissors!!!")
print("Select your choice P,R,or S")
ponescore=0
ptwoscore=0
while True:
  pone=input("Choose your option player one")
  ptwo=input("choose your option player two")
  if pone=="R":
    if ptwo =="S":
      print("Playerone wins R>S")
      ponescore+=1
    elif ptwo =="R":
      print("TIE")
    elif ptwo =="P":
      print(" Player one loses Paper beats Rock")
      ptwoscore+=1
  elif pone=="S":
    if ptwo =="S":
      print("Tie")
    elif ptwo =="R":
      print("Player two wins R>S")
      ptwoscore+=1
    elif ptwo =="P":
      print(" Player one wins S>P")
      ponescore+=1
  elif pone=="P":
    if ptwo =="S":
      print("Playertwo wins R>S")
      ptwoscore+=1
    elif ptwo =="P":
      print("TIE")
    elif ptwo =="R":
      print(" Player one loses Rock>scissors")
      ptwoscore+=1
  
  print("Player 2 has",ptwoscore,"wins")
  print(" Player 1 has",ponescore,"wins")
 
  if ponescore==3 or ptwoscore==3:
    exit()
  else:
    continue