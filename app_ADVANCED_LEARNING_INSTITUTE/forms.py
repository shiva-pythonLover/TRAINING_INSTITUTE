from django import forms
class ContactForm(forms.Form):
    name=forms.CharField(max_length=32)
    email=forms.EmailField(max_length=32)
    phone=forms.IntegerField()
    course_choices=[('python','python'),
             ('django','django'),
             ('ui','ui'),
             ('restAPI','restAPI'),
             ]
    courses = forms.MultipleChoiceField(choices=course_choices, widget=forms.CheckboxSelectMultiple)
    shifts_choices=[('morning','morning'),
            ('afternoon','afternoon'),
            ('evening','evening'),
            ('night','night')]
    shifts=forms.MultipleChoiceField(choices=shifts_choices,widget=forms.RadioSelect)
    location_choices = [('HYDERABAD', 'HYDERABAD'),
                      ('BANGLORE', 'BANGLORE'),
                      ('CHENNAI', 'CHENNAI'),
                      ('PUNE', 'PUNE')]
    location = forms.MultipleChoiceField(choices=location_choices, widget=forms.RadioSelect)
    gender_choices = [('male', 'male'),
                        ('female', 'female'),]
    gender = forms.MultipleChoiceField(choices=gender_choices, widget=forms.RadioSelect)
    start_date=forms.DateField()

class AdminLoginForm(forms.Form):
    User_Name=forms.CharField(max_length=32,label='User_Name' )
    Password=forms.CharField(max_length=20,widget=forms.PasswordInput,label='Password')
class AddCourseForm(forms.Form):
    course_id=forms.IntegerField()
    course_name=forms.CharField(max_length=32)
    course_duration=forms.IntegerField()
    course_fee=forms.IntegerField()
    course_start_date=forms.DateField()
    course_start_time=forms.TimeField()
    course_trainer_name=forms.CharField(max_length=32)
    course_trainer_exp=forms.FloatField()
class FeedBackForm(forms.Form):
    name=forms.CharField(max_length=32)
    rating=forms.IntegerField(max_value=10)
    feedback=forms.CharField(max_length=200,widget=forms.Textarea)
    feedback_date=forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),input_formats = ('%d/%m/%Y',))
