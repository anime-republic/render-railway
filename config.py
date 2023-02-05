from logging import FileHandler, StreamHandler, INFO, basicConfig, error as log_error
from os import path as ospath, environ, remove as osremove
from requests import get as rget
from subprocess import Popen, run as srun

if ospath.exists('log.txt'):
    with open('log.txt', 'r+') as f:
        f.truncate(0)

basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[FileHandler('log.txt'), StreamHandler()],
                    level=INFO)

CONFIG_FILE_URL = environ.get('CONFIG_FILE_URL')
try:
    if len(CONFIG_FILE_URL) == 0:
        raise TypeError
    try:
        res = rget(CONFIG_FILE_URL)
        if res.status_code == 200:
            with open('config.env', 'wb+') as f:
                f.write(res.content)
        else:
            log_error(f"Failed to download config.env {res.status_code}")
    except Exception as e:
        log_error(f"CONFIG_FILE_URL: {e}")
except:
    pass

try:
    TOKEN_PICKLE_URL = environ.get('TOKEN_PICKLE_URL')
    if len(TOKEN_PICKLE_URL) == 0:
        raise KeyError
    try:
        res = rget(TOKEN_PICKLE_URL)
        if res.status_code == 200:
            with open('token.pickle', 'wb+') as f:
                f.write(res.content)
        else:
            log_error(f"Failed to download token.pickle, link got HTTP response: {res.status_code}")
    except Exception as e:
        log_error(f"TOKEN_PICKLE_URL: {e}")
except:
    pass
try:
    ACCOUNTS_ZIP_URL = environ.get('ACCOUNTS_ZIP_URL')
    if len(ACCOUNTS_ZIP_URL) == 0:
        raise KeyError
    try:
        res = rget(ACCOUNTS_ZIP_URL)
        if res.status_code == 200:
            with open('accounts.zip', 'wb+') as f:
                f.write(res.content)
        else:
            log_error(f"Failed to download accounts.zip, link got HTTP response: {res.status_code}")
    except Exception as e:
        log_error(f"ACCOUNTS_ZIP_URL: {e}")
        raise KeyError
    srun(["unzip", "-q", "-o", "accounts.zip"])
    srun(["chmod", "-R", "777", "accounts"])
    osremove("accounts.zip")
except:
    pass
try:
    MULTI_SEARCH_URL = environ.get('MULTI_SEARCH_URL')
    if len(MULTI_SEARCH_URL) == 0:
        raise KeyError
    try:
        res = rget(MULTI_SEARCH_URL)
        if res.status_code == 200:
            with open('drive_folder', 'wb+') as f:
                f.write(res.content)
        else:
            log_error(f"Failed to download drive_folder, link got HTTP response: {res.status_code}")
    except Exception as e:
        log_error(f"MULTI_SEARCH_URL: {e}")
except:
    pass
try:
    YT_COOKIES_URL = environ.get('YT_COOKIES_URL')
    if len(YT_COOKIES_URL) == 0:
        raise KeyError
    try:
        res = rget(YT_COOKIES_URL)
        if res.status_code == 200:
            with open('cookies.txt', 'wb+') as f:
                f.write(res.content)
        else:
            log_error(f"Failed to download cookies.txt, link got HTTP response: {res.status_code}")
    except Exception as e:
        log_error(f"YT_COOKIES_URL: {e}")
except:
    pass
try:
    CATEGORIES_URL = environ.get('CATEGORIES_URL')
    if len(CATEGORIES_URL) == 0:
        raise KeyError
    try:
        res = rget(CATEGORIES_URL)
        if res.status_code == 200:
            with open('categories.txt', 'wb+') as f:
                f.write(res.content)
        else:
            log_error(f"Failed to download categories.txt, link got HTTP response: {res.status_code}")
    except Exception as e:
        log_error(f"CATEGORIES_URL: {e}")
except:
    pass
