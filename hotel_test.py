import unittest
from selenium import webdriver
from time import sleep


class HotelSearch(unittest.TestCase):
        
    @classmethod
    def setUpClass(self):
        print("setUpClass executed")
        self.browser = webdriver.Firefox()
        self.browser.get("https://www.phptravels.net/")
        search = self.browser.find_element_by_id('select2-hotels_city-container')
        search.click()
        search_box =  self.browser.find_element_by_class_name('select2-search__field')
        search_box.send_keys("munich")
        
        sleep(3)
        
        
        list_button = self.browser.find_element_by_id('select2-hotels_city-results')
        list_button.click()
        
        search_button = self.browser.find_element_by_id('submit')
        search_button.click()
    
        sleep(5)
        
        
    
    def test_1(self): #_search_count_check
        browser = self.browser
        all_li = []
        try:
            elem = browser.find_element_by_id('data')
            all_li = elem.find_elements_by_tag_name("li")
            print("Search results are %d" %len(all_li))
        except:
            print("Failed to extract any results")
            
        self.all_li = all_li
            
        self.assertTrue(len(all_li) >= 3,"Number of elements are less than 3")
        
    
        
    def test_2(self): #_search_price
        
        browser = self.browser
        all_li = []
        try:
            elem = browser.find_element_by_id('data')
            all_li = elem.find_elements_by_tag_name("li")
            print("Search results are %d" %len(all_li))
        except:
            print("Failed to extract any results")
        
        element_1_price = None
        
        try:
            element_1_price = all_li[0].find_element_by_class_name('card-price').find_element_by_class_name('mb-0').text
        except:
            print("Element does not exist or Failed to get the price")
        
        self.assertTrue(element_1_price != None ,"Element does not exist or Failed to get the price")
        
       
    def test_3(self): #image

        browser = self.browser
        all_li = []
        element_1_image =[]
        try:
            elem = browser.find_element_by_id('data')
            all_li = elem.find_elements_by_tag_name("li")
            print("Search results are %d" %len(all_li))
        except:
            self.assertTrue(len(all_li) != 0,"Number of elements are less than 3")
            return
        
        try:
            element_1_image = all_li[0].find_elements_by_tag_name('img')
        except:
            self.assertTrue(len(element_1_image) != 0,"Failed to get any image")
            return
        
        print("length of images is %d" %len(element_1_image))
        self.assertTrue(len(element_1_image) > 0,"Failed to get any image")
            
        
        
        # TODO check if image is displayed
     
    def test_4_sidebar_item(self):
        
        browser = self.browser
        elem = None
        all_ul = None
        all_li = None
        try:
            elem = browser.find_element_by_xpath("/html/body/section[2]/div/div/div[1]/div/div[3]/div/form/div[1]")
            all_ul = elem.find_element_by_tag_name("ul")
            all_li = all_ul.find_elements_by_tag_name("li")
        except:
            self.assertTrue(elem != None and all_ul != None and all_li != None ,"Failed to get sidebar")
            return
        
        print("length of star is %d" %len(all_li))
        self.assertTrue(len(all_li) == 5,"sidebar star items does not matches the expected value")
         
        
    """
    # Test pending due to broke website and no search results.....
    
    def test_5_detail_button(self):
        browser = self.browser
        elem = browser.find_element_by_id('data')
        
        all_li = elem.find_elements_by_tag_name("li")
        
        detail_button = all_li[0].find_element_by_tag_name("a")
        
        detail_button.click()
        
        sleep( 6);
    """
    @classmethod
    def tearDownClass(self):
        browser = self.browser
        browser.close()

if __name__ == "__main__":
    
    unittest.main()