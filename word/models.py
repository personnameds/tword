from django.db import models

class Word(models.Model):
    NOTLEVELED = ''
    PREKINDERGARTEN = 'PK'
    KINDERGARTEN = 'KG'
    GRADE1 = 'G1'
    GRADE2 = 'G2'
    GRADE3 = 'G3'
    WORD_LEVEL = [
        (NOTLEVELED, ''),
        (PREKINDERGARTEN, 'Pre-Kindergarten'),
        (KINDERGARTEN, 'Kindergarten'),
        (GRADE1, 'Grade 1'),
        (GRADE2, 'Grade 2'),
        (GRADE3, 'Grade 3'),
    ]	
    
    word = models.CharField(max_length=50)
    word_level = models.CharField(max_length=2, choices=WORD_LEVEL,null=True)
    word_length = models.PositiveSmallIntegerField(default=0)
    source = models.CharField(max_length=50, null=True)
    
    def __str__(self):
    	return self.word