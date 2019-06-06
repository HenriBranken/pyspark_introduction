# Spark and Python for Big Data with PySpark.

The coding and material found in this repository is based of a [MOOC Course](https://www.udemy.com/spark-and-python-for-big-data-with-pyspark)

Sections 1 of 6 of the course are not detailed in this GitHub repository as they cover setting up Python with Spark as well as a high-level introduction to the course.

**I strongly recommend following "Section 3:  Local VirtualBox Set-up" if you are running Windows/Mac.**

On a side note, Section 5 of the course gives a quick walkthrough for a **Databricks Setup.**

In case your computer runs a Linux distribution (like mine), I recommend the following steps:
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
  - The above was grabbed from [this link](https://stackoverflow.com/questions/53583199/pyspark-error-unsupported-class-file-major-version-55)

Sections 7 up until 17 are chronologically laid in in the ```course_walkthrough``` folder.  Here are the links to quickly jump to the section of interest:
- [Section 7, Python Crash Course](https://github.com/HenriBranken/spark_and_python_for_big_data_with_pyspark/tree/master/course_walkthrough/section_07__python_crash_course)
- [Section 8, Spark DataFrame Basics](https://github.com/HenriBranken/spark_and_python_for_big_data_with_pyspark/tree/master/course_walkthrough/section_08__Spark_DataFrame_Basics)
- [Section 9, Spark DataFrame Project Exercise](https://github.com/HenriBranken/spark_and_python_for_big_data_with_pyspark/tree/master/course_walkthrough/section_09__Spark_DataFrame_Project_Exercise)
- [Section 10, Introduction to Machine Learning with MLlib](https://github.com/HenriBranken/spark_and_python_for_big_data_with_pyspark/tree/master/course_walkthrough/section_10__Introduction_to_Machine_Learning_with_MLlib)
- [Section 11, Linear Regression](https://github.com/HenriBranken/spark_and_python_for_big_data_with_pyspark/tree/master/course_walkthrough/section_11__Linear_Regression)
- [Section 12, Logistic Regression](https://github.com/HenriBranken/spark_and_python_for_big_data_with_pyspark/tree/master/course_walkthrough/section_12__Logistic_Regression)
- [Section 13, Decision Trees and Random Forests](https://github.com/HenriBranken/spark_and_python_for_big_data_with_pyspark/tree/master/course_walkthrough/section_13__Decision_Trees_and_Random_Forests)
- [Section 14, K-means Clustering](https://github.com/HenriBranken/spark_and_python_for_big_data_with_pyspark/tree/master/course_walkthrough/section_14__K-means_Clustering)
- [Section 15, Collaborative Filtering for Recommender Systems](https://github.com/HenriBranken/spark_and_python_for_big_data_with_pyspark/tree/master/course_walkthrough/section_15__Collaborative_Filtering_for_Recommender_Systems)
- [Section 16, Natural Language Processing](https://github.com/HenriBranken/spark_and_python_for_big_data_with_pyspark/tree/master/course_walkthrough/section_16__Natural_Language_Processing)
- [Section 17, Spark Streaming with Python](https://github.com/HenriBranken/spark_and_python_for_big_data_with_pyspark/tree/master/course_walkthrough/section_17__Spark_Streaming_with_Python)

Each sub-folder under ```course_walkthrough``` is a standalone section complete with all the notebooks, slides, and data files you will need to complete the section.  Additionally, the instructor's resources for the corresponding section are stored in the sub-folders named ```instructors_notebooks```.

It is recommended to complete the reading assignments as prompted by the instructor during his presentations, however it is not compulsory.

The ```.pdf``` file [```Introduction_to_Statistical_Learning__Gareth_James__2013.pdf```](https://github.com/HenriBranken/spark_and_python_for_big_data_with_pyspark/blob/master/course_walkthrough/Introduction_to_Statistical_Learning__Gareth_James__2013.pdf), under the ```course_walkthrough``` folder, contains all the contents for carrying out the reading assignments.

You will notice that my ```Python``` Notebooks contain verbose comments.  This feature will be more appreciated if, say, you review the material in this repo after a year from now.
The comments are there to help the learning experience and clarify the concepts underpinning the coding.

All the best when working through this material,  
Henri.
