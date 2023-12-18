let availableKeywords = [
    'Dodge',
    'srt',
    'red eye',
    'mustang',
    'dodge old models',
    'mustang old models',
    'top models',
    'new models',

];
const resultBox = document.querySelector(".result-box");
const inputBox = document.getElementById("input-box");

inputBox.onkeyup = function(){
    let result = [];
    let input = inputBox.value;
    if(input.length){
        result = availableKeywords.filter((keyword)=>{
           return keyword.toLowerCase().includes(input.toLowerCase());

        });
        console.log(result);

    }
}