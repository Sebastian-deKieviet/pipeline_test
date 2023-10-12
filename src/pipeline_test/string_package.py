'''Description'''

class NotAStringException(Exception):
    '''
    
    '''
    pass

class NotAListException(Exception):
    '''
    
    '''
    pass

def concat_function(
        strings: list[str]
        ) -> str:
    '''

    '''

    # Check input
    if type(strings) != list:
        raise NotAListException

    # Perform function
    string = ""
    for stringElement in strings:

        # Make sure element is a string
        if type(stringElement) != str:
            raise NotAStringException

        # Append element to string
        string += stringElement
    return string

def search_function(
        string: str,
        stringToFind: str
        ) -> dict:
    '''
    
    '''

    # Check input
    if type(string) != str:
        raise NotAStringException
    if type(stringToFind) != str:
        raise NotAStringException

    # Perform function
    findings = {}
    return findings

if __name__ == "__main__":
    pass