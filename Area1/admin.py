from django.contrib import admin
from .models import Prof,Review



class ReviewAdmin(admin.ModelAdmin):
	list_display = ('prof','name','body','posted_on','active')
	list_filter = ('active','posted_on')
	search_fields = ('name','body')
	actions = ['approve_review']


	def approve_review(self,request,queryset):
		queryset.update(active=True)




admin.site.register(Prof)

admin.site.register(Review,ReviewAdmin)
