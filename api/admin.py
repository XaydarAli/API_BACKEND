
from django.contrib import admin
from .models import   Advisor,Author,Blog,Review,Service
from import_export.admin import ImportExportModelAdmin


@admin.register(Advisor)
class AdvisorAdmin(ImportExportModelAdmin):
    list_display = ("id","name","expertise","contact_info")
    list_display_links = ("name","contact_info")
    search_fields = ("name","slug")
    ordering = ("id",)

@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("id","nickname","slug","bio","profile_views")
    list_display_links = ("id","nickname","slug","bio")
    search_fields = ("nickname", "slug")
    search_fields = ("nickname", "slug")
    prepopulated_fields = {'slug': ('nickname',)}




@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin):
    list_display = ("id","title","content",'slug')
    list_display_links = ("title",'content')
    search_fields = ("slug","title")
    ordering = ("id",)


@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    list_display = ("id","name","description","price")
    list_display_links = ("name","price")
    search_fields = ("slug","name")
    ordering = ("price",)





@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = ("id","comment","rating","likes")
    list_display_links = ("comment","id")
    search_fields = ("slug","id")
    ordering = ("likes",)