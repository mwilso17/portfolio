//Mike Wilson 18 Jan 2022: Attempt to make a character creator for tabletop RPGs.
var characterName = true;

var button = document.getElementById('buildMyCharacter');

function validateCharacter(){
  let firstName = document.getElementById('firstName').value;
  let lastName = document.getElementById('lastName').value;
  alert(`Your character's name is: ${firstName} ${lastName}`);
}

button.addEventListener('click', validateCharacter);