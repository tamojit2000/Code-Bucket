const inputs = document.querySelectorAll(".input");


function addcl(){
	let parent = this.parentNode.parentNode;
	parent.classList.add("focus");
}

function remcl(){
	let parent = this.parentNode.parentNode;
	if(this.value == ""){
		parent.classList.remove("focus");
	}
}


inputs.forEach(input => {
	input.addEventListener("focus", addcl);
	input.addEventListener("blur", remcl);
});

function validate()
{
	var username = document.getElementById("uname");
	var pass = document.getElementById("pass");

if (username.value.trim() == "")
{
	alert("Please enter a username");
	username.style.borderBottom = "solid 3px red";
	document.getElementById("lb1").style.visibility= "visible";
	return false;
}
else if(pass.value.trim()=="")
{
	alert("blank passwod");
	return false;
}
else if(pass.value.trim().length< 5)
{
	alert("password minimum length is 5 ");
	return false;
}
else
{
	return true;
}
}
