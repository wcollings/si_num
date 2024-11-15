from math import log10 as log, floor,ceil
prefixes=['q','r','y','z','a','f','p','n','u','m','','K','M','G','T','P','E','Z','Y','R','Q']
units={v:p for v,p in zip(range(-10,11),prefixes)}
def sign(x) -> int:
	if x<0:
		return -1
	if x==0:
		return 0
	return 1

def true_floor(s:float) -> int:
	if s<0:
		return ceil(s)
	return floor(s)
def to_si(num:float,sig_figs:int=2,unit_diff:dict={},sign=False):
	"""
	Convert a number to use metric prefixes.

	Parameters
	----------
	num:float
		The number to convert
	sig_figs:int
		The number of decimal points to keep
	unit_diff:dict
		If you'd like to use a different prefix for some unit, specify that here. The old unit is the key, and the replacement is the value. This is useful for if you really need micro to be encoded with a mu, or if you want Mega to be Meg instead of M (for spice)
	sign:bool
		If the value is positive, whether or not to include the "+"
	"""
	if num==0:
		return "0"
	s=""
	if num < 0:
		s="-"
		num=abs(num)
	units={v:p for v,p in zip(range(-10,11),prefixes)}
	if unit_diff:
		inverse={v:k for k,v in units.items()}
		for unit in unit_diff:
			key=inverse[unit]
			units[key]=unit_diff[unit]
	inter=log(num)
	unit=units[floor(inter/3)]
	# print("Found unit:" +unit)
	pow=3*floor(inter/3)
	# print("Exponent="+str(pow))
	new_val=num/(10**pow)
	new_val=round(num/(10**pow),sig_figs)
	if sign and new_val>0:
		s="+"
	return f"{s}{new_val}{unit}"

if __name__=="__main__":
	test_nums=[5e7,2.34e-6,5.32e-3]
	answers=['50Meg','2.36u','5.32m']
	for t,a in zip(test_nums,answers):
		print("--------Running " + str(t) + "------")
		print(to_si(t,unit_diff={'u':'μ','M':'Meg'}) + "=?=" + a)
