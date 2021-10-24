# python_backend
The backend for the wifi crowdsourcing webapp for the hackathon

**Expected Json Format**

```python
jsonStr = {
	"lat": float, 
	"long": float, 
	"ID": {"flrID":int, "bldID":int}, 
	"dateTime": (ISO 8601 YMDHMSw.d: yyyy-mm-dd hh:mm:ss.s),
	"ntwrkData": {"wifiName": str, "dwnldSpd": float, "upldSpd":float, "outage": bool}
}
```
**Database Schema**

```
CREATE TABLE schema.wifi_crowdsourcing {
    latitude FLOAT, 
    longitude FLOAT, 
    floor_id INT, 
    building_id INT, 
    date_time TIMESTAMP, 
    wifi_name STRING 
    download_speed INT, 
    upload_speed FLOAT, 
    outage BOOL
}; 
```

### **Installations Required**

```
pip install jwt
pip install psycopg2-binary
brew install cockroachdb/tap/cockroach
```

### **Cockroach Stuff:**

```
1. Download the CRDB client, if you haven’t already done it before.
curl https://binaries.cockroachdb.com/cockroach-v21.1.10.darwin-10.9-amd64.tgz | tar -xz; sudo cp -i cockroach-v21.1.10.darwin-10.9-amd64/cockroach /usr/local/bin/

2. If you haven’t already, download the CA certificate using this command:
curl --create-dirs -o $HOME/.postgresql/root.crt -O https://cockroachlabs.cloud/clusters/e935fc52-2dc1-4321-a142-56a918011464/cert

3. Run this command to connect to your database.
cockroach sql --url 'postgresql://ofir:zPfIA64Mol4tYZCf@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert='$HOME'/.postgresql/root.crt&options=--cluster%3Dwifi-crowdsourcing-4313'

Connection string:

Username: ofir
host: free-tier.gcp-us-central1.cockroachlabs.cloud
port: 26257
database: wifi-crowdsourcing-4313.defaultdb
password: zPfIA64Mol4tYZCf
```

### **Data Visualization :**

```
Installation Required: 
Run this on install on the terminal: 
pip install pandas 
pip install matplotlib
pip install sqlalchemy 
pip install chart_studio

And import the following libraries in python: 
//import mpld3
import pandas as pd 
import matplotlib.pyplot as plt 
import sqlalchemy import create_engine 
```

### **Sources:**

https://docs.python.org/3/library/json.html

https://docs.python.org/3/library/json.html

