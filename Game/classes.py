from game_functions import damage, add
from lists import get_chance, get_damage, evolution
from pokedex import pokedex
from random import randint

class Player:
    def __init__(self, name):
        self.name           = name

        # Pokeballs
        self.pokeballs      = 0
        self.greatballs     = 0
        self.ultraballs     = 0
        self.masterballs    = 0

        # Potions
        self.potions        = 0
        self.super_potions  = 0
        self.hyper_potions  = 0
        self.max_potions    = 0
        self.xp_potions     = 0

        # Evolve Stones
        self.moon_stones    = 0
        self.fire_stones    = 0
        self.leaf_stones    = 0
        self.thunder_stones = 0
        self.sun_stones     = 0
        self.thunder_stones = 0
        self.water_stones   = 0

    def capture(self, pokemon, area, methods):
        probability = randint(0, 100)
        self.methods -= 1

        chance = get_chance(area, methods)
        if probability <= chance:
            add(pokemon)
            print(pokemon.name, 'Was Captured', f'{self.pokeballs} pokeballs remaining')
            return True
        
        else:
            print(pokemon.name, 'Was not Captured', f'{self.pokeballs} pokeballs remaining')
            return False
        
        


class Pokemon:
    def __init__(self, name, number):
        self.name       = name
        self.number     = number
        self.xp         = 0
        self.max_xp     = 50
        self.lvl        = 1
        self.health     = 20
        self.max_health = 20

    # this function will be called after every battle 
    def level_up(self):
        if self.xp >= self.max_xp:
            self.lvl        += 1
            self.max_xp     = evolution[self.lvl][0]
            self.max_health = evolution[self.lvl][1]
            self.health     = evolution[self.lvl][1]
        
    def atack(self, opponent):
        intensity   = get_damage(self.type, opponent.type)
        damage_1    = damage(self.max_health, intensity)          
        opponent.health -= damage_1
        return opponent.health

    # This function sets random levels to a single pokemon
    def set_level(self, min_l, max_l):
        lvl = randint(min_l, max_l)
        self.lvl         = lvl
        self.max_health  = evolution[lvl][1]
        self.health      = evolution[lvl][1]
        self.max_xp      = evolution[lvl][0]

    # This function sets a level to the initial pokemon
    def initial_level(self):
        lvl = 5
        self.lvl         = lvl
        self.max_health  = evolution[lvl][1]
        self.health      = evolution[lvl][1]
        self.max_xp      = evolution[lvl][0]
            

class Normal(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'normal'


class Fire(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;91m{name}\033[m'
        self.type = 'fire'      


class Water(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;34m{name}\033[m'
        self.type = 'water'


class Grass(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;92m{name}\033[m'
        self.type = 'grass'
    

class Electric(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;93m{name}\033[m'
        self.type = 'electric'


class Ice(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;36m{name}\033[m'
        self.type = 'ice'


class Fighting(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;31m{name}\033[m'
        self.type = 'fighting'


class Poison(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;35m{name}\033[m'
        self.type = 'poison'


class Ground(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;33m{name}\033[m'
        self.type = 'ground'


class Flying(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'flying'


class Psychic(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;95m{name}\033[m'
        self.type = 'psychic'


class Bug(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;32m{name}\033[m'
        self.type = 'bug'


class Rock(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;90m{name}\033[m'
        self.type = 'rock'


class Ghost(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;35m{name}\033[m'
        self.type = 'ghost'


class Dragon(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;91m{name}\033[m'
        self.type = 'dragon'


class Dark(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'dark'


class Steel(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'steel'


class Fairy(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'fairy'
