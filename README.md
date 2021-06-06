# ECE285_Project: Face Expression Recognization 

## Getting the Dataset (Tufts Face Database 2D RGB Expression (TDRGBE))
This dataset contains 250 images. It has 5 images from 50 different people. These 5 images are of 5 different expressions. (Neutral Face, Similing Face, Eyes Closed, Surprised, and with sunglasses.) Even though these are not all "Expressions", we couldn't find any other dataset that we liked.


The dataset can be downloaded by running the script provided in the folder:

```
bash get_dataset.sh
```
## Saving the Cropped and Resized Images. 
- Create a folder cropped folder 
- Run the script PrepData.py. This will save the cropped and resized images into the cropped folder. 
```
mkdir cropped
python PrepData.py
```
We used the Tufts Face Dataset from [1] 
chnage
### Dataset
We used the Tufts Face Dataset for training and testing the ***** model. This Dataset contains over 10,000 images of 74 female and 38 males from more than 15 countries with the age range between 4-70 years old. This dataset contains 7 image modalities, but we only use the Tufts Face Database 2D RGB Around (TDRGBA).

### Abstract 
Facial Recognitation a widely explored problem in the Machine Learning/Deep Learning field. This report disussing our unique approach to solving the problem of face recognizing using Elman Recurrent Neural Network. 

### Problem 
Face Recognitation is a method 

### Motivation 


### Approach 
Step 1: Standardization of the data
Zero-centered (subtract mean from each element)
Step 2: Computing the covariance Matrix
Step 3: Calculating the Eigenvectors and Eigenvalues
Step 4: Computing the Principal Components (PC)


## Model Achitecture. 


### Final Results 


### Analysis of the Results 


### Video link (Youtube unlisted) 
A 5-min recorded video demo introducing your method and the visualization of the results.

## Project Example link : DELETE AT THE END
https://drive.google.com/drive/folders/1id3grHu2xcbtolGzCuDJ6grVG1hZYb5r

## References 
[1] http://tdface.ece.tufts.edu/
[3] https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8554155
