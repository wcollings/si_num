from math import log10 as log, floor,ceil
prefixes=['q','r','y','z','a','f','p','n','u','m','','k','M','G','T','P','E','Z','Y','R','Q']
units={p:v for v,p in zip(range(-10,11),prefixes)}
def from_si(num:str,micro_is_mu:bool=False) ->float:
	if num[-1] in prefixes:
		unit=num[-1]
		num=num[:-1]
	else:
		unit=""
	if micro_is_mu and unit=="μ":
		unit="u"
	pow=10**(units[unit]*3)
	return float(num)*pow
