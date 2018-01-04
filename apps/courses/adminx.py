# _*_ encoding:utf-8 _*_

import xadmin

from .models import Course,CourseResource,Video,Lesson


class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','students','fav_nums','click_name','add_time']
    search_fields = ['name','desc','detail','degree','learn_times','students','fav_nums','click_name']
    list_filter = ['name','desc','detail','degree','learn_times','students','fav_nums','click_name','add_time']


class LessonAdmin(object):
    list_display = ['course','name','add_time','learn_times']
    search_fields = ['course','name','learn_times']
    list_filter = ['course__name','name','add_time','learn_times']


class VideoAdmin(object):
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['lesson','name','add_time']


class CourseResourceAdmin(object):
    list_display = ['course','name','add_time','down']
    search_fields = ['course','name','down']
    list_filter = ['course','name','add_time','down']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)