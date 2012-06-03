#-*- encoding: utf-8 -*-
__author__ = "Eduardo Orige"
__credits__ = ["Eduardo Orige"]
__version__ = "0.01 beta"
__maintainer__ = "Eduardo Orige"
__email__ = "eduardo.orige@gmail.com"
__status__ = "Em Producao"
__description__ = 'Testes Unitarios para o QuePlaca'

import unittest
from queplaca import QuePlaca

q = QuePlaca()
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


class QuePlaca_PR_Tests(unittest.TestCase):
	
	def test_PR_1(self):
		#AAA - AZZ
		for letra_1 in alfabeto:
			for letra_2 in alfabeto:
				v_placa = 'A%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)	
				self.failIf(placa != 'PR')
				
	def test_PR_2(self):
		#BAA - BEZ
		for letra_1 in alfabeto[1:5]:
			for letra_2 in alfabeto:
				v_placa = 'B%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'PR')
				

class QuePlaca_SP_Tests(unittest.TestCase):
	#BFA a GKI
	def test_SP_1(self):
		#BFZ - BZZ
		for letra_1 in alfabeto[5:]:
			for letra_2 in alfabeto:
				v_placa = 'B%s%s-1234' % (letra_1,letra_2) 
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'SP')
				
	def test_SP_2(self):
		#CAA - FZZ	
		for letra_0 in alfabeto[2:6]:
			for letra_1 in alfabeto:
				for letra_2 in alfabeto:
					v_placa = '%s%s%s-1234' % (letra_0,letra_1,letra_2)
					placa = q.quePlaca(v_placa)
					
					self.failIf(placa != 'SP')
	def test_SP_3(self):	
		#GAA - GJZ
		for letra_1 in alfabeto[:10]:
				for letra_2 in alfabeto:
					v_placa = 'G%s%s-1234' % (letra_1,letra_2)
					placa = q.quePlaca(v_placa)
			
					self.failIf(placa != 'SP')
	def test_SP_4(self):
		#GKA - GKI
		for letra_2 in alfabeto[:9]:
			v_placa = 'GK%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)

			self.failIf(placa != 'SP')

class QuePlaca_MG_Tests(unittest.TestCase):
	#GKJ a HOK
	
	def test_MG_1(self):
		#GKJ - GKZ
		for letra_2 in alfabeto[10:]:
			v_placa = 'GK%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MG')
			
	def test_MG_2(self):
		#GLA - GZZ
		for letra_1 in alfabeto[11:]:
			for letra_2 in alfabeto:
				v_placa = 'G%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'MG')
		
	def test_MG_3(self):
		#HAA - HNZ
		for letra_1 in alfabeto[:14]:
			for letra_2 in alfabeto:
				v_placa = 'H%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'MG')
				
	def test_MG_4(self):
		#HOA - HOK
		for letra_2 in alfabeto[:11]:
			v_placa = 'HO%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			self.failIf(placa != 'MG')
			
class QuePlaca_MA_Tests(unittest.TestCase):
	#HOL a HQE
	
	def test_MA_1(self):
		#HOL - HOZ
		for letra_2 in alfabeto[11:]:
			v_placa = 'HO%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)

			self.failIf(placa != 'MA')
	
	def test_MA_2(self):
		#HPA - HPZ
		for letra_2 in alfabeto:
			v_placa = 'HP%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)

			self.failIf(placa != 'MA')
			
	def test_MA_3(self):
		#HQA - HQE
		for letra_2 in alfabeto[:5]:
			v_placa = 'HQ%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MA')
			
class QuePlaca_MS_Tests(unittest.TestCase):
	#HQF a HTW
	
	def test_MS_1(self):
		#HQF - HQZ
		for letra_2 in alfabeto[5:]:
			v_placa = 'HQ%s-1234' % (letra_2) 
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MS')
			
	def test_MS_2(self):
		#HRA - HSZ
		for letra_1 in alfabeto[17:19]:
			for letra_2 in alfabeto:
				v_placa = 'H%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'MS')
	
	def test_MS_3(self):
		#HTA - HTW
		for letra_2 in alfabeto[:23]:
			v_placa = 'HT%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MS')
			
class QuePlaca_CE_Tests(unittest.TestCase):
	#HTX a HZA
	
	def test_CE_1(self):
		#HTX - HTZ
		for letra_2 in alfabeto[23:]:
			v_placa = 'HT%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'CE')
	
	def test_CE_2(self):
		#HUA - HYZ
		for letra_1 in alfabeto[20:25]:
			for letra_2 in alfabeto:
				v_placa = 'H%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'CE')

	def test_CE_3(self):
		#HZA
		placa = q.quePlaca('HZA-1234')	
		
		self.failIf(placa != 'CE')
		

class QuePlaca_SE_Tests(unittest.TestCase):
	#HZB a IAP
	
	def test_SE_1(self):
		#HZB - HZZ
		for letra_2 in alfabeto[1:]:
			v_placa = 'HZ%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'SE')
			
	def test_SE_2(self):
		#IAA - IAP
		for letra_2 in alfabeto[:16]:
			v_placa = 'IA%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'SE')
			
	
	
		
			
					
					
	
			

if __name__ == '__main__':
	unittest.main()