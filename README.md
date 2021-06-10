# ECE285_Project: Facial Expression Recognition 

## Getting the Dataset (Tufts Face Database 2D RGB Expression (TDRGBE))
This dataset contains 250 images. It has 5 images from 50 different people. These 5 images are of 5 different expressions. (Neutral Face, Smiiling Face, Eyes Closed, Surprised, and with sunglasses.) Even though these are not all "Expressions", we couldn't find any other dataset that we liked.

The dataset can be downloaded by running the script provided in the folder:

```
bash get_dataset.sh
```
## Saving the Cropped and Resized Images. 
- Create a folder called 'cropped' 
- Run the script PrepData.py. This will save the cropped and resized images into the cropped folder. 
```
mkdir cropped
python PrepData.py
```

### Dataset
We used the Tufts Face Dataset for training and testing the ***** model. This Dataset contains over 10,000 images of 74 female and 38 males from more than 15 countries with the age range between 4-70 years old. This dataset contains 7 image modalities, but we only use the Tufts Face Database 2D RGB Around (TDRGBA).


### Final Results 
WoodNet:
With no data augmentation - 71.4% accuracy on test set
With data augmentation - 98.75% accuracy on test set



### Video link (Youtube unlisted) 
A 5-min recorded video demo introducing your method and the visualization of the results.


## References 
[1] http://tdface.ece.tufts.edu/
[3] https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8554155
[3] https://arxiv.org/pdf/2011.11257.pdf (WoodNet)
