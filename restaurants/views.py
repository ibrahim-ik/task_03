from django.shortcuts import render

def welcome(request):
	return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

	context = {
		"my_list":
			[
				{
					"restaurant_name":"burgerhub",
					"food_type":"burgers",
				},
				{
					"restaurant_name":"pizzahub",
					"food_type":"pizzas",
				},
				{
					"restaurant_name":"pastahub",
					"food_type":"pastas",
				},
			]

		}
	return render(request, 'list.html', context)


def restaurant_detail(request):

	context = {
			"my_object":
				{
					"restaurant_name":"pastahub",
					"food_type":"pastas",
				}

	}
	return render(request, 'detail.html', context)
