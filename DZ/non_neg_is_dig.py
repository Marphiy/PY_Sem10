class NonNegativeIsDigit: 
        
    def __set_name__(self, owner, attr_name):
        self.attr_name = attr_name
    
    def __set__(self, instance, value):
        if type(value) != float and type(value) != int:
            raise ValueError("Введенные данные не являются числом!")
        elif value < 0:
            raise ValueError("Введенные данные не могут быть отрецательными!")
        instance.__dict__[self.attr_name] = value
        
        
        
      