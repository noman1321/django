# # listings/views.py
# from django.shortcuts import render, redirect
# from .model import Business
# from .form import BusinessForm
# from django.db.models import Q

# def business_list(request):
#     businesses = Business.objects.all()
#     query = request.GET.get('q')
#     if query:
#         businesses = businesses.filter(Q(name__icontains=query) | Q(city__icontains=query) | Q(country__icontains=query))
#     return render(request, 'listings/business_list.html', {'businesses': businesses})

# def add_business(request):
#     if request.method == "POST":
#         form = BusinessForm(request.POST)
#         if form.is_valid():
#             business = form.save(commit=False)
#             business.owner = request.user
#             business.save()
#             return redirect('business_list')
#     else:
#         form = BusinessForm()
#     return render(request, 'listings/add_business.html', {'form': form})


from django.shortcuts import render

def business_list(request):
    # Sample data to display (this would normally come from a database)
    businesses = [
        {'name': 'Business One', 'description': 'Description of Business One'},
        {'name': 'Business Two', 'description': 'Description of Business Two'},
    ]
    return render(request, 'listings/business_list.html', {'businesses': businesses})

def add_business(request):
    # Render a page for adding a new business
    return render(request, 'listings/add_business.html')
