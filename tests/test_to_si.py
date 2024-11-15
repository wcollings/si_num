import pytest
from si_num import to_si

def test_to_si():
	outpt=['14.1','141.0','1.41k','14.1k','141.0k','1.41M']
	inpt=[14.1,141,1410,14100,141000,1410000,14100000]
	for val,res in zip(inpt,outpt):
		assert to_si(val)==res,f"{val=} != {res=}"
	inpt=[1.41,1.41e-1,1.41e-2,1.41e-3,1.41e-4,1.41e-5,1.41e-6,1.41e-7,1.41e-8,1.41e-9]
	outpt=["1.41","141.0m","14.1m","1.41m","141.0u","14.1u","1.41u","141.0n","14.1n","1.41n"]
	for val,res in zip(inpt,outpt):
		assert to_si(val)==res,f"{to_si(val)=} != {res=}"
