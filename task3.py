# Task3.py

from fastapi import FastAPI, Query, HTTPException
from typing import Optional

app = FastAPI(title="API для меню ресторану")

# Список страв (умовна база даних)
menu_db = [
    {"id": 1, "name": "Борщ український", "category": "перші страви", "price": 95.0},
    {"id": 2, "name": "Вареники з картоплею", "category": "перші страви", "price": 80.0},
    {"id": 3, "name": "Котлета по-київськи", "category": "основні страви", "price": 120.0},
    {"id": 4, "name": "Деруни зі сметаною", "category": "основні страви", "price": 85.0},
    {"id": 5, "name": "Компот із сухофруктів", "category": "напої", "price": 30.0},
    {"id": 6, "name": "Морозиво з шоколадом", "category": "десерти", "price": 50.0},
    {"id": 7, "name": "Капучино", "category": "напої", "price": 45.0}
]

# Головна сторінка
@app.get("/")
async def root():
    return {"message": "Використайте /menu?category=напої для отримання меню"}

# Отримати меню з фільтрацією за категорією
@app.get("/menu")
async def get_menu(category: Optional[str] = Query(None, description="Категорія страв, напр. перші страви, напої, десерти")):
    filtered_menu = [item for item in menu_db if category is None or item['category'].lower() == category.lower()]
    if not filtered_menu:
        raise HTTPException(status_code=404, detail="Страви не знайдені або некоректна категорія")
    return {"menu": filtered_menu}

# Отримати страву за ID
@app.get("/menu/{item_id}")
async def get_menu_item(item_id: int):
    item = next((item for item in menu_db if item["id"] == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Страва не знайдена")
    return item
