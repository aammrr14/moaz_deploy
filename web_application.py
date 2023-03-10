# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
import pickle
import streamlit as st
#import os

#loading the models 
path_list=["Ridge(1).pkl","RandomForestRegressor(1).pkl","GradientBoostingRegressor(1).pkl","LinearRegression.pkl"]
#path_list=os.listdir("/home/aammrr3/Downloads/deployment")
#path_list.remove('web app.py')
#path_list.remove('espilon.i project (Compressive Strength prediction for concrete).ipynb')
model=[]
for model_filepath in path_list:
    with open(model_filepath,"rb") as f:
        model.append(pickle.load(f))
        

        
        
def make_pred(age, sex, bmi, children, smoker,region_southwest, region_southeast, region_northwest,region_northeast):
    
    data=[age, sex, bmi, children, smoker,region_southwest, region_southeast, region_northwest,region_northeast]
    
    data=np.asarray(data).reshape(1, -1)
    
    RIDGE_pred=model[0].predict(data)
    linear_pred=model[3].predict(data)
    GB_pred=model[2].predict(data)
    RF_pred=model[1].predict(data)
    
    
    
    return linear_pred,RIDGE_pred,GB_pred,RF_pred     

def main():
    
    #cereating the title 
    st.title("medical charges prediction")
    
    


    #creating input from the user
    age=st.number_input('age')
    children=st.number_input('children')
    bmi=st.number_input('bmi')
    
    gender = {"male":1,"female":2}
    def format_func_gen(option):
        return gender[option]
    sex=st.selectbox("Select gender", options=list(gender.keys()))
    sex=format_func_gen(sex)
    
    smoke = {"Yes":1,"No":2}
    def format_func_smoke(option):
        return smoke[option]
    smoker=st.selectbox("do you smoke?", options=list(smoke.keys()))
    smoker=format_func_smoke(smoker)
    
    
    
    def format_func_reg(option):
        region_southwest=1
        region_southeast=0
        region_northwest=0
        region_northeast=0
        if option =='region_southwest':
        
            region_southwest=1
            region_southeast=0
            region_northwest=0
            region_northeast=0
           
        if option =='region_southeast':
            
            region_southwest=0
            region_southeast=1
            region_northwest=0
            region_northeast=0
            
        if option =='region_northwest':
            region_southwest=0
            region_southeast=0
            region_northwest=1
            region_northeast=0

        if option =='region_northeast':
            region_southwest=0
            region_southeast=0
            region_northwest=0
            region_northeast=1
        
        return region_southwest, region_southeast, region_northwest,region_northeast
    reg=st.selectbox("region", options=['region_southwest',' region_southeast', 'region_northwest','region_northeast'])
    region_southwest, region_southeast, region_northwest,region_northeast=format_func_reg(reg)
    
    data=[age, sex, bmi, children, smoker,region_southwest, region_southeast, region_northwest,region_northeast]
    
    
    charges=0
    
    #creating buttons for predecting on deffirent models
    linear_button=st.button("prediction based on LINEAR model ")
    RIDGE_button=st.button("prediction based on RIDGE model ")
    GB_button=st.button("prediction based on GRADIENT BOOSTING model ")
    RF_button=st.button("prediction based on RANDOM FOREST model ")
    
    if linear_button:
        linear_pred,RIDGE_pred,GB_pred,RF_pred =make_pred(age, sex, bmi, children, smoker,region_southwest, region_southeast, region_northwest,region_northeast)
        charges=linear_pred
    elif  RIDGE_button :
        linear_pred,RIDGE_pred,GB_pred,RF_pred =make_pred(age, sex, bmi, children, smoker,region_southwest, region_southeast, region_northwest,region_northeast)
        charges=RIDGE_pred
    elif GB_button:
        linear_pred,RIDGE_pred,GB_pred,RF_pred =make_pred(age, sex, bmi, children, smoker,region_southwest, region_southeast, region_northwest,region_northeast)
        charges=GB_pred
    elif RF_button:
        linear_pred,RIDGE_pred,GB_pred,RF_pred=make_pred(age, sex, bmi, children, smoker,region_southwest, region_southeast, region_northwest,region_northeast)
        charges=RF_pred

    
    
    st.success(str(charges))
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    