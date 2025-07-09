#RAG integration for drinkware (Text2SQL)

#Import libraries 
import google.generativeai as genai
import sqlite3
from dotenv import load_dotenv
import os 

conn = None 

def init_db():
    global conn 
    #Connect / Create SQLite database
    conn = sqlite3.connect('outlet.db', check_same_thread=False)
    cursor = conn.cursor()

    #Create outlet data table 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ZUSoutlet_data(
                id INTEGER PRIMARY KEY, 
                location TEXT NOT NULL,
                hours TEXT,
                address TEXT NOT NULL
    )
    ''')
    #Insert data into table 
    outlets = [
        (1, 'ZUS Coffee - Temu Business Centre City Of Elmina', '8 am - 9:40 pm', 'No 5 (Ground Floor), Jalan Eserina AA U16/AA Elmina, East, Seksyen U16, 40150 Shah Alam, Selangor'),
        (2,'ZUS Coffee - Spectrum Shopping Mall', '8 am - 9:40 pm', 'Lot CW-5 Cafe Walk, Ground Floor Spectrum Shopping Mall Jalan Wawasan Ampang, 4, 2, Bandar Baru Ampang, 68000 Ampang, Selangor'),
        (3,'ZUS Coffee - Bandar Menjalara', '8 am - 9:40 pm', '37, Jalan 3/62a, Bandar Menjalara, 52200 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur'),
        (4,'ZUS Coffee - Jabatan Peguam Negara, Putrajaya', '7 am - 5:40 pm', 'Bangunan Jabatan Peguam Negara AGC Persint 4, Lot 1, Level 1, Putrajaya 62100 Malaysia'),
        (5,'ZUS Coffee - LSH33, Sentul', '7 am - 10:40 pm', 'G-11, Ground Floor, Laman Seri Harmoni (LSH33), No. 3, Jalan Batu Muda Tambahan 3, Sentul, 51100 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur'),
        (6,'ZUS Coffee - Bandar Tun Hussein Onn, Cheras', '8 am - 11:40 pm', 'No 48A Jalan Suarasa 8/4, Bandar Tun Hussein Onn, 43200 Cheras, Selangor'),
        (7,'ZUS Coffee - AEON BiG Wangsa Maju', '10 am - 9:40 pm', 'Lot F1.11 (First Floor), AEON BiG Wangsa Maju, 6, Jalan 8/27A, Section 5, Wangsa Maju, 53300, Kuala Lumpur, Wilayah Persekutuan'),
        (8,'ZUS Coffee - Cheras Business Centre', '7 am - 9:40 pm', 'No 6 Jalan 5/101C, Cheras Business Centre, 56100 Cheras, Kuala Lumpur'),
        (9,'ZUS Coffee - Damansara Perdana, Petaling Jaya', '7 am - 10:40 pm', '12-1 (Ground floor), Jalan PJU 8/5E, Bandar Damansara Perdana, 47820 Petaling Jaya, Selangor'),
        (10,'ZUS Coffee - Bandar Damai Perdana, Cheras', '7 am - 10:40 pm', 'No 19G (Ground floor), Jalan Damai Perdana 1/9b, Bandar Damai Perdana, 56000 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur'),
        (11,'ZUS Coffee - Desa Pandan, Ampang', '7 am - 10:40 pm', 'No 35 (Ground Floor), Jalan 3/76D, Desa Pandan, 55100, Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur')
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO ZUSoutlet_data (id, location, hours, address) VALUES (?,?,?,?)",
        outlets     
    )

    #Commit 
    conn.commit()
    return conn

#Load model
load_dotenv()
client = genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
    )

#Function
def sql_query(query: str)-> str:
    schema = f"""
    Table: ZUSoutlet_data (
        id: INTEGER PRIMARY KEY,
        location: TEXT NOT NULL,
        hours: TEXT,
        address: TEXT NOT NULL
    )
    """

    try:
        prompt = f"""
        Translate the following query into SQL:

        Database schema: {schema}
        User Query: "{query}"
        
        Return SQL query results properly WHERE clauses
        Include Limit 10 at the end
        """
        model= genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(
            prompt,
            security_settings={
                'HARM_CATEGORY_HARASSMENT': "BLOCK_NONE",
                'HARM_CATEGORY_HATESPEECH': "BLOCK_NONE"
            }
        )
        sql_response = response.text.strip().replace("```sql", "").replace("```", "")

        if not sql_response.upper().startswith("SELECT"):
            raise ValueError("Generated SQL is not a SELECT query")
            
        return sql_response
        
    except Exception as e:
        print(f"SQL Generation Error: {str(e)}")
        # Fallback (Simple search)
        return f"""
        SELECT * FROM ZUSoutlet_data 
        WHERE location LIKE '%{query}%' 
        OR address LIKE '%{query}%'
        LIMIT 10
        """

def execute_sql_query(sql: str, conn, max_results: int=10):
        try:
            cursor = conn.cursor()

            if "LIMIT" not in sql.upper():
                sql = sql.rstrip(";") + f" LIMIT {max_results};"

            #Prevent not safe sql 
            forbidden_keywords = ["DROP", "DELETE", "INSERT", "UPDATE", "ALTER","--", ";"]
            if any(keyword in sql.upper() for keyword in forbidden_keywords):
                raise ValueError("Unsafe SQL query detected")

            cursor.execute(sql)
            return{
                "data": cursor.fetchall(),
                "columns": [desc[0] for desc in cursor.description]
            }
        except sqlite3.Error as e:
             raise ValueError(f"SQL Error: {str(e)}")

#To test query 
#Simply type http://localhost:8000/outlets?query=Cheras and put on browser to view results