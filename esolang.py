def thing(code):
	stack=[]
	ptr=-1
	code="".join([i for i in code if i in "0!sl=+-;:o#S"])
	saves=[]
	"""<0> pushes a 0 on top of the stack.
<!> pops the top value of the stack and pushes 1 if it's 0 otherwise, it pushes 0.
<s> saves the next position to save states.
<l> pops the top value of the stack, and if the next value popped is not 0, it goes to the first popped value save state.
<=> pops two values from the stack and pushes 0 if they aren't equal, 1 otherwise.
<+> pops the top value from the stack, adds 1, and pushes it back.
<-> pops the top value from the stack, subtracts 1, and pushes it back.
<;> pops the top value from the stack.
<:> pops the top value from the stack, and pushes it twice.
<o> outputs the top value from the stack as an integer if the next popped value not 0, otherwise it outputs the popped value as a string.
<#> pops the top value from the stack and skips the next instruction if it's 0.
<S> stops the program.
EOF will return to the beginning of the program."""
	while(code[ptr]!="S"):
		ptr+=1
		if(ptr>=len(code)):ptr=0
		if(code[ptr]=="0"):stack.append(0)
		if(code[ptr]=="!"):stack.append(int(not(stack.pop)))
		if(code[ptr]=="s"):saves.append(ptr+1)
		if(code[ptr]=="l"):
			tmp1=stack.pop()
			if(stack.pop()!=0):
				ptr=saves[tmp1]
				continue
		if(code[ptr]==";"):stack.pop()
		if(code[ptr]==":"):stack.append(stack[-1])
		if(code[ptr]=="o"):
			tmp1=stack.pop()
			if(stack.pop()!=0):print(int(tmp1))
			else:print(ord(tmp1))
		if(code[ptr]=="#"):
			if(stack.pop()==0):
				ptr+=1
				continue
		if(code[ptr]=="S"):break
