from importers import *
import uvicorn

# list of all the API's in the projrct
try:
    from APIs.fetch_company_detail import *
    from APIs.search_algo import *
except Exception as e:
    print(e)

if __name__ == "__main__":
    uvicorn.run("run:app", host="localhost", port=6050, log_level="info", reload=True)
