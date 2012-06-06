#-*- encoding: utf-8 -*-
__author__ = "Eduardo Orige"
__credits__ = ["Eduardo Orige"]
__version__ = "1.0 stable"
__maintainer__ = "Eduardo Orige"
__email__ = "eduardo.orige@gmail.com"
__status__ = "Em Producao"

import re
class QuePlaca:
	
	detran = {
		'AC' : 'http://www.detran.ac.gov.br/',
		'AL' : 'http://www.detran.al.gov.br/',
		'AM' : 'http://www.detran.am.gov.br/',
		'AP' : 'http://www.detran.ap.gov.br/',
		'BA' : 'http://www.detran.ba.gov.br/',
		'CE' : 'http://www.detran.ce.gov.br/',
		'DF' : 'http://www.detran.df.gov.br/',
		'ES' : 'http://www.detran.es.gov.br/',
		'GO' : 'http://www.detran.go.gov.br/',
		'MA' : 'http://www.detran.ma.gov.br/',
		'MG' : 'http://www.detrannet.mg.gov.br/',
		'MS' : 'http://www.detran.ms.gov.br/',
		'MT' : 'http://www.detran.mt.gov.br/',
		'PA' : 'http://www.detran.pa.gov.br/',
		'PB' : 'http://www.detran.pb.gov.br/',
		'PE' : 'http://www.detran.pe.gov.br/',
		'PI' : 'http://www.detran.pi.gov.br/',
		'PR' : 'http://www.detran.pr.gov.br/',
		'RJ' : 'http://www.detran.rj.gov.br/',
		'RN' : 'http://www.detran.rn.gov.br/',
		'RO' : 'http://www.detran.ro.gov.br/',
		'RR' : 'http://www.detran.rr.gov.br/',
		'RS' : 'http://www.detran.rs.gov.br/',
		'SC' : 'http://www.detran.sc.gov.br/',
		'SE' : 'http://www.detran.se.gov.br/',
		'SP' : 'http://www.detran.sp.gov.br/',
		'TO' : 'http://www.detran.to.gov.br/',
	}
	
	def __init__(self):
		pass

	def regexp_numero(self,numero):
		"""
		Verifica se os numeros da placa estao entre 0001 e 9999 
		"""
		#TODO 
		#Arrumar ultimo digito, pode ser 0 somente quando nao ha 0000 no regexp
		if numero == '0000':
			return False
		else:
			regexp = re.compile("\d{3}[0-9]")
			if regexp.match(numero):
				return True
			else:
				return False
			
	def regexp_placa(self,placa):
		regexp = re.compile("\w{3}\-\d{4}")

		if regexp.match(str.upper(placa)):
			return True
		else:
			return False

	def split_placa(self,placa):
		"""
		Separa a placa em em letras e numeros. 
		
		Placa deve seguir o seguinte padrao: ABC-1234
		letras = ABC
		numeros = 1234
		"""
		if not self.regexp_placa(placa):
			return None, None
		else:
			letras = str.upper(placa.split('-')[0])
			numeros = placa.split('-')[1]

			return letras, numeros


	def quePlaca(self,placa):
		"""
		Regras para utilizacao das placas segundo: http://pt.wikipedia.org/wiki/Placas_de_identifica%C3%A7%C3%A3o_de_ve%C3%ADculos_no_Brasil
		Atualizados dia 05 de maio de 2012.
		"""
		
		letras, numeros = self.split_placa(placa)

		if letras == None or numeros == None:
			return False
		else:
			#PARANA - AAA a BEZ
			if letras[0] == 'A' and\
			 	letras[1] <= 'Z' and\
					letras[2] <= 'Z':
				return 'PR'

			elif letras[0] == 'B' and\
				 	letras[1] <= 'E' and\
				 		letras[2] <= 'Z':
				return 'PR'

			#SAO PAULO - BFA a GKI	
			elif letras[0] == 'B' and\
					letras[1] >= 'F' and \
						letras[2] <= 'Z':
				return 'SP'

			elif letras[0] >= 'C' and letras[0] < 'G':
				return 'SP'

			elif letras[0] == 'G' and\
					letras[1] < 'K' and\
						letras[2] <= 'Z':
				return 'SP'

			elif letras[0] == 'G' and\
					letras[1] == 'K' and\
						letras[2] <= 'I':
				return 'SP'

			#MINAS GERAIS - GKJ a HOK
			elif letras[0] == 'G' and\
					letras[1] == 'K' and\
						letras[2] >= 'J':
				return 'MG'
			
			elif letras[0] == 'G' and\
					letras[1] > 'K' and\
						letras <= 'Z':
				return 'MG'

			elif letras[0] == 'H' and\
					letras[1] < 'O' and\
						letras[2] <= 'Z':
				return 'MG'

			elif letras[0] == 'H' and\
					letras[1] == 'O' and\
						letras[2] <= 'K':
				return 'MG'


			#MARANHAO - HOL	a HQE
			elif letras[0] == 'H' and\
					letras[1] == 'O' and\
						letras[2] >= 'L':
				return 'MA'

			elif letras[0] == 'H' and\
					letras[1] > 'O' and letras[1] <= 'P' and\
						letras[2] <= 'Z':
				return 'MA'

			elif letras[0] == 'H' and\
					letras[1] == 'Q' and\
						letras[2] <= 'E':
				return 'MA'

			#MATO GROSSO DO SUL - HQF a HTW
			elif letras[0] == 'H' and\
					letras[1] == 'Q' and\
						letras[2] > 'E':
				return 'MS'

			elif letras[0] == 'H' and\
					letras[1] > 'Q' and letras[1] < 'T' and\
						letras[2] <= 'Z':
				return 'MS'

			elif letras[0] == 'H' and\
					letras[1] == 'T' and\
						letras[2] <= 'W':
				return 'MS'

			#CEARA - HTX a HZA
			elif letras[0] == 'H' and\
					letras[1] == 'T' and\
						letras[2] > 'W':
				return 'CE'

			elif letras[0] == 'H' and\
					letras[1] > 'T' and letras[1] < 'Z' and\
						letras[2] <= 'Z':
				return 'CE'

			elif letras[0] == 'H' and\
					letras[1] == 'Z' and\
						letras[2] == 'A':
				return 'CE'

			#SERGIPE - HZB a IAP
			elif letras[0] == 'H' and\
					letras[1] == 'Z' and\
						letras[2] >= 'B':
				return 'SE'

			elif letras[0] == 'I' and\
					letras[1] == 'A' and\
						letras[2] <= 'P':
				return 'SE'

			#RIO GRANDE DO SUL - IAQ a JDO
			elif letras[0] == 'I' and\
					letras[1] == 'A' and\
						letras[2] >= "Q":
				return 'RS'

			elif letras[0] == 'I' and\
					letras[1] >= 'B' and\
						letras[2] <= 'Z':
				return 'RS'

			elif letras[0] == 'J' and\
					letras[1] < 'D' and\
						letras[2] <= 'Z':
				return 'RS'

			elif letras[0] == 'J' and\
					letras[1] == 'D' and\
						letras[2] <= 'O':
				return 'RS'

			#DISTRITO FEDERAL - JDP a JKR
			elif letras[0] == 'J' and\
					letras[1] == 'D' and\
						letras[2] >= 'P':
				return 'DF'

			elif letras[0] == 'J' and\
					letras[1] > 'D' and letras[1] < 'K' and\
						letras[2] <= 'Z':
				return 'DF'

			elif letras[0] == 'J' and\
					letras[1] == 'K' and\
						letras[2] <= 'R':
				return 'DF'

			#BAHIA - JKS a JSZ
			elif letras[0] == 'J' and\
					letras[1] == 'K' and\
						letras[2] >= 'S':
				return 'BA'

			elif letras[0] == 'J' and\
					letras[1] > 'K' and letras[1] <= 'S' and\
						letras[2] <= 'Z':
				return 'BA'

			#PARA - JTA a JWE
			elif letras[0] == 'J' and\
					letras[1] >= 'T' and letras[1] < 'W' and\
						letras[2] <= 'Z':
				return 'PA'

			elif letras[0] == 'J' and\
					letras[1] == 'W' and\
						letras[2] <= 'E':
				return 'PA'

			#AMAZONAS - JWF a JXY		
			elif letras[0] == 'J' and\
					letras[1] == 'W' and\
						letras[2] >= 'F':
				return 'AM'

			elif letras[0] == 'J' and\
					letras[1] == 'X' and\
						letras[2] <= 'Y':
				return 'AM'

			#MATO GROSSO = JXZ a KAU
			elif letras[0] == 'J' and\
					letras[1] == 'X' and\
						letras[2] == 'Z':
				return 'MT'

			elif letras[0] == 'K' and\
					letras[1] == 'A' and\
						letras[2] <= 'U':
				return 'MT'

			#GOIAS - KAV a KFC
			elif letras[0] == 'K' and\
					letras[1] == 'A' and\
						letras[2] >= 'V':
				return 'GO'

			elif letras[0] == 'K' and\
					letras[1] > 'A' and letras[1] < 'F' and\
						letras[2] <= 'Z':
				return 'GO'

			elif letras[0] == 'K' and\
					letras[1] == 'F' and\
						letras[2] <= 'C':
				return 'GO'

			#PERNAMBUCO - KFD  a KME

			elif letras[0] == 'K' and\
				 	letras[1] <= 'F' and\
					 	letras[2] >= 'D' and letras[2] <= 'Z':
				return 'PE'

			elif letras[0] == 'K' and\
					letras[1] > 'F' and letras[1] < 'M' and\
						letras[2] <= 'Z':
				return 'PE'

			elif letras[0] == 'K' and\
					letras[1] == 'M' and\
						letras[2] <= 'E':
				return 'PE'

			#RIO DE JANEIRO - KMF a LVE
			elif letras[0] == 'K' and\
					letras[1] == 'M' and\
						letras[2] >= 'F':
				return 'RJ'

			elif letras[0] == 'K' and\
					letras[1] >= 'M' and\
						letras[2] <= 'Z':
				return 'RJ'

			elif letras[0] == 'L' and\
					letras[1] < 'V' and\
						letras[2] <= 'Z':
				return 'RJ'

			elif letras[0] == 'L' and\
					letras[1] == 'V' and\
						letras[2] <= 'E':
				return 'RJ'

			#PIAUI - LVF a LWQ 
			elif letras[0] == 'L' and\
					letras[1] == 'V' and\
						letras[2] >= 'F':
				return 'PI'

			elif letras[0] == 'L' and\
					letras[1] == 'W' and\
						letras[2] <= 'Q':
				return 'PI'

			#SANTA CATARINA - LWR a MMM
			elif letras[0] == 'L' and\
					letras[1] == 'W' and\
						letras[2] >= 'R':
				return 'SC'

			elif letras[0] == 'L' and \
					letras[1] >= 'W' and\
						letras[2] <= 'Z':
				return 'SC'

			elif letras[0] == 'M' and\
					letras[1] < 'M' and\
						letras[2] <= 'Z':
				return 'SC'

			elif letras[0] == 'M' and\
					letras[1] == 'M' and\
						letras[2] <= 'M':
				return 'SC'

			#PARAIBA - MMN a MOW
			elif letras[0] == 'M' and\
					letras[1] == 'M' and\
						letras[2] >= 'N':
				return 'PB'
				
			elif letras[0] == 'M' and\
					letras[1] == 'N' and\
						letras[2] <= 'Z':
				return 'PB'

			elif letras[0] == 'M' and\
					letras[1] == 'O' and\
						letras[2] <= 'W':
				return 'PB'

			#ESPIRITO SANTO - MOX a MTZ
			elif letras[0] == 'M' and\
					letras[1] == 'O' and\
						letras[2] >= 'X':
				return 'ES'

			elif letras[0] == 'M' and\
					letras[1] > 'O' and letras[1] < 'T' and\
						letras[2] <= 'Z':
				return 'ES'

			elif letras[0] == 'M' and\
					letras[1] == 'T' and\
						letras[2] <= 'Z':
				return 'ES'

			#ALAGOAS - MUA a MVK
			elif letras[0] == 'M' and\
				 	letras[1] == 'U' and\
				 		letras[2] <= 'Z':
				return 'AL'

			elif letras[0] == 'M' and\
					letras[1] ==  'V' and\
						letras[2] <= 'K':
				return 'AL'

			#TOCANTINS - MVL a MXG 
			elif letras[0] == 'M' and\
					letras[1] == 'V' and\
						letras[2] >= 'L':
				return 'TO'

			elif letras[0] == 'M' and\
					letras[1] > 'V' and letras[1] < 'X' and\
						letras[2] <= 'Z':
				return 'TO'

			elif letras[0] == 'M' and\
					letras[1] == 'X' and\
						letras[2] <= 'G':
				return 'TO'


			#RIO GRANDE DO NORTE - MXH a MZM
			elif letras[0] == 'M' and\
					letras[1] == 'X' and\
						letras[2] >= 'H':
				return 'RN'

			elif letras[0] == 'M' and\
					letras[1] > 'X' and letras[1] < 'Z' and\
						letras[2] <= 'Z':
				return 'RN'

			elif letras[0] == 'M' and\
					letras[1] == 'Z' and\
						letras[2] <= 'M':
				return 'RN'

			#ACRE - MZN a NAG
			elif letras[0] == 'M' and\
					letras[1] == 'Z' and\
						letras[2] >= 'N':
				return 'AC'

			elif letras[0] == 'N' and\
					letras[1] == 'A' and\
						letras[2] <= 'G':
				return 'AC'

			#RORAIMA - NAH a NBA
			elif letras[0] == 'N' and\
					letras[1] == 'A' and\
						letras[2] >= 'H':
				return 'RR'

			elif letras[0] == 'N' and\
					letras[1] == 'B' and\
						letras[2] == 'A':
				return 'RR'

			#RONDONIA - NBB a NEH 
			elif letras[0] == 'N' and\
					letras[1] == 'B' and\
						letras[2] >= 'B':
				return 'RO'

			elif letras[0] == 'N' and\
					letras[1] > 'B' and letras[1] < 'E' and\
						letras[2] <= 'Z':
				return 'RO'

			elif letras[0] == 'N' and\
					letras[1] == 'E' and\
						letras[2] <= 'H':
				return 'RO'

			#AMAPA - NEI a NFB
			elif letras[0] == 'N' and\
					letras[1] == 'E' and\
						letras[2] >= 'I':
				return 'AP'

			elif letras[0] == 'N' and\
					letras[1] == 'F' and\
						letras[2] <= 'B':
				return 'AP'

			#GOIAIS 2 - NFC 0001 a NGZ 9999
			elif letras[0] == 'N' and\
					letras[1] == 'F' and\
						letras[2] >= 'C':
				return 'GO'

			elif letras[0] == 'N' and\
					letras[1] == 'G' and\
						letras[2] <= 'Z':
				return 'GO'

			#MARANHAO 2 - NHA a NHT
			elif letras[0] == 'N' and\
					letras[1] == 'H' and\
						letras[2] <= 'T':
				return 'MA'

			#PIAUI 2 - NHU a NIX
			elif letras[0] == 'N' and\
					letras[1] == 'H' and\
						letras[2] >= 'U':
				return 'PI'

			elif letras[0] == 'N' and\
					letras[1] == 'I' and\
						letras[2] <= 'X':
				return 'PI'

			#MATO GROSSO 2 - NIY a NJW	
			elif letras[0] == 'N' and\
					letras[1] == 'I' and\
						letras[2] >= 'Y':
				return 'MT'
				
			elif letras[0] == 'N' and\
					letras[1] == 'J' and\
						letras[2] <= 'W':
				return 'MT'

			#GOIAS 3 - NJX a NLU
			elif letras[0] == 'N' and\
					letras[1] == 'J' and\
						letras[2] >= 'X':
				return 'GO'

			elif letras[0] == 'N' and\
					letras[1] < 'L' and\
						letras[2] <= 'Z':
				return 'GO'

			elif letras[0] == 'N' and\
					letras[1] == 'L' and\
						letras[2] <= 'U':
				return 'GO'

			#ALAGOAS 2 - NLV a NMO 
			elif letras[0] == 'N' and\
					letras[1] == 'L' and\
						letras[2] >= 'V':
				return 'AL'

			elif letras[0] == 'N' and\
					letras[1] == 'M' and\
						letras[2] <= 'O':
				return 'AL'

			#MARANHAO 3 - NMP a NNI
			elif letras[0] == 'N' and\
					letras[1] == 'M' and\
						letras[2] >= 'P':
				return 'MA'

			elif letras[0] == 'N' and\
					letras[1] == 'N' and\
						letras[2] <= 'I':
				return 'MA'

			#RIO GRANDE DO NORTE 2 - NNJ a NOH
			elif letras[0] == 'N' and\
					letras[1] == 'N' and\
						letras[2] >= 'J':
				return 'RN'

			elif letras[0] == 'N' and\
					letras[1] == 'O' and\
						letras[2] <= 'H':
				return 'RN'

			#AMAZONAS 2 - NOI a NPB
			elif letras[0] == 'N' and\
					letras[1] == 'O' and\
						letras[2] >= 'I':
				return 'AM'

			elif letras[0] == 'N' and\
					letras[1] == 'P' and\
						letras[2] <= 'B':
				return 'AM'

			#MATO GROSSO 3 - NPC a NPQ
			elif letras[0] == 'N' and\
					letras[1] == 'P' and\
						letras[2] >= 'C' and letras[2] <= 'Q':
				return 'MT'

			#PARAIBA 2 - NPR a NQK
			elif letras[0] == 'N' and\
					letras[1] == 'P' and\
						letras[2] >= 'R':
				return 'PB'

			elif letras[0] == 'N' and\
					letras[1] == 'Q' and\
						letras[2] <= 'K':
				return 'PB'

			#CEARA 2 - NQL a NRE
			elif letras[0] == 'N' and\
					letras[1] == 'Q' and\
						letras[2] >= 'L':
				return 'CE'

			elif letras[0] == 'N' and\
					letras[1] == 'R' and\
						letras[2] <= 'E':
				return 'CE'

			#MATO GROSSO DO SUL 2- NRF a NSD
			elif letras[0] == 'N' and\
					letras[1] == 'R' and\
						letras[2] >= 'F':
				return 'MS'

			elif letras[0] == 'N' and\
					letras[1] == 'S' and\
						letras[2] <= 'D':
				return 'MS'

			#PARA 2 - NSE a NTC
			elif letras[0] == 'N' and\
					letras[1] == 'S' and\
						letras[2] >= 'E' and letras[2] <= 'Z':
				return 'PA'

			elif letras[0] == 'N' and\
					letras[1] == 'T' and\
						letras[2] <= 'C':
				return 'PA'

			#BAHIA 2 - NTD a NTW
			elif letras[0] == 'N' and\
					letras[1] == 'T' and\
						letras[2] >= 'D' and\
							letras[2] <= 'W':
				return 'BA'


			#MATO GROSSO 4 - NTX a NUG 
			elif letras[0] == 'N' and\
					letras[1] == 'T' and\
						letras[2] >= 'X':
				return 'MT'

			elif letras[0] == 'N' and\
					letras[1] == 'U' and\
						letras[2] <= 'G':
				return 'MT'

			#RORAIMA 2 - NUH a NUL
			elif letras[0] == 'N' and\
					letras[1] == 'U' and\
						letras[2] >= 'H' and letras[2] <= 'L':
				return 'RR'

			#CEARA 3 - NUM a NVF 
			elif letras[0] == 'N' and\
					letras[1] == 'U' and\
						letras[2] >= 'M':
				return 'CE'

			elif letras[0] == 'N' and\
					letras[1] == 'V' and\
						letras[2] <= 'F':
				return 'CE'

			#SERGIPE 2 - NVG a NVN
			elif letras[0] == 'N' and\
					letras[1] == 'V' and\
						letras[2] >= 'G' and\
							letras[2] <= 'N':
				return 'SE'

			#GOIAS 4 - NVO a NWR
			elif letras[0] == 'N' and\
					letras[1] == 'V' and\
						letras[2] >= 'O':
				return 'GO'

			elif letras[0] == 'N' and\
					letras[1] == 'W' and\
						letras[2] <= 'R':
				return 'GO'		

			#MARANHAO 4 - NWS a NXQ
			elif letras[0] == 'N' and\
					letras[1] == 'W' and\
						letras[2] >= 'S':
				return 'MA'

			elif letras[0] == 'N' and\
					letras[1] == 'X' and\
						letras[2] <= 'Q':
				return 'MA'

			#ACRE 2 - NXR a NXT
			elif letras[0] == 'N' and\
					letras[1] == 'X' and\
						letras[2] >= 'R' and letras[2] <= 'T':
				return 'AC'

			#PERNAMBUCO 2 - NXU a NXW
			elif letras[0] == 'N' and\
					letras[1] == 'X' and\
						letras[2] >= 'U' and letras[2] <= 'W':
				return 'PE'

			#MINAS GERAIS 2 - NXX a NYG
			elif letras[0] == 'N' and\
					letras[1] == 'X' and\
						letras[2] >= 'X':
				return 'MG'

			elif letras[0] == 'N' and\
					letras[1] == 'Y' and\
						letras[2] <= 'G':
				return 'MG'

			#BAHIA 3 - NYH a NZZ
			elif letras[0] == 'N' and\
					letras[1] >= 'Y' and\
						letras[2] <= 'Z':
				return 'BA'

			#AMAZONAS 3 - OAA a OAO
			elif letras[0] == 'O' and\
					letras[1] == 'A' and\
						letras[2] >= 'A' and letras[2] <= 'O':
				return 'AM'

			#MATO GROSSO 5 - OAP a OBS 
			elif letras[0] == 'O' and\
					letras[1] == 'A' and\
						letras[2] >= 'P':
				return 'MT'

			elif letras[0] == 'O' and\
					letras[1] == 'B' and\
						letras[2] <= 'S':
				return 'MT'

			#PARA 3 - OBT a OCA
			elif letras[0] == 'O' and\
					letras[1] == 'B' and\
						letras[2] >= 'T':
				return 'PA'

			elif letras[0] == 'O' and\
					letras[1] == 'C' and\
						letras[2] == 'A':
				return 'PA'

			#CEARA 4 - OCB a OCT
			elif letras[0] == 'O' and\
					letras[1] == 'C' and\
						letras[2] >= 'B' and letras[2] <= 'T':
				return 'CE'

			#SEQUENCIA NAO UTILIZADA
			elif letras[0] == 'O' and\
					letras[1] == 'C' and\
						letras[2] == 'U':
				return None

			#ESPIRITO SANTO 2 - OCV a ODT
			elif letras[0] == 'O' and\
					letras[1] == 'C' and\
						letras[2] >= 'V':
				return 'ES'

			elif letras[0] == 'O' and\
					letras[1] == 'D' and\
						letras[2] <= 'T':
				return 'ES'

			#PIAUI 3 - ODU a OEI
			elif letras[0] == 'O' and\
					letras[1] == 'D' and\
						letras[2] >= 'U':
				return 'PI'

			elif letras[0] == 'O' and\
					letras[1] == 'E' and\
						letras[2] <= 'I':
				return 'PI'

			#SERGIPE 3 - OEJ a OES
			elif letras[0] == 'O' and\
					letras[1] == 'E' and\
						letras[2] >= 'J' and letras[2] <= 'S':
				return 'SE'

			#PARAIBA 3 - OET a OFH
			elif letras[0] == 'O' and\
					letras[1] == 'E' and\
						letras[2] >= 'T':
				return 'PB'

			elif letras[0] == 'O' and\
					letras[1] == 'F' and\
						letras[2] <= 'H':
				return 'PB'

			#PARA 4 - OFI a OGG
			elif letras[0] == 'O' and\
					letras[1] == 'F' and\
						letras[2] >= 'I':
				return 'PA'

			elif letras[0] == 'O' and\
					letras[1] == 'G' and\
						letras[2] <= 'G':
				return 'PA'

			#GOIAS 5 - OGH a OHA
			elif letras[0] == 'O' and\
					letras[1] == 'G' and\
						letras[2] >= 'H':
				return 'GO'

			elif letras[0] == 'O' and\
					letras[1] == 'H' and\
						letras[2] == 'A':
				return 'GO'

			#ALAGOAS 3 - OHB a OHK
			elif letras[0] == 'O' and\
					letras[1] == 'H' and\
						letras[2] >= 'B' and letras[2] <= 'K':
				return 'AL'

			#RONDONIA 2 - OHL a OHW
			elif letras[0] == 'O' and\
					letras[1] == 'H' and\
						letras[2] >= 'L' and letras[2] <= 'W':
				return 'RO'

			#CEARA 5 - OHX a OIQ
			elif letras[0] == 'O' and\
					letras[1] == 'H' and\
						letras[2] >= 'X':
				return 'CE'

			elif letras[0] == 'O' and\
					letras[1] == 'I' and\
						letras[2] <= 'Q':
				return 'CE'

			#SEQUENCIA NAO UTILIZADA - OIR a OKH
			elif letras[0] == 'O' and\
					letras[1] == 'I' and\
						letras[2] >= 'R':
				return None

			elif letras[0] == 'O' and\
					letras[1] == 'K' and\
						letras[2] <= 'H':
				return None

			#BAHIA 4 - OKI a OKM
			elif letras[0] == 'O' and\
					letras[1] == 'K' and\
						letras[2] >= 'I' and letras[2]<= 'M':
				return 'BA'

			#SEQUENCIA NAO DEFINIDA - OKN a PED
			elif letras[0] == 'O' and\
					letras[1] == 'K' and\
						letras[2] >= 'N':
				return None

			elif letras[0] == 'O' and\
					letras[1] > 'K' and\
						letras[2] <= 'Z':
				return None

			elif letras[0] == 'P' and\
					letras[1] < 'E' and\
						letras[2] <= 'Z':
				return None

			elif letras[0] == 'P' and\
					letras[1] == 'E' and\
						letras[2] == 'D':
				return None

			#PERNAMBUCO 3 - PEE a PFQ
			elif letras[0] == 'P' and\
					letras[1] == 'E' and\
						letras[2] >= 'E':
				return 'PE'

			elif letras[0] == 'P' and\
					letras[1] == 'F' and\
						letras[2] <= 'Q':
				return 'PE'

			#SEQUENCIA NAO DEFINIDA - PFR a ZZZ 
			elif letras[0] == 'P' and\
					letras[1] == 'F' and\
						letras[2] >= 'R':
				return None

			elif letras[0] > 'P':
				return None
			
	def ui(self):
		print "***********************"
		print "*                     *"
		print "*     quePlaca        *"
		print "*                     *"
		print "***********************"
		print
		print "Consulte Qualquer Placa"
		print "Ex: ABC-1234"

		placa = "abc-1234"
		while placa:
			print
			print "-> Deixe em Branco para Sair "
			placa = raw_input("-> ")
			
			retorno_placa = self.quePlaca(placa)
			if placa == '' :
				print 'Tchau!'
			elif not retorno_placa:
				print '!! Sequencia nao Utilizada !!'
			else:
				print retorno_placa
				

if __name__ == '__main__':
	q = QuePlaca()
	q.ui()