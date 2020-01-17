from behave import *
from src.data import Post


@given(u'I create a new tweet')
@when(u'I create a new tweet')
def step_impl(context):
    context.post_create_component.fill_editor(Post.standard_text)
    context.post_create_component.click_add_post()


@then(u'I can see new tweet should be visible on my personal feed')
def step_impl(context):
    context.timeline_component.is_tweet_present(Post.standard_text)


@then(u'I can see widget for tweet creation')
def step_impl(context):
    assert context.post_create_component.validate_component()


@when(u'I delete newly created tweet')
def step_impl(context):
    context.timeline_component.click_tweet_caret_button_by_text(Post.standard_text)
    context.timeline_component.click_tweet_delete_button()
    context.delete_modal_component.click_delete_button()


@then(u'I can no longer see it on my personal feed')
def step_impl(context):
    assert not context.timeline_component.is_tweet_present(Post.standard_text, timeout=1)


@when(u'I try to create tweet longer than 280 characters')
def step_impl(context):
    context.post_create_component.fill_editor(Post.text_290_char)


@then(u'I will be unable to click tweet button')
def step_impl(context):
    assert not context.post_create_component.is_tweet_button_enabled()
