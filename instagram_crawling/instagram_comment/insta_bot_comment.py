# 인스타 댓글 달기
# 셀레니움 
from selenium import webdriver
# 브라우저를 옵션을 이용해서 활성화 시키기 위한 Option
from selenium.webdriver.chrome.options import Options
# 클릭을 위한 keys
from selenium.webdriver.common.keys import Keys
# 작업사이의 딜레이
import time
import random

class commentBot:
    # 클래스 호출시 바로 실행되는 메서드
    def __init__(self):
        # 홈페이지를 쿼리 변수에 저장
        self.query = "https://www.instagram.com/explore/tags/"
        
        # 셀레니움 웹드라이버에 입력할 옵션 지정 
        self.options = Options()

        # 옵션 해상도 입력
        self.options.add_argument("--windwo-size=1920, 1080")
        # 화면 최대화
        self.options.add_argument('--start-maximized')
        
        # 크롬 드라이버 실행
        self.driver = webdriver.Chrome(
            executable_path="chromedriver_win32/chromedriver.exe",
            chrome_options=self.options
        )
    
    # 인스타그램 로그인 메서드
    def login(self, id, ps):
        
        # 로그인 페이지로 이동 
        self.driver.get("https://www.instagram.com/accounts/login/")
        
        # 딜레이
        time.sleep(5)
        
        # 아이디 패스워드 입력을 위한 input 태그 저장
        input_field = self.driver.find_elements_by_tag_name("input")
       
        # 첫 번째 요소에 아이디 입력
        input_field[0].send_keys(id)
        
        # 두 번째 요소에 비밀번호 입력
        input_field[1].send_keys(ps)
        
        # 엔터를 통해 로그인 -- > 비밀번호 입력하고 바로 엔터키 눌러서 로그인 하는 동작처럼
        input_field[1].send_keys(Keys.ENTER)
        
        # 딜레이
        time.sleep(5)
    
    # 인스타그램 태그 검색
    def search_tag(self, tag):
        
        # init에서 query에 저장한 주소에 입력받은 태그 결합한 브라우저 열기
        self.driver.get(self.query + tag)
        # 딜레이
        time.sleep(5)
    
    # 최근 게시물 첫 번째 사진을 선택하여 클릭하는 메서드
    def select_picture(self):
        
        # 최근 게시물의 위치를 popular_pic_xpath에 저장
        pic_xpath = '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]'
        
        # pic_xpath의 요소를 가져와서 저장
        pic = self.driver.find_element_by_xpath(pic_xpath)
        
        # 인기 게시물 클릭
        pic.click()
        
        # 딜레이
        time.sleep(5)


    def comment(self, num):
        # 반복할 횟수를 cnt에 저장
        cnt = num
       
        # cnt가 0이 될때까지 반복 , -1 일경우 무한루프
        while cnt != 0:
            
            # textarea 태그를 가진 모든 요소를 저장
            el = self.driver.find_element_by_tag_name("textarea")
            
            L = ['so cute', 'so lovely']
            # 댓글달고 엔터
            try:
                el.send_keys(random.choice(L)+Keys.RETURN)
            except:
                time.sleep(5)
                try:
                    el.send_keys(random.choice(L)+Keys.RETURN)
                except:
                        time.sleep(5)
                        el.send_keys(random.choice(L)+Keys.RETURN)

            next_button = '/html/body/div[6]/div[2]/div/div[2]/button/div/span'            
            next_button_element = self.driver.find_element_by_xpath(next_button)
            next_button_element.click()
            
            # 댓글을 달았을 경우에만 count 감소
            cnt -= 1
            
            #딜레이
            time.sleep(5)
            
            
    
    
    
    # 크롤러 종료 메서드
    def close(self):
        self.driver.quit()

        
    def insta_comment(self, tag, num):
        
        # 태그 검색
        self.search_tag(tag)
        
        # 사진 첫 장 선택
        self.select_picture()
        
        # 댓글을 남기면서 넘기기
        self.comment(num)
    