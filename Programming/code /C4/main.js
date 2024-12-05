window.red = 0;
window.green = 0;
window.blue = 0;

var container = document.getElementById('container');

document.getElementById('fc1').onmousemove = function() {f1(this.value)};
document.getElementById('fc2').onmousemove = function() {f2(this.value)};
document.getElementById('fc3').onmousemove = function() {f3(this.value)};

function f1(value) {
    window.red = value;
    change_bg();
}

function f2(value) {
    window.green = value;
    change_bg();
}

function f3(value) {
    window.blue = value;
    change_bg();
}

function change_bg() {
    document.getElementById('output').innerHTML = window.red+","+window.green+", "+window.blue;
    container.style.background = "rgb("+window.red+", "+window.green+", "+window.blue+")";

    //IF YOU WANT TO CHANGE THE BACKGROUND OF THE BODY JUST REPLACE ---> container.style to document.body
}