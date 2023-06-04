let canvas = document.getElementById("myCanvas");
const rect = canvas.getBoundingClientRect();
let ctx = canvas.getContext("2d");

const Reset = () => {
    ctx.reset();
}

let isDrawing = false;

const InitDraw = (event) => {
    ctx.fillStyle = "black";
    ctx.lineWidth = 15;
    ctx.moveTo(event.clientX - rect.left, event.clientY - rect.top);
    isDrawing = true;
}
const Draw = (event) => {
    if (!isDrawing) return;
    console.log(event.clientX - rect.left, event.clientY - rect.top);
    ctx.lineTo(event.clientX - rect.left, event.clientY - rect.top);
    ctx.stroke(); 
}
const EndDraw = (event) => {
    isDrawing = false;
}
canvas.onmousedown  = InitDraw;
canvas.onmousemove = Draw;
canvas.onmouseup  = EndDraw;
canvas.onmouseleave  = EndDraw;

const GetCookie = name => {
    if (document.cookie && document.cookie !== '') {
        for (let cookie of document.cookie.split(';')) {
            cookie = cookie.trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length) === name) {
                return decodeURIComponent(cookie.substring(name.length + 1));
            }
        }
    }
}
var csrftoken = GetCookie('csrftoken');
const CheckImg = () => {
    const request = new XMLHttpRequest();

    request.onreadystatechange = () => {
        if (request.readyState == XMLHttpRequest.DONE) {
            document.querySelector('h1#check').textContent = request.responseText;
            document.querySelector('button#SendButton').style.display = "block";;
        }
    }

    request.open('POST', '/latin2japanese/check/', true);
    request.setRequestHeader('X-CSRFToken', csrftoken);
    request.setRequestHeader('Content-Type', 'application/json');
    request.send(JSON.stringify({
        "img": canvas.toDataURL(),
    }));
}

const SendAnswer = () => {
    let answer = document.querySelector('h1#check').textContent ;
    const expectedAnswer = document.querySelector('h1#question').getAttribute('japanese');

    const resultDiv = document.querySelector('h1#result');
    if (answer === expectedAnswer){
        resultDiv.textContent = 'Good';
        resultDiv.style.color = "green";
    } else {
        resultDiv.textContent = `Bad result, expected: ${expectedAnswer}`;
        resultDiv.style.color = "red";
    }
    document.querySelector('button#newQuestionButton').style.display = "block";;
}