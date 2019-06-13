"""Test for some of my functions."""

from functions_and_classes import my_func, my_other_func

##
##

def test_check_wrong_response_mc():

    assert check_wrong_response_mc('a') == 'a'

def test_max_dict_key():
    my_dict = {'maximum' : 10, 'median' : 5, 'minimum' : 1}
    assert max_dict_key() == 'maximum'
