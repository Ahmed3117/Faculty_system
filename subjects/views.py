from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView,UpdateView,DeleteView
from .models import Branch, Department, Assignment, Grade, Lecture, Subject,Doctor
from django.urls import reverse_lazy
# get all subject list

class SubjectDetail(DetailView):
    
    model = Subject
    
    context_object_name = 'lectures'
    template_name = 'subjects/subject_lectures.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lectures"] = Lecture.objects.filter(subject_name=self.get_object().id)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['lectures'] = context['lectures'].filter(
                lecture_name__icontains=search_input
            )
        context['search_input'] = search_input
        return context

class LectureCreate(CreateView):
    model = Lecture
    template_name = 'subjects/create_lecture.html'
    fields = ['lecture_name','description', 'file', 'video', 'assignment_content','assignment_end_time']
    success_url = reverse_lazy('subjects:subjects')

class LectureEdit(UpdateView):
    model = Lecture
    template_name = 'subjects/edit_lecture.html'
    fields ='__all__'
    success_url = reverse_lazy('subjects:subjects')

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(LectureCreate, self).form_valid(form)
    
class LectureDelete(DeleteView):
    model = Lecture
    context_object_name = 'lecture'
    template_name = 'subjects/delete_lecture.html'
    success_url = reverse_lazy('subjects:subjects')