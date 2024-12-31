from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - project01-coll-d443961868824521a113d699e1ad9032',debug=False,docs_url='/hungry-tanvi-0af8c4c4c76f11efbd990242ac12000539/docs',openapi_url='/hungry-tanvi-0af8c4c4c76f11efbd990242ac12000539/openapi.json')

app.include_router(router, prefix='/hungry-tanvi-0af8c4c4c76f11efbd990242ac12000539/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()