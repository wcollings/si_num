from si_num import si
import pytest

def si_test():
	inpt=[14.1,1.41e5,1.41e-9]
	outpt=['14.1','141.0M','1.41n']
	for a,b in zip(inpt,outpt):
		assert str(si(a))==b
