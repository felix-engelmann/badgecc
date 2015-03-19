# BadgeControlCenter

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

This is not directly TeX code, but will be parsed by the Django templating system. This means that you can make parts conditional and use the badge variables at any position. As some TeX commands as `\color{}` do not allow for whitespaces in their arguments, and `{{{` can not be parsed, there exists the custom filter `brackets` which adds `{` and `}` around your variable, so you can use it like `\color{{ person.department.color|brackets }}`

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

To import Persons, it accepts a really specifically formatted excel (.xlsx) sheet.

For successfully imported persons, images can be uploaded and will be suggested to the best  matching name, based on the filename. These suggestion can be checked by hand and, if necessary adapted before the import. 

### Manage

The manage section is currently only a dashboard to view all the data in the system. To alter values, please refer to the admin panel.

### Export

The export function is only a selection interface so choose which badges should be generated. On print it creates the PDF on the fly and returns it directly to the browser. In addition to this, every person printed is marked by the `printed` flag. This might be interesting, if persons are altered afterwards, the flag can be removed. Then there is an option to only print new or altered badges.

In the case of an LaTeX error, the log is returned.
