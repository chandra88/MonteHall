#!/usr/bin/python
import os, sys, math, random

'''---------------------------------------------------------
Author:		Chandra Nepali
Program:	Monty Hall Problem
Date:		June 5, 2015
Contact:	coder5678@gmail.com

There are four doors, behind the two doors (random) have 
hidden prizes while behind the other two doors have goats. 
A person is asked to choose the door. After he choosed the 
door, he has chance to change his decision. What is his 
chance of winning (i. e. getting prize) if he do not change 
his decision vs if he change he decision.

Here: p -> doors with prize
      g -> doors with goats	
---------------------------------------------------------'''

door = ['p', 'p', 'g', 'g']
n = 4
m = 8000
nTrial = 20

nochange_succ = 0.0
nochange_fail = 0.0

change_succ = 0.0
change_fail = 0.0

for trial in range(0, nTrial):
	random.shuffle(door)
	for i in range(0, m):
		first_chose = random.randint(1, n)

		# if he does not change his decision
		if(door[first_chose-1] == 'g'): nochange_fail = nochange_fail + 1.0
		if(door[first_chose-1] == 'p'): nochange_succ = nochange_succ + 1.0

		# if he change his decision
		temp = door[:]
		temp.remove(temp[first_chose-1])
		temp.remove('g')

		second_chose = random.randint(1, 2)

		if(temp[second_chose-1] == 'g'): change_fail = change_fail + 1.0
		if(temp[second_chose-1] == 'p'): change_succ = change_succ + 1.0


print '\n\t========================================='
print '\tIn case he does not change his decision:'
print '\tSuccess:', '%0.1f'%(nochange_succ*100/(m*nTrial)), '%    Fail:' , '%0.1f'%(nochange_fail*100/(m*nTrial)), '%\n'

print '\tIn case he change his decision:'	
print '\tSuccess:', '%0.1f'%(change_succ*100/(m*nTrial)), '%    Fail:' , '%0.1f'%(change_fail*100/(m*nTrial)), '%'
print '\t========================================='
