# CS587-Database-Benchmarking-Project
Contains files for CS587 Database Implementation class project (Winter 2021).

Here you will find all information relevant to Stage One of the CS587 Database Benchmarking Project

Stage One Components:
  Selection of: Project Option & System(s)   
  Data Generation (test relations)
  GCP project creation and customization


Project Option & System(s):
  
  As we are both looking to develop a core competency within DB administration, we opted for Project Option #1 which will allow us to get exposure with more DBMS systems. For this option we have selected Cassandra and BigQuery as the DBMS we will be running tests on.  As it so happens, both of us are also focusing on AI/ML during our MS tenure. For this reason the exposure to Cassandra should prove to be particularly helpful given it's popularity in NoSQL data management applications. It will also be interesting to see if there is a significant performance difference between the two systems, sinced Cassandra is typically used more frequently in NoSQL applications

Data Generation:
  
  We spent quite a few hours looking for a data generation program online without much success initially. However, once we took to the task of programming algorithms to create the data ourselves we found the process to be fairly simple. The code which was used to create both datasets can be found in this repo in a file named "datagen.py". The program used to run said code is, predictably, Python.

  We worked out the development of the appropriate logic in stages, working a bit at a time over successive days and sharing our results until our work was complete. The Wisconson Benchmark papers made the structure and content of the relations used very transparent. There were only a handful of hurdles we encountered during this process. (A few odd issues with my IDE environment, the occassional mistake of referencing an incorrect definition of the string variables, and some questions regarding converting the C code they provided to python.) Given that these are the types of mistakes I expect to come across when attempting work of any type, I'd rank this portion of the exercise as fairly trivial.

  The data itself can be found in the GH repo under OneKTup.csv and TenKTup.csv. You can also see that we have loaded the data to our GCP storage by perusing the screenshots of our GCP project in the file "Part I - Data Loaded Images.pdf"

GCP project creation and customization:

  This part of the project proved to be surprisingly straightforward. I'd had some issues understanding how to make use of GCP in a past course, but the presentation and materials provided by Neha made it all very easy to understand. You can find additional screenshots of the GCP Project in the file named 'GCP_High_Level.pdf'. Here you'll be able to see the interiors of the VM and Storage aspects, as well as the project dashboard where the BigQuery instance is clearly visible.
