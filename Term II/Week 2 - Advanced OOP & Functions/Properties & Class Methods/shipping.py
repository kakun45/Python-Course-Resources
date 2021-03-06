class ShippingContainer:
    
    next_serial = 1337

# checkpoint 2
# work on terminal
   
    # @staticmethod
    # def _get_next_serial():
    #     result = ShippingContainer.next_serial
    #     ShippingContainer.next_serial += 1
    #     return result
    
# checkpoint 3
    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result
    
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)
    
    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))
    
    
 # Part 1   
    def __ini__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        self.next_serial += 1
        #ShippingContainer.next_serial += 1

# Checkpoint   1     
# Work on terminal 
       
        
        