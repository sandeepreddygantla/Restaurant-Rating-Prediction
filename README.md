## Introduction
Zomato is one of the best online food delivery apps which gives the users the ratings and the reviews on restaurants all over india.These ratings and the Reviews are considered as one of the most important deciding factors which determine how good a restaurant is.

We will therefore use the real time Data set with variuos features a user would look into regarding a restaurant. We will be considering Banglore City in this analysis.

Acknowledgements The data scraped was entirely for educational purposes only. Note that I don’t claim any copyright for the data. All copyrights for the data are owned by Zomato Media Pvt. Ltd..

Source Dataset: [Kaggle](https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants/data)

## Overview

This is a Streamlit web application that predicts the rating of a restaurant on Zomato based on user input. The application uses a machine learning model built on Regression.

## Requirements

- Python 3.8+
- Streamlit
- NumPy
- Pandas
- Seaborn
- Matplotlib
- Scikit-learn

## Project Structure
This project has four major parts :
- `model/model.ipynb`: This contains code for our Machine Learning model to predict restaurant ratings based on data in the 'zomato.csv' file and 
- `app.py`: The main Streamlit application script.
- `model/model.pkl`: The trained machine learning model file.
- `logs/`: Directory to store log files.

You can select any one of the options at a time to see the result.

## Install the required packages using:

```bash
pip install -r requirements.txt
```

## Running the project
1. Clone the repository:
```
git clone https://github.com/sandeepreddygantla/Restaurant-Rating-Prediction.git
```
2. Change directory
```
cd Restaurant-Rating-Prediction
```
3. Need a dataset to train model Download it from [Kaggle](https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants/data)

4. create a `data` folder and store the dataset in `data/zomato.csv`

5. Run `model/model.ipynb` file

6. install jupyter notebook to run the `model.ipynb`
```
pip install jupyter
``` 
7. You will get `model.pkl` file in `model/` folder

8. Ensure that you are in the project home directory. Run the below command to start streamlit app.
   
```
streamlit run app.py
```

9. Navigate to URL http://localhost:8501

You should be able to view the homepage.

Select all the option given in dropdown-->enter valid numerical values in votes and cost input boxes-->hit Predict.

If everything goes well, you should  be able to see the restaurant rating.

![image](https://github.com/sandeepreddygantla/Restaurant-Rating-Prediction/blob/main/img/zomato_output.png)

## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests.





