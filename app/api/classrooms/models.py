from django.db import models
from app.utils.base_model import BaseModel

class Classroom(BaseModel):
    subject = models.CharField(max_length=255)
    classroom = models.CharField(max_length=255)
    group_number = models.IntegerField()
    teacher_name = models.CharField(max_length=255)
    class_order = models.IntegerField()
    week_day = models.IntegerField()
    grade = models.IntegerField(blank=True, null=True)
    grade_letter = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return f"{self.subject} - Group {self.group_number}"

    def create_classroom(self, validated_data):
        class_instance = self.model(**validated_data)
        class_instance.save()
        return class_instance
