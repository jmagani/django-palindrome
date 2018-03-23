from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import PalindromeForm

# Create your views here.
def get_palindrome(request):
	palindrome = 'default';
	message = '';

	if request.method == 'POST':
		form = PalindromeForm(request.POST)			 
		if form.is_valid():

			palindrome = form.cleaned_data['your_Palindrome']
			if isPalindrome(palindrome):
				message = 'This is a palindrome'
			else:
				message = 'This is not a palindrome'

		else:
			palindrome = 'BAD INPUT'

	else:
		form = PalindromeForm()

	return render(request, 'bptjob/palindrome.html', {'form' : form, 'palindrome': palindrome, 'message': message})

def isPalindrome(palindrome):
	if palindrome == palindrome[::-1]:
		return True
	else:
		return False

def job_list(request):

    return render(request, 'bptjob/job_list.html', {})
