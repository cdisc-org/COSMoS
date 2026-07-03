call gen-json-schema ../model/cosmos_sdtm_model.yaml > ../model/cosmos_sdtm_model.json
call python create_svg.py ../model/cosmos_sdtm_model.yaml ../model/cosmos_sdtm_model.svg
..\venv\Scripts\gen-erdiagram.exe --no-structural ../model/cosmos_sdtm_model.yaml > ../model/cosmos_sdtm_model.md
call gen-yuml ../model/cosmos_sdtm_model.yaml > ../model/cosmos_sdtm_model.yuml
call gen-plantuml ../model/cosmos_sdtm_model.yaml --directory ..\model
REM call gen-project -d ../project/sdtm ../model/cosmos_sdtm_model.yaml
call gen-doc .\model\cosmos_sdtm_model.yaml --directory project/sdtm/docs/ --subfolder-type-separation --hierarchical-class-view --diagram-type er_diagram --sort-by rank --include-top-level-diagram --truncate-descriptions false
call gen-python ../model/cosmos_sdtm_model.yaml > ../project/sdtm/cosmos_sdtm_model.py
call gen-python-api -R SDTMGroup ../model/cosmos_sdtm_model.yaml > ../project/sdtm/cosmos_sdtm_model_api.py
call gen-pydantic ../model/cosmos_sdtm_model.yaml > ../project/sdtm/cosmos_sdtm_model_pydantic.py
