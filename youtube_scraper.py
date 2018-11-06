import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv

driver = webdriver.Chrome()

driver.get("https://www.youtube.com/channel/UCW6-BQWFA70Dyyc7ZpZ9Xlg/videos")
time.sleep(1)

elem = driver.find_element_by_tag_name("body")


lastHeight = driver.execute_script("return document.getElementById('content').scrollHeight")


while True:
  driver.execute_script("window.scrollTo(0, document.getElementById('content').scrollHeight);")
  time.sleep(3)
  newHeight = driver.execute_script("return document.getElementById('content').scrollHeight")
  if newHeight == lastHeight:
    break
  lastHeight = newHeight


post_tags = driver.find_elements_by_xpath('//div/h3/a')

with open('youtube_videos.csv', 'w',newline='') as csvfile:
  autowriter = csv.writer(csvfile)
  autowriter.writerow(['Title','URL'])
  for post in post_tags:
    autowriter.writerow([post.get_attribute('title'), post.get_attribute('href')])
