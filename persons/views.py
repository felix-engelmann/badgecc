from django.shortcuts import render

from django.views import generic

from persons.models import Role, Right, Department, Person

# Create your views here.

def index(request):
    right = Right.objects.all()
    role = Role.objects.all()
    dep = Department.objects.all()
    pers = Person.objects.all()
    
    for p in pers:
        r=set(p.extra_rights.all())
        r=r|set(p.department.rights.all())
        if(p.role):
            r=r|set(p.role.rights.all())
        p.calc_rights=list(r)
    
    return render(request, "persons/index.html", {'right': right, 'role': role, 'department':dep, 'person': pers})

def detail(request, id):
    right = Right.objects.all()
    role = Role.objects.all()
    dep = Department.objects.all()
    pers = [Person.objects.get(id=id)]
    
    for p in pers:
        r=set(p.extra_rights.all())
        r=r|set(p.department.rights.all())
        if(p.role):
            r=r|set(p.role.rights.all())
        p.calc_rights=list(r)
    
    return render(request, "persons/index.html", {'right': right, 'role': role, 'department':dep, 'person': pers})
    
class IndexView(generic.ListView):
    #template_name = 'persons/index.html'
    #context_object_name = 'roles'

    def get_queryset(self):
        """Return the last five published questions."""
        return Role.objects.all()
