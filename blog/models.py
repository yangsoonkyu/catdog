from django.db import models
from django.utils import timezone

class Kind(models.Model):
    CAT = "고양이"
    DOG = "강아지"
    type_choice = ((CAT, "고양이"), (DOG, "강아지"),)
    type = models.CharField(max_length=3,choices=type_choice)
    breed = models.CharField(max_length=200) #품종

    def __str__(self):
        return self.breed


class Animal(models.Model):
    type = models.ForeignKey('blog.Kind', on_delete=models.CASCADE)
    Female = "FE"
    Male = "MA"
    gender_choice = ((Female, "암컷"), (Male, "수컷"),)
    gender = models.CharField(max_length=2, choices=gender_choice)
    age = models.IntegerField(blank=True, null=True)
    find_point = models.CharField(max_length=200)  #발견장소
    find_date = models.DateField(blank=True, null=True)
    find_time = models.CharField(max_length=50, blank= True, null= True)
    other = models.TextField()   #기타 특징
    animal_shelter = models.CharField(max_length=200)   #보호센터
    shelter_tel = models.CharField(max_length=10, help_text='숫자만 10자리 입력하세요')   #보소센터 연락처
    created_date = models.DateTimeField(default=timezone.now)
    animal_move = models.BooleanField(default=False)

    def __str__(self):
        return self.type.breed


    def animove(self):
        self.animal_move = True
        self.save()

    def telnum(self):
        tel = self.shelter_tel
        first = tel[0:3]
        second = tel[3:6]
        third = tel[6:10]
        return '(' + first + ')' + '-' + second + '-' + third


class Comment(models.Model):
    animal = models.ForeignKey('blog.Animal', related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
