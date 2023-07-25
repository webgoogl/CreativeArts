from django import forms

class userform(forms.Form):
    num1=forms.CharField(label="YOUR NAME")
    num2=forms.CharField(label="PARTNER")
    num3=forms.IntegerField(label="INTEGER ")