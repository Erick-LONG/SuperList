from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		# 隐试等待，等待网页内容加载
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# 小明听说有一个很酷的在线待办事项应用
		# 他去看了这个应用的首页
		self.browser.get('http://localhost:8000')

		# 他注意到网页的标题和头部都包含’To-Do‘这个词
		self.assertIn('To-Do',self.browser.title)
		self.fail('停止测试')

		# 应用邀请他输入一个待办事项

		# 他在文本框中输入了“购买孔雀羽毛”

		# 他的爱好是钓鱼

		# 他按回车后页面更新了
		# 待办事项表格显示了“1：购买孔雀羽毛”

		# 页面中又显示了一个文本框，可以输入其他的待办事项
		# 他输入了“使用孔雀羽毛做鱼饵”
		# 小明做事很有条理

		# 页面再次更新，她的清单中显示了这两个待办事项

		# 小明想知道这个网站是否会记住她的清单

		# 他看到网站为他生成看一个唯一的URL
		# 而且页面中有一些文字解说这个功能

		# 他访问那个URL，发现她的待办事项列表还在

		# 他满意的睡觉去了

if __name__=='__main__':
	unittest.main(warnings='ignore')


