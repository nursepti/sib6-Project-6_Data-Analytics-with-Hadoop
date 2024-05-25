# Background Project 6 - Data Analytic with Hadoop

Pada Project 6 ini Data Warehouse yang ada pada postgres akan dimasukkan dalam Hadoop sebagai DWH dan dilakukan MapReduce untuk dilakukan proses ETL, dan diminta untuk membuat tabel data mart yang nantinya akan digunakan oleh data analis untuk membuat dashboard report order setiap bulannya. Proses yang dilakukan tidak boleh lebih dari 1 jam.
Requirement tabel data mart:
output columns: month, total_orders
 task yang harus dikerjakan :
- Extract data source ke database postgres.
- Buat file DWH ‘dim_orders’ dengan menggunakan hadoop.
- Buat data mart ‘total_orders_based_on_month’ dengan MapReduce, data diambil dari DWH.

# Tools
* Postgres (via Docker or direct install)
* Hadoop versi < 3.2.1
* Script Project 3 - Batch Processing
* GUI Postgres (Pgadmin, Dbeaver, dll) (optional)