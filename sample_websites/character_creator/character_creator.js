//Mike Wilson 18 Jan 2022: Attempt to make a character creator for tabletop RPGs.
var button = document.getElementById('buildMyCharacter');

function validateCharacter(){
  let firstName = document.getElementById('firstName').value;
  let lastName = document.getElementById('lastName').value;
  let characterName = firstName + ' ' + lastName;

  let characterClass = document.getElementById('characterClass').value;

  alert(`Your character's full name is: ${characterName} 
  ${firstName} is a level 1 ${characterClass}`);
}

function generateCharacterStats(){
  let race = document.getElementById('characterRace').value;
  let characterClass = document.getElementById('characterClass').value;


}

button.addEventListener('click', validateCharacter);