from django.contrib import admin
from .models import Activity_Period,Member

# Register your models here.
class Activity_Period_Admin(admin.ModelAdmin):
    list_display=["start_time","end_time"]
    
    class Meta:
        model = Activity_Period
admin.site.register(Activity_Period, Activity_Period_Admin)

class MemberAdmin(admin.ModelAdmin):
    list_display=["member_id","real_name","tz","get_activity_periods"]
    
    def get_activity_periods(self, obj):
        return ",".join([str(p.id) for p in obj.activity_periods.all()])
    
    class Meta:
        model = Member
admin.site.register(Member, MemberAdmin)