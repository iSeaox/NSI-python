const currency = new Map();
currency.set("EUR", 1);
currency.set("USD", 0.88);
currency.set("GBP", 1.19);
currency.set("CAD", 0.70);
currency.set("CNH", 0,14);

/* building of select */
var select1 = document.getElementById("base_select");
var select2 = document.getElementById("dest_select");
for(const key of currency.keys()) {
    select1.innerHTML += "<option>"+key+"</option>";
    select2.innerHTML += "<option>"+key+"</option>";
}


function convertUsingForm() {
    var baseSelect = document.getElementById("base_select");
    var baseValue = baseSelect.options[baseSelect.selectedIndex].value;

    var destSelect = document.getElementById("dest_select");
    var destValue = destSelect.options[destSelect.selectedIndex].value;

    var amount = parseInt(document.getElementById("input_amount").value);
    if(amount > 0) {
		var para = document.getElementById("convert_awnser")
		para.innerHTML = (amount * currency.get(baseValue)) * (1 / currency.get(destValue)) +" "+ destValue;
	}
}