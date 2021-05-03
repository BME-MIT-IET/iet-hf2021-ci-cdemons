import algorithms as algorithms
from behave import *
from algorithms import sort
import algorithms


@given('we run the app')
def step_impl(context):
    pass


@when('we start the sort on an array of numbers [3, 23, 7, 1, 95, 58, 36]')
def step_impl(context):
    array = [3, 23, 7, 1, 95, 58, 36]
    context.array = sort.bubble_sort(array)


@then('we will have 1 as first element')
def step_impl(context):
    assert context.array[0] == 1
