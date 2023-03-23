call ..\venv\Scripts\activate

call gen-python cosmos_cdash_bc_model.yaml > cosmos_cdash_bc_model.py
call gen-yuml cosmos_cdash_bc_model.yaml > cosmos_cdash_bc_model.yuml
call gen-python-api -R CDASHGroup cosmos_cdash_bc_model.yaml > cosmos_cdash_bc_model_api.py
call gen-erdiagram --no-structural cosmos_cdash_bc_model.yaml > cosmos_cdash_bc_model.md
call gen-json-schema .\cosmos_cdash_bc_model.yaml > cosmos_cdash_bc_model.json
call python .\create_svg.py .\cosmos_cdash_bc_model.yaml .\cosmos_cdash_bc_model.svg
