## Sports-Activity-Recognizer
Used fastai and ResNet50 model and **error_rate and accuracy** as evaluation metrics to develop this image recognition model with **~98.5% accuracy**.I gathered more than 4.5k data to train the model.
## Goal of the Project
The ultimate goal of this project is to distinguish the 15 most popular different types of **Sports Activities** around the world.<br/>
The types are following:
1. archery
2. baseball swing
3. basketball shot
4. boxing jab
5. cricket batting
6. cycling sprint
7. golf swing
8. horse riding gallop
9. ice hockey slapshot
10. rowing
11. rugby tackle
12. skiing parallel
13. soccer kick
14. surfing cutback
15. volleyball spike

## Dataset Preparation
**Data Collection:** I collected the necessary data from DuckDuckGo using the label name.<br/>
**DataLoader:** The DataLoader was configured using the fastai DataBlock API.<br/>
**Data Augmentation:** Fastai offers GPU-operated default data augmentation. You can find the details in ```notebooks/data_preparation.ipynb``` file.<br/>

## Model Training and Data Cleaning
**Model Training**: I used ResNet50 transfer learning model to train my model. I used 10 epochs at first time training,5 epochs at second time training,3 epochs at third time training and 2 epochs at fourth time training. Finally, I found **~98.5% Accuracy**,**~1.5% Error Rate**,**~5% Validation Loss** and **~9.87% Train Loss**.

<img width="317" alt="epochs" src="https://github.com/armanulalam/Sports-Activity-Recognizer/assets/65443530/338f98df-8db5-4f8c-87f1-d43e8308e3b8">

**Data Cleaning:** This part was the most time consuming part of this project. I cleaned the data based on the Confusion Matrix scores four times. At the very beginning, there was a lot of noise and irrelevant data in my dataset. Using the fastai ImageClassifierCleaner, I updated and cleaned the dataset. With the exception of the final iteration, which produced the final version of the model, I purged the data after every training or fine-tuning iteration.

## Model Deployment
After training the model and cleaning the data I deployed the final model ```sports-action-recognizer-version3.pkl``` into HuggingFace Spaces Gradio App. The implementation can be found in deployment folder or [here](https://huggingface.co/spaces/Armanul/sports-activity-recognizer)

<img width="858" alt="huggingface" src="https://github.com/armanulalam/Sports-Activity-Recognizer/assets/65443530/91de728a-fc81-4149-b32f-393df3694847">

## API Integration With Website
Finally, I made a simple two page website using HTML, CSS and JavaScript where I integrated the model API [here](https://armanulalam.github.io/Sports-Activity-Recognizer/) and I used Github Pages to host my website. Implementation and other details can be found in ```docs``` folder.

![index page](https://github.com/armanulalam/Sports-Activity-Recognizer/assets/65443530/bad0d8bb-c62b-4ffe-8c61-79890578d20e)


![output_page](https://github.com/armanulalam/Sports-Activity-Recognizer/assets/65443530/de6dadb7-d79f-451f-a46c-4a35bea986fb)




## Get Started

`Python version 3.10 or 3.11 is required.`

To get started with the project, follow these steps:

1. Clone the project repository from GitHub

    ```powershell
    git clone https://github.com/armanulalam/Sports-Activity-Recognizer.git
    ```

2. Set up the required dependencies and libraries by executing the following command:

    ```powershell
    pip install -r requirements.txt
    ```

3. Obtain a dataset of images representing the 15 sports activities by executing the following notebook: [data_preparation.ipynb](notebooks/data_preparation.ipynb).
4. Train the machine learning model using the dataset by executing the following notebook: [modelTraining_and_dataCleaning.ipynb](notebooks/modelTraining_and_dataCleaning.ipynb).
5. Now, you can identify the photography style of any image by executing the following commands:

    ```powershell
    cd .\deployment\
    python app.py
    ```

   Or you can visit [Hugging Face Space: Armanul/sports-activity-recognizer](https://huggingface.co/spaces/Armanul/sports-activity-recognizer)) to recognize different types of sports activity.

If you have any further queries then you can send me an email to armaanularmaan@gmail.com
