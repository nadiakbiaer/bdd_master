from behave import when,then
from numpy.testing import assert_equal

from selenium.webdriver.common.action_chains import ActionChains
@when(u'he move the slider bar 0 to 100')
def step_impl(context):
    context.dd.slider()

@then(u'he see the slider bar change')
def step_impl(context):
    assert_equal(context.dd.affichageSlider(),'100')

