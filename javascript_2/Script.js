alert ("You Will Be Asked To Enter Your Name");

let steps = 8;

let name = prompt ("Please Enter Your Name: ");

let extra = parseInt (prompt("Please Enter The Number Of Assumed Steps: "));

you.innerHTML = "Hello, " + name;

let x = document.getElementById("js");
x.textContent = "Welcome To The Channa Masala Website";
console.log(x);

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

function step (extra) {
    let counter = 0;
    while (counter < extra) {
    console.log ("Counter is at: " + counter);
    console.log ("Counter is at: " + extra)
    counter++
    }
}

step (extra);