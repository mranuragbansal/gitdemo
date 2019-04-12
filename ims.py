=======
df=spark.sql("select * from ims_ingestion")
df.registerTempTable('ims')

