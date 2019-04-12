df=spark.sql("select * from shs_ingestion")
df.registerTempTable('shs')
