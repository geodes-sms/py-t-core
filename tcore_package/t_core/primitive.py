
import uuid


# Abstract class
class Primitive(object):
    def __init__(self):
        self.is_success = False      # flags weather the primitive's action resulted in a success or not
        self.exception = None       # holds the exception object if one was raised
        self._id = uuid.uuid4() 
    
    def cancelIn(self, cancel):
        pass
    
    def __str__(self):
        return '%s %s' % (str(self.__class__.__name__), self._id) 