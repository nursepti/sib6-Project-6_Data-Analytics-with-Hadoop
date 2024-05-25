import os
import connection
import sqlparse
import pandas as pd

if __name__ == '__main__':
    
    
    #connection data source
    conf = connection.config('marketplace_prod')
    conn, engine = connection.get_conn(conf, 'DataSource')
    cursor = conn.cursor()

    #connection data source
    conf_dwh = connection.config('dwh')
    conn_dwh, engine_dwh = connection.get_conn(conf_dwh, 'DataWarehouse')
    cursor_dwh = conn_dwh.cursor()
    
    # connection hadoop
    conf_hadoop = connection.config('hadoop')
    client = connection.hadoop_conn(conf_hadoop)

    #get query string
    path_query = os.getcwd()+'/query/'
    query = sqlparse.format(
        open(path_query+'query.sql', 'r').read(), strip_comments=True
    ).strip()
    dwh_design = sqlparse.format(
        open(path_query+'dwh_design.sql', 'r').read(), strip_comments=True
    ).strip()
    
    try:
        #get data
        print('[INFO] service etl is running..')
        print('[INFO] service etl is success..')
        df = pd.read_sql(query, engine)
        
        # create schema to dwh
        # cursor_dwh.execute(dwh_design)
        # conn_dwh.commit()
        
        # ingest data to dwh
        # df.to_sql('dim_orders', engine_dwh, if_exists='append', index=False)
        
        # ingest data to hadoop
        # with client.write(f'/digitalskola/project/dim_orders_septi.csv', encoding='utf-8') as writer:
        #     df.to_csv(writer, index=False)
        # print('[INFO] service etl is success..')
        
    except Exception as e:
        print('[INFO] service etl is failes')
        print(str(e))
        