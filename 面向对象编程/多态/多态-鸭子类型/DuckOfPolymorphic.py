#encoding=utf-8
_metaclass=type #确定使用新式类
class Duck(object):
    def quack(self):
        print "Quaaaaaaack"
    def feathers(self):
        print "The duck has white and gray feathers"

class Person(object):
    def quack(self):
        print "The person imitates a duck"
    def feathers(self):
        print "The person takes a feather from the ground and shows it"

def BigPerson(Person):
    def quack(self):
        print "The Big Person is not a person"
    def feathers(self):
        print "The Big Person takes a feather and it is too ugly"
def in_the_forest(duck):
    duck.quack()
    duck.feathers()

def game():
    donald=Duck()
    john=Person()
    jrsmith=BigPerson()
    in_the_forest(donald)
    in_the_forest(john)
    in_the_forest(jrsmith)
game()