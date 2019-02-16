import random


class Item:

    def __init__(self, name, dmg_bonus):
        self.name = name
        self.dmg_bonus = dmg_bonus


class Char:

    def __init__(self, name, dmg, max_hp):
        self.name = name
        self._dmg = dmg
        self.max_hp = max_hp
        self.hp = max_hp
        self.equipment = []

    @property
    def dmg(self):
        return self._dmg + sum([e.dmg_bonus for e in self.equipment])
                            # funkcja sumuje jedynie dmg_bonus z elementów w liście self.equipment

    def __str__(self):
        text = f'{self.name}, damage {self.dmg}, hp {self.hp}/{self.max_hp}'
        for item in self.equipment:
            text += str(item)
        return text

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def heal(self, points):
        if self.hp == 0:
            return False
        self.hp += points
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def equip_item(self, item):
        self.equipment.append(item)

    def unequip_item(self, item):
        self.equipment.remove(item)

    def attack_power(self):
        return random.randint(self.dmg//2, self.dmg)


def fight(attacker, defender):

    print(f'Fight {attacker.name} vs {defender.name}')
    print(attacker)
    print(defender)
    print("-"*40)

    while attacker.hp > 0 and defender.hp > 0:
        attacker_power = attacker.attack_power()
        print(f'{attacker.name} hits {defender.name} for {attacker_power}')
        defender.take_damage(attacker_power)

        print("-"*40)

        if defender.hp > 0:
            defender_power = defender.attack_power()
            print(f'{defender.name} hits {attacker.name} for {defender_power}')
            attacker.take_damage(defender_power)

    print("End of fight")

    print(attacker)
    print(defender)


rafal = Char("Rafał", 5, 200)
janusz = Char("Janusz", 3, 400)
axe = Item("Axe", 2)
rafal.equip_item(axe)
fight(rafal, janusz)


def test_new_char():
    char = Char("Albert", 1, 20)
    assert char.name == "Albert" and char.dmg == 1 and char.hp == 20 and char.max_hp == 20


def test_damage():
    char = Char("Rafał", 5, 200)
    assert char.hp == 200
    char.take_damage(80)
    assert char.hp == 120
    char.take_damage(200)
    assert char.hp == 0


def test_heal():
    char = Char("Rafał", 5, 200)
    char.take_damage(80)
    assert char.hp == 120
    char.heal(50)
    assert char.hp == 170


def test_heal_when_char_died():
    char = Char("Rafał", 5, 200)
    char.take_damage(800)
    assert char.hp == 0
    char.heal(50)
    assert char.hp == 0


def test_overheal():
    char = Char("Rafał", 5, 200)
    char.take_damage(80)
    assert char.hp == 120
    char.heal(500)
    assert char.hp == 200

def test_item():
    item = Item("Axe", 20)
    assert item.name == "Axe"
    assert item.dmg_bonus == 20

def test_equip_item():
    char = Char("Rafał", 5, 200)
    item = Item("Axe", 20)
    assert item not in char.equipment
    assert char.dmg == 5
    char.equip_item(item)
    assert item in char.equipment
    assert char.dmg == 25

def test_unequip_item():
    char = Char("Rafał", 5, 200)
    item = Item("Axe", 20)
    char.equip_item(item)
    char.unequip_item(item)
    assert item not in char.equipment
    assert char.dmg == 5

def test_char_attack_power():
    char = Char("Rafał", 5, 200)
    assert char.dmg == 5
    attack_power = char.attack_power()
    assert (char.dmg // 2) <= attack_power <= char.dmg
