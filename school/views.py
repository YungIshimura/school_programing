from django.shortcuts import render
from .models import Course

def view_index(request):
    recomended_courses = Course.objects.filter(is_recomended=True)
    courses = []
    for recomended_course in recomended_courses:
        recomended_courses_for_main_page = {
            'id': recomended_course.id,
            'name': recomended_course.name,
            'short_description': recomended_course.short_description,
            'age_category': recomended_course.get_age_category_display(),
            'image': recomended_course.main_image.url
        }
        courses.append(recomended_courses_for_main_page)

    return render(request, 'school/index.html', context={'courses': courses})


def view_sign_in(request):
    return render(request, 'school/sign-in.html')


def view_registration(request):
    return render(request, 'school/registration.html')

def view_course_page(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'course': course
    }
    return render(request, 'school/course_page.html', context=context)