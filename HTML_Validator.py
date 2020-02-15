#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags

    validate = True
    tags =_extract_tags(html)
    s = []
    for i in range(len(tags)):
        if "/" not in tags[i]:
            s.append(tags[i])
        else:
            if s == []:
                validate = False
            else:
                left = s.pop()
                if not tags[i][2:] == left[1:]:
                    validate = False
    if validate and s == []:
        return True
    else:
        return False


            

def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    import re
    
    tags = re.findall(r'<[^>]+>', html)
    return tags 


