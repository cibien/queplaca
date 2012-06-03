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
			

class QuePlaca_RS_Tests(unittest.TestCase):
	#IAQ a JDO
	def test_RS_1(self):
		#IAQ - IAZ
		for letra_2 in alfabeto[16:]:
			v_placa = 'IA%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)

			self.failIf(placa != 'RS')

	def test_RS_2(self):	
		#IBA - IZZ
		for letra_1 in alfabeto[1:]:
			for letra_2 in alfabeto:
				v_placa = 'I%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				self.failIf(placa != 'RS')
				
	def test_RS_3(self):
		#JAA - JCZ
		for letra_1 in alfabeto[:3]:
			for letra_2 in alfabeto:
				v_placa = 'J%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				self.failIf(placa != 'RS')
				
	def test_RS_4(self):
		#JDA - JDO
		for letra_2 in alfabeto[:15]:
			v_placa = 'JD%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			self.failIf(placa != 'RS')
			

class QuePlaca_DF_Tests(unittest.TestCase):
	#JDP a JKR
	def test_DF_1(self):
		#JDP - JDZ
		for letra_2 in alfabeto[15:]:
			v_placa = 'JD%s-1234' % (letra_2)		
			placa = q.quePlaca(v_placa)
			self.failIf(placa != 'DF')
			
	def test_DF_2(self):
		#JEA - JJZ
		for letra_1 in alfabeto[4:10]:
			for letra_2 in alfabeto:
				v_placa = 'J%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				self.failIf(placa != 'DF')
	
	def test_DF_3(self):
		#JKA - JKR
		for letra_2 in alfabeto[:18]:
			v_placa = 'JK%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			self.failIf(placa != 'DF')
	
class QuePlaca_BA_Tests(unittest.TestCase):
	#JKS a JSZ
	def test_BA_1(self)	:
		#JKS - JKZ
		for letra_2 in alfabeto[18:]:
			v_placa = 'JK%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			self.failIf(placa != 'BA')
			
	def test_BA_2(self):
		#JLA - JSZ
		for letra_1 in alfabeto[11:19]:
			for letra_2 in alfabeto:
				v_placa = 'J%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				self.failIf(placa != 'BA')
				
class QuePlaca_PA_Tests(unittest.TestCase):
	#JTA a JWE
	def test_PA_1(self):
		#JTA - JVZ
		for letra_1 in alfabeto[19:22]:
			for letra_2 in alfabeto:
				v_placa = 'J%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				self.failIf(placa != 'PA')
				
	def test_PA_2(self):
		#JWA - JWE
		for letra_2 in alfabeto[:5]:
			v_placa = 'JW%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PA')

class QuePlaca_AM_Tests(unittest.TestCase):
	#JWF a JXY
	def test_AM_1(self):
		#JWF - JWZ 
		for letra_2 in alfabeto[5:]:
			v_placa = 'JW%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AM')
	
	def test_AM_2(self):
		#JXA - JXY
		for letra_2 in alfabeto[:25]:
			v_placa = 'JX%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AM')

class QuePlaca_MT_Tests(unittest.TestCase):
	#JXZ a KAU
	
	def test_MT_1(self):
		#JXZ
		v_placa = 'JXZ-1234'
		placa = q.quePlaca(v_placa)
		
		self.failIf(placa != 'MT')
		
	def test_MT_2(self):
		#KAA- KAU
		for letra_2 in alfabeto[:21]:
			v_placa = 'KA%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MT')
			
class QuePlaca_GO_Tests(unittest.TestCase):
	#KAV a KFC
	
	def test_GO_1(self):
		#KAV - KAZ
		for letra_2 in alfabeto[21:]:
			v_placa = 'KA%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'GO')
			
	def test_GO_2(self):
		#KBA - KEZ
		for letra_1 in alfabeto[1:5]:
			for letra_2 in alfabeto:
				v_placa = 'K%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'GO')
				
	def test_GO_3(self):
		#KFA - KFC
		for letra_2 in alfabeto[:3]:
			v_placa = 'KF%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'GO')

class QuePlaca_PE_Tests(unittest.TestCase):
	#KFD  a KME
	
	def test_PE_1(self):
		#KFD - KFZ
		for letra_2 in alfabeto[3:]:
			v_placa = 'KF%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PE')
			
	def test_PE_2(self):
		#KGA - KLZ
		for letra_1 in alfabeto[6:12]:
			for letra_2 in alfabeto:
				v_placa = 'K%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				self.failIf(placa != 'PE')
			
	def test_PE_3(self):
		#KMA - KME
		for letra_2 in alfabeto[:5]:
			v_placa = 'KM%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PE')

class QuePlaca_RJ_Tests(unittest.TestCase):
	#KMF a LVE
	
	def test_RJ_1(self):
		#KMF - KMZ
		for letra_2 in alfabeto[5:]:
			v_placa = 'KM%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RJ')
			
	def test_RJ_2(self):
		#KNA - KZZ
		for letra_1 in alfabeto[13:]:
			for letra_2 in alfabeto:
				v_placa = 'K%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'RJ')
				
	def test_RJ_3(self):
		#LAA - LUZ
		for letra_1 in alfabeto[:21]:
			for letra_2 in alfabeto:
				v_placa = 'L%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'RJ')
				
	def test_RJ_4(self):
		#LVA - LVE
		for letra_2 in alfabeto[:5]:
			v_placa = 'LV%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RJ')
			
		

class QuePlaca_PI_Tests(unittest.TestCase):
	#LVF a LWQ 
	
	def test_PI_1(self):
		#LVF - LVZ
		for letra_2 in alfabeto[5:]:
			v_placa = 'LV%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PI')
			
	def test_PI_2(self):
		#LWA - LWQ
		for letra_2 in alfabeto[:17]:
			v_placa = 'LW%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PI')
	

class QuePlaca_SC_Tests(unittest.TestCase):
	#LWR a MMM
	
	def test_SC_1(self):
		#LWR - LWZ
		for letra_2 in alfabeto[17:]:
			v_placa = 'LW%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'SC')
			
	def test_SC_2(self):
		#LXA - LZZ
		for letra_1 in alfabeto[23:]:
			for letra_2 in alfabeto:
				v_placa = 'L%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'SC')
				
	def test_SC_3(self):
		#MAA - MLZ
		for letra_1 in alfabeto[:12]:
			for letra_2 in alfabeto:
				v_placa = 'M%s%s-1234' % (letra_1, letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'SC')
				
	def test_SC_4(self):
		#MMA - MMM
		for letra_2 in alfabeto[:13]:
			v_placa = 'MM%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'SC')
			
		
class QuePlaca_PB_Tests(unittest.TestCase)	:
	#MMN a MOW
	
	def test_PB_1(self):
		#MMN - MMZ
		for letra_2 in alfabeto[13:]:
			v_placa = 'MM%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PB')
			
	def test_PB_2(self):
		#MNA - MNZ
		for letra_2 in alfabeto:
			v_placa = 'MN%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
						
			self.failIf(placa != 'PB')
			
	def test_PB_3(self):
		#MOA - MOW
		for letra_2 in alfabeto[:23]:
			v_placa = 'MO%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PB')
			
			

class QuePlaca_ES_Tests(unittest.TestCase):
	#MOX a MTZ
	
	def test_ES_1(self):
		#MOX - MOZ
		for letra_2 in alfabeto[23:26]:
			v_placa = 'MO%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'ES')
			
	def test_ES_2(self):
		#MPA - MTZ
		for letra_1 in alfabeto[15:20]:
			for letra_2 in alfabeto:
				v_placa = 'M%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'ES')				

class QuePlaca_AL_Tests(unittest.TestCase):
	#MUA a MVK
	
	def test_AL_1(self):
		#MUA - MUZ
		for letra_2 in alfabeto:
			v_placa = 'MU%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AL')
			
	def test_AL_2(self):
		#MVA - MVK
		for letra_2 in alfabeto[:11]:
			v_placa = 'MV%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AL')
			
class QuePlaca_TO_Tests(unittest.TestCase):
	#MVL a MXG 
	
	def test_TO_1(self):
		#MVL - MVZ
		for letra_2 in alfabeto[11:]:
			v_placa = 'MV%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			self.failIf(placa != 'TO')
			
	def test_TO_2(self):
		#MWA - MWZ
		for letra_2 in alfabeto:
			v_placa = 'MW%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'TO')
			
	def test_TO_3(self):
		#MXA - MXG
		for letra_2 in alfabeto[:7]:
			v_placa = 'MX%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'TO')

class QuePlaca_RN_Tests(unittest.TestCase):
	#MXH a MZM
	
	def test_RN_1(self):
		#MXH - MXZ
		for letra_2 in alfabeto[7:]:
			v_placa = 'MX%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RN')
			
	def test_RN_2(self):
		#MYA - MYZ
		for letra_2 in alfabeto:
			v_placa = 'MY%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RN')
			
	def test_RN_3(self):
		#MZA - MZM
		for letra_2 in alfabeto[:13]:
			v_placa = 'MZ%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RN')
			
class QuePlaca_AC_Tests(unittest.TestCase)	:
	#MZN a NAG
	
	def test_AC_1(self):
		#MZN - MZZ
		for letra_2 in alfabeto[13:]:
			v_placa = 'MZ%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AC')
			
	def test_AC_2(self):
		#NAA - NAG
		for letra_2 in alfabeto[:7]:
			v_placa = 'NA%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AC')

class QuePlaca_RR_Tests(unittest.TestCase)	:
	#NAH a NBA
	
	def test_RR_1(self):
		#NAH - NAZ
		for letra_2 in alfabeto[7:]:
			v_placa = 'NA%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			self.failIf(placa != 'RR')
			
	def test_RR_2(self):
		#NBA
		v_placa = 'NBA-1234'
		placa = q.quePlaca(v_placa)
		self.failIf(placa != 'RR')
class QuePlaca_RO_Tests(unittest.TestCase):
	#NBB a NEH
	
	def test_RO_1(self):
		#NBB - NBZ
		for letra_2 in alfabeto[1:]:
			v_placa = 'NB%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RO')
	
	def test_RO_2(self):
		#NCA - NDZ
		for letra_1 in alfabeto[2:4]:
			for letra_2 in alfabeto:
				v_placa = 'N%s%s-1234' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'RO')
				
	def test_RO_3(self):
		#NEA - NEH
		for letra_2 in alfabeto[:8]:
			v_placa = 'NE%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)

			self.failIf(placa != 'RO')

class QuePlaca_AP_Tests(unittest.TestCase)	:
	#NEI a NFB
	def test_AP_1(self):
		#NEI - NEZ
		for letra_2 in alfabeto[8:]:
			v_placa = 'NE%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AP')
	
	def test_AP_2(self):
		#NFA - NFB
		for letra_2 in alfabeto[:2]:
			v_placa = 'NF%s-1234' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AP')


if __name__ == '__main__':
	unittest.main()