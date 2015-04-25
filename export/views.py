from django.shortcuts import render
from django.template.loader import render_to_string

from django.http import HttpResponse

from django.conf import settings

from persons.models import Role, Right, Department, Person

from math import floor
import os
from subprocess import Popen, PIPE

import tempfile

# Create your views here.

def _render_tex(texcode):
    with tempfile.TemporaryDirectory(dir=os.path.join(settings.BASE_DIR, 'tex')) as tempdir:
        # Create subprocess, supress output with PIPE and 
        # run latex twice to generate the TOC properly. 
        # Finally read the generated pdf.
        env = os.environ.copy()
        #env["TEXINPUTS"] = env["TEXINPUTS"]+":"+os.path.join(settings.BASE_DIR, 'media')
        for i in range(1):
            process = Popen(
                ['pdflatex', '-output-directory', tempdir, '-halt-on-error'],
                stdin=PIPE,
                stdout=PIPE,
                stderr=PIPE,
                env=env,
            )
            out, err = process.communicate(bytes(texcode, 'UTF-8'))
            if process.returncode:
                return HttpResponse(err.decode('UTF-8')+'\n\n\n'+out.decode('UTF-8')+'\n\n\n'+texcode)
        with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as f:
            pdf = f.read()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="{}"'.format("badges.pdf")
    response.write(pdf)

    return response

def _make_side(x,y,person,template):
    render_to_string("export/tex/front.tex",{'x':"felix"})

def _make_sheet(front,back):
    """
    Arranges a double sided sheet
    Args:
        front: plain tikz commands for front sides
        back: plain tikz commands for back sides
    Returns:
        String of self contained TeX commands
    """
    sheet=""
    
    sheet+="\\centering\\begin{tikzpicture}[font=\\sffamily]\n"
    sheet+=front
    sheet+="\\end{tikzpicture}\n"
    sheet+="\\newpage\n"
    
    sheet+="\\centering\\begin{tikzpicture}[font=\\sffamily]\n"
    sheet+=back
    sheet+="\\end{tikzpicture}\n"
    sheet+="\\newpage\n"
    
    return sheet
    
def texit(persons):
    
    for p in persons:
        p.printed = True;
        p.save()
        r=set(p.extra_rights.all())
        r=r|set(p.department.rights.all())
        if(p.role):
            r=r|set(p.role.rights.all())
        rslug=[]
        for ro in list(r):
            rslug.append(ro.slug)
        print(rslug)
        p.calc_rights=list(rslug)
    
    #sheet layout in cm
    badge_height=6
    badge_width=9.5
    #count of badges
    badge_rows=4
    badge_cols=2
    
    document=""

    evenpage=""
    oddpage=""

    for idx,person in enumerate(persons):
        evenpage+=render_to_string("export/tex/front.tex",{'x':(idx%badge_cols)*badge_width,'y':floor((idx%(badge_cols*badge_rows))/badge_cols)*badge_height,'person':person})
        oddpage+=render_to_string("export/tex/back.tex",{'x':badge_width-(idx%badge_cols)*badge_width,'y':floor((idx%(badge_cols*badge_rows))/badge_cols)*badge_height,'person':person})
    
        if idx%(badge_cols*badge_rows)==7:
            document+=_make_sheet(evenpage,oddpage)
        
            evenpage=""
            oddpage=""

    if evenpage!="":
        document+=_make_sheet(evenpage,oddpage)
      
    #return document
    
    
    return _render_tex(render_to_string("export/tex/wrapper.tex", {'content':document}))

def index(request):
    
    if request.method == 'POST':
        
        persons = Person.objects.filter(id__in=request.POST.getlist('print')).order_by("department")
        
        return texit(persons)
    
    else:
        
        persons = Person.objects.order_by("department")

        for p in persons:
            r=set(p.extra_rights.all())
            r=r|set(p.department.rights.all())
            if(p.role):
                r=r|set(p.role.rights.all())
            p.calc_rights=list(r)
    
        return render(request, "export/index.html", {'person':persons})

def update(request):
    
    if request.method == 'POST':
        
        persons = Person.objects.filter(id__in=request.POST.getlist('print')).order_by("department")
        
        return texit(persons)
    
    else:
        
        persons = Person.objects.order_by("department")

        for p in persons:
            r=set(p.extra_rights.all())
            r=r|set(p.department.rights.all())
            if(p.role):
                r=r|set(p.role.rights.all())
            p.calc_rights=list(r)
    
        return render(request, "export/updates.html", {'person':persons})

def dep(request):
    
    if request.method == 'POST':
        
        persons = Person.objects.filter(id__in=request.POST.getlist('print')).order_by("department")
        
        #print(persons)
        #print(request.GET['id'])
        
        return texit(persons)
        #return render(request, "export/departments.html", {'departments':None})
    else:
        
        departments = Department.objects.order_by("name")
        
        for d in departments:
            d.persons = Person.objects.filter(department=d)
            for p in d.persons:
                r=set(p.extra_rights.all())
                r=r|set(p.department.rights.all())
                if(p.role):
                    r=r|set(p.role.rights.all())
                p.calc_rights=list(r)
    
        return render(request, "export/departments.html", {'departments':departments})

