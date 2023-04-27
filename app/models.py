from django.db import models

# Create your models here.


class Registration(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    fees = models.IntegerField()
    duration = models.CharField(max_length=300)
    comments = models.TextField()

    def __str__(self):
        return self.name


class AddStudents(models.Model):
    id = models.BigAutoField(primary_key=True)
    sname = models.CharField(max_length=100)
    semail = models.EmailField(max_length=100)
    smobile = models.CharField(max_length=10)
    saddress = models.CharField(max_length=255)
    scollege = models.CharField(max_length=255)
    sdegree = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    due_amount = models.FloatField()
    scourse = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.sname





class Teacher(models.Model):
    id = models.BigAutoField(primary_key=True)
    teachername = models.CharField(max_length=300)
    employeesid = models.IntegerField()
    teacheremail = models.CharField(max_length=200)
    teacherpassword = models.CharField(max_length=300)
    teachermobile = models.CharField(max_length=300)
    joindate = models.DateField()
    education = models.CharField(max_length=100)
    workexp = models.CharField(max_length=200)
    photo = models.FileField(upload_to='Teacher/')
    teachercourse = models.ForeignKey(Course, on_delete=models.CASCADE)
    gender = models.CharField(choices=(('O', 'Other'),('F', 'Female'),('M', 'Male')), max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.teachername