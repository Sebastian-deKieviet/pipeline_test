'''Description'''

class NotANumberException(Exception):
    '''
    
    '''
    pass

def _check_if_number(num: int |float):
    '''
    
    '''
    # Check input
    if type(num) != int and type(num) != float:
        raise NotANumberException

def add_function(
        num1: int | float,
        num2: int | float
        ) -> int | float:
    '''
    
    '''
    # Check input
    _check_if_number(num1)
    _check_if_number(num2)

    # Perform function
    return num1+num1

def subtract_function(
        num1: int | float,
        num2: int | float
        ) -> int | float:
    '''
    
    '''
    # Check input
    _check_if_number(num1)
    _check_if_number(num2)

    # Perform function
    return num1-num2

def min_function(
    num1: int | float,
    num2: int | float
    ) -> int | float:
    '''
    
    '''
    # Check input
    _check_if_number(num1)
    _check_if_number(num2)

    # Perform function
    return float(num1) if num1 < num2 else float(num2)

def max_function(
        num1: int | float,
        num2: int | float
        ) -> int | float:
    '''
    
    '''
    # Check input
    _check_if_number(num1)
    _check_if_number(num2)

    # Perform function
    return num1 if num1 > num2 else num2

if __name__ == "__main__":
    pass