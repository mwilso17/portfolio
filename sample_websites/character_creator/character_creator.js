//Mike Wilson 18 Jan 2022: Attempt to make a character creator for tabletop RPGs.
var button = document.getElementById('buildMyCharacter');

function generateCharacter(){
  let firstName = document.getElementById('firstName').value;
  let lastName = document.getElementById('lastName').value;
  let characterName = firstName + ' ' + lastName;

  let characterClass = document.getElementById('characterClass').value;
  let race = document.getElementById('characterRace').value;

  let strength = 1;
  let wisdom = 1;
  let intelligence = 1;
  let dexterity = 1;
  let charisma = 1;
  let hitPoints = 1;
  
  if (race == 'Human') {
    strength = strength + generateRandomNumber(20);
    wisdom = wisdom + generateRandomNumber(20);
    intelligence = intelligence + generateRandomNumber(20);
    dexterity = dexterity + generateRandomNumber(20);
    charisma = charisma + generateRandomNumber(20);
    hitPoints = hitPoints + generateRandomNumber(20);
  } else if (race == 'Elf') {
    strength = strength + generateRandomNumber(14);
    wisdom = wisdom + generateRandomNumber(25);
    intelligence = intelligence + generateRandomNumber(26);
    dexterity = dexterity + generateRandomNumber(23);
    charisma = charisma + generateRandomNumber(15);
    hitPoints = hitPoints + generateRandomNumber(14);
  } else if (race == 'Dwarf') {
    strength = strength + generateRandomNumber(23);
    wisdom = wisdom + generateRandomNumber(17);
    intelligence = intelligence + generateRandomNumber(14);
    dexterity = dexterity + generateRandomNumber(17);
    charisma = charisma + generateRandomNumber(12);
    hitPoints = hitPoints + generateRandomNumber(26);
  }

  if (characterClass == 'Warrior') {
    strength = strength + 4;
    charisma = charisma + 3;
  } else if (characterClass == 'Mage') {
    wisdom = wisdom + 4;
    intelligence = intelligence + 3;
  } else if (characterClass == 'Archer') {
    dexterity = dexterity + 4;
    intelligence = intelligence + 3;
  }

  console.log(`Your attributes are: 
    strength: ${strength}
    wisdom: ${wisdom}
    intelligence: ${intelligence}
    dexterity: ${dexterity}
    charisma: ${charisma}
    hitPoints: ${hitPoints}`);

  alert(`Your character's full name is: ${characterName} 
    ${firstName} is a level 1 ${characterClass}`);
}

function generateRandomNumber(max) {
  return Math.floor(Math.random() * max);
}

button.addEventListener('click', generateCharacter);
