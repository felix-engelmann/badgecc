## BadgeControlCenter

This Django application was written to facilitate the creation of badges for events. At it's core it follows a simple _import - manipulate - export_ workflow. 

## Install

As it is a standard Django application, it meant to run on a server and be accessed by clients via a browser. Because of the large file sizes of images and the final PDFs it is recommended to run server an client on the same machine, or at least within a high speed network (100Mbit)

### Requirements

To function properly, badgecc is dependent on multiple programs. The python (V. 3) related packages can be installed from the `requirements.txt` via `pip`

### LaTeX

Besides the python stuff, a working LaTeX installation is needed with `pdflatex` in your `PATH`

### Setup

To set up a the database, which is realised as a SQLite file, run

`python manage.py migrate`

In order to have access to the administration panel, you have to create a super user

`python manage.py createsuperuser`

You can either set up the application inside a web server as apache, nginx, ... or run it in development mode with the python built in server:

`python manage.py runserver`

## Usage

The data model is divided into 4 objects.

* **Right**: A right is an atomic value of a right a person can possess.
* **Role**: A role is an attribute which can be assigned to a person and probably adds some rights to all holders of this role.
* **Department**: A person belongs to a department. This sets properties of the badges, such as background image, default face, colour and rights for all members.
* **Person**: Finally a person has a first and last name and maybe an image or additional individual rights.

### Admin Interface

The default Django administration interface is available at /admin/ and serves as a complete editor for all properties. If something does not work in the front end, stuff can be fixed here.

### Configuration

The final badges are rendered by LaTeX as tikz drawings. The tikz commands are set in `export/templates/export/tex/front.tex` and `back.tex` respectively.

To place them on an A4 sheet, the offset in x and y direction has to match the drawing size. The parameters are set in `export/views.py`:

```
    #sheet layout in cm
    badge_height=6
    badge_width=9.5
    #count of badges
    badge_rows=4
    badge_cols=2
```

### Import

### Manage

### Export