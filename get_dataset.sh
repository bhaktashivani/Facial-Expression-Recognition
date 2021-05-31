# took this file from Assignment 3 start code and edited it to our needs. Thank you. 
# By running this file one can download the dataset required for the project
# We used the Tifts dataset. Links to all their data can be found here: https://www.kaggle.com/kpvisionlab/tufts-face-database
# Their Website is http://tdface.ece.tufts.edu/
# http://tdface.ece.tufts.edu/downloads/

# wget http://tdface.ece.tufts.edu/downloads/TD_RGB_A/TD_RGB_A_Set1.zip
# wget http://tdface.ece.tufts.edu/downloads/TD_RGB_A/TD_RGB_A_Set2.zip
# wget http://tdface.ece.tufts.edu/downloads/TD_RGB_A/TD_RGB_A_Set3.zip
# wget http://tdface.ece.tufts.edu/downloads/TD_RGB_A/TD_RGB_A_Set4.zip

mkdir Tufts
mkdir Tufts/Set1
mkdir Tufts/Set2
# mkdir Tufts/Set3
# mkdir Tufts/Set4

unzip TD_RGB_A_Set1.zip -d Tufts/Set1/
unzip TD_RGB_A_Set2.zip -d Tufts/Set2/
# unzip TD_RGB_A_Set3.zip -d Tufts/
# unzip TD_RGB_A_Set4.zip -d Tufts/

# rm TD_RGB_A_Set1.zip
# rm TD_RGB_A_Set2.zip
# rm TD_RGB_A_Set3.zip
# rm TD_RGB_A_Set4.zip