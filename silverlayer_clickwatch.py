#!/usr/bin/env python
# coding: utf-8

# ## silverlayer_clickwatch
# 
# New notebook

# In[7]:


df = spark.sql("SELECT * FROM streamingpulse.web_cookies")


# In[8]:


from pyspark.sql.functions import *
df2=df.withColumn("page_url",regexp_replace(col("page_url"), r"[^a-zA-Z0-9- ]", "")) \
       .withColumn("timestamp",translate(col('timestamp'),'TZ',' ').cast('timestamp')) \
       .withColumnRenamed("utm_source","Platform") 
display(df2)


# In[9]:


df3=df2.withColumn("events",explode(col('events')))

df4=df3.withColumn('event_type',col("events.event_type")).drop('events')


# In[10]:


df5=df4.select("session_id","user_id","timestamp","device_type","os",
"browser","page_url","referrer","Platform","event_type","time_spent_seconds","is_returning_visitor","visit_count")


# In[11]:


df6=df5.groupBy("user_id").agg(sum('visit_count').alias("visitor_count"))
display(df6)


# In[12]:


df6.write \
  .format("delta") \
  .mode("overwrite") \
  .saveAsTable("visit_count")

df5.write \
  .format("delta") \
  .mode("overwrite") \
  .saveAsTable("final_cookies")

