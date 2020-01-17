from behave import *
from src.objects.component import PostCreateComponent, TimelineComponent, DeleteConfirmationModalComponent
from src.data import Post

# Page Objects
post_create_component = PostCreateComponent.PostCreateComponent()
timeline_component = TimelineComponent.TimelineComponent()
delete_modal_component = DeleteConfirmationModalComponent.DeleteConfirmationModalComponent()


@given(u'I create a new tweet')
@when(u'I create a new tweet')
def step_impl(context):
    post_create_component.fill_editor(Post.standard_text)
    post_create_component.click_add_post()


@then(u'I can see new tweet should be visible on my personal feed')
def step_impl(context):
    timeline_component.is_tweet_present(Post.standard_text)


@then(u'I can see widget for tweet creation')
def step_impl(context):
    assert post_create_component.validate_component()


@when(u'I delete newly created tweet')
def step_impl(context):
    timeline_component.click_tweet_caret_button_by_text(Post.standard_text)
    timeline_component.click_tweet_delete_button()
    delete_modal_component.click_delete_button()


@then(u'I can no longer see it on my personal feed')
def step_impl(context):
    assert not timeline_component.is_tweet_present(Post.standard_text)


@when(u'I try to create tweet longer than 280 characters')
def step_impl(context):
    post_create_component.fill_editor(Post.text_290_char)


@then(u'I will be unable to click tweet button')
def step_impl(context):
    assert not post_create_component.is_tweet_button_enabled()
