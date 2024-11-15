import pytest
from si_num import from_si

def test_from_si():
	inpt=['14.1','141.0','1.41k','14.1k','141.0k','1.41M']
	outpt=[14.1,141,1410,14100,141000,1410000,14100000]
	for val,res in zip(inpt,outpt):
		assert from_si(val)==res,f"{val=} != {res=}"
