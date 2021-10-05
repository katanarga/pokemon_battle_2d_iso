class Trainer:
    def __init__(self, active_pokemons, bench_pokemons):
        self.active_pokemons = active_pokemons
        self.bench_pokemons = bench_pokemons

    def switch_pokemon(active_pokemon, bench_pokemon):
        pass

class Pokemon:
    def __init__(self, name, types, talent, attacks, item, stats, sprite_recto, sprite_verso, status, is_alive):
        self.name = name
        self.types = types
        self.talent = talent
        self.attacks = attacks
        self.item = item
        self.stats = stats
        self.sprite_recto = sprite_recto
        self.sprite_verso = sprite_verso
        self.status = status
        self.is_alive = is_alive

    def attack(self, attack_name, target_pokemon):
        pass

    def affected_by_status(self):
        pass

class Stats:
    def __init__(self, health_points, attack, defense, special_attack, special_defense, speed):
        self.health_points = health_points
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed

class Talent:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

class Attack:
    def __init__(self, name, type, pp, power, manor):
        self.name = name
        self.type = type
        self.pp = pp
        self.power = power
        self.manor = manor
        
class Type:
    def __init__(self, name, strengths, weaknesses, resistances, insensitivity):
        self.name = name
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.resistances = resistances
        self.insensitivity = insensitivity

class Item:
    def __init__(self, name, sprite, effect):
        self.name = name
        self.sprite = sprite
        self.effect = effect
    
class Ground:
    def __init__(self, pdr, rain, sun, grele):
        self.pdr = pdr
        self.rain = rain
        self.sun = sun
        self.grele = grele

class Fight:
    def __init__(self, trainer_1, trainer_2, ground) -> None:
        self.trainer_1 = trainer_1
        self.trainer_2 = trainer_2
        self.ground = ground

    def run(self):
        pass

TYPES = ["normal", "grass", "fire", "water", "dragon", "psy", "steel", "poison"]



pokemons = ["Pikachu", "Dracaufeu", "Tortank", "Florizarre", "Ronflex", "Ectoplasma"]
        
    

