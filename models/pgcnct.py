from psycopg2 import connect,sql
import logging
_logger = logging.getLogger(__name__)


db_host = 'localhost'
db_name = 'lias'
db_password = 'benantar'
db_user = 'abdenour'

def connecct():
    try:
        conn=connect(
            dbname=db_name,
            user=db_user,
            host=db_host,
            password=db_password
        )
        _logger.debug(conn)

    except Exception as err:
        _logger.debug("ERR"+str(err))
        conn=None
    return conn
    
def get_col_names(table,conn):
    cols=[]
    col_crusor= conn.cursor()
    col_names_str="SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE "
    col_names_str += "table_name = '{}';".format(table)

    _logger.debug("col_names_str"+str(col_names_str))
    try:
        sql_object=sql.SQL(col_names_str).format(sql.Identifier(table))
        col_crusor.execute(sql_object)
        col_names=(col_crusor.fetchall())
        _logger.debug("col_names"+str(col_names))
        for tup in col_names:
            cols+= [tup[0]]
        col_crusor.close()
    
    except Exception as err:
        _logger.debug(err)
    return cols
