from django.db import models
from django.utils import timezone
# from - import는 다른 파일에 있는 것을 추가하라는 뜻

# Create your models here.

class Post(models.Model): # 모델을 정의하는 코드 # 클래스 이름의 첫 글자는 대문자로 써야 함
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # 다른 모델에 대한 링크를 나타냄
	title = models.CharField(max_length=200) # 글자 수가 제한된 텍스트를 정의할 때에 사용
	text = models.TextField() # 글자 수에 제한이 없는 긴 텍스트를 위한 속성
	created_date = models.DateTimeField( # 날짜와 시간
		default = timezone.now)
	published_date = models.DateTimeField(
		blank = True, null = True)

	def publish(self): 
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
