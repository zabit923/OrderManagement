from sqladmin import ModelView

from core.database.models import Order


class OrderAdmin(ModelView, model=Order):
    column_list = [
        Order.id,
        Order.status,
        Order.total_price,
    ]
    column_default_sort = [("created_at", True)]
    name = "Заказ"
    name_plural = "Заказы"
    icon = ""
