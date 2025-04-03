from sqladmin import ModelView

from core.database.models import User


class UserAdmin(ModelView, model=User):
    column_list = [
        User.id,
        User.email,
    ]
    column_searchable_list = [User.email]
    column_default_sort = [("created_at", True)]
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
