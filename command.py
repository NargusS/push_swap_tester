# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    command.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: achane-l <achane-l@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/10/20 14:16:43 by achane-l          #+#    #+#              #
#    Updated: 2021/10/22 16:37:08 by achane-l         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def push(stack_a, stack_b, command):
	if (command == "pa\n"):
		value = stack_b[0];
		stack_b.pop(0);
		stack_a.insert(0, value);
	else:
		value = stack_a[0];
		stack_a.pop(0);
		stack_b.insert(0, value);

def rotate_stack(my_stack):
	value = my_stack[0];
	my_stack.pop(0);
	my_stack.append(value);

def	rotate(stack_a, stack_b, command):
	if (command == "ra\n"):
		rotate_stack(stack_a);
	elif (command == "rb\n"):
		rotate_stack(stack_b);
	else:
		rotate_stack(stack_a);
		rotate_stack(stack_b);

def reverse_rotate_stack(my_stack):
	value = my_stack[-1];
	my_stack.pop(-1);
	my_stack.insert(0,value);

def	reverse_rotate(stack_a, stack_b, command):
	if (command == "rra\n"):
		reverse_rotate_stack(stack_a);
	elif (command == "rrb\n"):
		reverse_rotate_stack(stack_b);
	else:
		reverse_rotate_stack(stack_a);
		reverse_rotate_stack(stack_b);

def	swap_stack(my_stack):
	value = my_stack[1];
	my_stack.pop(1);
	my_stack.insert(0,value);

def swap(stack_a, stack_b, command):
	if (command == "sa\n"):
		swap_stack(stack_a);
	elif (command == "sb\n"):
		swap_stack(stack_b);
	else:
		swap_stack(stack_a);
		swap_stack(stack_b);

def	initiate_command(stack_a, stack_b, command):
	if (command[0] == 'p'):
		push(stack_a, stack_b, command);
	elif (command[0] == 'r' and command[2] == '\n'):
		rotate(stack_a, stack_b, command);
	elif (command[0] == 'r' and command[3] == '\n'):
		reverse_rotate(stack_a, stack_b, command);
	elif (command[0] == 's'):
		swap(stack_a, stack_b, command);
	else:
		return (0);
	return (1);
