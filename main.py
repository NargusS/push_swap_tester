import command
import sys
import os
import random

exec_command = ".././push_swap "
stack_a = [];
stack_b = [];

"""
for arg in sys.argv:
	if (arg != "main.py"):
		exec_command += (arg + ' ');
		stack_a.append(int(arg));"""
number_of_test = int(sys.argv[1]);
size_of_stack = int(sys.argv[2]);

stack_a = random.sample(range(-2147483648, 2147483647), size_of_stack);
for elem in stack_a:
	exec_command += (str(elem) + ' ');
os.system(exec_command + "> command.txt");
file = open("command.txt", "r");

for line in file:
	command.initiate_command(stack_a, stack_b, line);

prec = stack_a[0];
for i in stack_a:
	if (prec > i):
		print("KO");
		break;
	prec = i;
if not stack_b:
	print("OK");
else:
	print("KO STACK_B IS NOT EMPTY");
os.system("rm command.txt");