from .base_dao import BaseDAO
from .models import Product

class ProductsDAO(BaseDAO):
    model = Product