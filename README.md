# TE-MPE-EP-3 - coding exercies
Coding exercises assigned as part of the TE-MPE-EP-3 technical assessment.

I will unpublish this repository once you ask me to do so.

## First exercise
### Execution output

```
[rdm@rdm-mbp ~/Documents/tech/te-mpe-ep-3-coding-exercises] λ python3 duplicate.py
Actual output matches the expected output.
Expected output: ['a', 'c', 'd']
Actual output: ['a', 'c', 'd']
Actual output matches the expected output.
Expected output: [{'a': 'b'}, {'d': 'e'}]
Actual output: [{'a': 'b'}, {'d': 'e'}]
```

## Second exercise
I decided to name the module `json_graph_extractor` since it can be used as a generic module
to extract information from a JSON file into a graph 
(so there could be more use cases other than listing packages and their dependencies)

### Usage
```python -m json_graph_extractor [filename]```

If `python` is not found, you might need to use `python3`, so the command would be:

```python3 -m json_graph_extractor [filename]```

#### Example

From the `te-mpe-ep-3-coding-exercises/02-json` directory you can run:

```python3 -m json_graph_extractor tmp/deps.json```

### Execution output
```
[rdm@rdm-mbp ~/Documents/tech/te-mpe-ep-3-coding-exercises/02-json] λ python3 -m json_graph_extractor tmp/deps.json
- pkg1
 - pkg2
  - pkg3
 - pkg3
- pkg2
 - pkg3
- pkg3
```

### Test outcome
```
[rdm@rdm-mbp ~/Documents/tech/te-mpe-ep-3-coding-exercises/02-json] λ python3 -m unittest tests/test_json_graph_extractor.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```