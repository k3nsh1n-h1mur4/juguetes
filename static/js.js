const btn = document.getElementById('btn-calculateAge');

const form = document.querySelector('.form')
let f_nac = form.f_nac.value

//console.log(f_nac)
//const years = 0;

btn.addEventListener('click', (e) => {
    e.preventDefault();
    //console.log(e);
    const form = document.querySelector('.form');
    const d = form.f_nac.value;
    if (d === '') {
        alert('Campo vacío')
    } else {
        let birthDateToMillis = Date.parse(d);
        //console.log(birthDateToMillis)
        let nowToMillis = Date.now();
        console.log(nowToMillis);
        let subT = (nowToMillis - birthDateToMillis) / 86400000;
        const age = subT / 365.25;
        //console.log(age);
        if (age >= 6){
            alert('Registro no Apto, supera la edad');
        }else {
        document.getElementById('id_edad').value = age;
        }
    }
})

const API = 'http://127.0.0.1:8000/juguete/v1/worker/list/';

let workers = null;

const getWorkers = async() => {
    const res = await fetch(API);
    console.log(res)
    const data = await res.text()
    console.log(data)
    //const data = await res.json();
    
};

window.addEventListener('load', function() {
    getWorkers();
})