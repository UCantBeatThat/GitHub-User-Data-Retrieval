from selenium import webdriver

user = raw_input("Enter User Name: ")

url = "https://github.com/" + user

#driver = webdriver.Firefox()
driver = webdriver.PhantomJS()
driver.get(url + "?tab=repositories")

repos = driver.find_elements_by_xpath("//div[@class='d-inline-block mb-1']/h3/a")
langs = driver.find_elements_by_name('language')

print("\n\nREPOSITORIES: ")
count = 0
for repo in repos:
	text = repo.text
	if text:
		print(text)
		count = count+1

print("\n\nTOTAL REPOSITORIES = "),
print(count)

print("\nLANGUAGES USED: ")
for lang in langs:
	val = lang.get_attribute("value")
	if val:
		print(val),

driver.get(url + "?tab=followers")

followers = driver.find_element_by_xpath("//a[@class='UnderlineNav-item selected']/span")
count = followers.text

print("\n\nFollowers ="),
print(count)
print("")
driver.close();