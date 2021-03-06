### This is more of a joke, and trying to make something turing-complete.
def t000(code):
	stack=[]
	ptr=-1
	code="".join([i for i in code if i in "0!sl=+-;:o#S~`g"])
	saves=[]
	dir_=1
	"""<0> pushes a 0 on top of the stack.
<!> pops the top value of the stack and pushes 1 if it's 0, otherwise it pushes 0.
<s> saves the next position to save states.
<l> pops the top value of the stack, and if the next value popped is not 0, it goes to the first popped value save state.
<=> pops two values from the stack and pushes 0 if they aren't equal, 1 otherwise.
<+> adds two popped items from stack, and pushes it.
<-> decrements the top of the stack.
<;> pops the top value from the stack.
<:> pops the top value from the stack, and pushes it twice.
<o> outputs the top value from the stack as an integer if the next popped value not 0, otherwise it outputs the popped value as a string.
<#> pops the top value from the stack and skips the next instruction if it's 0.
<S> stops the program.
<~> swaps the top two items on the stack.
<`> change code direction.
EOF will return to the beginning of the program."""
	while(code[ptr]!="S"):
		ptr+=dir_
		if(ptr>=len(code)):ptr=0
		if(code[ptr]=="0"):stack.append(0)
		if(code[ptr]=="!"):stack.append(int(not(stack.pop)))
		if(code[ptr]=="s"):saves.append(ptr+1)
		if(code[ptr]=="l"):
			tmp1=stack.pop()
			if(stack.pop()!=0):
				ptr=saves[tmp1]
				continue
		if(code[ptr]=="="):stack.append(int(stack.pop()==stack.pop()))
		if(code[ptr]=="+"):stack.append(stack.pop()+stack.pop())
		if(code[ptr]=="-"):stack[-1]-=1
		if(code[ptr]==";"):
			if(len(stack)>=1):stack.pop()
			else:raise Exception("The stack can't be smaller than 0.")
		if(code[ptr]==":"):stack.append(stack[-1])
		if(code[ptr]=="o"):
			tmp1=stack.pop()
			if(stack.pop()!=0):print(int(tmp1))
			else:print(ord(tmp1))
		if(code[ptr]=="#"):
			if(stack.pop()==0):
				ptr+=dir_
				continue
		if(code[ptr]=="~"):
			tmp1=stack.pop()
			tmp2=stack.pop()
			stack.append(tmp1)
			stack.append(tmp2)
		if(code[ptr]=="`"):dir_*=-1
### Another joke. but with a tape.
def t001(code):
	tape=[0]*30000 # I've just seen this number a lot with tapes.
	ptr=0
	tptr=0
	code="".join([i for i in code if i in "!()g+;:S"])
	"""figure it out."""
	while(code[ptr]!="S"):
		if(code[ptr]=="!"):tape[tptr]=int(not(tape[tptr]))
		if(code[ptr]=="("):tptr+=1
		if(code[ptr]==")"):
			if(tptr>0):tptr-=1
			else:raise Exception("The pointer can't be negative.")
		if(code[ptr]=="g"):
			ptr=tape[tptr]
			continue
		if(code[ptr]=="+"):tape[tptr]+=tape[tptr+1]
		if(code[ptr]==";"):tape[tptr]*=-1
		if(code[ptr]==":"):tape[tptr]=tape[tptr-1]
