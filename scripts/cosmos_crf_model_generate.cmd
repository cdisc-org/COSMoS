call gen-json-schema ../model/cosmos_crf_model.yaml > ../model/cosmos_crf_model.json
call python create_svg.py ../model/cosmos_crf_model.yaml ../model/cosmos_crf_model.svg
..\venv\Scripts\gen-erdiagram.exe --no-structural ../model/cosmos_crf_model.yaml > ../model/cosmos_crf_model.md
call gen-yuml ../model/cosmos_crf_model.yaml > ../model/cosmos_crf_model.yuml
call gen-plantuml ../model/cosmos_crf_model.yaml --directory ..\model
call gen-project -d ../project/crf ../model/cosmos_crf_model.yaml

call gen-python ../model/cosmos_crf_model.yaml > ../project/crf/cosmos_crf_model.py
call gen-python-api -R CRFGroup ../model/cosmos_crf_model.yaml > ../project/crf/cosmos_crf_model_api.py
call gen-pydantic ../model/cosmos_crf_model.yaml > ../project/crf/cosmos_crf_model_pydantic.py
