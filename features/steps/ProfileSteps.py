from behave import *
from src.data import Profile


@when(u'I navigate to edit profile section')
def step_impl(context):
    context.navigation_bar_component.click_profile_button()
    context.profile_page.click_edit_profile()


@then(u'I can see edit profile section')
def step_impl(context):
    assert context.edit_profile_component.validate_component()


@when(u'I will update my bio')
def step_impl(context):
    context.edit_profile_component.fill_bio(Profile.bio)
    context.edit_profile_component.click_save_button()


@then(u'I will see my bio updated')
def step_impl(context):
    context.edit_profile_component.wait_for_modal_to_close()
    assert Profile.bio in context.profile_page.get_profile_bio()


@when(u'I will update my location')
def step_impl(context):
    context.edit_profile_component.fill_location(Profile.location)
    context.edit_profile_component.click_save_button()


@then(u'I will see my location updated')
def step_impl(context):
    context.edit_profile_component.wait_for_modal_to_close()
    assert Profile.location in context.profile_page.get_profile_location()
