//Mike Wilson 18 Jan 2022: Attempt to make a character creator for tabletop RPGs.
let maleFirstName = ['Estenian', 'Alph', 'Rollo'];
let femaleFirstName = ['Freya', 'Eowyn', 'Lagertha'];
let lastName = ['Greystorm', 'Miller', 'Smith'];

let warriorSkills = ['All out attack', 'Jump', 'Leadership'];
let archerSkills = ['Volley', 'Dodge', 'Detect traps'];
let mageSkills = ['Fireball', 'Sleep', 'Detect magic fields'];

var characterName = true;

var button = document.getElementById('build-my-character');

button.addEventListener('click', validateCharacter);

function validateCharacter(){
  alert('Your character has been created');
}
