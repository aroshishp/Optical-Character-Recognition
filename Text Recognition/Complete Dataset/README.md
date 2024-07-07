### Training the Model
Preprocessing the image (involving resizing and normalizing pixel values) and training the model was done in the 
'text_recog.ipynb' file. The model was trained an saved as 'handwritten_text_recognition_model.h5'.

### Identifying Single Characters
To verify the working of the model, single letter containing images were given as input initially. These images were read 
in the 'identifying.ipynb' file and printed out. One such image is 'test7.jpg' which contains the letter 'm', identified as 'M'.

### Identifying Target Images
The target images were read in the 'reading.ipynb' file and the output was written to 'identified_text.csv' for sentiment 
analysis.
