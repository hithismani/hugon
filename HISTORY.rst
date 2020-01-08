=======
History
=======

0.1.7 (2020-08-01)
------------------
- Fixed Functionality:
    - CSV would now "continue" to next row instead of earlier "break", if the values in the row are incorrect.
    - By default, path field in front matter would remove the first folder. (Eg: "static/img/ex.jpg" would be saved into the static folder, but inserted into front matter as "img/ex.jpg")
    - You can still retain parent folder in your front matter by adding "?" to the beginning of your path.
- Tiny fixes and performance improvements.

0.1.6 (2019-12-27)
------------------
- Added new functionality:
    - CSV now allows you to download a single file into your project folder. Specify 'da-' suffix in the key column, and mention the anchor link in your values field. Might not work with restricted URLs.
    - Above functionality works only when you have a 'path' column specified with the name of the folder the file should go into, within the root of your project. Does not currently support downloading multiple files related to a single page.
- Added sample CSV link to help understand the above functionality and others better.
- Fixed typos and grammatical errors within the code and readme file. Oops!
- Added comment entries to a few functions for easier readability.
- Homogenized the method used to combine folder paths, making the script function more predictably cross platform.
- Cleaned up the terminal, and added closing credits (script name) to show up after execution.
- Updated readme to make it easier to understand.
- Renamed "images" folder (in the github repository) to "sample".

0.1.5 (2019-12-26)
------------------
- Fixed bug that stopped you from specifying a file name with separators within the name.
- Updated display screenshot to reflect the above change.
- Added do-it-live.sh file for ease of screenshot creation. Not added the same into dependencies. 

0.1.4 (2019-12-13)
------------------

- Fixed bug that stopped you from specifying a sequence.
- Fixed content replacement (CSV) issue that duplicated the section instead of replacing it.
- Pushed non-hugo CLI messages to colorama function for easy readability.
- Added pretty 'horizontal line breaks' after any code is executed. (Resizes the next output to your existing terminal size).
- Other bug fixes and optimizations.

0.1.1 (2019-12-13)
------------------
- Added CSV support for dynamic YAML markdown file generation.

0.1.0 (2019-12-06)
------------------

- First release on PyPI.