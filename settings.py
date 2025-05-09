pip install dj-database-url
import dj-database-url
import os
DATABASES  
 "default": dj_database_url.parse(os.environ.get("postgresql://test_db_qlr3_user:DK6vSLXZZcF44VcAogWMLVcjomqGb1Wo@dpg-d0epgs95pdvs73au98k0-a.oregon-postgres.render.com/test_db_qlr3"))
 }
