from importers import *


@app.get("/corporate_data/search")
def update_nominee_details(request: Request, response: Response, q: str):
    results = db_.exec_stored_procedure(
        db_conn_,
        "public.search_company",
        [
            q
        ]
    )
    return results[0][0][0]
