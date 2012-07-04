/*
	quePlaca
	Copyright (c) 2012 Eduardo Orige (www.eduardoorige.com.br)
	Licensed under the BSD license 
	Version: 1.0
*/

/* TODOTODOTODOTODOTODO
*
* Funçao de data para Emplacamento
*/
function detran(uf){
	if (uf == ""){
		return false;

	} else if (uf == "MG"){
		return "http://www.detrannet.mg.gov.br/";
	
	} else if (uf != "MG"){
		return "http://www.detran." + uf.toLowerCase() + ".gov.br/"; 	
	}
}

function estado(uf){
	switch (uf) {
		case "AC": return "ACRE";
		case "AL": return "ALAGOAS";
		case "AM": return "AMAZONAS";
		case "AP": return "AMAPÁ";
		case "BA": return "BAHIA";
		case "CE": return "CEARÁ";
		case "DF": return "DISTRITO FEDERAL";
		case "ES": return "ESPIRITO SANTO";
		case "GO": return "GOIÁS";
		case "MA": return "MARANHÃO";
		case "MG": return "MINAS GERAIS";
		case "MS": return "MATO GROSSO DO SUL";
		case "MT": return "MATO GROSSO";
		case "PA": return "PARÁ";
		case "PB": return "PARAIBA";
		case "PE": return "PERNAMBUCO";
		case "PI": return "PIAUÍ";
		case "PR": return "PARANÁ";
		case "RJ": return "RIO DE JANEIRO";
		case "RN": return "RIO GRANDE DO NORTE";
		case "RO": return "RONDONIA";
		case "RR": return "RORAIMA";
		case "RS": return "RIO GRANDE DO SUL";
		case "SC": return "SANTA CATARINA";
		case "SE": return "SERGIPE";
		case "SP": return "SÃO PAULO";
		case "TO": return "TOCANTINS";
		default: return "";
	}
	
}

function quePlaca(_letras){
	letras = _letras.toUpperCase();
	
	letras_0 = letras.charAt(0);
	letras_1 = letras.charAt(1);
	letras_2 = letras.charAt(2);
	
	//PARANA - AAA a BEZ
	if (letras_0 == "A" &&
		letras_1 <= "Z" &&
		letras_2 <= "Z") {
					
		return "PR";
	
	} else if (letras_0 == "B" && 
				letras_1 <= "E" &&
				letras_2 <= "Z") {
		return "PR";
	
	// SAO PAULO - BFZ a GKI
	} else if (letras_0 == "B" &&
				letras_1 >= "F" &&
				letras_2 <= "Z"){
		return "SP";
	
	} else if (letras_0 >= "C" && letras_0 < "G" ){ 
		return "SP";
	
	} else if (letras_0 == "G" &&
				letras_1 < "K" &&
				letras_2 <= "Z"){
		return "SP";
		
	} else if (letras_0 == "G" &&
				letras_1 == "K" &&
				letras_2 <= "I"){
		return "SP";
	
	//MINAS GERAIS - GKJ a HOK
	} else if (letras_0 == "G" && 
				letras_1 == "K" &&
				letras_2 >= "J"){
		return "MG";
	
	} else if (letras_0 == "G" &&
				letras_1 > "K" &&
				letras_2 <= "Z"){
		return "MG";
	
	} else if (letras_0 == "H" &&
				letras_1 < "O" &&
				letras_2 <= "Z"){
		return 'MG';
	
	} else if (letras_0 == "H" &&
				letras_1 == "O" &&
				letras_2 <= "K"){
		return "MG";
	
	//MARANHAO - HOL a HQE
	} else if (letras_0 == "H" &&
				letras_1 == "P" &&
				letras_2 <= "Z"){
		return "MA";
		
	} else if (letras_0 == "H" && 
				letras_1 == "Q" &&
				letras_2 <= "E"){
		return "MA";

	//MATO GROSSO DO SUL - HQF a HTW
	} else if (letras_0 == "H" &&
				letras_1 == "Q" &&
				letras_2 >= "F"){
		return "MS";
		
	} else if (letras_0 == "H" &&
				letras_1 > "Q" && letras_2 < "T" &&
				letras_2 <= "Z"){
		return "MS";
		
	} else if (letras_0 == "H" &&
				letras_1 == "T" &&
				letras_2 <= "W"){
		return "MS";
	
	// CEARA = HTX a HZA
	} else if (letras_0 == "H" &&
				letras_1 == "T" &&
				letras_2 >= "X"){
		return "CE";

	} else if (letras_0 == "H" &&
				letras_1 > "T" && letras_1 < "Z" &&
				letras_2 <= "Z"){
		return "CE";

	} else if (letras_0 == "H" &&
				letras_1 == "Z" &&
				letras_2 == "A"){
		return "CE";
	
	//SERGIPE - HZB a IAP
	} else if (letras_0 == "H" &&
				letras_1 == "Z" &&
				letras_2 >= "B") {
		return "SE";
	
	} else if (letras_0 == "I" &&
				letras_1 == "A" &&
				letras_2 <= "P"){
		return "SE";

	//RIO GRANDE DO SUL - IAQ a JDO
	} else if (letras_0 == "I" &&
				letras_1 == "A" &&
				letras_2 >= "Q"){
		return "RS";

	} else if (letras_0 == "I" &&
				letras_1 >= "B" &&
				letras_2 <= "Z"){
		return "RS";

	} else if (letras_0 == "J" &&
				letras_1 < "D" &&
				letras_2 <= "Z"){
		return "RS";

	} else if (letras_0 == "J" &&
				letras_1 == "D" &&
				letras_2 <= "O"){
		return "RS";

	// DISTRITO FEDERAL - JDP a JKR
	} else if (letras_0 == "J" &&
				letras_1 == "D" &&
				letras_2 >= "P"){
		return "DF";

	} else if (letras_0 == "J" &&
				letras_1 > "D" && letras_1 < "K" &&
				letras_2 <= "Z"){
		return "DF";
	
	} else if (letras_0 == "J" &&
				letras_1 == "K" &&
				letras_2 <= "R"){
		return "DF";
	
	// BAHIA - JKS a JSZ
	} else if (letras_0 == "J" &&
				letras_1 == "K" &&
				letras_2 >= "S"){
		return "BA";
	
	} else if (letras_0 == "J" &&
				letras_1 > "K" && letras_1 <= "S" &&
				letras_2 <= "Z"){
		return "BA";
	
	// PARA - JTA a JWE
	} else if (letras_0 == "J" &&
				letras_1 >= "T" && letras_2 < "W" &&
				letras_2 <= "Z"){
		return "PA";
	
	} else if (letras_0 == "J" &&
				letras_1 == "W" &&
				letras_2 <= "E"){
		return "PA";
	
	// AMAZONAS - JWF a JXY 
	} else if (letras_0 == "J" &&
				letras_1 == "W" &&
				letras_2 >= "F"){
		return "AM";
	
	} else if (letras_0 == "J" &&
				letras_1 == "X" &&
				letras_2 <= "Y"){
		return "AM";
	
	// MATO GROSSO - JXZ a KAU
	} else if (letras_0 == "J" &&
				letras_1 == "X" &&
				letras_2 == "Z"){
		return "MT";
	
	} else if (letras_0 == "K" &&
				letras_1 == "A" &&
				letras_2 <= "U"){
		return "MT";
	
	// GOIAS - KAV a KFC
	} else if (letras_0 == "K" &&
				letras_1 == "A" &&
				letras_2 >= "V"){
		return "GO";
	
	} else if (letras_0 == "K" &&
				letras_1 > "A" && letras_1 < "F" &&
				letras_2 <= "Z"){
		return "GO";
	
	} else if (letras_0 == "K" &&
				letras_1 == "F" &&
				letras_2 <= "C"){
		return "GO";
	
	// PERNAMBUCO - KFD a KME
	} else if (letras_0 == "K" &&
				letras_1 <= "F" &&
				letras_2 >= "D"){
		return "PE";
	
	} else if (letras_0 == "K" &&
				letras_1 > "F" && letras_1 < "M" &&
				letras_2 <= "Z"){
		return "PE";
	
	} else if (letras_0 == "K" &&
				letras_1 == "M" &&
				letras_2 <= "E"){
		return "PE";
	
	// RIO DE JANEIRO - KMF a LVE
	} else if (letras_0 == "K" &&
				letras_1 == "M" &&
				letras_2 >= "F"){
		return "RJ";
	
	} else if (letras_0 == "K" && 
				letras_1 > "M" &&
				letras_2 <= "Z"){
		return "RJ";
	
	} else if (letras_0 == "L" &&
				letras_1 < "V" &&
				letras_2 <= "Z"){
		return "RJ";
	
	} else if (letras_0 == "L" &&
				letras_1 == "V" &&
				letras_2 <= "E"){
		return 'RJ';
	
	// PIAUI - LVF a LWQ
	} else if (letras_0 == "L" &&
				letras_1 == "V" &&
				letras_2 >= "F"){
		return "PI";
	
	} else if (letras_0 == "L" &&
				letras_1 == "W" &&
				letras_2 <= "Q"){
		return "PI";
	
	// SANTA CATARINA - LWR a MMM
	} else if (letras_0 == "L" &&
				letras_1 == "W" &&
				letras_2 >= "R"){
		return "SC";
	
	} else if (letras_0 == "L" &&
				letras_1 > "W" &&
				letras_2 <= "Z"){
		return "SC";
	
	} else if (letras_0 == "M" &&
				letras_1 < "M" &&
				letras_2 <= "Z"){
		return "SC";
	
	} else if (letras_0 == "M" &&
				letras_1 == "M" && 
				letras_2 <= "M"){
		return "SC";
	
	// PARAIBA - MMN A MOW
	} else if (letras_0 == "M" && 
				letras_1 == "M" &&
				letras_2 >= "N"){
		return "PB";

	} else if (letras_0 == "M" &&
				letras_1 == "N" &&
				letras_2 <= "Z"){
		return "PB";
	
	} else if (letras_0 == "M" &&
				letras_1 == "O" &&
				letras_2 <= "W"){
		return "PB";
	
	//ESPIRITO SANTO = MOX a MTZ
	} else if (letras_0 == "M" &&
				letras_1 == "O" &&
				letras_2 >= "X"){
		return "ES";

	} else if (letras_0 == "M" &&
				letras_1 > "O" && letras_1 <= "T" &&
				letras_2 <= "Z"){
		return "ES";
	
	//ALAGOAS - MUA a MVK	
	} else if (letras_0 == "M" &&
				letras_1 == "U" &&
				letras_2 <= "Z"){
		return "AL";
	
	} else if (letras_0 == "M" &&
				letras_1 == "V" &&
				letras_2 <= "K"){
		return "AL";
	
	// TOCANTINS - MVL a MXG
	} else if (letras_0 == "M" &&
				letras_1 == "V" &&
				letras_2 >= "L"){
		return "TO";
	
	} else if (letras_0 == "M" &&
				letras_1 > "V" && letras_1 < "X" &&
				letras_2 <= "Z"){
		return "TO";
	
	} else if (letras_0 == "M" &&
				letras_1 == "X" &&
				letras_2 <= "G"){
		return "TO";
	
	// RIO GRANDE DO NORTE - MXH a MZM
	} else if (letras_0 == "M" &&
				letras_1 == "X" &&
				letras_2 >= "H"){
		return "RN";
	
	} else if (letras_0 == "M" &&
				letras_1 > "X" && letras_1 < "Z" &&
				letras_2 <= "Z"){
		return "RN";
	
	} else if (letras_0 == "M" &&
				letras_1 == "Z" &&
				letras_2 <= "M"){
		return "RN";
	
	// ACRE - MZN a NAG
	} else if (letras_0 == "M" &&
				letras_1 == "Z" &&
				letras_2 >= "N"){
		return "AC";
	
	} else if (letras_0 == "N" &&
				letras_1 == "A" &&
				letras_2 <= "G"){
		return 'AC';
		
	// RORAIMA - NAH a NBA
	} else if (letras_0 == "N" &&
				letras_1 == "A" &&
				letras_2 >= "H"){
		return "RR";
	
	} else if (letras_0 == "N" &&
				letras_1 == "B" &&
				letras_2 == "A"){
		return "RR";
	
	// RONDONIA - NBB a NEH
	} else if (letras_0 == "N" &&
				letras_1 == "B" &&
				letras_2 >= "B"){
		return "RO";
	
	} else if (letras_0 == "N" &&
				letras_1 > "B" && letras_1 < "E" &&
				letras_2 <= "Z"){
		return "RO";
	
	} else if (letras_0 == "N" &&
				letras_1 == "E" &&
				letras_2 <= "H"){
		return "RO";
	
	// AMAPA - NEI a NFB
	} else if (letras_0 == "N" &&
				letras_1 == "E" &&
				letras_2 >= "I"){
		return "AP";
	
	} else if (letras_0 == "N" &&
				letras_1 == "F" &&
				letras_2 <= "B"){
		return "AP";
	
	// GOIAS 2 - NFC a NGZ
	} else if (letras_0 == "N" &&
				letras_1 == "F" &&
				letras_2 >= "C"){
		return "GO";
	
	} else if (letras_0 == "N" &&
				letras_1 == "G" &&
				letras_2 <= "Z"){
		return "GO";
	
	// MARANHAO 2 - NHA a NHT
	} else if (letras_0 == "N" &&
				letras_1 == "H" &&
				letras_2 <= "T"){
		return "MA";
	
	// PIAUI 2 - NHU a NIX
	} else if (letras_0 == "N" &&
				letras_1 == "H" &&
				letras_2 >= "U"){
		return "PI";
	
	} else if (letras_0 == "N" &&
				letras_1 == "I" &&
				letras_2 <= "X") {
		return "PI";
	
	// MATO GROSSO 2 - NIY a NJW
	} else if (letras_0 == "N" &&
				letras_1 == "I" &&
				letras_2 >= "Y"){
		return "MT";
	
	} else if (letras_0 == "N" && 
				letras_1 == "J" &&
				letras_2 <= "W"){
		return "MT";
	
	// GOIAS 3 - NJX a NLU
	} else if (letras_0 == "N" &&
				letras_1 == "J" &&
				letras_2 >= "X"){
		return "GO";
	
	} else if (letras_0 == "N" &&
				letras_1 == "K" && 
				letras_2 <= "Z"){
		return "GO";
	
	} else if (letras_0 == "N" &&
				letras_1 == "L" &&
				letras_2 <= "U"){
		return "GO";
	
	// ALAGOAS 2 - NLV a NMO
	} else if (letras_0 == "N" &&
				letras_1 == "L" &&
				letras_2 >= "V"){
		return "AL";
	
	} else if (letras_0 == "N" &&
				letras_1 == "M" &&
				letras_2 <= "O"){
		return "AL";
	
	// MARANHAO 3 - NMP a NNI
	} else if (letras_0 == "N" &&
				letras_1 == "M" &&
				letras_2 >= "P"){
		return "MA";
	
	} else if (letras_0 == "N" &&
				letras_1 == "N" &&
				letras_2 <= "I"){
		return "MA";
	
	// RIO GRANDE DO NORTE 2 - NNJ a NOH
	} else if (letras_0 == "N" &&
				letras_1 == "N" &&
				letras_2 >= "J"){
		return "RN";
	
	} else if (letras_0 == "N" &&
				letras_1 == "O" &&
				letraS_2 <= "H"){
		return "RN";
	 
	// AMAZONAS 2 - NOI a NPB
	} else if (letras_0 == "N" &&
				letras_1 == "O" &&
				letras_2 >= "I"){
		return "AM";
	
	} else if (letras_0 == "N" &&
				letras_1 == "P" &&
				letras_2 <= "B"){
		return "AM";
	
	// MATO GROSSO 3 - NPC a NPQ
	} else if (letras_0 == "N" &&
				letras_1 == "P" &&
				letras_2 >= "C" && letras_2 <= "Q"){
		return "MT";
	
	// PARAIBA 2 - NPR a NQK
	} else if (letras_0 == "N" &&
				letras_1 == "P" &&
				letras_2 >= "R"){
		return "PB";
	
	} else if (letras_0 == "N" &&
				letras_1 == "Q" &&
				letras_2 <= "K"){
		return "PB";
	
	// CEARA 2 - NQL a NRE
	} else if (letras_0 == "N" &&
				letras_1 == "Q" &&
				letras_2 >= "L"){
		return "CE";
	
	} else if (letras_0 == "N" &&
				letras_1 == "R" &&
				letras_2 <= "E"){
		return "CE";
	
	// MATO GROSSO DO SUL 2 - NRF a NSD
	} else if (letras_0 == "N" &&
				letras_1 == "R" &&
				letras_2 >= "F"){
		return "MS";
	
	} else if (letras_0 == "N" &&
				letras_1 == "S" &&
				letras_2 <= "D"){
		return "MS";
	
	// PARA 2 - NSE a NTC
	} else if (letras_0 == "N" &&
				letras_1 == "S" &&
				letras_2 >= "E"){
		return "PA"; 
	
	} else if (letras_0 == "N" &&
				letras_1 == "T" &&
				letras_2 <= "C"){
		return "PA";
	
	// BAHIA 2 - NTD a NTW
	} else if (letras_0 == "N" &&
				letras_1 == "T" &&
				letras_2 >= "D" && letras_2 <= "W"){
		return "BA";
	
	// MATO GROSSO 4 - NTX a NUG
	} else if (letras_0 == "N" &&
				letras_1 == "T" &&
				letras_2 >= "X"){
		return "MT";
	
	} else if (letras_0 == "N" &&
				letras_1 == "U" &&
				letras_2 <= "G"){
		return "MT";
	
	// RORAIMA 2 - NUH a NUL
	} else if (letras_0 == "N" &&
				letras_1 == "U" &&
				letras_2 >= "H" && letras_2 <= "L"){
		return "RR";
	
	// CEARA 3 - NUM a NVF
	} else if (letras_0 == "N" &&
				letras_1 == "U" &&
				letras_2 >= "M"){
		return "CE";
	
	} else if (letras_0 == "N" &&
				letras_1 == "V" &&
				letras_2 <= "F"){
		return "CE";
	
	// SERGIPE 2 - NVG a NVN
	} else if (letras_0 == "N" &&
	 			letras_1 == "V" &&
				letras_2 >= "G" && letras_2 <= "N"){
		return "SE";
	
	// GOIAS 4 - NVO a NWR
	} else if (letras_0 == "N" &&
				letras_1 == "V" &&
				letras_2 >= "O"){
		return "GO";
	
	} else if (letras_0 == "N" &&
				letras_1 == "W" &&
				letras_2 <= "R"){
		return "GO";
	
	// MARANHAO 4 - NWS a NXQ
	} else if (letras_0 == "N" &&
				letras_1 == "W" &&
				letras_2 >= "S"){
		return "MA";
	
	} else if (letras_0 == "N" &&
				letras_1 == "X" &&
				letras_2 <= "Q"){
		return "MA";
	
	// ACRE 2 - NXR a NXT
	} else if (letras_0 == "N" &&
				letras_1 == "X" &&
				letras_2 >= "R" && letras_2 <= "T"){
		return "AC";
	
	// PERNAMBUCO 2 - NXU a NXW
	} else if (letras_0 == "N" &&
				letras_1 == "X" &&
				letras_2 >= "U" && letras_2 <= "W"){
		return "PE";
	
	// MINAS GERAIS 2 - NXX a NYG
	} else if (letras_0 == "N" &&
				letras_1 == "X" &&
				letras_2 >= "X"){
		return "MG";
	
	} else if (letras_0 == "N" &&
				letras_1 == "Y" &&
				letras_2 <= "G"){
		return "MG";			
	
	// BAHIA 3 - NYH a NZZ
	} else if (letras_0 == "N" &&
				letras_1 >= "Y" &&
				letras_2 <= "Z"){
		return "BA";
	
	// AMAZONAS 3 - OAA a OAO
	} else if (letras_0 == "O" &&
				letras_1 == "A" &&
				letras_2 >= "A" && letras_2 <= "O"){
		return "AM";
	
	//MATO GROSSO 5 - OAP a OBS 
	} else if (letras_0 == "O" &&
				letras_1 == "A" &&
				letras_2 >= "P"){
		return "MT";
	
	} else if (letras_0 == "O" &&
				letras_1 == "B" &&
				letras_2 <= "S") {
		return "MT";			
	
	// PARA 3 - OBT a OCA
	} else if (letras_0 == "O" &&
				letras_1 == "B" &&
				letras_2 >= "T"){
		return "PA";
	
	} else if (letras_0 == "O" &&
				letras_1 == "C" && 
				letras_2 == "A"){
		return "PA";
	
	// CEARA 4 - OCB a OCT
	} else if (letras_0 == "O" &&
				letras_1 == "C" &&
				letras_2 >= "B" && letras_2 <= "T"){
		return "CE";
	
	// SEQUENCIA NAO UTILIZADA - OCU
	} else if (letras_0 == "O" &&
				letras_1 == "C" &&
				letras_2 == "U"){
		return "";
	
	// ESPIRITO SANTO 2 - OCV a ODT
	} else if (letras_0 == "O" &&
				letras_1 == "C" &&
				letras_2 >= "V"){
		return "ES";
	
	} else if (letras_0 == "O" &&
				letras_1 == "D" &&
				letras_2 <= "T"){
		return "ES";

	// PIAUI 3 - ODU a OEI
	} else if (letras_0 == "O" &&
				letras_1 == "D" &&
				letras_2 >= "U"){
		return "PI";
	
	} else if (letras_0 == "O" &&
				letras_1 == "E" &&
				letras_2 <= "I"){
		return "PI";
	
	// SERGIPE 3 - OEJ a OES
	} else if (letras_0 == "O" &&
				letras_1 == "E" &&
				letras_2 >= "J" && letras_2 <= "S"){
		return "SE";
	
	// PARAIBA 3 - OET a OFH
	} else if (letras_0 == "O" &&
				letras_1 == "E" &&
				letras_2 >= "T"){
		return "PB";
	
	} else if (letras_0 == "O" &&
				letras_1 == "F" &&
				letras_2 <= "H"){
		return "PB";
	
	// PARA 4 - OFI a OGG
	} else if (letras_0 == "O" &&
				letras_1 == "F" &&
				letras_2 >= "I"){
		return "PA";
	
	} else if (letras_0 == "O" &&
				letras_1 == "G" &&
				letras_2 <= "G"){
		return "PA";
	
	// GOIAS 5 - OGH a OHA
	} else if (letras_0 == "O" &&
				letras_1 == "G" && 
				letras_2 >= "H"){
		return "GO";
	
	} else if (letras_0 == "O" &&
				letras_1 == "H" &&
				letras_2 == "A"){
		return "GO";
	
	// ALAGOAS 3 - OHB a OHK
	} else if (letras_0 == "O" &&
				letras_1 == "H" &&
				letras_2 >= "B" && letras_2 <= "K"){
		return "AL";
	
	// RONDONIA 2 - OHL a OHW
	} else if (letras_0 == "O" &&
				letras_1 == "H" &&
				letras_2 >= "L" && letras_2 <= "W"){
		return "RO";
	
	// CEARA 5 - OHX a OIQ
	} else if (letras_0 == "O" &&
				letras_1 == "H" &&
				letras_2 >= "X"){
		return "CE";
	
	} else if (letras_0 == "O" &&
				letras_1 == "I" &&
				letras_2 <= "Q"){
		return "CE";
	
	// SEQUENCIA NAO UTILIZADA - OIR a OKH
	} else if (letras_0 == "O" &&
				letras_1 == "I" &&
				letras_2 >= "R"){
		return "";
	
	} else if (letras_0 == "O" &&
				letras_1 == "J" &&
				letras_2 <= "Z"){
		return "";
	
	} else if (letras_0 == "O" &&
				letras_1 == "K" &&
				letras_2 <= "H"){
		return "";
	
	// BAHIA 4 - OKI a OKM
	} else if (letras_0 == "O" &&
				letras_1 == "K" &&
				letras_2 >= "I" && letras_2 <= "M"){
		return "BA";
	
	// SEQUENCIA NAO DEFINIDA - OKN a PED
	} else if (letras_0 == "O" &&
				letras_1 == "K" &&
				letras_2 >= "N"){
		return "";
	
	} else if (letras_0 == "O" &&
				letras_1 > "K" &&
				letras_2 <= "Z"){
		return "";
	
	} else if (letras_0 == "P" &&
				letras_1 < "E" &&
				letras_2 <= "Z"){
		return "";
	
	} else if (letras_0 == "P" &&
				letras_1 == "E" &&
				letras_2 == "D"){
		return "";
	
	// PERNAMBUCO 3 - PEE a PFQ
	} else if (letras_0 == "P" &&
				letras_1 == "E" &&
				letras_2 >= "E"){
		return "PE";
	
	} else if (letras_0 == "P" &&
				letras_1 == "F" &&
				letras_2 <= "Q"){
		return "PE";
	
	// SEQUENCIA NAO DEFINIDA - PFR a ZZZ
	} else if (letras_0 == "P" &&
				letras_1 == "F" &&
				letras_2 >= "R"){
		return "";
	
	} else if (letras_0 > "P"){
		return "";
	
	} else {
		return false;
	}
}