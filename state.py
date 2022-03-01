class State():
	def __init__(self, pos = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR', WorB = 'w', kq = 'KQkq', enp = '-', halfm = 0, fullm = 1):
		self.pos = pos.split(sep = '/')
		self.WorB = WorB
		self.kq = kq
		self.enp = enp
		self.halfm = halfm
		self.fullm = fullm
	def get_fen(self):
		return f"{self.pos} {self.WorB} {self.kq} {self.enp} {self.halfm} {self.fullm}"
	
	#now: we want sth close to the 'inverse' of what is written above so that when passed a fen will produce an object of class State (so would that be a class function?)
	@classmethod
	def get_state(cls, fen):
		return cls(fen.split())
