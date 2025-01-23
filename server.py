from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "db_phone"
}

app = FastAPI()

class Phone(BaseModel):
    id: int = None
    name: str
    brand: str
    category: str
    released: int
    display: str
    camera: str
    ram: str
    chipset: str
    battery: str
    price: float

class PhoneCreate(BaseModel):
    name: str
    brand: str
    category: str
    released: int
    display: str
    camera: str
    ram: str
    chipset: str
    battery: str
    price: float

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.post("/phones", response_model=Phone)
def create_phone(phone: PhoneCreate):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        INSERT INTO phones (name, brand, category, released, display, camera, ram, chipset, battery, price) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (phone.name, phone.brand, phone.category, phone.released, phone.display, phone.camera,
                           phone.ram, phone.chipset, phone.battery, phone.price))
    connection.commit()
    phone_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return {**phone.dict(), "id": phone_id}

@app.get("/phones", response_model=List[Phone])
def read_phones():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM phones"
    cursor.execute(query)
    phones = cursor.fetchall()
    cursor.close()
    connection.close()
    return phones

@app.get("/phones/{phone_id}", response_model=Phone)
def read_phone(phone_id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM phones WHERE id = %s"
    cursor.execute(query, (phone_id,))
    phone = cursor.fetchone()
    cursor.close()
    connection.close()
    if not phone:
        raise HTTPException(status_code=404, detail="Phone not found")
    return phone

@app.put("/phones/{phone_id}", response_model=Phone)
def update_phone(phone_id: int, phone: PhoneCreate):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        UPDATE phones 
        SET name = %s, brand = %s, category = %s, released = %s, display = %s, camera = %s, 
            ram = %s, chipset = %s, battery = %s, price = %s
        WHERE id = %s
    """
    cursor.execute(query, (phone.name, phone.brand, phone.category, phone.released, phone.display, phone.camera,
                           phone.ram, phone.chipset, phone.battery, phone.price, phone_id))
    connection.commit()
    cursor.close()
    connection.close()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Phone not found")
    return {**phone.dict(), "id": phone_id}

@app.delete("/phones/{phone_id}")
def delete_phone(phone_id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "DELETE FROM phones WHERE id = %s"
    cursor.execute(query, (phone_id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Phone not found")
    return {"message": "Phone deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
