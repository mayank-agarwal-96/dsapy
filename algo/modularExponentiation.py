Time complexity : log(y) 

def power(x,y,p):
	ans = 1
	
	x = x % p
	
	while y>0:
		if y & 1:
			ans = (ans*x) % p
			
		y = y>>1
		x = (x*x) % p
	return ans
	