<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>

alert ("You Will Be Asked To Enter Your Name");

let steps = 8;

let name = prompt ("Please Enter Your Name: ");

let extra = parseInt (prompt("Please Enter The Number Of Assumed Steps: "));

you.innerHTML = "Hello, " + name;

let welcome = document.getElementById("js");
welcome.innerHTML= "Welcome To The Channa Masala Website";
console.log(welcome);

let replace = document.getElementsByClassName("group");
for (let i = 0;i < replace.length;i++){
replace[i].innerHTML = "Channa Ingredients";
console.log(replace[i]);
}

const me = name

// steps = steps + extra

if (extra > 8){
    console.log ("More Steps")
}
else if (extra == 8){
    console.log ("Equal Steps")
}
else {
    console.log ("Less Steps")
}

// steps = steps + extra

// AND Comparison
if (steps == 8 && name == me) {
  console.log ("8 Steps With No Extra Steps By The Name, " + me);
}

function step (extra, steps, name) {
    let counter = 1;
    console.log ("User " + name +" Has Thought There Are " + extra + " Steps. There Are Actually " + steps + " Steps.")
    while (counter < extra + 1) {
    console.log ("Counter Is At: " + counter);
    counter++
    }
}

// SET TIMEOUT
let timeoutId = setTimeout(function () {
    console.log("The User Has 8 Seconds");
}, 8000);

if (extra == 8) {
    clearTimeout(timeoutId);
    console.log("Timeout Was Cancelled Because Steps = 8");
}

step (extra, steps, name);