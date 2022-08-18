
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from models.student import Student 

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "App runing."}

@app.get('/csv-analysis')
async def csvAnalylis():
    df = pd.read_csv('./static/survey_lung_cancer.csv')

    # Remove rows that contain empty cells
    df.dropna()

    # Remove rows that contain NULL values
    df.dropna(inplace = True)

    # Replace values for specific column data
    # df['longitude'] = 0

    # Drop a column from dataset
    df.drop(['GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY', 'PEER_PRESSURE'], inplace=True, axis=1)

    print(df)

    return JSONResponse(status_code=200, content=df.to_string())

@app.post('/student')
async def createStudent(data: Student):
    return data
