class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def nameprint(self):
        print('Имя героя:', self.name)

    def умножить_здоровье_на_2(self):
        self.health_points *= 2

    def __init__(self, nickname, superpower, health_points):
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points

    def __len__(self):
        return len(self.catchphrase)

Harleen_Frances_Quinzel = SuperHero('Harleen Frances Quinzel', 'Harley Quinn',
                                    'immunity to poisons', 100, 'My love scares you, but no gun?')
Harleen_Frances_Quinzel.умножить_здоровье_на_2()
print(len(Harleen_Frances_Quinzel))
Harleen_Frances_Quinzel.nameprint()