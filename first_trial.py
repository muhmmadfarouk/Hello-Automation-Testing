import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#test data
user= "admin"          #variable of username in login page
password="admin"       #variable of password in login page
un="admin"           #the username will used in create user
pwd="1234567"          #the password will used in create user
mails="assdsa@sdadasdad.com"    #the mail will used in create user
Role="client"                   #Role is client

class Create_User(unittest.TestCase):  # create the test case
  def setUp(self):  # Test fixture, This is t.est preparation task, to start the test
    self.driver = webdriver.Chrome()  # create a new chrome session
    self.driver.implicitly_wait(2)  # wait for 2 seconds
    self.driver.maximize_window()  # maximize the window
    self.driver.get("http://35.185.110.72/#/login")  # navigate to the website login page

  def test_login(self):   # go to login page
    self.type_user= self.driver.find_element_by_xpath('//*[@id="mat-input-0"]')
    self.type_user.send_keys(user)
    self.type_password= self.driver.find_element_by_xpath('//*[@id="password"]')
    self.type_password.send_keys(password)  # type your data in password button
    self.type_password.send_keys(Keys.RETURN)  # click on login button
    self.all_users = self.driver.find_element_by_xpath('/html/body/app-root/div/section/app-admin/div/div/div/div/div[1]/div[2]/span')
    self.all_users.click()
    self.create_user= self.driver.find_element_by_xpath('/html/body/app-root/div/section/app-admin/div/div/div/div/div[2]/button[2]')
    self.create_user.click()
    self.current_html=self.driver.page_source
    self.type_username= self.driver.find_element_by_xpath('//*[@id="mat-input-5"]')
    self.type_username.send_keys(un)
    self.type_pwd = self.driver.find_element_by_xpath('//*[@id="mat-input-6"]')     # get the search textbox
    self.type_pwd.send_keys(pwd)      # enter search keyword and submit
    self.type_mail= self.driver.find_element_by_xpath('//*[@id="mat-input-7"]')
    self.type_mail.send_keys(mails)
    self.checkbox= self.driver.find_element_by_xpath('//*[@id="mat-radio-5"]/label')
    self.checkbox.click()
    self.type_mail.send_keys(Keys.RETURN)
    self.new_html = self.driver.page_source

    try:
      if self.driver.find_element_by_xpath('//*[@id="mat-dialog-2"]/div/div').is_displayed():
        print("success")
    except:
      print("fails")

  def tearDown(self):  # test fixture, to end the test
    self.driver.quit()   # close the browser window

if __name__ == '__main__':    # execute the test
  unittest.main()    #Run the test
