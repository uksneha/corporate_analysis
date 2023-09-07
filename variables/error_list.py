def databaseError(error: str):
    return {
        "status": "Failed",
        "code": "400",
        "name": "DATABASE_ERROR",
        "error": {
            "field": "database",
            "message": "Failed to do the database transaction",
            "error": error
        }
    }

