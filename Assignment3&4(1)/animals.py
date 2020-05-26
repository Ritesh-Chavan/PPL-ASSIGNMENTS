from abc import ABC, abstractmethod

class animals(ABC):
    @abstractmethod
    def __init__(self, name, t_type): 
        self.name = name
        self.t_type = t_type
        self.lifespan = None
    
    @abstractmethod
    def set_lifespan(self, lifespan):
        pass
    
    @abstractmethod
    def get_lifespan(self):
        pass



class multiple(ABC):
    
    def is_poisonous(self):
        pass
    
    def get_legs():
        pass


class reptile(animals):
    
    def __init__(self, name, t_type, sub_type):
        super(). __init__(name, t_type) 
        self.sub_type = None
        self.length = None
        self.weight = None
        self.legs = None
        self.lifespan = None

    def set_length(self,length):
        self.length = length
    
    def get_length(self):
        print('The average length is', self.length, 'meters')

    def set_weight(self, weight):
        self.weight = weight
    
    def get_weight(self):
        print('The average weight is', self.weight, 'kgs')

    def set_lifespan(self, lifespan):
        self.lifespan = lifespan

    def get_lifespan(self):
        print('The life span is', self.lifespan, 'years')
    
   

class cobra(reptile, multiple):

    def is_poisonous(self):
        print('Yes, Cobra is a poisonous snake..')

    def color(self):
        print('The color of a cobra is generally patterned in yellow, red, black')


class python(reptile, multiple):

    def is_poisonous(self):
        print('No, Python is not a poisonous snake..')

    def color(self):
        print('The color of a Pyhton is typically brown, tan, black..')


class black_mamba(reptile, multiple):
    
    def is_poisonous(self):
        print('Yes, Black Mamba is the most poisonous snake..')

    def color(self):
        print('The color of a Black Mamba ranges from gray to dark brown..')

class saltwater_crocodile(reptile, multiple):

    def get_legs(self):
        print('They have 4 legs...')

    def color(self):
        print('The color of a saltwater crocodile is pale yellow..')







class multiple1(ABC):
    @abstractmethod
    def sound(self):
        pass
    
    @abstractmethod
    def eats(self):
        pass

class mammals(animals):

    def __init__(self, name, t_type):
        super().__init__(name, t_type)
        self.weight = None
        self.height = None
        self.sub_type = None

    def set_weight(self, weight):
        self.weight = weight
    
    def get_weight(self):
        print('The average weight is', self.weight, 'kgs')
    
    def set_height(self, height):
        self.height = height
    
    def get_height(self):
        print('The average height is', self.height, 'meters')

    def set_lifespan(self, lifespan):
        self.lifespan = lifespan

    def get_lifespan(self):
        print('The life span is', self.lifespan, 'years')

class dog(mammals, multiple1):
    
    def sound(self):
        print('The Dog Barks...')

    def eats(self):
        print('Dog like eating bones')

class cat(mammals, multiple1):
    
    def sound(self, multiple1):
        print('The Cat Meows...')
    
    def eats(self):
        print('Cats like drinking milk and eating fish')


class lion(mammals, multiple1):

    def sound(self):
        print('The Lion roars...')
    
    def eats(self):
        print('Lion feeds on other animals like Deers and Giraffes')










