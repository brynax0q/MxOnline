# -*- coding:utf-8 -*-
__author__ = 'brynao'
__date__ = '2017/7/27 上午11:54'

import xadmin
from .models import Course, Lesson, Video, CourseResource, BannerCourse
from organization.models import CourseOrg

# 嵌套， 课程中增加章节 方便添加数据
class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name','desc', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time', 'get_zj_nums', 'got_to']
    search_fields = ['name','desc', 'degree', 'students', 'fav_nums', 'click_nums']
    list_filter = ['name','desc', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']
    # 排序
    ordering = ['-click_nums']
    # 只读数据
    readonly_fields = ['click_nums', 'fav_nums', 'students']
    # 不显示数据 和 只读冲突
    #exclude = ['click_nums', 'fav_nums', 'students']
    # 嵌套章节和资源
    inlines = [LessonInline, CourseResourceInline]
    # 在列表页可直接修改
    list_editable = ['degree', 'desc']
    # 每几秒刷新一次 3到5秒可选
    #refresh_times = [3, 5]

    # 指明样式
    style_fields = {"detail": "ueditor"}
    import_excel = True


    # 对表中数据进行过滤
    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        #在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.courses_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    # 导入excel
    # def post(self, request, *args, **kwargs):
    #     if 'excel' in request.FILES:
    #         pass
    #     return super(CourseAdmin, self).post(request, args, kwargs)


class BannerCourseAdmin(object):
    list_display = ['name','desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    search_fields = ['name','desc', 'detail', 'degree', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name','desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    # 排序
    ordering = ['-click_nums']
    # 只读数据
    readonly_fields = ['click_nums', 'fav_nums', 'students']
    # 嵌套章节和资源
    inlines = [LessonInline, CourseResourceInline]

    # 对表中数据进行过滤
    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields =['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields =['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']  # 显示字段
    search_fields = ['course', 'name', 'download']  # 搜索功能
    list_filter = ['course', 'name', 'download', 'add_time']  # 过滤器

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)