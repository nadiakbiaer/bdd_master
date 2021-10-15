import allure
from numpy.testing import assert_equal
from behave import given,when,then



@given(u'the user look at the home page DragnDrop')
def step_impl(context):
    context.dd.url("https://qavbox.github.io/demo/dragndrop/")
    # context.dd.url()

@when(u'he move the box drag me to my  in the box')
def step_impl(context):
    context.dd.drag()

@then(u'he see the text change')
def step_impl(context):
    assert_equal(context.dd.affichageDrop(),"Dropped!")


