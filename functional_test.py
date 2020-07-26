from selenium import webdriver

browser = webdriver.Firefox()

# Edith has heard about a cool new online to-do app. She goes 
# to check out its homepage

browser.get('http://localhost:8000')

#she notices the page title and the header mention to-do list

assert 'To-Do' in browser.title

#she is invited to enter to-do item straight away

#she types 'Buy peacock feathers' into a text box (Ediths hobby is trying fly-fishing lures)

#when she hits enter, the page updates, and now the page lists 
# "1: Buy peacock feathers as an item in a to-do list

#There is still a text box inviting her to add another item. She 
#enters "use peacock feathers to make a fly" (Edith is very methodiccal)

#The page updates again, and now shows both items on her list
#Edith wonders whether the site will remember her list. Then she sees 
#that the site has generated a unique URL for her -- there is some 
#explanatory text to that effect

#she visits that URL - her to-do list is still there.

#satisfied, she goes back to sleep

browser.quit()

