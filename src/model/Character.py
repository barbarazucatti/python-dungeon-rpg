class Persona:
    def __init__(self, name, class_type, max_health, health, strength, spell_power, defense, agility, critical_strike, healing_power, protection, revival, weapon, special_skill):
        self.name = name
        self.class_type = class_type
        self.max_health = max_health
        self.health = health
        self.strength = strength
        self.spell_power = spell_power
        self.defense = defense
        self.agility = agility
        self.critical_strike = critical_strike
        self.healing_power = healing_power
        self.protection = protection
        self.revival = revival
        self.weapon = weapon
        self.special_skill = special_skill

    def greet(self):
        print("Hello, my name is " + self.name)

    def take_damage(self, amount):
        # aplica redução de dano pela defesa e atualiza a vida.
        pass

    def heal(self, amount):
        # recupera vida sem ultrapassar a vida máxima.
        pass

    def calculate_damage(self):
        # calcula o dano base do ataque.
        pass

    def calculate_critical(self):
        # verifica se o ataque será crítico.
        pass

    def attack(self, target):
        # realiza um ataque básico contra um alvo.
        pass

    def defend(self):
        # aumenta temporariamente a defesa no turno atual.
        pass

    def rest(self):
        # recupera parte da vida do personagem.
        pass

    def special_action(self, target=None):
        # método genérico que será sobrescrito pelas subclasses.
        pass
    
    def is_alive(self):
        return self.health > 0

