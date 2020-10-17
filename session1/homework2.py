import gc

from catlib import breeds, bug_cat


class Robot:
    region = ""
    abilities = []

    def __init__(self, sale_country):
        Robot.region = sale_country
        Robot.id = id(self)
        Robot.serial_number = "{}_{}".format(Robot.region.lower(), Robot.id)

    def save_ability(self, ability):
        if isinstance(self, RoboCat) and ability not in Robot.abilities:
            super().add_skill(ability)
            Robot.abilities.append(ability)
            return True

    def remove_ability(self, ability, obj):
        if isinstance(self, RoboCat) and ability in Robot.abilities:
            super().add_skill(ability)
            Robot.abilities.append(ability)
            return True


class Cat:

    def __init__(self, name, age, bread, *skills):
        self.name = name
        self.age = age
        if bread in breeds.keys():
            self.bread = bread
        else:
            raise ValueError("I don't know such a bread.\nIs \"{}\" a cat at all?? {}"
                             "Here is a valid list of breeds supported:\n {}""".format(bread, bug_cat, breeds))
        self.skills = list(skills)

    @property
    def knowledge_level(self):
        skills_amount = len(self.skills)
        print("{name} has {num} {Adjective}".format(name=self.name, num=skills_amount,
                                                    Adjective='skill' if skills_amount == 1 else 'skills'))
        return len(self.skills)

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
            print("{} mastered skill: \"{}\"".format(self.name, skill))
            return True

    def forget_skill(self, skill):
        if skill in self.skills:
            self.skills.remove(skill)
            print("{} just forget skill: \"{}\"".format(self.name, skill))
            return True


class RoboCat(Robot, Cat):

    def __init__(self, name, age, bread):
        Cat.__init__(self, name, age, bread,)
        sale_country = breeds[bread]
        Robot.__init__(self, sale_country)

    def add_skill(self):
        pass

    def remove_skill(self):
        pass

    def sync(self):
        pass
############

cat1 = Cat('Belyash', 12, 'British Shorthair', 'meow')
cat1.add_skill('run')
print(cat1.skills)
cat1.forget_skill('run')

cat2 = Cat('Cheburek', 12, 'Cyprus', 'pee', 'stink')
cat3 = Cat('Shaverma', 12, 'Serengeti', 'sleep', 'yell')


robo1 = Robot('Asia')


robocatx = RoboCat('lol', 13, 'Cyprus')
robocatx.save_ability('Jump')