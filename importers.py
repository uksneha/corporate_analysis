import psycopg2
import json
import requests
import uuid
import base64
from typing import *
import io
from io import BytesIO
from pathlib import Path
from pydantic import constr, BaseModel
from dotenv import load_dotenv
from datetime import datetime
from db_connection import Database
from fastapi import FastAPI, Request, Response, File, UploadFile, Form, Header, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from variables.error_list import *

app = FastAPI()

db_ = Database()
db_conn_ = db_.get_connection()
