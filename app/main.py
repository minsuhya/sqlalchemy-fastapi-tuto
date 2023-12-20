#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import os
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException
from routes.test import router as test_router

app = FastAPI()
app.include_router(test_router, prefix="/test", tags=["test"])


@app.get("/")
def index():
    return {"message": "Hello World"}
