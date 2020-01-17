## Clustering students
### Installation
The code should run with no issues using Python versions 3.X. Uses sklearn and pickle
### Project Motivation
This is a simple attempt to group the students based on various input parameters. The data is loaded from a pkl file. If you are interested in how data was generated please refer to this (repo)[https://github.com/sanjayaben/random-student-data-generator]. The students are grouped in to clsuters and plotted.

### File Descriptions
There are couple of python files and a pkl file
1. student_instructional_groups.py - generated clusters based on KMeans algorithm and plots them
2. utils/draw_graph.py - draw the cluster points
3. utils/feature_format.py  - format the dataset for clustering. removes Nans, all zeros etc.


### Licensing, Authors, Acknowledgements
Feel free to use this as you want
