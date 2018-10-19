import sys
import traceback

from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from appium.webdriver.webdriver import WebDriverWait
from xnntest import mydriver
# WebDriverWait(mydriver.driver, 20).until(lambda x: x.find_element_by_id('com.aspire.mm:id/mgr_icon')).click()


def ele_mgr(self, timeout, method):
    try:
        return WebDriverWait(mydriver.driver, timeout).until(method)
    except TimeoutException:
        print('出现了TimeoutException')
        return None
    except WebDriverException:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        print('出现了WebDriverException')
        raise
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        print("出现了其他异常")


if __name__=='__main__':
    el = ele_mgr(mydriver.driver, 20, lambda x: x.find_element_by_id('com.aspire.mm:id/mgr_icon11'))
    # el = ele_mgr(mydriver.driver, 20, lambda x: x.find_element_by_xpath('//android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]'))
    if el:
        el.click()
    else:
        print('not found')