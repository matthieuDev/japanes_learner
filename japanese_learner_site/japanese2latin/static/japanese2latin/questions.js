let nbQuestions=0, goodResults=0;
console.log('===', document.querySelectorAll('input[latin]'));
document.querySelectorAll('input[latin]').forEach(inp => {
    inp.value = '';
    console.log(inp.value);
});

const GetResults = () => {
    const listInput = document.querySelectorAll('input[latin]');
    listInput.forEach( inp => {
        goodResults += inp.getAttribute('latin') === inp.value.trim().toLowerCase() ;
    });
    nbQuestions = listInput.length;
    console.log('____', nbQuestions, goodResults);
}

const reset = () => {
    nbQuestions=0, goodResults=0;
}