from src.helpers import Logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.objects.component import PostCreateComponent, TimelineComponent, DeleteConfirmationModalComponent, \
    NavigationBarComponent, EditProfileComponent
from src.objects.page import StaticLoggedOutHomePage, LoginPage, ProfilePage

from src.data import Post
from src.helpers import ScreenshotHelper
from src.config import TestConf


def before_all(context):
    Logger.start_logger()
    ScreenshotHelper.clear_screenshot_dir()


def after_all(context):
    Logger.stop_logger()


def before_scenario(context, scenario):
    options = Options()
    if TestConf.headless:
        options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    context.driver = webdriver.Chrome(chrome_options=options)

    # Component objects
    context.post_create_component = PostCreateComponent.PostCreateComponent(context)
    context.timeline_component = TimelineComponent.TimelineComponent(context)
    context.delete_modal_component = DeleteConfirmationModalComponent.DeleteConfirmationModalComponent(context)
    context.navigation_bar_component = NavigationBarComponent.NavigationBarComponent(context)
    context.edit_profile_component = EditProfileComponent.EditProfileComponent(context)

    # Page Objects
    context.profile_page = ProfilePage.ProfilePage(context)
    context.static_logged_out_homepage = StaticLoggedOutHomePage.StaticLoggedOutHomeObject(context)
    context.login_page = LoginPage.LoginObject(context)


def after_scenario(context, scenario):
    if "T.1.1" in str(scenario):
        context.timeline_component.navigate_to()
        context.timeline_component.click_tweet_caret_button_by_text(Post.standard_text)
        context.timeline_component.click_tweet_delete_button()
        context.delete_modal_component.click_delete_button()
    if "T.2.2" in str(scenario):
        context.profile_page.click_edit_profile()
        context.edit_profile_component.clear_bio()
        context.edit_profile_component.click_save_button()
        context.edit_profile_component.wait_for_modal_to_close()
    if "T.2.3" in str(scenario):
        context.profile_page.click_edit_profile()
        context.edit_profile_component.clear_location()
        context.edit_profile_component.click_save_button()
        context.edit_profile_component.wait_for_modal_to_close()
    context.driver.close()


def after_step(context, step):
    if step.status == 'failed':
        ScreenshotHelper.make_screenshot(context.driver)
