from behave import *
from algorithms import search


@given('we run the search')
def step_impl(context):
    pass


@when('we start the search for 8 on an array of numbers [3, 5, 8, 26, 58, 99]')
def step_impl(context):
    array = [3, 5, 8, 26, 58, 99]
    context.result = search.binary_search(array, 8)


@when('we start the search for 1 on an array of numbers [3, 5, 8, 26, 58, 99]')
def step_impl(context):
    array = [3, 5, 8, 26, 58, 99]
    context.result = search.binary_search(array, 1)


@when('we start the search for 58 on an array of numbers [3, 58, 5, 8, 26, 99]')
def step_impl(context):
    array = [3, 58, 5, 8, 26, 99]
    context.result = search.binary_search(array, 58)


@when('we start the search for -2.54 on an array of numbers [-95423814.4, -851, -52.4856324126, -2.54, 26, 99]')
def step_impl(context):
    array = [-95423814.4, -851, -52.4856324126, -2.54, 26, 99]
    context.result = search.binary_search(array, -2.54)

@when('we start the search for 1 on an array of numbers []')
def step_impl(context):
    array = []
    context.result = search.binary_search(array, 1)


@then('we will have 2 as result')
def step_impl(context):
    assert context.result == 2


@then('we will have 3 as result')
def step_impl(context):
    assert context.result == 3


@then('we will have None as result')
def step_impl(context):
    assert context.result is None
