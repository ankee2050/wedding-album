def init_menu(request):
	
	context = {}
	menu = "<ul class='menu'>"
	
	if request.get_full_path() == '/':
		menu += "<li><a class='active' href='/'>About</a></li>"
	else:
		menu += "<li><a href='/'>About</a></li>"

	if request.get_full_path() == '/album':
		menu += "<li><a class='active' href='/album'>Album</a></li>"
	
	else:
		menu += "<li><a href='/album'>Album</a></li>"
	
	if request.get_full_path() == '/wedding':
		menu += "<li><a class='active' href='/wedding'>Wedding</a></li>"
	else:
		menu += "<li><a href='/wedding'>Wedding</a></li>"
	
	if request.get_full_path() == '/links':
		menu += "<li><a class='active' href='/links'>Links</a></li>"
	else:
		menu += "<li><a href='/links'>Links</a></li>"
	
	if request.get_full_path() == '/contacts':
		menu += "<li><a class='active' href='/contacts'>Contacts</a></li>"
	else:
		menu += "<li><a href='/contacts'>Contacts</a></li>"

	menu += '</ul>'
	context['menu'] = menu
	return context