#-*- encoding: utf-8 -*-
__author__ = "Eduardo Orige"
__credits__ = ["Eduardo Orige"]
__version__ = "1.0 stable"
__maintainer__ = "Eduardo Orige"
__email__ = "eduardo.orige@gmail.com"
__status__ = "Em Producao"
__description__ = 'Testes Unitários para o QuePlaca'

"""
Testes Unitários QuePlaca 1.0 stable

Os testes estão dispostos nos seguintes padrões:

- A classe de teste deve conter o prefixo QuePlaca_, em seguida a sigla do estado que 
o teste será rodado e em seguida _Tests.
	- Caso exista mais de uma classe para teste do mesmo estado é colocado um _ e em seguida o número de 
	teste da classe ou nome da mesma.
	
	Ex: Preciso fazer testes para o estado de SC.
			class QuePlaca_SC_MeusTestes_Test .... ou
			class QuePlaca_SC_2_Test ....
			
- A variável "alfabeto" é utilizada por todos os testes até essa versão (1.0) e NUNCA deve ser alterada assim como 
o objeto "q" que é um objeto de QuePlaca().

"""

########################################## NAO ALTERAR ###############################################################
import unittest
from queplaca import QuePlaca
q = QuePlaca()
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
######################################################################################################################

class QuePlaca_PR_Tests(unittest.TestCase):
	def test_PR_1(self):
		#AAA - AZZ
		for letra_1 in alfabeto:
			for letra_2 in alfabeto:
				v_placa = 'A%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)	
				self.failIf(placa != 'PR')
				
	def test_PR_2(self):
		#BAA - BEZ
		for letra_1 in alfabeto[1:5]:
			for letra_2 in alfabeto:
				v_placa = 'B%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'PR')
				

class QuePlaca_SP_Tests(unittest.TestCase):
	#BFA a GKI
	def test_SP_1(self):
		#BFZ - BZZ
		for letra_1 in alfabeto[5:]:
			for letra_2 in alfabeto:
				v_placa = 'B%s%s-9999' % (letra_1,letra_2) 
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'SP')
				
	def test_SP_2(self):
		#CAA - FZZ	
		for letra_0 in alfabeto[2:6]:
			for letra_1 in alfabeto:
				for letra_2 in alfabeto:
					v_placa = '%s%s%s-9999' % (letra_0,letra_1,letra_2)
					placa = q.quePlaca(v_placa)
					
					self.failIf(placa != 'SP')
	def test_SP_3(self):	
		#GAA - GJZ
		for letra_1 in alfabeto[:10]:
				for letra_2 in alfabeto:
					v_placa = 'G%s%s-9999' % (letra_1,letra_2)
					placa = q.quePlaca(v_placa)
			
					self.failIf(placa != 'SP')
	def test_SP_4(self):
		#GKA - GKI
		for letra_2 in alfabeto[:9]:
			v_placa = 'GK%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)

			self.failIf(placa != 'SP')

class QuePlaca_MG_Tests(unittest.TestCase):
	#GKJ a HOK
	
	def test_MG_1(self):
		#GKJ - GKZ
		for letra_2 in alfabeto[10:]:
			v_placa = 'GK%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MG')
			
	def test_MG_2(self):
		#GLA - GZZ
		for letra_1 in alfabeto[11:]:
			for letra_2 in alfabeto:
				v_placa = 'G%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'MG')
		
	def test_MG_3(self):
		#HAA - HNZ
		for letra_1 in alfabeto[:14]:
			for letra_2 in alfabeto:
				v_placa = 'H%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'MG')
				
	def test_MG_4(self):
		#HOA - HOK
		for letra_2 in alfabeto[:11]:
			v_placa = 'HO%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			self.failIf(placa != 'MG')
			
class QuePlaca_MA_Tests(unittest.TestCase):
	#HOL a HQE
	
	def test_MA_1(self):
		#HOL - HOZ
		for letra_2 in alfabeto[11:]:
			v_placa = 'HO%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)

			self.failIf(placa != 'MA')
	
	def test_MA_2(self):
		#HPA - HPZ
		for letra_2 in alfabeto:
			v_placa = 'HP%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)

			self.failIf(placa != 'MA')
			
	def test_MA_3(self):
		#HQA - HQE
		for letra_2 in alfabeto[:5]:
			v_placa = 'HQ%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MA')
			
class QuePlaca_MS_Tests(unittest.TestCase):
	#HQF a HTW
	
	def test_MS_1(self):
		#HQF - HQZ
		for letra_2 in alfabeto[5:]:
			v_placa = 'HQ%s-9999' % (letra_2) 
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MS')
			
	def test_MS_2(self):
		#HRA - HSZ
		for letra_1 in alfabeto[17:19]:
			for letra_2 in alfabeto:
				v_placa = 'H%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'MS')
	
	def test_MS_3(self):
		#HTA - HTW
		for letra_2 in alfabeto[:23]:
			v_placa = 'HT%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MS')
			
class QuePlaca_CE_Tests(unittest.TestCase):
	#HTX a HZA
	
	def test_CE_1(self):
		#HTX - HTZ
		for letra_2 in alfabeto[23:]:
			v_placa = 'HT%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'CE')
	
	def test_CE_2(self):
		#HUA - HYZ
		for letra_1 in alfabeto[20:25]:
			for letra_2 in alfabeto:
				v_placa = 'H%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'CE')

	def test_CE_3(self):
		#HZA
		placa = q.quePlaca('HZA-9999')	
		
		self.failIf(placa != 'CE')
		

class QuePlaca_SE_Tests(unittest.TestCase):
	#HZB a IAP
	
	def test_SE_1(self):
		#HZB - HZZ
		for letra_2 in alfabeto[1:]:
			v_placa = 'HZ%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'SE')
			
	def test_SE_2(self):
		#IAA - IAP
		for letra_2 in alfabeto[:16]:
			v_placa = 'IA%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'SE')
			

class QuePlaca_RS_Tests(unittest.TestCase):
	#IAQ a JDO
	def test_RS_1(self):
		#IAQ - IAZ
		for letra_2 in alfabeto[16:]:
			v_placa = 'IA%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)

			self.failIf(placa != 'RS')

	def test_RS_2(self):	
		#IBA - IZZ
		for letra_1 in alfabeto[1:]:
			for letra_2 in alfabeto:
				v_placa = 'I%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				self.failIf(placa != 'RS')
				
	def test_RS_3(self):
		#JAA - JCZ
		for letra_1 in alfabeto[:3]:
			for letra_2 in alfabeto:
				v_placa = 'J%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				self.failIf(placa != 'RS')
				
	def test_RS_4(self):
		#JDA - JDO
		for letra_2 in alfabeto[:15]:
			v_placa = 'JD%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			self.failIf(placa != 'RS')
			

class QuePlaca_DF_Tests(unittest.TestCase):
	#JDP a JKR
	def test_DF_1(self):
		#JDP - JDZ
		for letra_2 in alfabeto[15:]:
			v_placa = 'JD%s-9999' % (letra_2)		
			placa = q.quePlaca(v_placa)
			self.failIf(placa != 'DF')
			
	def test_DF_2(self):
		#JEA - JJZ
		for letra_1 in alfabeto[4:10]:
			for letra_2 in alfabeto:
				v_placa = 'J%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				self.failIf(placa != 'DF')
	
	def test_DF_3(self):
		#JKA - JKR
		for letra_2 in alfabeto[:18]:
			v_placa = 'JK%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			self.failIf(placa != 'DF')
	
class QuePlaca_BA_Tests(unittest.TestCase):
	#JKS a JSZ
	def test_BA_1(self)	:
		#JKS - JKZ
		for letra_2 in alfabeto[18:]:
			v_placa = 'JK%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			self.failIf(placa != 'BA')
			
	def test_BA_2(self):
		#JLA - JSZ
		for letra_1 in alfabeto[11:19]:
			for letra_2 in alfabeto:
				v_placa = 'J%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				self.failIf(placa != 'BA')
				
class QuePlaca_PA_Tests(unittest.TestCase):
	#JTA a JWE
	def test_PA_1(self):
		#JTA - JVZ
		for letra_1 in alfabeto[19:22]:
			for letra_2 in alfabeto:
				v_placa = 'J%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				self.failIf(placa != 'PA')
				
	def test_PA_2(self):
		#JWA - JWE
		for letra_2 in alfabeto[:5]:
			v_placa = 'JW%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PA')

class QuePlaca_AM_Tests(unittest.TestCase):
	#JWF a JXY
	def test_AM_1(self):
		#JWF - JWZ 
		for letra_2 in alfabeto[5:]:
			v_placa = 'JW%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AM')
	
	def test_AM_2(self):
		#JXA - JXY
		for letra_2 in alfabeto[:25]:
			v_placa = 'JX%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AM')

class QuePlaca_MT_Tests(unittest.TestCase):
	#JXZ a KAU
	
	def test_MT_1(self):
		#JXZ
		v_placa = 'JXZ-9999'
		placa = q.quePlaca(v_placa)
		
		self.failIf(placa != 'MT')
		
	def test_MT_2(self):
		#KAA- KAU
		for letra_2 in alfabeto[:21]:
			v_placa = 'KA%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MT')
			
class QuePlaca_GO_Tests(unittest.TestCase):
	#KAV a KFC
	
	def test_GO_1(self):
		#KAV - KAZ
		for letra_2 in alfabeto[21:]:
			v_placa = 'KA%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'GO')
			
	def test_GO_2(self):
		#KBA - KEZ
		for letra_1 in alfabeto[1:5]:
			for letra_2 in alfabeto:
				v_placa = 'K%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'GO')
				
	def test_GO_3(self):
		#KFA - KFC
		for letra_2 in alfabeto[:3]:
			v_placa = 'KF%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'GO')

class QuePlaca_PE_Tests(unittest.TestCase):
	#KFD  a KME
	
	def test_PE_1(self):
		#KFD - KFZ
		for letra_2 in alfabeto[3:]:
			v_placa = 'KF%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PE')
			
	def test_PE_2(self):
		#KGA - KLZ
		for letra_1 in alfabeto[6:12]:
			for letra_2 in alfabeto:
				v_placa = 'K%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				self.failIf(placa != 'PE')
			
	def test_PE_3(self):
		#KMA - KME
		for letra_2 in alfabeto[:5]:
			v_placa = 'KM%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PE')

class QuePlaca_RJ_Tests(unittest.TestCase):
	#KMF a LVE
	
	def test_RJ_1(self):
		#KMF - KMZ
		for letra_2 in alfabeto[5:]:
			v_placa = 'KM%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RJ')
			
	def test_RJ_2(self):
		#KNA - KZZ
		for letra_1 in alfabeto[13:]:
			for letra_2 in alfabeto:
				v_placa = 'K%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'RJ')
				
	def test_RJ_3(self):
		#LAA - LUZ
		for letra_1 in alfabeto[:21]:
			for letra_2 in alfabeto:
				v_placa = 'L%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'RJ')
				
	def test_RJ_4(self):
		#LVA - LVE
		for letra_2 in alfabeto[:5]:
			v_placa = 'LV%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RJ')
			
		

class QuePlaca_PI_Tests(unittest.TestCase):
	#LVF a LWQ 
	
	def test_PI_1(self):
		#LVF - LVZ
		for letra_2 in alfabeto[5:]:
			v_placa = 'LV%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PI')
			
	def test_PI_2(self):
		#LWA - LWQ
		for letra_2 in alfabeto[:17]:
			v_placa = 'LW%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PI')
	

class QuePlaca_SC_Tests(unittest.TestCase):
	#LWR a MMM
	
	def test_SC_1(self):
		#LWR - LWZ
		for letra_2 in alfabeto[17:]:
			v_placa = 'LW%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'SC')
			
	def test_SC_2(self):
		#LXA - LZZ
		for letra_1 in alfabeto[23:]:
			for letra_2 in alfabeto:
				v_placa = 'L%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'SC')
				
	def test_SC_3(self):
		#MAA - MLZ
		for letra_1 in alfabeto[:12]:
			for letra_2 in alfabeto:
				v_placa = 'M%s%s-9999' % (letra_1, letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'SC')
				
	def test_SC_4(self):
		#MMA - MMM
		for letra_2 in alfabeto[:13]:
			v_placa = 'MM%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'SC')
			
		
class QuePlaca_PB_Tests(unittest.TestCase)	:
	#MMN a MOW
	
	def test_PB_1(self):
		#MMN - MMZ
		for letra_2 in alfabeto[13:]:
			v_placa = 'MM%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PB')
			
	def test_PB_2(self):
		#MNA - MNZ
		for letra_2 in alfabeto:
			v_placa = 'MN%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
						
			self.failIf(placa != 'PB')
			
	def test_PB_3(self):
		#MOA - MOW
		for letra_2 in alfabeto[:23]:
			v_placa = 'MO%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PB')
			
			

class QuePlaca_ES_Tests(unittest.TestCase):
	#MOX a MTZ
	
	def test_ES_1(self):
		#MOX - MOZ
		for letra_2 in alfabeto[23:26]:
			v_placa = 'MO%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'ES')
			
	def test_ES_2(self):
		#MPA - MTZ
		for letra_1 in alfabeto[15:20]:
			for letra_2 in alfabeto:
				v_placa = 'M%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'ES')				

class QuePlaca_AL_Tests(unittest.TestCase):
	#MUA a MVK
	
	def test_AL_1(self):
		#MUA - MUZ
		for letra_2 in alfabeto:
			v_placa = 'MU%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AL')
			
	def test_AL_2(self):
		#MVA - MVK
		for letra_2 in alfabeto[:11]:
			v_placa = 'MV%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AL')
			
class QuePlaca_TO_Tests(unittest.TestCase):
	#MVL a MXG 
	
	def test_TO_1(self):
		#MVL - MVZ
		for letra_2 in alfabeto[11:]:
			v_placa = 'MV%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			self.failIf(placa != 'TO')
			
	def test_TO_2(self):
		#MWA - MWZ
		for letra_2 in alfabeto:
			v_placa = 'MW%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'TO')
			
	def test_TO_3(self):
		#MXA - MXG
		for letra_2 in alfabeto[:7]:
			v_placa = 'MX%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'TO')

class QuePlaca_RN_Tests(unittest.TestCase):
	#MXH a MZM
	
	def test_RN_1(self):
		#MXH - MXZ
		for letra_2 in alfabeto[7:]:
			v_placa = 'MX%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RN')
			
	def test_RN_2(self):
		#MYA - MYZ
		for letra_2 in alfabeto:
			v_placa = 'MY%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RN')
			
	def test_RN_3(self):
		#MZA - MZM
		for letra_2 in alfabeto[:13]:
			v_placa = 'MZ%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RN')
			
class QuePlaca_AC_Tests(unittest.TestCase)	:
	#MZN a NAG
	
	def test_AC_1(self):
		#MZN - MZZ
		for letra_2 in alfabeto[13:]:
			v_placa = 'MZ%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AC')
			
	def test_AC_2(self):
		#NAA - NAG
		for letra_2 in alfabeto[:7]:
			v_placa = 'NA%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AC')

class QuePlaca_RR_Tests(unittest.TestCase)	:
	#NAH a NBA
	
	def test_RR_1(self):
		#NAH - NAZ
		for letra_2 in alfabeto[7:]:
			v_placa = 'NA%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			self.failIf(placa != 'RR')
			
	def test_RR_2(self):
		#NBA
		v_placa = 'NBA-9999'
		placa = q.quePlaca(v_placa)
		self.failIf(placa != 'RR')
class QuePlaca_RO_Tests(unittest.TestCase):
	#NBB a NEH
	
	def test_RO_1(self):
		#NBB - NBZ
		for letra_2 in alfabeto[1:]:
			v_placa = 'NB%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RO')
	
	def test_RO_2(self):
		#NCA - NDZ
		for letra_1 in alfabeto[2:4]:
			for letra_2 in alfabeto:
				v_placa = 'N%s%s-9999' % (letra_1,letra_2)
				placa = q.quePlaca(v_placa)
				
				self.failIf(placa != 'RO')
				
	def test_RO_3(self):
		#NEA - NEH
		for letra_2 in alfabeto[:8]:
			v_placa = 'NE%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)

			self.failIf(placa != 'RO')

class QuePlaca_AP_Tests(unittest.TestCase)	:
	#NEI a NFB
	def test_AP_1(self):
		#NEI - NEZ
		for letra_2 in alfabeto[8:]:
			v_placa = 'NE%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AP')
	
	def test_AP_2(self):
		#NFA - NFB
		for letra_2 in alfabeto[:2]:
			v_placa = 'NF%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AP')

class QuePlaca_GO_2_Tests(unittest.TestCase):
	#NFC a NGZ
	def test_GO_1(self):
		#NFC a NFZ
		for letra_2 in alfabeto[3:]:
			v_placa = 'NF%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'GO')
			
	def test_GO_2(self):
		#NGA - NGZ
		for letra_2 in alfabeto:
			v_placa = 'NG%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'GO')

class QuePlaca_MA_2_Tests(unittest.TestCase):
	#NHA a NHT
	def test_MA_1(self):
		for letra_2 in alfabeto[:20]:
			v_placa = 'NH%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)

			self.failIf(placa != 'MA')

class QuePlaca_PI_2_Tests(unittest.TestCase):
	#NHU a NIX
	def test_PI_1(self):
		#NHU - NHZ
		for letra_2 in alfabeto[20:]:
			v_placa = 'NH%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PI')
	
	def test_PI_2(self):
		#NIA - NIX
		for letra_2 in alfabeto[:24]:
			v_placa = 'NI%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PI')

class QuePlaca_MT_2_Tests(unittest.TestCase):
	#NIY a NJW
	
	def test_MT_1(self):
		#NIY - NIZ
		for letra_2 in alfabeto[24:]:
			v_placa = 'NI%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)

			self.failIf(placa != 'MT')
	
	def test_MT_2(self):
		#NJA - NJW
		for letra_2 in alfabeto[:23]:
			v_placa = 'NJ%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MT')
			
class QuePlaca_GO_3_Tests(unittest.TestCase):
	#NJX a NLU
	
	def test_GO_1(self):
		#NJX - NJZ
		for letra_2 in alfabeto[23:]:
			v_placa = 'NJ%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'GO')
			
	def test_GO_2(self):
		#NKA - NKZ
		for letra_2 in alfabeto:
			v_placa = 'NK%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'GO')
			
	def test_GO_3(self):
		#NLA - NLU
		for letra_2 in alfabeto[:21]:
			v_placa = 'NL%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'GO')

class QuePlaca_AL_2_Tests(unittest.TestCase):
	#NLV a NMO 
	
	def test_AL_1(self):
		#NLV - NLZ
		for letra_2 in alfabeto[21:]:
			v_placa = 'NL%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AL')
			
	def test_AL_2(self):
		#NMA - NMO
		for letra_2 in alfabeto[:15]:
			v_placa = 'NM%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AL')
			
class QuePlaca_MA_3_Tests(unittest.TestCase):
	#NMP a NNI
	
	def test_MA_1(self):
		#NMP - NMZ
		for letra_2 in alfabeto[15:]:
			v_placa = 'NM%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MA')
			
	def test_MA_2(self):
		#NNA - NNI
		for letra_2 in alfabeto[:9]:
			v_placa = 'NN%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MA')

class QuePlaca_RN_2_Tests(unittest.TestCase):
	#NNJ a NOH
	
	def test_RN_1(self):
		#NNJ - NNZ
		for letra_2 in alfabeto[9:]:
			v_placa = 'NN%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RN')
			
	def test_RN_2(self):
		#NOA - NOH
		for letra_2 in alfabeto[:8]:
			v_placa = 'NO%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RN')
			
class QuePlaca_AM_2_Tests(unittest.TestCase):
	#NOI a NPB
	
	def test_AM_1(self):
		#NOI - NOZ
		for letra_2 in alfabeto[8:]:
			v_placa = 'NO%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AM')
	
	def test_AM_2(self):
		#NPA - NPB
		for letra_2 in alfabeto[:2]:
			v_placa = 'NP%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AM')
			
	
class QuePlaca_MT_3_Tests(unittest.TestCase):
	#NPC a NPQ
	def test_MT_1(self)	:
		#NPC - NPQ
		for letra_2 in alfabeto[2:17]:
			v_placa = 'NP%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MT')


class QuePlaca_PB_2_Tests(unittest.TestCase):
	#NPR a NQK
	
	def test_PB_1(self)	:
		#NPR - NPZ
		for letra_2 in alfabeto[17:]:
			v_placa = 'NP%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)

			self.failIf(placa != 'PB')
			
	def test_PB_2(self):
		#NQA - NQK
		for letra_2 in alfabeto[:11]:
			v_placa = 'NQ%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PB')

class QuePlaca_CE_2_Tests(unittest.TestCase):
	#NQL a NRE
	
	def test_CE_1(self):
		#NQL - NQZ
		for letra_2 in alfabeto[11:]:
			v_placa = 'NQ%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'CE')
			
	def test_CE_2(self):
		#NRA - NRE
		for letra_2 in alfabeto[:5]:
			v_placa = 'NR%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'CE')

class QuePlaca_MS_2_Tests(unittest.TestCase):
	#NRF a NSD
	
	def test_MS_1(self):
		#NRF - NRZ
		for letra_2 in alfabeto[5:]:
			v_placa = 'NR%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MS')
			
	def test_MS_2(self):
		#NSA - NSD
		for letra_2 in alfabeto[:4]:
			v_placa =  'NS%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MS')
			
class QuePlaca_PA_2_Tests(unittest.TestCase):
	#NSE a NTC
	
	def test_PA_1(self):
		#NSE - NSZ
		for letra_2 in alfabeto[4:]:
			v_placa = 'NS%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PA')
			
	def test_PA_2(self):
		#NTA - NTC
		for letra_2 in alfabeto[:3]:
			v_placa = 'NT%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PA')

class QuePlaca_BA_2_Tests(unittest.TestCase):
	#NTD a NTW
	
	def test_BA_1(self):
		#NTD - NTW
		for letra_2 in alfabeto[3:23]:
			v_placa = 'NT%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'BA')
			

class QuePlaca_MT_4_Tests(unittest.TestCase):
	#NTX a NUG 
	
	def test_MT_1(self):
		#NTX - NTZ
		for letra_2 in alfabeto[23:]:
			v_placa = 'NT%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MT')
			
	def test_MT_2(self):
		#NUA - NUG
		for letra_2 in alfabeto[:7]:
			v_placa = 'NU%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MT')
			
class QuePlaca_RR_2_Tests(unittest.TestCase):
	#NUH a NUL
	
	def test_RR_1(self):
		#NUH - NUL
		for letra_2 in alfabeto[7:12]:
			v_placa = 'NU%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RR')
			
class QuePlaca_CE_3_Tests(unittest.TestCase):
	#NUM a NVF 
	
	def test_CE_1(self):
		#NUM - NUZ
		for letra_2 in alfabeto[12:]:
			v_placa = 'NU%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
		
			self.failIf(placa != 'CE')

	def test_CE_2(self):
		#NVA-NVF
		for letra_2 in alfabeto[:6]:
			v_placa = 'NV%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'CE')

class QuePlaca_SE_2_Tests(unittest.TestCase):
	#NVG a NVN
	
	def test_SE_1(self):
		#NVG- NVN
		for letra_2 in alfabeto[6:14]:
			v_placa = 'NV%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'SE')
			
	
class QuePlaca_GO_4_Tests(unittest.TestCase):
	#NVO a NWR
	
	def test_GO_1(self):
		#NVO - NVZ
		for letra_2 in alfabeto[14:]:
			v_placa = 'NV%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'GO')
			
	def test_GO_2(self):
		#NWA - NWR
		for letra_2 in alfabeto[:18]:
			v_placa = 'NW%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'GO')

class QuePlaca_MA_4_Tests(unittest.TestCase):
	#NWS a NXQ
	
	def test_MA_1(self):
		#NWS - NWZ
		for letra_2 in alfabeto[18:]:
			v_placa = 'NW%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MA')
			
	def test_MA_2(self):
		#NXA - NXQ
		for letra_2 in alfabeto[:17]:
			v_placa = 'NX%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MA')
	
class QuePlaca_AC_2_Tests(unittest.TestCase):
	#NXR a NXT
	
	def test_AC_1(self):
		#NXR a NXT
		for letra_2 in alfabeto[17:20]:
			v_placa = 'NX%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AC')

class QuePlaca_PE_2_Tests(unittest.TestCase):
	#NXU a NXW
	
	def test_PE_1(self):
		for letra_2 in alfabeto[20:23]:
			v_placa = 'NX%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PE')
class QuePlaca_MG_2_Tests(unittest.TestCase):
	#NXX a NYG
	
	def test_MG_1(self):
		#NXX - NXZ
		for letra_2 in alfabeto[23:]:
			v_placa = 'NX%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MG')
			
	def test_MG_2(self):
		#NYA - NYG
		for letra_2 in alfabeto[:7]:
			v_placa = 'NY%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MG')
			
class QuePlaca_BA_3_Tests(unittest.TestCase):
	#NYH a NZZ
	
	def test_BA_1(self):
		#NYH - NYZ
		for letra_2 in alfabeto[7:]:
			v_placa = 'NY%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'BA')
	
	def test_BA_2(self):
		#NZA - NZZ
		for letra_2 in alfabeto:
			v_placa = 'NZ%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'BA')

class QuePlaca_AM_3_Tests(unittest.TestCase):
	#OAA a OAO
	
	def test_AM_1(self):
		#OAA - OAO
		for letra_2 in alfabeto[:15]:
			v_placa = 'OA%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AM')
			
class QuePlaca_MT_5_Tests(unittest.TestCase):
	#OAP a OBS 
	
	def test_MT_1(self):
		#OAP - OAZ
		for letra_2 in alfabeto[15:]:
			v_placa = 'OA%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MT')
			
	def test_MT_2(self):
		#OBA - OBS
		for letra_2 in alfabeto[:19]:
			v_placa = 'OB%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'MT')
	
class QuePlaca_PA_3_Tests(unittest.TestCase):
	#OBT a OCA
	
	def test_PA_1(self):
		#OBT - OBZ
		for letra_2 in alfabeto[19:]:
			v_placa = 'OB%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PA')
			
	def test_PA_2(self):
		v_placa = 'OCA-9999'
		placa = q.quePlaca(v_placa)
		
		self.failIf(placa != 'PA')
		
		
class QuePlaca_CE_4_Tests(unittest.TestCase):
	#OCB a OCT
	
	def test_CE_1(self):
		#OCB - OCT
		for letra_2 in alfabeto[1:20]:
			v_placa = 'OC%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
		
			self.failIf(placa != 'CE')
			
class QuePlaca_None_Tests(unittest.TestCase):
	#OCU
	def test_None_1(self):
		v_placa = 'OCU-9999'
		placa = q.quePlaca(v_placa)
		
		self.failIf(placa != None)

class QuePlaca_ES_2_Tests(unittest.TestCase):
	#OCV a ODT
	def test_ES_1(self):
		#OCV - OCZ
		for letra_2 in alfabeto[21:]:
			v_placa = 'OC%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'ES')
			
	def test_ES_2(self):
		#ODA - ODT
		for letra_2 in alfabeto[:20]:
			v_placa = 'OD%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'ES')

class QuePlaca_PI_3_Tests(unittest.TestCase):
	#ODU a OEI
	def test_PI_1(self):
		#ODU - ODZ
		for letra_2 in alfabeto[20:]:
			v_placa = 'OD%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PI')
			
	def test_PI_2(self):
		#OEA - OEI
		for letra_2 in alfabeto[3:9]:
			v_placa = 'OE%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PI')

class QuePlaca_SE_3_Tests(unittest.TestCase):
	#OEJ a OES
	def test_SE_1(self):
		#OEJ - OES
		for letra_2 in alfabeto[9:19]:
			v_placa = 'OE%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'SE')

class QuePlaca_PB_3_Tests(unittest.TestCase):
	#OET a OFH
	def test_PB_1(self):
		#OET - OEZ
		for letra_2 in alfabeto[19:]:
			v_placa = 'OE%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PB')
			
	def test_PB_2(self):
		#OFA - OFH
		for letra_2 in alfabeto[:8]:
			v_placa = 'OF%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PB')
			
class QuePlaca_PA_4_Tests(unittest.TestCase):
	#OFI a OGG
	
	def test_PA_1(self):
		#OFI - OFZ
		for letra_2 in alfabeto[8:]:
			v_placa = 'OF%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PA')
			
	def test_PA_2(self):
		#OGA - OGG
		for letra_2 in alfabeto[:7]:
			v_placa = 'OG%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PA')
			

class QuePlaca_GO_5_Tests(unittest.TestCase):
	#OGH a OHA
	
	def test_GO_1(self):
		#OGH - OGZ
		for letra_2 in alfabeto[7:]:
			v_placa = 'OG%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'GO')
			
	def test_GO_2(self):
		#OHA
		v_placa = 'OHA-9999'
		placa = q.quePlaca(v_placa)
		
		self.failIf(placa != 'GO')

class QuePlaca_AL_3_Tests(unittest.TestCase):
	#OHB a OHK
	
	def test_AL_1(self):
		#OHB - OHK
		for letra_2 in alfabeto[1:11]:
			v_placa = 'OH%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'AL')

class QuePlaca_RO_2_Tests(unittest.TestCase):
	#OHL a OHW
	
	def test_RO_1(self):
		for letra_2 in alfabeto[11:23]:
			v_placa = 'OH%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'RO')

class QuePlaca_CE_5_Tests(unittest.TestCase):
	#OHX a OIQ
	
	def test_CE_1(self):
		for letra_2 in alfabeto[23:]:
			v_placa = 'OH%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'CE')
			
	
	def test_CE_2(self):
		#OIA - OIQ
		for letra_2 in alfabeto[:17]:
			v_placa = 'OI%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'CE')
			
class QuePlaca_None_2_Tests(unittest.TestCase):
	#OIR a OKH
	
	def test_None_1(self):
		#OIR - OIZ
		for letra_2 in alfabeto[17:]:
			v_placa = 'OI%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != None)
			
	def test_None_2(self):
		#OJA - OJZ
		for letra_2 in alfabeto:
			v_placa = 'OJ%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != None)
			
	def test_None_3(self):
		#OKA - OKH
		for letra_2 in alfabeto[:8]:
			v_placa = 'OK%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != None)
			
class QuePlaca_BA_4_Tests(unittest.TestCase):
	#OKI a OKM
	def test_BA_1(self):
		for letra_2 in alfabeto[8:13]:
			v_placa = 'OK%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'BA')

class QuePlaca_None_3_Tests(unittest.TestCase):
	#OKN a PED
	def test_None_1(self):
		#OKN - OKZ
		for letra_2 in alfabeto[13:]:
			v_placa = 'OK%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != None)
			
	def test_None_2(self):
		#PAA - PDZ
		for letra_1 in alfabeto[:4]:
			for letra_2 in alfabeto:
				v_placa = 'P%s%s-9999' % (letra_1, letra_2)
				placa = q.quePlaca(v_placa)

				self.failIf(placa != None)
				
	def test_None_3(self):
		#PEA - PED
		for letra_2 in alfabeto[:4]:
			v_placa = 'PE%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != None)
	

class QuePlaca_PE_3_Tests(unittest.TestCase):
	#PEE a PFQ
	
	def test_PE_1(self):
		#PEE - PEZ
		for letra_2 in alfabeto[4:]:
			v_placa = 'PE%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PE')
			
	def test_PE_2(self):
		#PFA-PFQ
		for letra_2 in alfabeto[:17]:
			v_placa = 'PF%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != 'PE')

class QuePlaca_None_4_Tests(unittest.TestCase):
	#PFR a ZZZ 
	
	def test_None_1(self):
		#PFR - PFZ
		for letra_2 in alfabeto[17:]:
			v_placa = 'PF%s-9999' % (letra_2)
			placa = q.quePlaca(v_placa)
			
			self.failIf(placa != None)
	
	def test_None_2(self):
		for letra_0 in alfabeto[16:]:
			for letra_1 in alfabeto:
				for letra_2 in alfabeto:
					v_placa = '%s%s%s-9999' % (letra_0, letra_1, letra_2)
					placa = q.quePlaca(v_placa)
					
					self.failIf(placa != None)
			

if __name__ == '__main__':
	unittest.main()