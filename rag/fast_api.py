#Part 4: Custom API and RAG integration & Part 5: Unhappy flows
#Fast API & RAG integration
from fastapi import FastAPI, Query, HTTPException
from rag_drinkware_gemini import build_faiss_index, search, generate_summary #may change to openai
from rag_outlet_gemini import init_db, sql_query, execute_sql_query
import uvicorn

app = FastAPI() 

index, document = build_faiss_index()
conn = init_db() 

#Fast API endpoints 
@app.get("/")
async def root():
    return {"message": "API connected"}

@app.get("/products")
async def get_product(query: str= Query(..., description="User question on drinkware")):
    try:
        top_doc = search(query, index, document, k=3)
        summary = generate_summary(query, top_doc)
        return{
            "query": query,
            "retrieved": top_doc,
            "summary": summary
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    
@app.get("/outlets")
async def get_outlet(query: str= Query(..., description="User question on outlet"),
                      max_results: int = Query(10, ge=1, le=50)
                      ):
    try:
        #generate SQL
        sql = sql_query(query)
        
        #execute query
        results = execute_sql_query(sql, conn, max_results)
        
        #return response
        return {
            "outlets":[
                {
                    "id": row[0],
                    "location": row[1],
                    "hours": row[2],
                    "address": row[3]
                }
                for row in results["data"]
            ],
        }
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)