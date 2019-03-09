print("hello world")
print("àäèí àäèí äâà")

print("hel")
print("trololo")


111123
print("1")
print("gadost'")
f = open('input.txt','r') #enter the number of transfers in the file
g = open('output.txt','w')
i = int(f.readline())
for j in range(i):
	a,b = map(int,f.readline().split())
	def slk (a,b):
		m = ''
		s = ''
		while a != 0:
			if a%b >= 10:
				if a%b == 10:
					m+='A'
				elif a%b == 11:
					m+='B'
				elif a%b == 12:
					m+='C'
				elif a%b == 13:
					m+='D'
				elif a%b == 14:
					m+='E'
				elif a%b == 15:
					m+='F'
			else:
				m+=str(a%b)
			a//=b
		m =list(m)
		m.reverse()
		for i in range(len(m)):
			s+=str(m[i])
		g.write(str(s))
		g.write('\n')
		return 
	slk(a,b)
g.close()
f.close()
