#브라우저를 제어하기 위해 selenium 모듈의 webdriver를 import
from selenium import webdriver
# 브라우저를 옵션을 이용해서 활성화시키기 위해 option을 improt
from selenium.webdriver.chrome.options import Options
# 클릭과 캡쳐를 위해 keys를 import
from selenium.webdriver.common.keys import Keys
# 작업과 작업 사이에 딜레이를 주기 위해 
import time

class CaptureBot:
    def __init__(self):
        # 홈페이지를 변수에 저장
        self.query = "https://www.instagram.com/explore/tags/"
        # 셀레늄 웹드라이버에 입력할 옵션을 지정
        self.options =Options()
        # 옵션에 해상도를 입력
        self.options.add_argument("--window-size=1920, 1080")
        # 화면이 존재하지 않는 서버에서 사용한다면? 해상도 입력옵션 사용 x -> headless사용
        # self.options.add_argument("headless")
        
        #크롬 드라이버 실행
        self.driver = webdriver.Chrome(
            executable_path="chromedriver_win32/chromedriver.exe", 
            chrome_options = self.options)
    
    # 크롤러 종료 메서드 
    def kill(self):
        self.driver.quit()
    
    # 스크린샷 메서드
    def screen_shot(self, filename):
        self.driver.save_screenshot(filename)
    
    # 인스타그램 로그인 메서드
    def login(self, id, ps):
        # 로그인 페이지로 이동
        self.driver.get("https://www.instagram.com/accounts/login/")
        
        # 다음 동작을 위해 딜레이 시간 부여
        time.sleep(5)
        
        # id, password 입력을 위해 <input>태그 찾기
        input_field = self.driver.find_elements_by_tag_name("input")
        
        # 첫 번째 요소 아이디를 입력
        input_field[0].send_keys(id)
        
        # 두 번째 요소 패스워드 입력
        input_field[1].send_keys(ps)
        
        # 엔터키를 눌러서 로그인
        input_field[1].send_keys(Keys.RETURN) # return이 enter기능
        
        # 다음 동작을 위해 딜레이 시간 부여
        time.sleep(4)
        
    # 인스타그램 태그 검색 메서드
    def search_tag(self, tag):
        
        # 위에서 지정한 URL 주소와 태그를 결합해서 브라우저를 열어줌
        self.driver.get(self.query + tag)
    
        # 다음 동작을 위해 딜레이 시간 부여
        time.sleep(4)
        
    # 최근 게시물 첫 번째 사진을 선택하여 클릭하는 메서드
    def select_picture(self):
        
        # 최근 게시물의 위치를 xpath에 지정
        recent_picture_xpath = '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]'
        
        # recent_picture_xpath의 요소를 가져와서 저장
        recent_picture = self.driver.find_element_by_xpath(recent_picture_xpath)
        
        # 최근 게시물 클릭
        recent_picture.click()
        
        # 다음 동작을 위해 딜레이 시간 부여
        time.sleep(4)
        
    # 게시물들을 돌아다니면서 캡처하는 메서드
    # num 변수에 몇 번 반복할 것인지를 저장
    # -1을 입력하면 직접 종료하기 전까지 무한정을 계속 캡처
    def capture_pictures(self, directory, num):
        
        # 반복할 횟수를 count에 저장
        count = num
        
        # count가 0이 될때까지 계속 반복
        while count != 0:
            
            #카운트를 1씩 차감
            count -= 1
            
            # 캡처할 그림 위치를 article_xpath에 지정
            article_xpath = '/html/body/div[6]/div[3]/div/article/div/div[1]/div/div/div[2]'
                
            # article_xpath의 요소를 가져와서 저장
            article_element = self.driver.find_element_by_xpath(article_xpath)
            
            # html요소를 이용한 스크린샷
            article_element.screenshot(directory + "/"+ str(time.time())+".png")
                                       #폴더명     구분자    랜덤값       확장자
            # 다음 동작을 위해 딜레이 시간 부여
            time.sleep(5)
            
            # 다음 게시물로 이동
            next_button = '/html/body/div[6]/div[2]/div/div[2]/button/div/span'
            next_button_element = self.driver.find_element_by_xpath(next_button)
            next_button_element.click()
            
            # 다음 동작을 위해 딜레이 시간 부여
            time.sleep(5)
            
    # 검색, 캡처를 하나로 묶은 매크로 만들기
    # id, ps, tag, directory, num 변수 필요 <---- 위에 메서드에서 찾기
    def insta_var(self, tag, directory, num):

        # 태그 검색
        self.search_tag(tag)
        
        # 사진 첫 장 선택
        self.select_picture()
            
        # 캡처를 하면서 한 장씩 넘기기
        self.capture_pictures(directory, num)