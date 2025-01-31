
// Variables
const poke_container = document.getElementById('poke-container')
const pokemon_count = 151
let pokemon_array = [];
const colors = {
    fire: '#fddfdf',
    grass: '#defde0',
    electric: '#fcf7de',
    water: '#def3fd',
    ground: '#f4e7da',
    rock: '#d5d5d4',
    fairy: '#fceaff',
    poison: '#98d7a5',
    bug: '#f8d5a3',
    dragon: '#97b3e6',
    psychic: '#eaeda1',
    flying: '#f5f5f5',
    fighting: '#e6e0d4',
    normal: '#f5f5f5'
}

//Eventlisteners

function getSelectValue()
{
    var selectValue = document.getElementById('list').value;
}
getSelectValue();

const main_types = Object.keys(colors)
// console.log(main_types);

const fetchPokemons = async () => {
    for(let i = 1; i <= pokemon_count; i++) {
        await getPokemon(i)
        // console.log(getPokemon);
    }
}

const getPokemon = async (id) => {
    const url = `https://pokeapi.co/api/v2/pokemon/${id}`
    const res = await fetch(url)
    const data = await res.json()
    pokemon_array.push(data)
    console.log(pokemon_array)
    createPokemonCard(data)
    // console.log(data); 
}

function generateTypesHTML(typesArray) {
  const typesHTML = typesArray.map(type => `
   <div class='type ${type.type.name}'>
  ${type.type.name}
   </div>
   `)
  return typesHTML.join('')
  }

function createPokemonCard (pokemon) {
  
    const pokemonEl = document.createElement('div')
    pokemonEl.classList.add('pokemon')

    const name = pokemon.name
    const id = pokemon.id.toString().padStart(3, '0')

    const poke_types = pokemon.types.map(type => type.type.name);
    // console.log(poke_types);
    let type = main_types.find(type => poke_types.indexOf(type) == 0)
    let type2 = main_types.find(type => poke_types.indexOf(type) == 1)
    if (type2 === undefined){
      type2 = "none"
    }
    if (type === undefined){
      type = "none"
    }
    // console.log(main_types);
    // const color = colors[type]
    // console.log(poke_types);
    // pokemonEl.style.backgroundColor = color​​​​​​​​
    

    const pokemonInnerHTML = `
            <div class="img-container">
            <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemon.id}.png" alt="">
            </div> 
            <div class="info">
                <span class="number">#${id}</span>
                <h3 class="name">${name}</h3>
            <div class='type-container'>Type: <div class="type ${type}">${type}</div> <div class="type2 ${type2}">${type2}</div></div>
                </div>
            `
    pokemonEl.innerHTML = pokemonInnerHTML

    poke_container.appendChild(pokemonEl)
   
}
// Filtering and Sorting


function filterPokemon(e) {
    const term = e.target.value.toUpperCase();
    const pokemon = document.querySelectorAll('.pokemon');
  
    pokemon.forEach(post => {
      const title = post.querySelector('.number').innerText.toUpperCase();
      const body = post.querySelector('.name').innerText.toUpperCase();
  
      if (title.indexOf(term) > -1 || body.indexOf(term) > -1) {
        post.style.display = 'flex';
      } else {
        post.style.display = 'none';
      }
    });
  }
  





fetchPokemons()
filter.addEventListener('input', filterPokemon);

// Better images
// <img src="https://pokeres.bastionbot.org/images/pokemon/${pokemon.id}.png" alt=""> 
// Old Types
// Type: <div class="type ${type}">${type}</div> <div class="type2 ${type2}">${type2}</div></div>