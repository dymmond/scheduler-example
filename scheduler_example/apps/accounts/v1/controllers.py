"""
Generated by 'esmerald createapp' using Esmerald 3.2.0.
"""

from esmerald import JSONResponse, get


@get("/ping")
async def welcome() -> JSONResponse:
    return JSONResponse({"message": "Welcome to Esmerald!"})
