#Part 5: Unhappy flows (Test file)
import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from fast_api import app 
import rag_drinkware_gemini

client = TestClient(app) 

#Missing parameters
def test_missing_product():
    response = client.get("/products")
    assert response.status_code == 422
    print(response.status_code, response.text)

def test_missing_outlet():
    response = client.get("/outlets?query=Damansara")
    assert response.status_code == 200
    assert "outlets" in response.json()

#API downtime 
@patch ("rag_drinkware_gemini.generate_summary", effect = Exception("Simulated error"))
def test_server_error(mock_summary):
    response = client.get("/products?query=glass")
    assert response.status_code == 500
    assert "Internal server error" in response.text

#Malicious payload
def test_sql_injection():

    payloads = [
        "DROP TABLE users",        
        "DELETE FROM ZUSoutlet",   
        "INSERT INTO ZUSoutlet",   
        "UPDATE ZUSoutlet SET",    
        "ALTER TABLE ZUSoutlet",   
        "1' OR '1'='1",            
        "test; DROP TABLE users",  
        "test -- comment",         
    ]

    for payload in payloads:
        response = client.get(f"/outlets?query={payload}")
        assert response.status_code in [400, 500]
        assert "Unsafe SQL query detected" in response.text or "Internal server error" in response.text

#Run testing
#Run "pytest rag/chatbot_unhappy.py"