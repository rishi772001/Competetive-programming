def calc(s):
	for i in s:
		p=s.count(i)
		if(p>1):
			m=p%2
			s=s.replace(i,'',p-m)
	if(len(s)>0):
		return s
	else:
		r="Empty String"
		return r
print(calc("daad"))
		
				
				
				
				
				
				
				
				
				
				
				
			