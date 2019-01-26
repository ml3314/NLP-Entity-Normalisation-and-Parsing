# NLP-addresses-normalisation-and-parsing
Minyi Liang

minyi_liang@hotmail.com


In this project, I used Python open source packages to parse and normalise addresses and turned unstructured data into structured data.


1. Goal

The objective of this project is to clean a given dataset that contains unstructured data, i.e.
parse and normalise information.

2. Dataset

The input is a JSON file with a list of roughly 140,000 strings. Each string contains information
about a location, a date or both. The data is not completely clean and may contain irrelevant
input.

3. Project

This project is to separate the location and date information and normalise the date to the following the format: YYYY-MM-DD. The location information is further parsed into city, country and road. Additionally, a ranking concept is provided that indicates the quality of the output. 

4. Output data

The unstructured data will be turned into structured data. 

For example:

"May 2009" 

→ 

{address: ““, date_iso: “2009-05-01”, ranking: “xxx”}

Another example:

"20 Rayman House, Augustus Road, London, UK, 03/05/2009" 

→ 

{flat number: "15", house: "Rayman House", road: "Augustus Road", city: "London", country: "UK", date_iso: “2009-05-03”, ranking: “xxx”}



5. Deliverables

The files contained in this repo is as follows:

- A detailed description of the design decisions (libraries, tradeoffs, etc.), how I evaluated
the results, as well as ideas for further improvement (see explainations.pdf).

- A flowchart of the processing of the input data (see Flowchart.pdf).

- A functional python module (see Entity_Parsing.py).

- JSON files of the input (see data.json) and output data (result.json).
