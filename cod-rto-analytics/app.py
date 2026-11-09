import pandas as pd
import streamlit as st
from pathlib import Path
st.set_page_config(page_title="COD / RTO Analytics",layout="wide")
st.title("COD / RTO Analytics")
up=st.file_uploader("Upload fulfillment CSV",type="csv")
df=pd.read_csv(up if up else Path(__file__).with_name("sample_fulfillment.csv"))
required={"order_id","payment_method","status","order_value","forward_shipping","return_shipping"}
if not required.issubset(df.columns):st.error("CSV missing: "+", ".join(sorted(required-set(df.columns))));st.stop()
for c in ["order_value","forward_shipping","return_shipping"]:df[c]=pd.to_numeric(df[c],errors="coerce").fillna(0)
df["payment_method"]=df.payment_method.astype(str).str.strip().str.upper()
df["status"]=df.status.astype(str).str.strip().str.upper()
df["is_rto"]=df.status.eq("RTO")
df["logistics_cost"]=df.forward_shipping+df.return_shipping
summary=df.groupby("payment_method").agg(orders=("order_id","nunique"),rto_orders=("is_rto","sum"),logistics_cost=("logistics_cost","sum"))
summary["rto_rate_pct"]=(summary.rto_orders/summary.orders.replace(0,float("nan"))*100).round(1)
st.dataframe(summary,use_container_width=True)
st.metric("Total logistics expense",f"₹{df.logistics_cost.sum():,.0f}")
st.bar_chart(summary[["orders","rto_orders"]])
st.subheader("Courier/status breakdown")
if "courier" in df.columns:st.dataframe(pd.crosstab(df.courier,df.status),use_container_width=True)
else:st.info("Optional courier column not found.")
st.download_button("Export analyzed orders",df.to_csv(index=False).encode(),"fulfillment_analysis.csv","text/csv")
st.caption("Statuses must use RTO to identify return-to-origin cases. A sample of rows may include repeated order IDs; deduplicate before financial reporting.")
