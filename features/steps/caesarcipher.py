from behave import *
from algorithms import strings


@given('we run the cipher')
def step_impl(context):
    pass


@when('we start the cipher with offset of 8 on alphabet of {alphabet}')
def step_impl(context, alphabet):
    context.result = strings.caesar_cipher(alphabet, 8)


@when('we start the cipher with offset of 5 on alphabet of {alphabet}')
def step_impl(context, alphabet):
    context.result = strings.caesar_cipher(alphabet, 5)


@when('we start the cipher with offset of -3 on alphabet of {alphabet}')
def step_impl(context, alphabet):
    context.result = strings.caesar_cipher(alphabet, -3)


@when('we start the cipher with offset of 0 on alphabet of {alphabet}')
def step_impl(context, alphabet):
    context.result = strings.caesar_cipher(alphabet, 0)


@then('we will have {result} as result')
def step_impl(context, result):
    assert context.result == result
