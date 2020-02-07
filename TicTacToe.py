import os
from time import sleep
from pyfiglet import figlet_format
from random import randint

########################################### ALL FUNCTIONS ###########################################

def greeting(uname1, uname2):
	print("\n\n\n")
	print(figlet_format("TIC TAC TOE"))

#####################################################################################################

def assignment(uname1, uname2):
	choices = ['X', 'O']
	global playerflag
	global u1
	global u2
	while(True):
		u1 = input(f"\n  {uname1} Enter your Choice [X/O]: ")
		if u1.upper() not in choices:
			continue
		else:
			if u1.upper()=='X':
				u2 = 'o'
				playerflag=2
				break
			else:
				u2='x'
				playerflag=1
				break
	print(f"\n\t  {uname1} you are '{u1.upper()}' and {uname2} you are '{u2.upper()}'\n\n")

#####################################################################################################

def gameboard():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("\n\n")
	print(f"         |         |         ")
	print("    "+l[6]+"    |    "+l[7]+"    |    "+l[8])
	print(f"         |         |         ")
	print(f"-----------------------------")
	print(f"         |         |         ")
	print("    "+l[3]+"    |    "+l[4]+"    |    "+l[5])
	print(f"         |         |         ")
	print(f"-----------------------------")
	print(f"         |         |         ")
	print("    "+l[0]+"    |    "+l[1]+"    |    "+l[2])
	print(f"         |         |         ")


#####################################################################################################

def gameplay(uname1, uname2):
	sleep(4)
	if randint(0,1):
		t1=True
	else:
		t1=False
	while(True):
		if(check_victory()):
			gameboard()
			winning_player(uname1, uname2)
			break
		else:
			gameboard()
			if t1:
				print(f"\n  {uname1} it's your Turn")
				c1 = int(input("  Enter your Choice on Board: "))
				if c1 in range(10) and l[c1-1]==" ":
					l[c1-1] = u1.upper()
					t1 = False
				else:
					continue
			else:
				print(f"\n  {uname2} it's your Turn")
				c2 = int(input("  Enter your Choice on Board: "))
				if c2 in range(10) and l[c2-1]==" ":
					l[c2-1] = u2.upper()
					t1 = True
				else:
					continue

#####################################################################################################

def check_victory():
	global markflag

	if l[0]==l[1]==l[2]=='X' or l[3]==l[4]==l[5]=='X' or l[6]==l[7]==l[8]=='X':
		markflag=0
		return True
	if l[0]==l[1]==l[2]=='O' or l[3]==l[4]==l[5]=='O' or l[6]==l[7]==l[8]=='O':
		markflag=1
		return True
	elif l[0]==l[3]==l[6]=='X' or l[1]==l[4]==l[7]=='X' or l[2]==l[5]==l[8]=='X':
		markflag=0
		return True
	elif l[0]==l[3]==l[6]=='O' or l[1]==l[4]==l[7]=='O' or l[2]==l[5]==l[8]=='O':
		markflag=1
		return True
	elif l[0]==l[4]==l[8]=='X' or l[2]==l[4]==l[6]=='X':
		markflag=0
		return True
	elif l[0]==l[4]==l[8]=='O' or l[2]==l[4]==l[6]=='O':
		markflag=1
		return True
	elif l.count(" ")==0:
		return True
	else:
		return False

#####################################################################################################

def winning_player(uname1, uname2):
	global markflag
	global playerflag
	if markflag==1 and playerflag==1:
		print(f"\n\n  {uname1} is the WINNER.  CONGRATULATIONS !!!\n")
	elif markflag==1 and playerflag==2:
		print(f"\n\n  {uname2} is the WINNER.  CONGRATULATIONS !!!\n")
	elif markflag==0 and playerflag==1:
		print(f"\n\n  CONGRATULATIONS {uname2} is the WINNER.  CONGRATULATIONS !!!\n")
	elif markflag==0 and playerflag==2:
		print(f"\n\n  {uname1} is the WINNER.  CONGRATULATIONS !!!\n")
	else:
		print("\n\n  GAME ENDS IN A DRAW :-|\n")


#####################################################################################################
########################################## MAIN PROGRAM #############################################

uname1 = input("\n  Player-I Enter your Name: ")
uname2 = input("  Player-II Enter your Name: ")

while(True):
	os.system('cls' if os.name == 'nt' else 'clear')
	l = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
	markflag=3
	playerflag=3
	u1 = None
	u2 = None

	greeting(uname1, uname2)
	assignment(uname1, uname2)
	gameplay(uname1, uname2)
	res = input(("\n\n\t  Wanna Play Again ? ['N' to exit]:"))
	if res.lower() == 'n':
		exit()
	else:
		continue