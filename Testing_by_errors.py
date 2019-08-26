import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# test data
user = "admin"  #the data username in login page
password = "admin"  #the data password in login page
un = "admin"  # the data will used in create user (username)
pwd = "1234567"  # the data will used in create user (Password)
mails = "assdsa@sdadasdad.com"  # the data will used in create user (mail)

class Create_User(unittest.TestCase):  # create the test case
  def setUp(self):  # Test fixture, This is t.est preparation task, to start the test
    self.driver = webdriver.Chrome()  # create a new chrome session
    self.driver.implicitly_wait(2)  # wait for 2 seconds
    self.driver.maximize_window()  # maximize the window
    self.driver.get("http://35.185.110.72/#/login")  # navigate to the website login page

  def test_login(self):  # go to login page
    self.type_user = self.driver.find_element_by_xpath(
      '//*[@id="mat-input-0"]')  # find the username field in login Page
    self.type_user.send_keys(user)  # write the username
    self.type_password = self.driver.find_element_by_xpath(
      '//*[@id="password"]')  # find the Password field in login Page
    self.type_password.send_keys(password)  # write your data in password button
    self.type_password.send_keys(Keys.RETURN)  # click Enter to login
    # find all Users Page
    self.all_users = self.driver.find_element_by_xpath(
      '/html/body/app-root/div/section/app-admin/div/div/div/div/div[1]/div[2]/span')
    self.all_users.click()  # click on the all users button
    # find create user page
    self.create_user = self.driver.find_element_by_xpath(
      '/html/body/app-root/div/section/app-admin/div/div/div/div/div[2]/button[2]')
    self.create_user.click()  # click on create user button
    self.current_html=self.driver.page_source
    # find the username field in create user Page
    self.type_username = self.driver.find_element_by_xpath('//*[@id="mat-input-5"]')
    self.type_username.send_keys(un)  # write the data of username in create user page
    self.type_pwd = self.driver.find_element_by_xpath(
      '//*[@id="mat-input-6"]')  # find the password field in create user Page
    self.type_pwd.send_keys(pwd)  # write the data of password in create user page
    self.type_mail = self.driver.find_element_by_xpath(
      '//*[@id="mat-input-7"]')  # find the mails field in create user Page
    self.type_mail.send_keys(mails)  # write the data of mails in create user page
    # find the checkbox of Role of the user you want to create inc create user page
    self.checkbox = self.driver.find_element_by_xpath('//*[@id="mat-radio-5"]/label')
    self.checkbox.click()  # click on the role you select
    self.type_mail.send_keys(Keys.RETURN)  # click enter to create the user
    self.new_html = self.driver.page_source

    try:
      self.error = self.driver.find_element_by_xpath('//*[@id="mat-input-5"]') #error of username
      print (self.error.text)
      print("i am empty string")
    except:
      print("error1 didn't appear")

    try:
      self.error2= self.driver.find_element_by_xpath('//*[@id="mat-error-10"]') #error of Password
      print(self.error2.text)
    except:
      print("error2 didn't appear")

    try:
      self.error3= self.driver.find_element_by_xpath('//*[@id="mat-error-12"]')   #error of mails
      print(self.error3.text)
    except:
      print("error3 didn't appear")

    try:
      self.error4= self.driver.find_element_by_xpath('//*[@id="mat-error-9"]') #final error after clicking on enter
      print(self.error4.text)
    except:
      print("error4 didn't appear")


    if self.error.text in self.new_html or self.error2.text in self.new_html or self.error3.text in self.new_html or self.error4.text in self.new_html:
      print("test successful")
    else:
      print ("Test fails")

  def tearDown(self):  # test fixture, to end the test
    self.driver.quit()   # close the browser window

if __name__ == '__main__':    # execute the test
  unittest.main()    #Run the test
