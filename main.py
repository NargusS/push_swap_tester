# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: achane-l <achane-l@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/10/20 14:16:29 by achane-l          #+#    #+#              #
#    Updated: 2021/10/22 17:48:51 by achane-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import command
import sys
import os
import random

def make_my_push_swap(stack_a, n_testcase):
	exec_command = ".././push_swap ";
	for elem in stack_a:
		exec_command += (str(elem) + ' ');
	os.system(exec_command + "> errors/command_test_"+ str(n_testcase) +".txt");

def	read_and_exec_command(stack_a, stack_b, n_testcase):
	file = open("errors/command_test_"+ str(n_testcase) +".txt", "r");
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

def	check_number_of_instruction_points(size_of_stack, nb_of_cmd):
	if (size_of_stack == 3):
		if (nb_of_cmd == 2 or nb_of_cmd == 3):
			print("SORT ==> "+ '\033[92m' +str(nb_of_cmd)+ " instructions ✅"+'\033[0m');
		else :
			print("SORT WITH TO MANY INSTRUCTIONS ==> " +  '\033[91m'+str(nb_of_cmd)+" instructions ❌" +'\033[0m');
	elif (size_of_stack > 3 and size_of_stack <= 5):
		if (nb_of_cmd <= 12):
			print("SORT ==> "+ '\033[92m' +str(nb_of_cmd)+ " instructions ✅"+'\033[0m');
		else :
			print("SORT WITH TO MANY INSTRUCTIONS ==> " + '\033[91m'+str(nb_of_cmd)+ " instructions ❌"+'\033[0m');
	elif (size_of_stack == 100):
		if (nb_of_cmd < 700):
			print("SORT ==> "+ '\033[92m' +str(nb_of_cmd)+ " instructions ✅ 5 POINTS"+'\033[0m');
		elif (nb_of_cmd < 900):
			print("SORT ==> "+ '\033[92m' +str(nb_of_cmd)+ " instructions ✅ 4 POINTS"+'\033[0m');
		elif (nb_of_cmd < 1100):
			print("SORT ==> "+ '\033[92m' +str(nb_of_cmd)+ " instructions ✅ 3 POINTS"+'\033[0m');
		elif (nb_of_cmd < 1300):
			print("SORT ==> "+ '\033[92m' +str(nb_of_cmd)+ " instructions ✅ 2 POINTS"+'\033[0m');
		elif (nb_of_cmd < 1500):
			print("SORT ==> "+ '\033[92m' +str(nb_of_cmd)+ " instructions ✅ 1 POINTS"+'\033[0m');
		else:
			print("SORT WITH TO MANY INSTRUCTIONS ==> " + '\033[91m'+ str(nb_of_cmd)+" instructions ❌"+'\033[0m');
	elif (size_of_stack == 500):
		if (nb_of_cmd < 5500):
			print("SORT ==> "+ '\033[92m' +str(nb_of_cmd)+ " instructions ✅ 5 POINTS"+'\033[0m');
		elif (nb_of_cmd < 7000):
			print("SORT ==> "+ '\033[92m' +str(nb_of_cmd)+ " instructions ✅ 4 POINTS"+'\033[0m');
		elif (nb_of_cmd < 8500):
			print("SORT ==> "+ '\033[92m' +str(nb_of_cmd)+ " instructions ✅ 3 POINTS"+'\033[0m');
		elif (nb_of_cmd < 10000):
			print("SORT ==> "+ '\033[92m' +str(nb_of_cmd)+ " instructions ✅ 2 POINTS"+'\033[0m');
		elif (nb_of_cmd < 11500):
			print("SORT ==> "+ '\033[92m' +str(nb_of_cmd)+ " instructions ✅ 1 POINTS"+'\033[0m');
		else:
			print("SORT WITH TO MANY INSTRUCTIONS ==> " + '\033[91m' + str(nb_of_cmd)+" instructions ❌"+'\033[0m');
	else :
		print("SORT ==> "+ '\033[92m' +str(nb_of_cmd)+ " instructions ✅"+'\033[0m');

def	check_data(stack_a, stack_b, n_testcase, size_of_stack):
	command_file = open("errors/command_test_"+ str(n_testcase) +".txt", "r");
	command_file = command_file.readlines();
	check_number_of_instruction_points(size_of_stack, len(command_file));
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
	return (len(command_file));

def all_is_good(stack_a, stack_b, n_testcase, size_of_stack):
	if not stack_b and check_sort(stack_a) == 1:
		return(check_data(stack_a, stack_b, n_testcase, size_of_stack));
	else :
		save_error_stack = open("errors/stacks_of_test_"+ str(n_testcase)+".txt", "a");
		if (check_sort(stack_a) == 0):
			print('\033[91m'+"NOT WORKS ❌ STACK_A IS NOT SORT ❌"+'\033[0m');
		if stack_b:
			print('\033[91m' + "NOT WORKS ❌ STACK_B IS NOT EMPTY ❌"+'\033[0m');
		print_my_stacks(stack_a,stack_b, save_error_stack);
		save_error_stack.close();
		return (0);

def	get_test(min_value, max_value, size_of_stack, n_testcase, state_test):
	random.seed(n_testcase);
	number_of_moves = 0;
	stack_a = random.sample(range(min_value, max_value), size_of_stack);
	stack_b = [];
	make_my_push_swap(stack_a, n_testcase);
	if (read_and_exec_command(stack_a, stack_b, n_testcase) == 1):
		number_of_moves = all_is_good(stack_a, stack_b, n_testcase, size_of_stack);
		os.system("rm errors/command_test_" + str(n_testcase) + ".txt");
		if (number_of_moves > 0):
			state_test[0] += 1;
		else:
			state_test[1] += 1;
			number_of_moves = 0;
	else:
		print('\033[91m' + "NOT WORKS ❌ You display something that is not a command ❌"+'\033[0m');
		failed_test += 1;
	return (number_of_moves);

if __name__ == "__main__":
	number_of_test = int(sys.argv[1]);
	size_of_stack = int(sys.argv[2]);
	min_value = int(sys.argv[3]);
	max_value = int(sys.argv[4]);
	number_of_moves_total = 0;
	i = 1;

	if (min_value >= max_value):
		print("ERROR :The Min_Value is greather or equal to Max_Value");
	elif (min_value + size_of_stack > max_value):
		print("ERROR : The Difference between Min_value and Max_value is too small");
	else :
		state_test = [0,0];
		while i <= number_of_test:
			print('\033[93m'+"========================= TEST_CASE N°",str(i), " ========================="+'\033[0m');
			number_of_moves_total += get_test(min_value, max_value, size_of_stack, i, state_test);
			i += 1;
	print('\033[92m' +"SUCCESS : " + str(state_test[0]) + '✅' +'\033[0m');
	print('\033[91m' +"FAILED : " + str(state_test[1]) + '✅' +'\033[0m');
	print('\033[93m' +"Average of moves for SUCCESS TEST: " + str(number_of_moves_total/state_test[0])+'\033[0m');
