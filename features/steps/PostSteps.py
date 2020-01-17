from behave import *
from src.objects.component import PostCreateComponent, TimelineComponent
from src.data import Post

# Page Objects
post_create_component = PostCreateComponent.PostCreateComponent()
timeline_component = TimelineComponent.TimelineComponent()

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
