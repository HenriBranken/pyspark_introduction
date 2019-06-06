# Spark and Python for Big Data with PySpark.

Sections 1 of 6 of the course are not detailed in this GitHub repository as they cover setting up Python with Spark as well as a high-level introduction to the course.

**I strongly recommend following "Section 3:  Local VirtualBox Set-up" if you are running Windows/Mac.**

In case your computer runs a Linux distrobution (like mine), I recommend the following steps:
- Install anaconda on your computer.
- Then from your terminal, execute the following.
  - ```conda update conda```
  - ```conda update --all```
  - ```conda install pyspark```
- Install Java 8 and set it as your default (NOT Java 11).
  - ```sudo ap install openjdk-8-jdk```
  - ```sudo apdate-alternatives --config java```
  - Select ```Java 8```, and then confirm your changes:
  - ```java -version```
  - The above was grabbed from https://stackoverflow.com/questions/53583199/pyspark-error-unsupported-class-file-major-version-55

Sections 7 up until 17 are chronologically laid in in the course_walkthrough folder.  Here are the links to quickly jump to the section of interest:
- [Python Crash Course](https://github.com/HenriBranken/spark_and_python_for_big_data_with_pyspark/tree/master/course_walkthrough/section_07__python_crash_course)

Each sub-folder under ```course_walkthrough``` is a standalone section complete with all the notebooks, slides, and data files you will need to complete the section.  Additionally, the instructor's resources for the corresponding section are stored in the sub-folders named ```instructors_notebooks```.

It is recommended to complete the reading assignments as prompted by the instructor during his presentations, however it is not compulsory.

The ```.pdf``` file ```Introduction_to_Statistical_Learning__Gareth_James__2013.pdf```, under the ```course_walkthrough``` folder, contains all the contents for carrying out the reading assignments.

You will notice that my Python Notebooks contain verbose comments.  This feature will be more appreciated if, say, you review the material in this repo after a year from now.
The comments are there to help the learning experience and clarify the concepts underpinning the coding.

All the best when working through this material,
Henri.
