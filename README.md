# python_backend
The backend for the wifi crowdsourcing webapp for the hackathon

**Expected Json Format**

```python
jsonStr = {
	"lat": float, 
	"long": float, 
	"ID": {"flrID":int, "bldID":int}, 
	"dateTime": (ISO 8601 YMDHMSw.d: yyyy-mm-dd hh:mm:ss.s),
	"ntwrkData": {"dwnldSpd": float, "upldSpd":float}
}
```



### **Sources:**

 https://docs.python.org/3/library/json.html