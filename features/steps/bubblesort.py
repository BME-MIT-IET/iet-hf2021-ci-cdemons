import algorithms as algorithms
from behave import *
from algorithms import sort
import algorithms


@given('we run the sort')
def step_impl(context):
    pass


@when('we start the sort on an array of numbers [3, 23, 7, 1, 95, 58, 36]')
def step_impl(context):
    array = [3, 23, 7, 1, 95, 58, 36]
    context.result = sort.bubble_sort(array)


@when('we start the sort on an array of numbers [-45, 56.7, 8532, -8542.53, 54523321]')
def step_impl(context):
    array = [-45, 56.7, 8532, -8542.53, 54523321]
    context.result = sort.bubble_sort(array)


@when('we start the sort on an array of numbers [0]')
def step_impl(context):
    array = [0]
    context.result = sort.bubble_sort(array)


@when('we start the sort on an array of numbers []')
def step_impl(context):
    array = []
    context.result = sort.bubble_sort(array)

@then('we will have 1 as first element')
def step_impl(context):
    assert context.result[0] == 1


@then('we will have -8542.53 as first element')
def step_impl(context):
    assert context.result[0] == -8542.53


@then('we will have 0 as first element')
def step_impl(context):
    assert context.result[0] == 0


@then('we will have empty as result')
def step_impl(context):
    assert context.result == []
