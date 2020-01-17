from src.config import TestConf
from src.data import Profile
# Place for storing URL paths for different pages

root = TestConf.env

home_page = '/home'
login_page = '/login'
static_logged_out_home_page = '/'
profile_page = '/'+Profile.account_id
edit_profile = '/settings/profile'
