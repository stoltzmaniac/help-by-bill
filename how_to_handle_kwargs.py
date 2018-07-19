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


def newFunction(data = 'dict_or_list', return_type = 'dict_or_list', what_should_go_in_here = 'not_sure'):
    # Function needs to accept the dict or list
    # Should perform the calculations from above "existingFunction()"
    # how will existingFunction know 'function to perform' ??
    # Should return either a dict or list (should this be converted here??)
    # if the calculation needs to return a specific one, is the an "if" statement or something better?
    return('dict or list specified by user within this')

