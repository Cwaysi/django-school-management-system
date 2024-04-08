from django.db import models
from django.contrib.auth.models import User

gend = [
    ('Male','Male'),
    ('Female','Female')
]

class AcademicYear(models.Model):
    name = models.CharField(max_length=100, null=True,blank=False)
    description = models.TextField(null=True, blank=False)
    current= models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Term(models.Model):
    name = models.CharField(max_length=100, null=True,blank=False)
    description = models.TextField(null=True, blank=True)
    current= models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Classs (models.Model):
    name = models.CharField(max_length=100, null=True,blank=False)
    stage = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return self.name + ' stage-' + str(self.stage)
    
class Students(models.Model):
    firstname = models.CharField(max_length=100, null=True,blank=False)
    lastname = models.CharField(max_length=100, null=True,blank=False)
    middlename = models.CharField(max_length=100, null=True,blank=True)
    dob = models.DateField('Date of Birth', null=True, blank=False)
    gender = models.CharField(max_length=100, null=True,blank=False, choices = gend)
    location = models.TextField(help_text='Enter all address with GPS', null=True, blank=False)
    enrolled_class = models.CharField(max_length=100, null=True,blank=True)
    current_class = models.ForeignKey(Classs, on_delete=models.DO_NOTHING)
    pic = models.ImageField(upload_to='students_pics/', null=True, blank=True)

    f_fullname = models.CharField("Father's fullname", max_length=100, null=True,blank=True)
    f_occupation = models.CharField("Father's Occupation ", max_length=100, null=True,blank=True)
    f_address = models.TextField("Father's Address ",null=True,blank=True)
    f_mobile = models.CharField("Father's phone number ",max_length=100, null=True,blank=True)
    f_alive = models.BooleanField('Is he alive', default=True)

    m_fullname = models.CharField("Mother's fullname", max_length=100, null=True,blank=True)
    m_occupation = models.CharField("Mother's Occupation ", max_length=100, null=True,blank=True)
    m_address = models.TextField("Mother's Address ",null=True,blank=True)
    m_mobile = models.CharField("Mother's phone number ",max_length=100, null=True,blank=True)
    m_alive = models.BooleanField('Is she alive', default=True)

    g_fullname = models.CharField("Guardian's fullname", max_length=100, null=True,blank=True)
    g_occupation = models.CharField("Guardian's Occupation ", max_length=100, null=True,blank=True)
    g_address = models.TextField("Guardian's Address ",null=True,blank=True)
    g_mobile = models.CharField("Guardian's phone number ",max_length=100, null=True,blank=True)

    enrolled_date = models.DateField(auto_now_add =True)
    active = models.BooleanField(default=True, null=True, blank=True)
    formerschool = models.CharField("Former School", max_length=500,null=True, blank=True, help_text="Which school is he or her coming from")

    def __str__(self):
        if self.middlename is not None:
            md = str(self.middlename)
        else:
            md = " "
        return str(self.firstname) + " " + md + " " + str(self.lastname) + ", "  + str(self.current_class.name)
    
class Attendance (models.Model):
    year = models.IntegerField(null=True, blank=True)
    month = models.CharField(max_length=100, )
    academicYear = models.ForeignKey(AcademicYear, on_delete = models.CASCADE)
    term = models.ForeignKey(Term, on_delete = models.DO_NOTHING, null=True, blank=True)
    student = models.ForeignKey(Students, on_delete = models.CASCADE)
    check_in_date = models.DateField(null=True, blank=True)
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)
    checkin_by = models.CharField(max_length=100, null=True, blank=True)
    checkout_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null= True, blank=True)
    picked_by = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return str(self.student.lastname)+ ' -' + str(self.academicYear)+ ' (' + str(self.term)+ ')'