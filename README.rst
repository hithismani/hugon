=====
hugon
=====


.. image:: https://img.shields.io/pypi/v/hugon.svg
        :target: https://pypi.python.org/pypi/hugon


An incredibly simple python script that makes working with archetypes in Hugo 0.5x much easier.

* Free software: MIT license

Why
----
* When working with archetypes, the CLI expects us to mention the exact file name we want to create, instead of converting simply converting a provided string into a filename.
* Inability to create a sequence of files (Example, creating an FAQ's Markdown Page with faq-1.md, faq-2.md, faq-3.md file names). We're expected to enter them manually each time.
* When working with projects that require us to create multiple markdown files, we can't add more than the "title" field to our markdown files.

Features
--------

* Enter a string with as many special characters you wish to enter, the script will conver it into a suitable filename. Eg: "This new blog post I want to write!" in the command line would be converted into "this-new-blog-post-i-want-to-write.md".
* Enter the archetype you wish to enter, the script will check if the archetype exists. If it doesn't exist, Hugo CLI will prompt you with an error.
* Create multiple markdown files, and automatically populate the variables + content fields from a local CSV! (YAML format front matter only)
* Let's you use a custom prefix CLI if you're using any other CLI that handshakes with hugo. Only changes prefix that could replace the "hugo new" function
* Enter the amount of files you want to create in sequence, the script will create everything.
* Colour codes the output (uses Colorama!) for you to differenciate between outputs.
* Let's you use a custom separator if you'd like something apart from '-' hyphens in your file name.

Requirements
------------
* Python 3.x
* Hugo CLI (Tested on 0.59.1)

How To Use (Normal)
-------------------
1) pip install hugon
2) cd Into your hugo initialized folder.
3) run the command 'hugon -name "N3w F!le" -arch "default" -sequence "5"

Syntax (Normal)
---------------
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------+------------------------------------------------+
| Command    | Description                                                                                                                                                                                                                       | Required? | Example           | Converts Into                                  |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------+------------------------------------------------+
| -archetype | Define Archetype Name (without file extension). The Archetype file of this name should be present in the archetype folder. (Name is automatically converted to lowercase)                                                         | Yes       | Default           | default                                        |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------+------------------------------------------------+
| -name      | Filename you'd want to set. Can contain spaces, numbers, special characters, all which will be stripped (and converted to lowercase) to create a seamless file name to send to Hugo CLI.                                          | Yes       | FILE NAM3 Ex@mple | file-nam3-exmple.md                            |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------+------------------------------------------------+
| -sequence  | Let's you create multiple files with a sequence as a postfix. Helpful of you're working with FAQ's, or other pages where file name doesn't necessarily matter. Value has to be more than 1, with sequence kicking off skipping 0. | No        | 5                 | file-nam3-exmple1.md                           |
|            |                                                                                                                                                                                                                                   |           |                   +------------------------------------------------+
|            |                                                                                                                                                                                                                                   |           |                   | file-nam3-exmple2.md                           |
|            |                                                                                                                                                                                                                                   |           |                   +------------------------------------------------+
|            |                                                                                                                                                                                                                                   |           |                   | file-nam3-exmple3.md                           |
|            |                                                                                                                                                                                                                                   |           |                   +------------------------------------------------+
|            |                                                                                                                                                                                                                                   |           |                   | file-nam3-exmple4.md                           |
|            |                                                                                                                                                                                                                                   |           |                   +------------------------------------------------+
|            |                                                                                                                                                                                                                                   |           |                   | file-nam3-exmple5.md                           |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------+------------------------------------------------+
| -separator | Let's you define a custom separatorthat's not "-" a hyphen.                                                                                                                                                                       | No        | _                 | file_nam3_example.md                           |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------+------------------------------------------------+
| -prefix    | Use another command instead of "hugo new".                                                                                                                                                                                        | No        | npm run customdev | npm run customdev default/file_nam3_example.md |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------+------------------------------------------------+


How To Use (Generate From CSV)
-------------------------------
1) Create a 'data.csv' file in the root of your hugo site.
2) Enter all the required variable fields (along with the required compulsory fields) as columns on your first row, and populate to your hearts content.
3) Run command 'hugon -csv yes'

Syntax (CSV)
------------

+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Column Name | Required | Purpose                                                                                                                                                                           |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| archetype   | Yes      | States archetype of post to be made.                                                                                                                                              |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| content     | No       | Let's you add matter to the "content" section of your markdown file.                                                                                                              |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| filename    | No       | Let's you specify another filename if you don't want to use a 'sluggified' title. Please ensure you don't add '.md' to the filename and your file name has the proper separators. |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| title       | Yes      | Title field/filename.                                                                                                                                                             |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| prefix      | No       | Any custom build command you'd like to specify.                                                                                                                                   |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| separator   | No       | Any custom separator (if you're generating from title column) apart from default '-'                                                                                              |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

* Looking to add tags/taxonomies? Separate your values in the column with a *^;*
* Looking to values to your YAML without quotation marks? (Eg: true/false values) Prepend your value with *^*



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
