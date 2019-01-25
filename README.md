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

This project is to separate the location and date information and normalise the date to the following
format: YYYY-MM-DD. The location information are further parsed into city, country and road.

Additionally, a ranking concept is provided that indicates the quality of the
output. 

The unstructured data will be turned into structured data. For example:
"May 2009" → {address: ““, date_iso: “2009-05-01”, ranking: “xxx”}
"Portland United States of America, 03/05/2009" → {address: “Portland United States of
America“, date_iso: “2009-05-03”, ranking: “xxx”}



4. Deliverables

The files contained in this repo is as follows:

4.1. A detailed description of the design decisions (libraries, tradeoffs, etc.), how I evaluated
your results, as well as ideas for further improvement (see explainations.pdf).

4.2. A flowchart of the processing of the input data (see Flowchart.pdf).

4.3. A functional python module (see Entity_Parsing.py).

4.4. JSON files of the input (see data.json) and output data (result.json).
