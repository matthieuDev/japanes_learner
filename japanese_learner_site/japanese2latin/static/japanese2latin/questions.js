let nbQuestions=0, goodResults=0;
const resultString = document.querySelector('h2#result');
const buttonSubmit = document.querySelector('input#submit');

const GetResults = () => {
    const listInput = document.querySelectorAll('input[latin]');
    listInput.forEach( inp => {
        goodResults += inp.getAttribute('latin') === inp.value.trim().toLowerCase() ;
    });
    nbQuestions = listInput.length;

    resultString.textContent = `${goodResults}/${nbQuestions}`;

    buttonSubmit.value = 'New Test';
    buttonSubmit.onclick = function() {location.href='/japanese2latin'; };
}

const Reset = () => {
    nbQuestions=0, goodResults=0;
}

document.querySelectorAll('input[latin]').forEach(inp => {
    inp.value = '';
    console.log(inp.value);
});