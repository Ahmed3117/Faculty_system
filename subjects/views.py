from django.views.generic import DetailView , CreateView,UpdateView,DeleteView
from .models import Lecture, Subject
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
    fields = ['subject_name','lecture_name','description', 'file', 'video', 'assignment_content','assignment_end_time']
    success_url = reverse_lazy('accounts:subjects')
    # def form_valid(self, form):
    #     form.instance.subject_name = self.get_object().subject_name
    #     return super(LectureCreate, self).form_valid(form)
class LectureEdit(UpdateView):
    model = Lecture
    template_name = 'subjects/edit_lecture.html'
    fields =['lecture_name','description', 'file', 'video', 'assignment_content','assignment_end_time']
    success_url = reverse_lazy('accounts:subjects')
    
class LectureDelete(DeleteView):
    model = Lecture
    context_object_name = 'lecture'
    template_name = 'subjects/delete_lecture.html'
    success_url = reverse_lazy('accounts:subjects')