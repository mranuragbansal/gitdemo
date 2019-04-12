df1=spark.sql("select * from ims left join shs on ims.key=shs.key")
df1.write.saveAsTable('dw_shs_ims')
