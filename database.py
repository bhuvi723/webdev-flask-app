from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_port = os.getenv("db_port")
db_name = os.getenv("db_name")
ssl_ca_path = os.getenv("ssl_ca_path")

conn_str = (
    f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    f"?ssl_ca={ssl_ca_path}&ssl_verify_cert=false"
)

engine = create_engine(conn_str)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs_dict_list = []

    for job in result.all():
      jobs_dict_list.append(job._asdict())

    return jobs_dict_list