=======================
hugon (Hugo + Python)
=======================
.. image:: https://raw.githubusercontent.com/hithismani/hugon/master/sample/header.jpg
    :alt: Hugon Header Image
    
.. image:: https://img.shields.io/pypi/v/hugon.svg
    :target: https://pypi.python.org/pypi/hugon

An incredibly simple (CLI) python script that makes working with archetypes in Hugo 0.5x much easier. Also automates the process of bulk file creation via a single .csv!

Read `my medium post`_ for a quick idea of what this package does.

.. _`my medium post`: https://medium.com/@helloitsmani/trying-to-speed-up-your-hugo-workflow-with-python-try-hugon-13e81cc32571

.. image:: https://raw.githubusercontent.com/hithismani/hugon/master/sample/hugon-single-file.gif
    :alt: Hugon Sample Run

* Free software: MIT license

Why
----


* When working with archetypes, the CLI expects us to mention the exact file name we want to create, instead of converting a provided string into a valid file name. 
* Inability to create a sequence of files (Example, creating an FAQ’s Markdown Page with faq-1.md, faq-2.md, faq-3.md file names). We’re expected to enter them manually each time. 
* When working with projects that require us to create multiple markdown files, we can’t add more than the "title" field to our markdown files. 


Features 
--------

* Enter a string with as many special characters, watcht them be converted into a suitable file name. 

    Eg: "This new blog post I want to write!" in the command line would convert into "this-new-blog-post-i-want-to-write.md". 

* Enter the archetype you wish to enter, the script will check if the archetype exists. If it doesn’t exist, Hugo CLI will prompt you with an error. 
* Create multiple markdown files and automatically populate the variables + content fields from a local CSV! (YAML format front matter only) 
* (NEW) Lets you download files from a link into a specific path within your project and aassign the values into your .md file! (CSV Only)
* Lets you use a custom prefix CLI if you’re using any other CLI that handshakes with hugo. Only changes prefix that could replace the "hugo new" function 
* Enter the amount of files you want to create in sequence, the script will create everything.  
* Lets you use a custom separator if you’d like something apart from ‘-‘ hyphens in your file name. 
* Colour codes the output (ft. colorama) for you to differentiate between outputs.


Requirements
------------
* Python 3.x
* Hugo CLI (Tested on 0.59.1)
* Archetype file within your project root/theme archetype folder.

How To Use (Normal)
-------------------

1. Install Hugon::

    pip install hugon

2) cd Into your hugo project folder.
3) run the command::

    hugon -name "N3w F!le" -archetype "default" -sequence "5"

 

Syntax (Normal)
---------------
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------+------------------------------------------------+
| Command    | Description                                                                                                                                                                                                                       | Required? | Example           | Converts Into                                  |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------+------------------------------------------------+
| -archetype | Define Archetype Name (without file extension). The Archetype file of this name should be present in the archetype folder. (Name is automatically converted to lowercase)                                                         | Yes       | Default           | default                                        |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------+------------------------------------------------+
| -name      | Filename you'd want to set. Can contain spaces, numbers, special characters, all which will be stripped (and converted to lowercase) to create a seamless file name to send to Hugo CLI.                                          | Yes       | FILE NAM3 Ex@mple | file-nam3-exmple.md                            |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------+------------------------------------------------+
| -sequence  | Lets you create multiple files with a 'sequence' as a postfix. Helpful if you're working with FAQ's, or other pages where file name doesn't necessarily matter. Value has to be more than 1, with sequence kicking off skipping 0.| No        | 5                 | file-nam3-exmple1.md                           |
|            |                                                                                                                                                                                                                                   |           |                   +------------------------------------------------+
|            |                                                                                                                                                                                                                                   |           |                   | file-nam3-exmple2.md                           |
|            |                                                                                                                                                                                                                                   |           |                   +------------------------------------------------+
|            |                                                                                                                                                                                                                                   |           |                   | file-nam3-exmple3.md                           |
|            |                                                                                                                                                                                                                                   |           |                   +------------------------------------------------+
|            |                                                                                                                                                                                                                                   |           |                   | file-nam3-exmple4.md                           |
|            |                                                                                                                                                                                                                                   |           |                   +------------------------------------------------+
|            |                                                                                                                                                                                                                                   |           |                   | file-nam3-exmple5.md                           |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------+------------------------------------------------+
| -separator | Lets you define a custom separator that's not "-" a hyphen.                                                                                                                                                                       | No        | _                 | file_nam3_example.md                           |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------+------------------------------------------------+
| -prefix    | Use another command instead of "hugo new".                                                                                                                                                                                        | No        | npm run customdev | npm run customdev default/file_nam3_example.md |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------+------------------------------------------------+


How To Use (Generate From CSV)
-------------------------------
1) Create a 'data.csv' file in the root of your hugo site.
2) Enter all the required variable fields (along with the required compulsory fields) as columns on your first row, and populate to your hearts content.
3) Run command::

    hugon -csv yes
4) If you'd like to overwrite your files without being prompted (Risky) just pass '-overwrite true' as an argument.::

    hugon -csv yes -overwrite true

Syntax (CSV)
------------

.. image:: https://raw.githubusercontent.com/hithismani/hugon/master/sample/hugon-csv.gif
    :alt: Hugon Sample Run | CSV

Warning: Files would be modified the moment they're made. Mistakes cannot be undone.

+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Column Name | Required | Purpose                                                                                                                                                                           |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| archetype   | Yes      | States archetype of post to be made.                                                                                                                                              |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| content     | No       | Lets you add matter to the "content" section of your markdown file.                                                                                                               |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| filename    | No       | Lets you specify another filename if you don't want to use a 'sluggified' title. Please ensure you don't add '.md' to the filename and your file name has the proper separators.  |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| title       | Yes      | Title field/filename.                                                                                                                                                             |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| da-<key>    | No       | Download Anchorlink column that lets the script know that the value of the field is a download link. Must be followed by the key it assigns to. Eg: 'da-image'. Single use only.  |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| path        | No(?)    | (Required if 'da-' is specified) Lets the script set the download location of the file specified above. Creates the folder if it doesn't exist.                                   |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| prefix      | No       | Any custom build command you'd like to specify.                                                                                                                                   |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| separator   | No       | Any custom separator (if you're generating from title column) apart from default '-'.                                                                                             |
+-------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

* Looking to add tags/taxonomies? Separate your values in the column with a "^;" 
* Looking to values to your YAML without quotation marks? (Eg: true/false values) Prepend your value with "^" 
* Need line breaks within your 'content' cell? Specify them with a '\n' 
* If you're using the "path" key, note that the script would add the path into your front matter by ommiting the first folder. Eg: "static/img/ex.jpg" would be inserted as "img/ex". If you'd like to retain the parent folder name in front matter, just add "?" to the beginning of the value in your CSV path field.
* View `sample CSV attached within this repository`_ for more information.
* Note: 
    * Remember to remove any whitespace around your cell headings and values.
    * If the script doesn't work as expected, please check your archetype keys for typos/spaces as well.

.. _`sample CSV attached within this repository`: https://github.com/hithismani/hugon/blob/master/sample/data.csv


TO DO
------

* Adding option to input values from CSV. (Done!)
* Adding option to get image/file from a URL and downloading it straight into a specified folder. CSV Only. (Done!)
* Adding option to expand download functionality to allow for download of multiple files.
* TOML format support.
* Fixing typos and grammatical errors in code + this readme doc. (Never ending :( )

Credits 
------- 

* Color support via Colarama.
* This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template. 

.. _Cookiecutter: https://github.com/audreyr/cookiecutter 
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage 