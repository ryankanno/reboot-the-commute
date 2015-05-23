Instructions
============

  - Start mongodb (check etc/mongodb.conf)
    - `mongod -f /opt/local/etc/mongodb/mongod.conf --httpinterface --noauth`
  - Create geospatial indices
    - db.parkings.ensureIndex({location:"2dsphere"})
    - db.locations.ensureIndex({location:"2dsphere"})
  - `pip install -r requirements.txt`
  - python run.py
  - python seed.py
  - PROFIT

Sample Queries
==============

**Find all parking structures near (21.297165, -157.861866)**

`curl http://localhost:5000/parkings?where={"location": {"$near": {"$geometry": {"type":"Point", "coordinates": [-157.861866, 21.297165]}, "$maxDistance": 1000}}}`

**Find parkings**

  * `curl http://localhost:5000/parkings`
  * `curl http://localhost:5000/parkings?page=2`
