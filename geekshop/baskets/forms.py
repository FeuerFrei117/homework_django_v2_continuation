from django.views.generic.edit import CreateView

from baskets.models import Basket


class BasketCreateForm(CreateView):
    Meta = Basket
    fields = ('user', 'product', 'quantity')
