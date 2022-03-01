from django.shortcuts import render, redirect
from .models import Team
from mainevent.models import User
from .forms import create_teamForm, join_teamForm, position_form, SubmitForm
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
	return render(request, 'pitchers/index.html')

@login_required
def dashboard(request):
	c_form = create_teamForm()
	j_form = join_teamForm()
	p_form = position_form()
	team   = request.user.team
	users  = User.objects.all()
	team_members = User.objects.filter(team = request.user.team)
	context = {
		'c_form' : c_form,
		'j_form' : j_form,
		'team'	 : team,
		'users'  : users,
		'p_form' : p_form,
		'team_members' : team_members
	}
	return render(request, 'user/dashboard.html', context)


def assign_position(request):
	teams = Team.objects.all()
	if request.method == 'POST':
		form = position_form(request.POST)
		if form.is_valid():
			user = request.user
			u_position = form.cleaned_data['position']
			if u_position == None:
				user.position = form.instance.position
				user.save()
				return redirect('dashboard')
			y = User.objects.all().filter(team = user.team).filter(position = u_position)
			print(y.count())
			if y.count()==0:
				# x = form.save()
				user.position = str(form.instance.position)
				user.save()
				return redirect('dashboard')
			else:
				messages.add_message(request, messages.INFO, f'This position is already taken by your team mate!')
				return redirect('dashboard')
	return redirect('dashboard')
	
	


	
def create_team(request):
	return redirect('dashboard')
	teams = Team.objects.all()
	if request.method == 'POST':
		user = request.user
		unique_id = get_random_string(length=6)
		flag = 0
		while True:
			for team in teams:
				if team.code == unique_id:
					unique_id = get_random_string(length=6)
				if team == teams.last():
					flag = 1
			if flag:
				break
		form = create_teamForm(request.POST)
		if form.is_valid():
			for team in teams:
				if form.instance.team_name == team.team_name:
					messages.add_message(request, messages.INFO, f'Team Name already Exist.')
					return redirect('dashboard')
			form.instance.code = unique_id
			x = form.save()
			user.team = x
			user.save()
	return redirect('dashboard')

def join_team(request):
		return redirect('dashboard')
		teams = Team.objects.all()
		user = request.user
		users = User.objects.all()
		if request.method == 'POST':
			form = join_teamForm(request.POST)
			if form.is_valid():
				input_code = form.instance.code
				for team in teams:
					if team.code == input_code:
						count = 0
						for u in users:
							if u.team == team:
								count += 1
								if count == 5:
									messages.add_message(request, messages.INFO, f'Team already Full.')
									return redirect('dashboard')
						user.team = team
						user.save()
						messages.add_message(request, messages.INFO, f'You have sucessfully joined this team.')
						return redirect('dashboard')
				messages.add_message(request, messages.INFO, f'Wrong Code.')
			return redirect('dashboard')

def leave_team(request):
	return redirect('dashboard')
	user = request.user
	user.team = None
	user.position = None
	user.save()
	return redirect('dashboard')

def submit_ppt(request, pk):
	team = Team.objects.filter(id=pk).first()
	team_members = User.objects.filter(team = request.user.team)
	if request.method == 'POST':
		form = SubmitForm(request.POST, request.FILES)
		if form.is_valid():
			team.presentation = form.instance.presentation
			team.save()
			messages.add_message(request, messages.INFO, f'Submission Successful')
			return redirect('dashboard')
	else:
		form = SubmitForm()
	context = {
		'form' : form,
		'team_members' : team_members
	}
	return render(request, 'user/dashboard.html', context)