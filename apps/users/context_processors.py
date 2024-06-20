from .models import Category

def user_categories(request):
    if request.user.is_authenticated:
        is_admin = 'admin' in request.user.categories.values_list('name', flat=True)
        categories = request.user.categories.all()
        return {
            'is_admin': is_admin,
            'user_categories': categories
        }
    return {}