def push(stack_a, stack_b, command):
	if (command == "pa\n"):
		value = stack_b[0];
		stack_b.pop(0);
		stack_a.insert(0, value);
	else:
		value = stack_a[0];
		stack_a.pop(0);
		stack_b.insert(0, value);

def	rotate(stack_a, stack_b, command):
	if (command == "ra\n"):
		value = stack_a[0];
		stack_a.pop(0);
		stack_a.append(value);
	elif (command == "rb\n"):
		value = stack_b[0];
		stack_b.pop(0);
		stack_b.append(value);
	else:
		value = stack_a[0];
		stack_a.pop(0);
		stack_a.append(value);
		value = stack_b[0];
		stack_b.pop(0);
		stack_b.append(value);

def	reverse_rotate(stack_a, stack_b, command):
	if (command == "rra\n"):
		value = stack_a[-1];
		stack_a.pop(-1);
		stack_a.insert(0,value);
	elif (command == "rrb\n"):
		value = stack_b[-1];
		stack_b.pop(-1);
		stack_b.insert(0,value);
	else:
		value = stack_a[-1];
		stack_a.pop(-1);
		stack_a.insert(0,value);
		value = stack_b[-1];
		stack_b.pop(-1);
		stack_b.insert(0,value);

def swap(stack_a, stack_b, command):
	if (command == "sa\n"):
		value = stack_a[1];
		stack_a.pop(1);
		stack_a.insert(0,value);
	elif (command == "sb\n"):
		value = stack_b[1];
		stack_b.pop(1);
		stack_b.insert(0,value);
	else:
		value = stack_a[1];
		stack_a.pop(1);
		stack_a.insert(0,value);
		value = stack_b[1];
		stack_b.pop(1);
		stack_b.insert(0,value);

def	initiate_command(stack_a, stack_b, command):
	if (command[0] == 'p'):
		push(stack_a, stack_b, command);
	elif (command[0] == 'r' and command[1] != 'r'):
		rotate(stack_a, stack_b, command);
	elif (command[0] == 's'):
		swap(stack_a, stack_b, command);
	else:
		reverse_rotate(stack_a, stack_b, command);
