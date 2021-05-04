from behave import *
from algorithms import search


@given('we run the search')
def step_impl(context):
    pass


@when('we start the search for 8 on an array of numbers [3, 5, 8, 26, 58, 99]')
def step_impl(context):
    array = [3, 5, 8, 26, 58, 99]
    context.result = search.binary_search(array, 8)


@then('we will have 2 as result')
def step_impl(context):
    assert context.result == 2


@when('we start the search for 1 on an array of numbers [3, 5, 8, 26, 58, 99]')
def step_impl(context):
    array = [3, 5, 8, 26, 58, 99]
    context.result = search.binary_search(array, 1)


@then('we will have None as result')
def step_impl(context):
    assert context.result is None

