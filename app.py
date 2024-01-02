import streamlit as st 
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

import pickle
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def load_model():
    # Load the Extra Trees Regression model from the saved file
    with open('./model/model.pkl', 'rb') as file:
        regressor = pickle.load(file)
    return regressor

def main():
    logging.info("Starting the application...")
    
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Restaurant Rating Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.text("")

    regressor = load_model()

    column_train = ['location_Banashankari', 'location_Bannerghatta Road',
                    'location_Bellandur', 'location_Brigade Road',
                    'location_Electronic City', 'location_HSR', 'location_Indiranagar',
                    'location_JP Nagar', 'location_Jayanagar',
                    'location_Koramangala 1st Block', 'location_Koramangala 4th Block',
                    'location_Koramangala 5th Block', 'location_Koramangala 6th Block',
                    'location_Koramangala 7th Block', 'location_MG Road',
                    'location_Marathahalli', 'location_Sarjapur Road', 'location_Ulsoor',
                    'location_Whitefield', 'location_other_location', 'rest_type_Bar',
                    'rest_type_Beverage Shop', 'rest_type_Cafe', 'rest_type_Casual Dining',
                    'rest_type_Casual Dining, Bar', 'rest_type_Delivery',
                    'rest_type_Dessert Parlor', 'rest_type_Quick Bites',
                    'rest_type_Takeaway, Delivery', 'rest_type_other_rest_type',
                    'cuisines_Bakery, Desserts', 'cuisines_Biryani', 'cuisines_Cafe',
                    'cuisines_Chinese', 'cuisines_Chinese, North Indian',
                    'cuisines_Desserts', 'cuisines_Fast Food',
                    'cuisines_Ice Cream, Desserts', 'cuisines_Mithai, Street Food',
                    'cuisines_North Indian', 'cuisines_North Indian, Chinese',
                    'cuisines_North Indian, Chinese, Biryani', 'cuisines_South Indian',
                    'cuisines_South Indian, North Indian, Chinese',
                    'cuisines_other_cuisines', 'type_Cafes', 'type_Delivery',
                    'type_Desserts', 'type_Dine-out', 'type_Drinks & nightlife',
                    'type_Pubs and bars', 'online_order', 'book_table', 'votes', 'cost',
                    'reviews_list']

    Location = st.selectbox('Select Location:', column_train[:20])
    Rest_type = st.selectbox('Select Restaurant Type:', column_train[20:30])
    Cuisines = st.selectbox('Select cuisines:', column_train[30:45])
    Service_type = st.selectbox('Select service type:', column_train[45:51])
    Online_order = st.selectbox('Select online order available:', ['Yes', 'No'])
    Book_table = st.selectbox('Select book table available:', ['Yes', 'No'])
    Reviews_list = st.selectbox("Rating given by user:", [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
    Votes = st.text_input("Total Votes given (e.g., 700):", 700)
    Cost = st.text_input("Approximate cost for two people (e.g., 800):", 800)

    locations_input, rest_type_input, cuisines_input, service_type_input = [0] * 20, [0] * 10, [0] * 15, [0] * 6

    # INPUT 
    # Location
    locations_train_column = column_train[:20]
    locations_input =[0]*20
    locations_column = []
    for location in locations_train_column:
        new_location = location.replace("location_","")
        locations_column.append(new_location)
    for i in range(20):
        if locations_column[i]==Location:
            locations_input[i] =1

    # Rest_type
    rest_type_train_column = column_train[20:30]
    rest_type_input =[0]*10
    rest_type_column = []
    for rest_type in rest_type_train_column:
        new_rest_type = rest_type.replace("rest_type_","")
        rest_type_column.append(new_rest_type)
    for i in range(10):
        if rest_type_column[i]==Rest_type:
            rest_type_input[i] =1

    # Cuisines
    cuisines_train_column = column_train[30:45]
    cuisines_input =[0]*15
    cuisines_column = []
    for cuisines in cuisines_train_column:
        new_cuisines = cuisines.replace("cuisines_","")
        cuisines_column.append(new_cuisines)
    for i in range(15):
        if cuisines_column[i]==Cuisines:
            cuisines_input[i]=1

    # Service_type
    service_type_train_column = column_train[45:51]
    service_type_input =[0]*6
    service_type_column = []
    for service_type in service_type_train_column:
        new_service_type = service_type.replace("type_","")
        service_type_column.append(new_service_type)
    for i in range(6):
        if service_type_column[i]==Service_type:
            service_type_input[i]=1

    # Online_order
    online_order_input = []
    if Online_order=='Yes':
        new_online_order = 1
        online_order_input.append(new_online_order)
    else:
        new_online_order = 0
        online_order_input.append(new_online_order)

    # Book_table
    book_table_input = []
    if Book_table=='Yes':
        new_book_table = 1
        book_table_input.append(new_book_table)
    else:
        new_book_table = 0
        book_table_input.append(new_book_table)

    # Votes
    votes_input = [np.log(int(Votes))]
    # Cost
    cost_input = [np.log(float(Cost))]
    # Reviews_list
    review_list_input = [Reviews_list]

    input_data = locations_input + rest_type_input + cuisines_input + service_type_input + [new_online_order] + [new_book_table] + [np.log(int(Votes))] + [np.log(float(Cost))] + [Reviews_list]

    if st.button("Predict"):
        logging.info("Predict button clicked.")
        prediction = regressor.predict([input_data])
        st.success(f'Restaurant rating is {round(prediction[0], 2)}')
        logging.info(f'Predicted rating: {round(prediction[0], 2)}')

if __name__ == '__main__':
    main()
