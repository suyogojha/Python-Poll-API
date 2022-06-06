from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

        
class Question(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    question_text = models.CharField(max_length=200)
 

    def calculate_percentage(self):
        answers = self.answers.all()
        total_votes = 0
        for answer in answers:
            total_votes += answer.counter
                    
        payload = []        
        for answer in answers:
            payload.append(int((answer.counter / total_votes) * 100))
        return payload
       
    def __str__(self):
        return self.question_text




    
class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.CharField(max_length=200)
    counter = models.IntegerField(default=0)
    
    def __str__(self):
        return self.answer_text
    
