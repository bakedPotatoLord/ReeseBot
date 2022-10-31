import random

def display(a,ah,v,vh,t,d=None):
	if d == None:
		return f"---------------------\n\n{a.display_name}'s health {ah}\n\n{v.display_name}'s health {vh}\n\n{t.mention}'s turn\n\n---------------------"
	else:
		return f"---------------------\n{d} damage was dealt\n\n{a.display_name}'s health {ah}\n\n{v.display_name}'s health {vh}\n\n{t.mention}'s turn\n\n---------------------"

def atk(h,p=1):
	num = random.randint(0,15*p)
	return h - num,num

def turnmgr(a,v,t):
	if t == a:
		return v
	else:
		return a

def checkdead(a,ah,v,vh):
	if ah <= 0:
		return True, a
	elif vh <= 0:
		return True, v
	else:
		return False, a
