function init(){
	document.getElementById("letras").value = "";
	document.getElementById("numeros").value = "";
}

function formClick($key){
	$key.select();
}

function verifica_placa() {
	if (document.getElementById("letras").value == ""){	
		document.getElementById("letras").select();
	} else {
		if (document.getElementById("numeros").value == ""){
			document.getElementById("numeros").select();
		} else {
			get_placa();
		}
	}
}

function get_placa() {	
	var letras = document.getElementById("letras").value;
	var numeros = document.getElementById("numeros").value;

	var placa = quePlaca(letras);
	var site_detran = detran(placa);
	var estado_ext = estado(placa);
	
	if (estado_ext == ""){
		estado_ext = "Não encontrado!";
	} 

	document.getElementById("placaTag").innerHTML = placa + " - " + estado_ext;

}