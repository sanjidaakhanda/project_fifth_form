from django import forms

class ContactForm(forms.Form):
    char_field = forms.CharField(max_length=100, label='Character Field')
    int_field = forms.IntegerField(label='Integer Field')
    float_field = forms.FloatField(label='Float Field')
    decimal_field = forms.DecimalField(max_digits=5, decimal_places=2, label='Decimal Field')
    date_field = forms.DateField(label='Date Field')
    time_field = forms.TimeField(label='Time Field')
    datetime_field = forms.DateTimeField(label='Date and Time Field')
    email_field = forms.EmailField(label='Email Field')
    url_field = forms.URLField(label='URL Field')
    boolean_field = forms.BooleanField(label='Boolean Field')
    file_field = forms.FileField(label='File Field')
    image_field = forms.ImageField(label='Image Field')
    
    choice_field = forms.ChoiceField(choices=[('option1', 'Option 1'), ('option2', 'Option 2')], label='Choice Field')
    multi_choice_field = forms.MultipleChoiceField(choices=[('option1', 'Option 1'), ('option2', 'Option 2')], label='Multiple Choice Field')
    
    