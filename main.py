import command
import sys
import os
import random

def make_my_push_swap(stack_a, n_testcase):
	exec_command = ".././push_swap ";
	for elem in stack_a:
		exec_command += (str(elem) + ' ');
	os.system(exec_command + "> command_test_"+ str(n_testcase) +".txt");

def	read_and_exec_command(stack_a, stack_b, n_testcase):
	file = open("command_test_"+ str(n_testcase) +".txt", "r");
	for line in file:
		if command.initiate_command(stack_a, stack_b, line) == 0:
			file.close();
			return (0);
	file.close();
	return (1);

def print_my_stacks(stack_a, stack_b, file):
	i = 0;
	file.write(5 * ' '+"STACK_A" + ' ' * 5+ "STACK_B" + "\n");
	while i < len(stack_a) or i < len(stack_b):
		if (i < len(stack_a) and i < len(stack_b)):
			file.write(5 * ' ' + str(stack_a[i]) + 5 * ' ' + str(stack_b[i]) + "\n");
		elif (i < len(stack_a) and i >= len(stack_b)):
			file.write(5 * ' ' + str(stack_a[i]) + 5 * ' ' + "Empty" + "\n");
		else :
			file.write(5 * ' ' + "Empty" + 5 * ' ' +str(stack_b[i]) + "\n");
		i += 1;

def check_sort(stack):
	i = 1
	while (i < len(stack)):
		if (stack[i] < stack[i - 1]):
			return (0);
		i += 1;
	return (1);

def	check_data(stack_a, stack_b, n_testcase):
	command_file = open("command_test_"+ str(n_testcase) +".txt", "r");
	command_file = command_file.readlines();
	print("All is sort with " + str(len(command_file)) +" moves with :");
	print("pa : ", str(command_file.count("pa\n")));
	print("pb : ", str(command_file.count("pb\n")));
	print("ra : ", str(command_file.count("ra\n")));
	print("rb : ", str(command_file.count("rb\n")));
	print("rr : ", str(command_file.count("rr\n")));
	print("rra : ", str(command_file.count("rra\n")));
	print("rrb : ", str(command_file.count("rrb\n")));
	print("rrr : ", str(command_file.count("rrr\n")));
	print("sa : ", str(command_file.count("sa\n")));
	print("sb : ", str(command_file.count("sb\n")));
	print("ss : ", str(command_file.count("ss\n")));

def all_is_good(stack_a, stack_b, n_testcase):
	if not stack_b and check_sort(stack_a) == 1:
		check_data(stack_a, stack_b, n_testcase);
	else :
		save_error_stack = open("stacks_of_test_"+ str(n_testcase)+".txt", "a");
		if (check_sort(stack_a) == 0):
			print("Stack not sort.");
		if stack_b:
			print("Stack_b is not empty.");
		print_my_stacks(stack_a,stack_b, save_error_stack);
		save_error_stack.close();

def	get_test(size_of_stack, n_testcase):
	stack_a = random.sample(range(-2147483648, 2147483647), size_of_stack);
	stack_b = [];
	make_my_push_swap(stack_a, n_testcase);
	if (read_and_exec_command(stack_a, stack_b, n_testcase) == 1):
		all_is_good(stack_a, stack_b, n_testcase);
		os.system("rm command_test_" + str(n_testcase) + ".txt");
	else:
		print("You display something that is not a command");

number_of_test = int(sys.argv[1]);
size_of_stack = int(sys.argv[2]);
i = 1;
while i <= number_of_test:
	print("========================= TEST_CASE N°",str(i), " =========================");
	get_test(size_of_stack, i);
	i += 1;