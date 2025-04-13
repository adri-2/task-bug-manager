from .models import Category, BugReport, BugAssignment,Tags
from django import forms

class CategoryForm(forms.ModelForm):
    
    """FORMNAME definition."""
    class Meta:
        model = Category
        fields = ('title','type','description')       
    
    
    # TODO: Define form fields here


class BugReportForm(forms.ModelForm):
    """BugReportForm definition."""
    class Meta:
        model = BugReport
        fields = ('titre','description','type_bug','rapporteur_employee','rapporteur_client','statut','priorite','category')

    # TODO: Define form fields here
    
class AssignationBugForm(forms.ModelForm):
    """AssignationBugForm definition."""
    class Meta:
        model = BugAssignment
        fields = ('bug','assigneur','assigne_a')

    # TODO: Define form fields here
    
class TagForm(forms.Form):
    """TagForm definition."""
    class Meta:
        model = Tags
        fields = ('title')

    # TODO: Define form fields here
    
    

