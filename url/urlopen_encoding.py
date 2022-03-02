# 표준 에러를 지정하기 위해 sys 모듈 import
import sys

from urllib.request import urlopen

# 해당 홈페이지를 객체로 저장
f = urlopen("http://hanbit.co.kr/store/books/full_book_list.html")

# 객체 f의 정보를 기반으로 인코딩 방식을 추출하여 encoding 객체에 저장
encoding = f.info().get_content_charset(failobj = 'utf-8')

# 인코딩 방식을 출력, 출력 과정에서 생긴 에러는 file 객체에 저장후 출력
#  sys.srderr 에 의해서 밑에 출력
print('encoding :', encoding, file= sys.stderr)

# 추출한 인코딩 방식으로 디코딩
text = f.read().decode(encoding)

#디코딩된 결과를 출력
print(text)