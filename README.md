# WikiBank
WikiBank is a new partially annotated resource for multilingual frame-semantic parsing task.

## Available Datasets
The available datasets are for 5 languages: EN, ES, DE, FR, and IT and their are in the dataset folder.

## Procedure for creations
NOTES: The space required is round 1TB, so be sure to have the required amount of space before starting the process.

### Requirements
1. MongoDB
2. Python

### Required files

1. Download Wikidata JSON dump from [here](https://www.wikidata.org/wiki/Wikidata:Database_download)
2. Download Wikipedia XML dump from [here](https://dumps.wikimedia.org/backup-index.html), or a JSON dump from [here](https://dumps.wikimedia.org/other/cirrussearch/current/) (download the "content" one).

If using the XML dump, converto it to JSON using one of the tools present in [this](https://www.mediawiki.org/wiki/Alternative_parsers) page.

### Data preprocessing
To merge Wikidata and Wikipedia, we need to have in both documents the Wikidata id. If your Wikipedia dump, doesn't contain this filed,
to can compute a mapping from wikipedia id to wikidata id using the script "src/scripts/wiki_props.py" and the dump of the Wikipedia properties ([here](https://dumps.wikimedia.org/) - called <lang>wiki-latest-page_props.sql) and then use the output file to add the wikidata id to the JSON document.


### Data import
3. Import the Wikidata dump into MongoDB in it's own collection using: 
    ```bash
    mongoimport --db WikiSRL --collection wikidata --file wikidata_dump.json --jsonArray
    ```
4. Create an index on the "id" field
    ```
    db.wikidata.createIndex({"id": 1})
    ```
5. Import the JSON wikipedia dump into MongoDB
6. Create an index on the wikidata id field:
    ```
    db.wikidata.createIndex({"wikidata_id": 1})
    ```

### Data integration
7. To merge Wikidata and wikipedia configure the config.py file, and then run merge_wikis.py

### SRL extraction
8. To extract the triples and create the SRL file, configure the config.py file, and run srl.py
