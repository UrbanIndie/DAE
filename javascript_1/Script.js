alert ("You Will Be Asked To Enter Your Name");

let steps = 8;

let name = prompt ("Please Enter Your Name: ");

let extra = parseInt (prompt("Please Enter The Number Of Assumed Steps: "));

you.innerHTML = "Hello, " + name;

const me = name

steps = steps + extra

if (steps > 8){
    console.log ("More Steps")
}
else if (steps == 8){
    console.log ("Equal Steps")
}
else {
    console.log ("Less Steps")
}

// AND Comparison
if (steps == 8 && name == me) {
  console.log ("8 Steps With No Extra Steps By The Name, " + me);
}