def toString(List): 
	return ''.join(List) 

def permute(a, l, r): 
	if l == r: 
		print(toString(a)) 
	else: 
		for i in range(l, r): 
			a[l], a[i] = a[i], a[l] 
			permute(a, l+1, r) 
			a[l], a[i] = a[i], a[l] # backtrack 
 
string = "aeiou"
n = len(string) 
a = list(string) 

# Function call 
permute(a, 0, n) 

# This code is contributed by Bhavya Jain 

