from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from forms import UserForm, UserProfForm, postmodelform, UpdateProfile
from models import postmodel, CustomUser
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def index(request):
	context_instance = RequestContext(request)
	
	return render_to_response("main/index.html", {}, context_instance)
		

def search(request):
	context_instance = RequestContext(request)
	query_string = ''
	found_entries = None
	print "am just a normal search"
	if ("search_key" in request.GET) and request.GET['search_key'].strip():
			query_string = request.GET['search_key']
			found_entries = postmodel.objects.filter(property_location__icontains=query_string)
	if found_entries == None:
		return HttpResponseRedirect("/main/index/")
	paginator = Paginator(found_entries, 4)
	page = request.GET.get("page")
	try:
		results = paginator.page(page)
	except PageNotAnInteger:
		#deliver first page if page not not integer
		results = paginator.page(paginator.num_pages)
	
	except EmptyPage:
		#if page out of range deliver last page
		results = paginator.page(paginator.num_pages)
	return render(request, "main/search.html",{ 'results':results}, context_instance)





def advanced_search(request):
	context_instance = RequestContext(request)
	found_entries = None
	print "hellow there an advanced"
	if ("search_key" in request.GET) and request.GET['search_key'].strip():
			one =""
			two = (0, 1000)
			three = (1001, 3500)
			four = (3501, 7000)
			five =(7001, 11000)
			six = (11001, 20000)
			seven = (20001, 30000)
			eight = (30001, 100000)
			
			
			
			
			query_string = request.GET['search_key']
			agent = request.GET["agent"]
			area = request.GET["area"]
			typ = request.GET["typ"]
			found_entries = None
			found_entries = postmodel.objects.filter(property_location__icontains=query_string)
			if len(typ) > 0:
				found_entries = found_entries.filter(property_type__iexact=typ)
			if len(area) > 0:
				found_entries = found_entries.filter(area__icontains=area)
			if len(agent) > 0:
				found_entries = found_entries.filter(owner__username__iexact=agent)
	if found_entries == None:
		return HttpResponseRedirect("/main/search/")
	paginator = Paginator(found_entries, 5)
	page = request.GET.get("page")
	try:
		results = paginator.page(page)
	except PageNotAnInteger:
		#deliver first page if page not not integer
		results = paginator.page(paginator.num_pages)
	
	except EmptyPage:
		#if page out of range deliver last page
		results = paginator.page(paginator.num_pages)
	return render(request, "main/advanced_search.html",{ 'results':results}, context_instance)



	
def profile(request):
	email = request.GET.get("email")
	telephone = request.GET.get("tell")
	user = CustomUser.objects.filter(Q(email__iexact=email) | Q(telephone__iexact=tellphone) )
	context_instance = RequestContext(request)
	return render(request, "main/profile.html",{ 'user':user}, context_instance)
	
	

'''@login_required
def edit_user(request):
	if "_auth_user_id" in request.session:
		userId = request.session["_auth_user_id"]
		userDetails = CustomUser.objects.get(pk=userId)
		if request.method == "POST":
			userDetails.first_name = request.POST["first_name"]
			userDetails.last_name = request.POST["last_name"]
			userDetails.email = request.POST["email"]
			userDetails.username = request.POST["username"]
			
			userDetails.save()
	template_var["new_profile_user"] = '''
		
@login_required
def home(request):
	context_instance = RequestContext(request)
	category_list = postmodel.objects.filter(owner_id=request.user.id)
	

	paginator = Paginator(category_list, 4)
	page = request.GET.get("page")
	try:
		results = paginator.page(page)
	except PageNotAnInteger:
		#deliver first page if page not not integer
		results = paginator.page(paginator.num_pages)
	
	except EmptyPage:
		#if page out of range deliver last page
		results = paginator.page(paginator.num_pages)

	return render(request, "main/home.html",{ 'categories':results}, context_instance)



@login_required
def add_todo(request):

	context = RequestContext(request)
	if request.method == 'POST':
		form = postmodelform(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.owner = request.user
			profile.save()
			return home(request)


		else:
			print form.errors
	else:
		form = postmodelform()

	return render_to_response(
			"main/post.html",
			{"form": form}, context)
@login_required
def log_out(request):
	logout(request)
	return HttpResponseRedirect("/main/index/")

def register(request):
	context = RequestContext(request)
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		#prof_form = UserProfForm(data=request.POST)
		#validate form data
		if user_form.is_valid():# and prof_form.is_valid():
			user = user_form.save() #save the user form data to the database
			user.set_password(user.password)#hash the password
			if 'picture' in request.FILES:
				user.picture = request.FILES['picture']
			#profile.save() # save the user_prof instance
			user.save()
			registered = True #update the variable
			return HttpResponseRedirect("/main/signup_login/")
		else:
			print user_form.errors

	else:
		user_form = UserForm()
	return render_to_response(
			"registration/register.html",
			{"user_form": user_form, "registered":registered}, context)


def signup_login(request):    
	context = RequestContext(request)    
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(email=email, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/main/fin_register/')
			else:               
				return HttpResponse("You must first login")
		else: 
			print "Invalid login details: {0}, {1}".format(email, password)
			return render(request, "registration/invalid.html")
	return render_to_response('registration/login.html', {}, context)

	
@login_required
def fin_register(request):
	context = RequestContext(request)
	registered = False
	
	if request.method == 'POST':
		prof_form = UserProfForm(data=request.POST)
		#validate form data
		if prof_form.is_valid():
			profile = prof_form.save(commit=False)
			#save  the picture if provided'''
			if 'picture' in request.FILES:
				user.picture = request.FILES['picture']
			profile.save() # save the user_prof instance
			return HttpResponseRedirect("/main/home/")
		else:
			print prof_form.errors

	else:
		prof_form =UserProfForm()
	return render_to_response(
			"registration/fin_register.html",
			{"prof_form":prof_form, "registered":registered}, context)




def user_login(request):    
	context = RequestContext(request)    
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=email, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/main/home')
			else:               
				return HttpResponse("You must first login")
		else: 
			print "Invalid login details: {0}, {1}".format(email, password)
			return render(request, "registration/invalid.html")
	return render_to_response('registration/login.html', {}, context)

def about(request):
	return render(request, "registration/about.html")


def help(request):
	return render(request, "registration/help.html")


