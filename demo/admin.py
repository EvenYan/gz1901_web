from django.contrib import admin

# Register your models here.
from demo.models import Student, Grade


class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sex:
            return "男"
        return "女"
    gender.short_description = "性别"
    list_per_page = 2
    list_display = ['name', 'age', gender]
    list_filter = ("name", "age")
    search_fields = ("name", "age", "hobby")
    # fields = ("name",)
    fieldsets = (
        ("基本信息", {"fields": ("name", "age", "grade")}),
        ("更多信息", {"fields": ("hobby", "sex")}),
    )


class StudentInline(admin.TabularInline):
    model = Student
    extra = 5


class GradAdmin(admin.ModelAdmin):
    inlines = [StudentInline]


admin.site.register(Student, StudentAdmin)
admin.site.register(Grade, GradAdmin)