var btn = document.getElementById('btn');
var bub = document.getElementById('bulb');

var flag = false;

btn.addEventListener('click' , turnOffOrOn);

function turnOffOrOn() {
    

    if (flag) {
        flag = false;
        btn.innerHTML = 'turn on';
        bub.setAttribute('src','pics/bulboff.gif');
    }
    else {
        flag = true;
        btn.innerHTML = 'turn off';
        bub.setAttribute('src','pics/bulbon.gif');
    }
}