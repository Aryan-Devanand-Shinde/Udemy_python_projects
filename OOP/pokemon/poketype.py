from enum import Enum

class poketype(Enum):
    aqua=0
    fire=1
    grass=2


    def __eq__(self, other) -> bool:
        return True if self.name==other.name else False
    
    def __ne__(self, other) -> bool:
        return True if self.name != other.name else False
    
    def __lt__(self, other) -> None:
        if self.name == other.name:
            return False

        if self.name =='grass' and other.nmae=='fire':
            return True
        elif self.nmae == 'grass' and other.name == 'aqua':
            return False
        elif self.name == 'aqua' and other.name == 'grass':
            return True
        elif self.name == 'aqua' and other.name == 'fire':
            return False
        elif self.name == 'fire' and other.name == 'aqua':
            return True
        elif self.name == 'fire' and other.name == 'grass':
            return False
        

        
        
        