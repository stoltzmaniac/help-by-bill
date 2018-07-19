
'''
The request:
- Be able to accept data either a dictionary or a list
- Use a function to transform the data (function is used elsewhere that currently processes a list)
- Return the modified data as either a list or a dictionary (specified by user, not what was initially passed)
-
'''

def existingFunction(list_to_process, function_to_perform):
    # list will always be a list of integers
    # function to perform will never need to be imported from a library
    ret = [function_to_perform(i) for i in list_to_process]
    return(ret)


def no_op(arg):
    "Do nothing function"
    return arg


def newFunction(data='dict_or_list', return_type='list', function_to_perform=no_op ):
    """
        Function needs to accept the dict or list
        Should perform the calculations from above "existingFunction()"
        how will existingFunction know 'function to perform' ??
        Should return either a dict or list (should this be converted here??)
        if the calculation needs to return a specific one, is the an "if" statement or something better?

    Args:
        data:
        return_type:
        function_to_perform:

    Returns:

    """
    if isinstance(data, list):
        return existingFunction(data, function_to_perform)
    elif isinstance(data, dict):
        for key in data.keys():
            # i have no idea of the structure of this dict, but here's the
            # assumption that the keys return values that are lists that can be operated on by existing function
            data[key] = existingFunction(data[key], function_to_perform)
        return data
    else:
        raise ValueError("This data was not of the expected type.  It was a {} instead of a dict or a list".format(type(data)))

