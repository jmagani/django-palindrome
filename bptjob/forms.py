from django import forms

class PalindromeForm(forms.Form):
    your_Palindrome = forms.CharField(label='Your Palindrome', max_length=100)
    your_name       = forms.CharField(label='Your Name', max_length=100)