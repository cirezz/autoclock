import selenium
from selenium import webdriver
import time
from PIL import Image
import ddddocr


driver = webdriver.Chrome(r"C:\Users\Cirezz\AppData\Local\Google\Chrome\chromedriver.exe")
driver.get(r"http://yq.nauvpn.cn/login")
driver.set_window_size(1400,900)

XPath_dic = {
"下次不再显示":"//*[@id=\"app\"]/div/div[3]/label",
"我已认真阅读":"//*[@id=\"app\"]/div/div[4]/label",
"开始填报":"//*[@id=\"app\"]/div/button",
"学号":"//*[@id=\"app\"]/div/div[1]/div[2]/div/div[1]/div[2]/div/input",
"密码":"//*[@id=\"app\"]/div/div[1]/div[2]/div/div[2]/div[2]/div/input",
"验证码":"//*[@id=\"app\"]/div/div[1]/div[2]/div/div[3]/div[2]/input",
"登录":"//*[@id=\"app\"]/div/div[1]/div[4]/button",
"体温":"//*[@id=\"app\"]/div/div[2]/div[14]/div/div[2]/div/input",
"上传图片":"//*[@id=\"takePhoto\"]",
"次数":"//*[@id=\"app\"]/div/div[2]/div[16]/div/div[2]/div/input",
"提交！":"//*[@id=\"app\"]/div/div[2]/div[18]/button"
}
driver.find_element_by_xpath(XPath_dic["下次不再显示"]).click()
driver.find_element_by_xpath(XPath_dic["我已认真阅读"]).click()
time.sleep(10) # 等到10秒
driver.find_element_by_xpath(XPath_dic["开始填报"]).click()
time.sleep(1)
driver.find_element_by_xpath(XPath_dic["学号"]).send_keys('你的学号')
driver.find_element_by_xpath(XPath_dic["密码"]).send_keys('你的密码')

enter = 0
while enter == 0:
	driver.save_screenshot('screenshot.png')
	time.sleep(1)
	# with open('screenshot.png') as Image
	image = Image.open('screenshot.png')
	image = image.crop((1850, 500, 2079, 600))
	image.save('img.png')

	ocr = ddddocr.DdddOcr()
	with open('img.png', 'rb') as f:
		img_bytes = f.read()
	verification = ocr.classification(img_bytes)
	driver.find_element_by_xpath(XPath_dic["验证码"]).send_keys(str(verification))
	driver.find_element_by_xpath(XPath_dic["登录"]).click()
	time.sleep(1)
	try:
		driver.find_element_by_xpath(XPath_dic["体温"]).send_keys('36')
		enter = 1
		break
	except:
		time.sleep(2)
		continue

driver.find_element_by_xpath(XPath_dic["上传图片"]).send_keys(r'C:\Users\Cirezz\Desktop\health_code.jpg')
driver.find_element_by_xpath(XPath_dic["次数"]).send_keys('4')

driver.find_element_by_xpath(XPath_dic["提交！"]).click()

time.sleep(3)
driver.close()
