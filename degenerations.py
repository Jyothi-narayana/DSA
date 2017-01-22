def is_a_solution(a, k, n):
    if (k == n):
    	return True
    else:
    	return False

def generate_candidates(a, k, n):
	# the candidates for the next position excludes all the elements which have already appeared and correct position element
	candidates = []
	for i in range(1, n+1):
		if i not in a and i != k:
			candidates.append(i)
	return candidates

def process_solution(a):
	print "{", a[1:], "}"

def backtrack(a, k, n):
	if (is_a_solution(a, k, n)):
		process_solution(a)
	else:
		k = k + 1
    	candidates = generate_candidates(a, k, n)
    	for c in candidates:
    		perm = list(a)
    		perm[k] = c
    		#print a, k
    		backtrack(perm, k, n)
n = 4
a = [0]*(n+1)
backtrack(a, 0, n)
