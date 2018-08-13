class MainPage:

    # Use __init__() to obtain required elements from the webpage
    def __init__(self, driver):
        self.driver=driver
        self.main_news=self.driver.find_element_by_class_name("hero__figcaption")
        self.title_logo=self.driver.find_element_by_class_name("header__logo")
        self.right_side_ad=self.driver.find_element_by_class_name("right-banner-ad")
        self.social_links=self.driver.find_elements_by_class_name("social__item")

    # Proc to check if the headline news is displayed
    def headline_news_is_displayed(self):
        assert self.main_news.is_displayed()
        
    # Proc to check if the website's logo is displayed
    def planetf1_logo_is_displayed(self):
        assert self.title_logo.is_displayed()

    # Proc to check if the advertisement is displayed
    def advert_is_displayed(self):
        assert self.right_side_ad.is_displayed()
        
    # Proc to check if the Twitter and Facebook links are displayed
    def social_media_is_displayed(self):
        facebookPresent=False
        twitterPresent=False
        for item in self.social_links: 
            link=item.find_element_by_css_selector('a').get_attribute('href')
            if "twitter" in link:
                twitterPresent=True
            if "facebook" in link:
                facebookPresent=True
        assert facebookPresent
        assert twitterPresent
        
