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
	
	if request.get_full_path() == '/family':
		menu += "<li><a class='active' href='/links'>Family</a></li>"
	else:
		menu += "<li><a href='/family'>Family</a></li>"
	
	if request.get_full_path() == '/wishes':
		menu += "<li><a class='active' href='/wishes'>Wishes</a></li>"
	else:
		menu += "<li><a href='/wishes'>Wishes</a></li>"

	menu += '</ul>'
	context['menu'] = menu
	return context