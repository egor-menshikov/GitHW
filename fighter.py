from random import randint


class Fighter:
    crit_dmg_mod = 1.5
    body_part = {'head': 1.25, 'body': 1, 'arms': 0.8, 'legs': 0.6}

    def __init__(self,
                 name: str,
                 hp: int,
                 dodge: int,
                 block: int,
                 attack: int,
                 accuracy: int,
                 crit: int):
        self.name = name
        self.hp = hp
        self.dodge = dodge
        self.block = block
        self.attack = attack
        self.accuracy = accuracy
        self.crit = crit

    def __str__(self):
        return f'{self.name}\n' \
               f'HP: {self.hp} | Dodge: {self.dodge} | Block: {self.block}\n' \
               f'ATT: {self.attack} | ACC: {self.accuracy} | Crit%: {self.crit}\n'

    # Метод удара
    def strike(self, opponent):
        # Рандомим в какую часть тела пойдет удар, и создаем модификатор дамага
        loc_roll = randint(0, 9)
        dmg_mod: float
        if loc_roll == 0:
            dmg_mod = Fighter.body_part['head']
        elif 1 <= loc_roll < 3:
            dmg_mod = Fighter.body_part['legs']
        elif 3 <= loc_roll < 6:
            dmg_mod = Fighter.body_part['arms']
        else:
            dmg_mod = Fighter.body_part['body']

        # Тут считаем урон, если критануло - ставим флаг для вывода другого текста в комбат логе
        damage = self.attack * dmg_mod
        did_crit = False
        if self.crit >= randint(1, 100):
            damage *= Fighter.crit_dmg_mod
            did_crit = True

        # Наносим урон если попали, пишем комбат лог
        if self.accuracy >= randint(1, 100):
            if opponent.dodge < randint(1, 100):
                if opponent.block < randint(1, 100):
                    opponent.hp -= int(damage)
                    if did_crit:
                        print(f'{self.name} critically hits {opponent.name}'
                              f' in the {next(k for k, v in Fighter.body_part.items() if v == dmg_mod)}'
                              f' for {int(damage)} damage!'
                              f' ------> {self.name}: {self.hp} | {opponent.name}: {opponent.hp}')
                    else:
                        print(f'{self.name} hits {opponent.name}'
                              f' in the {next(k for k, v in Fighter.body_part.items() if v == dmg_mod)}'
                              f' for {int(damage)} damage.'
                              f' ------> {self.name}: {self.hp} | {opponent.name}: {opponent.hp}')
                else:
                    print(f'{self.name} attacks, but is blocked by {opponent.name}.')
            else:
                print(f'{self.name} attacks, but {opponent.name} dodges.')
        else:
            print(f'{self.name} attacks {opponent.name}, but misses.')

    def isalive(self):
        if self.hp < 1:
            return False
        return True


sub_zero = Fighter('Sub-Zero', 100, 33, 40, 18, 85, 15)
scorpion = Fighter('Scorpion', 110, 33, 25, 21, 80, 15)
