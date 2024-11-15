from .to_si import to_si
from .from_si import from_si
__all__=['to_si','from_si']

class si(float):
	sign=False
	def __new__(self,val):
		if isinstance(val,str):
			return float.__new__(self,from_si(val))
		return float.__new__(self,val)
	def __repr__(self):
		return to_si(self,sign=self.sign)
