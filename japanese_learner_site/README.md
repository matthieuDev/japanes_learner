

## Init data

run generate_datasets.py at the base of the project :

```
generate_datasets.py
```

and then run :

```
python manage.py loaddata japanese2latin/data_init.json
python manage.py loaddata latin2japanese/data_init.json
```

in japanese_learner_site/ folder