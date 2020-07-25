import logging
from abc import abstractmethod
from src.aws import config

log = logging.getLogger(__name__)


class Person():

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
    
    @abstractmethod
    def create_person(self): 
        """
        this is a comment 
        """
        raise NotImplementedError()


"""
Manager inherite from Person
"""
class Manager(Person):
    """
    This is a constructor 
    """
    def __init__(self, id=None, name=None, salary=None, sex=None):
        super().__init__(id, name)
        self.salary = salary
        self.sex = sex

    def set_priviliges(self, previliges=None):
        if previliges is not None: 
            for priv in previliges: 
                if priv in ('execute', 'write'): 
                    print("Priv is E/W: ", priv)
                else:
                    print("Read priv")
        else: 
            print("No priv")


# Encrypt & Decrypt
_fernet = None

def get_fernet(): 
    # not a variable as global
    global _fernet

    try:
        fernet_key = config.get('core', 'ccccc')
        if not fernet_key:
            log.warning("Encryption key is null")             
    except Exception as ex:
        raise Exception("Ex")



# ?? 

if __name__ == "__main__":

    manager = Manager(1, 'Massipssa', 1000, "male")
    print("id : ", manager.id)   
    print("sex : ", manager.sex)   

    if isinstance(manager, Person) or isinstance(manager, Manager):
        print("Yes")

    priviliges = ["read", "write", "execute"]
    manager.set_priviliges(priviliges)
