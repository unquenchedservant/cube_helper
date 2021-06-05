import requests
from dotenv import dotenv_values
import os
import sys

CURRENT_VERSION = "0.12"
extDataDir = os.getcwd()
if getattr(sys, 'frozen', False):
	parentDir = os.path.dirname(__file__)
	parentDir = parentDir.replace(r"\utilities", "")
	extDataDir = os.path.abspath(os.path.join(parentDir, '.env'))
dotenv_val = dotenv_values(dotenv_path=os.path.join(extDataDir, '.env'))

def update_available():
	user = 'unquenchedservant'
	token = dotenv_val.get("GITHUB_TOKEN")
	gh_session = requests.Session()
	gh_session.auth = (user, token)
	response = gh_session.get("https://api.github.com/repos/unquenchedservant/cube_helper/releases/latest")
	return response.json()["tag_name"] != CURRENT_VERSION
