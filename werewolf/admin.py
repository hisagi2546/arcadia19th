from django.contrib import admin
from .models import Choice, Question, Village, Remark, Resident

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}),('Date information', {'fields':['pub_date']}),]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class RemarkInline(admin.TabularInline):
    model = Remark
    extra = 0
    max_num = 100
    show_change_link = True

class RemarkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['village']}),
        (None, {'fields':['serial_no']}),
        (None, {'fields':['days']}),
        (None, {'fields':['types']}),
        (None, {'fields':['user']}),
        (None, {'fields':['charaset']}),
        (None, {'fields':['character']}),
        (None, {'fields':['character_img_url']}),
        (None, {'fields':['date']}),
        (None, {'fields':['text']}),
    ]
    list_display = ('text', 'id', 'village', 'user_id', 'serial_no', 'days', 'types', 'user', 'character', 'charaset', 'character_img_url', 'date',)
    list_filter = ['village', 'user_id', 'days', 'types', 'user','charaset', 'character', 'date',]
    search_fields = ['text',]

class ResidentInline(admin.TabularInline):
    model = Resident
    extra = 0
    show_change_link = True

class ResidentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['village']}),
        (None, {'fields':['resident']}),
        (None, {'fields':['character']}),
        (None, {'fields':['character_img_url']}),
        (None, {'fields':['position']}),
        (None, {'fields':['death_flag']}),
    ]
    list_display = ('resident','village','character','character_img_url','position','death_flag','id',)

class VillageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['name']}),
        (None, {'fields':['auther']}),
        (None, {'fields':['character']}),
        (None, {'fields':['character_name']}),
        (None, {'fields':['character_img_url']}),
        (None, {'fields':['created_date']}),
        (None, {'fields':['palflag']}),
        (None, {'fields':['endflag']}),
        (None, {'fields':['delflag']}),
    ]
    inlines = [ResidentInline, RemarkInline]
    list_display = ('name','id','auther','character','character_name','created_date','palflag','endflag','delflag',)
    list_filter = ['created_date','auther','character','character_name','created_date','palflag','endflag','delflag',]
    search_fields = ['name','auther',]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Village, VillageAdmin)
admin.site.register(Remark, RemarkAdmin)
admin.site.register(Resident, ResidentAdmin)
