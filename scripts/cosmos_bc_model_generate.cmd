call gen-json-schema ../model/cosmos_bc_model.yaml > ../model/cosmos_bc_model.json
call python create_svg.py ../model/cosmos_bc_model.yaml ../model/cosmos_bc_model.svg
..\venv\Scripts\gen-erdiagram.exe --no-structural ../model/cosmos_bc_model.yaml > ../model/cosmos_bc_model.md
call gen-yuml ../model/cosmos_bc_model.yaml > ../model/cosmos_bc_model.yuml
call gen-plantuml ../model/cosmos_bc_model.yaml --directory ..\model
call gen-project -d ../project/bc ../model/cosmos_bc_model.yaml

call gen-python ../model/cosmos_bc_model.yaml > ../project/bc/cosmos_bc_model.py
call gen-python-api -R BiomedicalConcept ../model/cosmos_bc_model.yaml > ../project/bc/cosmos_bc_model_api.py
call gen-pydantic ../model/cosmos_bc_model.yaml > ../project/bc/cosmos_bc_model_pydantic.py
