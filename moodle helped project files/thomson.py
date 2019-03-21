#Raja Naseer Ahmed Khan G00351263
#Graph Theory Project

class state:
	label = None
	edge1 = None
	edge2 = None
	
class nfa:
	initial = None
	accept = None

	def __init__(self, initial, accept):
		self.initial = initial
		self.accept = accept
	
def compile(pofix):
	nfastack = []
	
	for c in pofix:	
			# Pop two NFA's of the stack
		if c == '.':
			nfa2 = nfastack.pop()
			nfa1 =nfastack.pop()
				
				# Connect first NFA's accept state to the second's initial
			nfa1.accept.edge1 = nfa2.initial
				
				# Push NFA to the stack.
			newnfa = nfa(nfa1.initial, nfa2.accept)
			nfastack.append(newnfa)
				
		#//////////////////////////////////////		
		elif c == '|':
		
				# Pop two NFA's off the stack
			nfa2 = nfastack.pop()
			nfa1 = nfastack.pop()
		
			#Create a new initial state, connect it to initial states
			# of the two NFA's popped from the stack.
			initial = state()
			initial.edge1 = nfa1.initial
			initial.edge2 = nfa2.initial
			
			#Create new accept state, connecting the accept states
				# of the two NFA's popped from the stack, to the new state
			accept = state()
			nfa1.accept.edge1 = accept
			nfa2.accept.edge1 = accept
			
			# Push new NFA to the stack.
			newnfa = nfa(initial, accept)
			nfastack.append(newnfa)
				
			#/////////////////////////////////////////
		elif c == '*':
			# Pop a single NFA from the stack.
			nfa1 = nfastack.pop()
		
			# Create new initial and accept state
			initial = state()
			accept = state()

			#join the new initial state to nfa1's initial state and the new accept state.
			initial.edge1 = nfa1.initial
			initial.edge2 = accept
			
			#join the old accept state to the new accept state and nfa1's initial state.
			nfa1.accept.edge1 = nfa1.initial
			nfa1.accept.edge2 = accept
			
			# Push new NFA to the stack.
			newnfa = nfa(initial,accept)
			nfastack.append(newnfa)
		
		#/////////////////////////////////////////////
		else:
			# Create new initial adn accept states.
				
			accept = state()
			initial = state()
				
				# Join the initial state the accept state using an arrow labelled c.
			initial.label = c
			initial.edge1 = accept
				
				# Push new NFA to the stack.
			newnfa = nfa(initial, accept)
			nfastack.append(newnfa)
				
				# nfastack should only have a single nfa on it at this point.
	return nfastack.pop()

	
print(compile("ab.cd.|"))
print(compile("aa.*"))