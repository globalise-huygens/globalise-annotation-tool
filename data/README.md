# Globalise Annotation Tool Data

## Subdirectories
The `data/` directory should be contain the following directories:

* `lexical_data/` which contains (generated) FrameNet data,
* `structured/` which contains generated index files,
* `strucutred_raw/` which contains `entities.json` and `grouped_events.json` for index generation,
* `unstructured/` which contains all NAF files.

## Files
The `data/` directory should also contain the following files:

* `allowed.json` which is a username -> password mapping,
* `DynamicLexicon.json` containing the user generated lexicon, should start out as empty json file containg only `{}`,
* `Notes.json` containing notes written by users, should start out as empty json file containg only `{}`,
* `Suggestions.json` containting frame suggestions by users, should start out as empty json file containg only `{}`.

## Index Generation & Lexicon Filtering
To generate the required data from `structured_raw` the `structured_data.py` script should be ran. By running `filter_lexical_lookup.py`, the lexicon is reduced to only the relevant frames. 
