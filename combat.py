from fighter import Fighter


def combat(one: Fighter, two: Fighter):
    if not one.isalive():
        print('======================================================================')
        print(f'{one.name} is dead. {two.name} has {two.hp} health.')
        return
    one.strike(two)
    return combat(two, one)