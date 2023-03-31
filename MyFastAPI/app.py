from fastapi import FastAPI
import uvicorn
import pickle
import sklearn


app = FastAPI(debug=True)

@app.get('/')
def home():
    return {"text": "Telco Churn Prediction Model"}

@app.get('/predict')
async def predict( tenure: int, age: int, address: int, income: float, employ: int, retire: int, 
              reside: int, tollfree: int, equip: int, callcard: int,
              wireless: int,
              multline: int,
              voice: int,
              pager: int,
              internet: int,
              callid: int,
              callwait: int,
              forward: int,
              confer: int,
              ebill: int,
              loglong: float, Ininc: float, total_monthly_bill: float, total_bill: float ,
              region_zone_1: int, region_zone_2:int,
              region_zone_3:int,
              marital_married:int,
              marital_unmarried:int,
              ed_college_degree:int,
              ed_did_not_complete_high_school:int,
              ed_high_school_degree:int,
              ed_post_undergraduate_degree:int,
              ed_some_college:int,
              gender_female:int,
              gender_male:int,
              custcat_basic_service:int,
              custcat_e_service:int,
              custcat_plus_service:int,
              custcat_total_service:int):
                       
            
            model = pickle.load(open('C:/Users/kaund/OneDrive/Desktop/MyFastAPI/svm_clf.pkl','rb'))
            makeprediction = model.predict([[ tenure, age, address, income, employ, retire, reside,
            tollfree, equip, callcard, wireless, multline, voice, pager, internet, callid, callwait, forward, confer, ebill, loglong, 
            Ininc, total_monthly_bill, total_bill, region_zone_1, region_zone_2, region_zone_3, marital_married,  marital_unmarried,
            ed_college_degree, ed_did_not_complete_high_school, ed_high_school_degree, ed_post_undergraduate_degree, ed_some_college,
            gender_female, gender_male,custcat_basic_service, custcat_e_service,custcat_plus_service, custcat_total_service
             ]])
            output = round(makeprediction[0],2)

            return {'The percentage likelihood the customer will churn is  {}'.format(output)}

if __name__ == '__main__':
    uvicorn.run(app)

    ##uvicorn.run(app, host="127.0.0.1", port=8000)
