from django.views.generic import TemplateView

class ProductsPage(TemplateView):
    template_name = "products.html"
