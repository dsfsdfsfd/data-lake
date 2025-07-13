# Diagram
![Image](./access/diagram.png)

# I. Data architectures
***Describe how data is managed***
* Collection
* Transformation
* Distribution
* Consumption

![i](./access/data_architectures.png)

## II. Type of Data architectures
1. Data Fabric: Unify(thống nhất) multiple and disjoint data sources in varios(nhiều loại)
    - Data sources: data warehouses, data lakes, and data marts
    - Environments: on-prem, cloud, and edge
2. Data Mesh: Distribute data ownership to domain-specific teams.  
    - Each team manages, owns, and serves the data as a product
## III. Type of DMS
1. Data Warehouse
- A central data hub containing highly formatted and structured data for analytics
Eg: GCP, BigQuery, AWS...

2. Data Mart
- A subset of a warehouse to serve a specific domain
Eg: sales, accounting, IT...

3. Data Lake
- A central location for both structured and unstructured data in its raw form.

4. Lake house
- Add layers for data management, governance and query performance on top of Data Lake

## IV. Types of architectures
1. Lambda Architecture
    - Stream processing
    - Batch processing
- Tow separate serving layer
- Often used for historical analysis

2. Kappa Architecture
    - Stream processing
- Unified serving layer
- Often used for real-time analysis

## V. Dataflow model
```bash
batch is a special case of streaming 
```
-> beam


