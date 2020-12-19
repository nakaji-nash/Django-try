from django.db import models

# Create your models here.

# QuestionとChoiceのモデルを作る

class Question(models.Model):
    question_text = models.CharField(max_length=200) # CharField→文字クラス , max_lengthを指定する必要あり
    pub_date = models.DateTimeField('date published') # DateTimeField→日時フィールド
    def __str__(self):
        return self.question_text
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
# django.db.models.modelのサブクラス
