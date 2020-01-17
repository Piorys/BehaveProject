from src.helpers import Logger
from selenium import webdriver

from src.objects.component import PostCreateComponent, TimelineComponent, DeleteConfirmationModalComponent
from src.objects.page import StaticLoggedOutHomePage, LoginPage

from src.data import Account,Post


def before_all(context):
    Logger.start_logger()


def after_all(context):
    Logger.stop_logger()


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()

    context.post_create_component = PostCreateComponent.PostCreateComponent(context)
    context.timeline_component = TimelineComponent.TimelineComponent(context)
    context.delete_modal_component = DeleteConfirmationModalComponent.DeleteConfirmationModalComponent(context)
    context.static_logged_out_homepage = StaticLoggedOutHomePage.StaticLoggedOutHomeObject(context)
    context.login_page = LoginPage.LoginObject(context)


def after_scenario(context, scenario):
    if "T.1.1" in str(scenario):
        context.timeline_component.navigate_to()
        context.timeline_component.click_tweet_caret_button_by_text(Post.standard_text)
        context.timeline_component.click_tweet_delete_button()
        context.delete_modal_component.click_delete_button()
    context.driver.close()
