
from uuid import uuid4
from typing import Union

def new_identifier() -> str:
    '''
    Create a random unique universal identifier of 32 characters.
    '''
    return uuid4().hex

def identifier(name:str) -> Union[str,None]:
    '''

    '''

def exists(name:str) -> bool:
    '''
    
    '''


def create(name:str, code:str, is_active:bool = True) -> bool:
    '''

    '''
    
def rename(activity_id:str, new_name:str) -> bool:
    '''

    '''

def modify(activity_id:str, new_code:str) -> bool:
    '''

    '''

def enable(activity_id:str, state:bool=True) -> bool:
    '''

    '''




if __name__ == '__main__':
    identity = new_identifier()
    print(len(identity), identity)