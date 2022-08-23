call ..\venv\Scripts\activate

call gen-python cosmos_bc_model.yaml > cosmos_bc_model.py
call gen-yuml cosmos_bc_model.yaml > cosmos_bc_model.yuml
call gen-json-schema .\cosmos_bc_model.yaml > cosmos_bc_model.json
call python .\create_svg.py .\cosmos_bc_model.yaml .\cosmos_bc_model.svg
