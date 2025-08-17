from .models import SiteSetting
from products.models import Category

def site_settings(request):
    setting = SiteSetting.objects.first()
    banners = setting.banners.all() if setting else []
    return {'site_setting': setting,
            'banners': banners,
    }

def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}
