class ShipStats:
    ship_decks = [4,3,3,2,2,2,1,1,1,1] #Число - палубы у одного коробля
    @staticmethod
    def textHit(thisHit):
        if thisHit == True:
            print('Попадание')
        else:
            print('Промах')

    def __init__ (self,deck,Ox,Oy,rotation):
        self.deck = deck #Количество палуб
        self.Ox = Ox #Координаты начала корабля по оси X
        self.Oy = Oy #Координаты начала корабля по оси Y
        self.rotation = rotation #Угол поворота относительно X,Y

def myDecor(func_to_decor):
    def Wrapper(arg_1,arg_2):
        print('id_', str(func_to_decor(arg_1,arg_2)),sep='')

    return Wrapper


def myFunc (a,b):
    return a+b

