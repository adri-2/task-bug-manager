# from django.shortcuts import render
# from django.views.generic import ListView, FormView,DateDetailView,DeleteView,DetailView
# from .models import BugAssignment,Category,BugReport
# from .forms import CategoryForm,BugReportForm


# # Create your views here.

# # class CategoryView(FormView,ListView):

# class BugView(FormView,ListView):
#     model = BugReport
#     template_name = 'bug/main.html'
#     context_object_name = 'bug_listes'
#     form_class = BugReportForm
    
#     i_instance = None
    
#     def get_success_url(self):
#         return self.request.path
    
#     def form_valid(self, form):
#         # form = form.save()
#         self.i_instance = self.request.user
#         self.i_instance = form.save()
#         return super().form_valid(form)
    
    
    
    
