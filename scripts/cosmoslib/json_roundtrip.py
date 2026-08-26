"""
Flattens a raw CDISC Library API JSON record (one BC/SDTM/CRF specialization, as returned
by e.g. CDISCLibraryClient.get_bc_latest_biomedicalconcept() /
get_sdtm_latest_sdtm_datasetspecialization()) into row dicts shaped like the curation-
spreadsheet columns excel_reader.read_named_range() produces - for ad hoc round-trip
comparison against curation data, replacing utilities/macros/read_{bc,sdtm,crf}_from_json.sas.
Used by scripts/dump_{bc,sdtm,crf}_from_json.py; not used by any converter or validator.

Field mappings mirror the already-working, independently-authored JSON parsing in
scripts/create_cosmos_{bc,sdtm,crf}_excel.py's -s API path (get_bc_data/get_bc_dec_data,
get_sdtm_data/get_sdtm_variable_data, get_crf_data/get_crf_item_data) rather than
re-deriving from the SAS macros' dense, conditionally-branching PROC SQL joins (which switch
between a JSON *package* export's _links-based cross-references and a live single-record
fetch's inline fields) - there's no SAS installation available to verify a from-scratch
re-derivation against, whereas create_cosmos_*_excel.py's parsing of this exact live-API
shape is already exercised in practice. Confirmed byte-for-byte against real published data:
bc_rows_from_json(yaml.safe_load(open("yaml/20260714_r18/bc/bc__c191040.yaml"))) reproduces
the original curation row from R18_BC_PASI_FREDRIKSSON.xlsx exactly, and likewise for
sdtm_rows_from_json() against sdtm_pasi03headscaling.yaml.
"""


def _join(values):
    return ";".join(str(value) for value in values)


def _yn(obj, key):
    """SAS-QUIRK equivalent: the generated YAML stores these as YAML booleans
    (mandatoryVariable: true/false), but the curation spreadsheet - and so this round-trip
    row shape - represents them as "Y"/"N"/"" text, matching nsv_flag/mandatory_variable/etc.
    in cosmoslib.{bc,sdtm,crf}_converter."""
    value = obj.get(key)
    if value is None:
        return ""
    return "Y" if value else "N"


def bc_rows_from_json(bc):
    """One row per DEC (or one row with blank dec_* fields if there are none), matching the
    BC curation sheet's one-row-per-DEC convention."""
    links = bc.get("_links") or {}
    parent = links.get("parentBiomedicalConcept")
    if parent:
        parent_bc_id = parent.get("href", "").split("/")[-1]
    else:
        parent_bc_id = bc.get("parentConceptId", "")

    parent_package = links.get("parentPackage")
    if parent_package:
        package_date = parent_package.get("href", "").split("/")[-2]
    else:
        package_date = bc.get("packageDate", "")

    coding = bc.get("coding", [])
    base = {
        "package_date": package_date,
        "bc_id": bc.get("conceptId", ""),
        "ncit_code": bc.get("href", "").split("/")[-1],
        "parent_bc_id": parent_bc_id,
        "bc_categories": _join(bc.get("categories", [])),
        "short_name": bc.get("shortName", ""),
        "synonyms": _join(bc.get("synonyms", [])),
        "result_scales": _join(bc.get("resultScales", [])),
        "definition": bc.get("definition", ""),
        "system": _join(c.get("system", "") for c in coding),
        "system_name": _join(c.get("systemName", "") for c in coding),
        "code": _join(c.get("code", "") for c in coding),
    }

    decs = bc.get("dataElementConcepts", [])
    if not decs:
        return [dict(base, dec_id="", ncit_dec_code="", dec_label="", data_type="", example_set="")]

    return [
        dict(
            base,
            dec_id=dec.get("conceptId", ""),
            ncit_dec_code=dec.get("href", "").split("/")[-1],
            dec_label=dec.get("shortName", ""),
            data_type=dec.get("dataType", ""),
            example_set=_join(dec.get("exampleSet", [])),
        )
        for dec in decs
    ]


def sdtm_rows_from_json(sdtm):
    """One row per variable, matching the SDTM curation sheet's one-row-per-variable
    convention."""
    links = sdtm.get("_links") or {}
    parent = links.get("parentBiomedicalConcept")
    if parent:
        bc_id = parent.get("href", "").split("/")[-1]
    else:
        bc_id = sdtm.get("biomedicalConceptId", "")

    parent_package = links.get("parentPackage")
    if parent_package:
        package_date = parent_package.get("href", "").split("/")[-2]
    else:
        package_date = sdtm.get("packageDate", "")

    base = {
        "package_date": package_date,
        "bc_id": bc_id,
        "sdtmig_start_version": sdtm.get("sdtmigStartVersion", ""),
        "sdtmig_end_version": sdtm.get("sdtmigEndVersion", ""),
        "domain": sdtm.get("domain", ""),
        "vlm_source": sdtm.get("source", ""),
        "vlm_group_id": sdtm.get("datasetSpecializationId", ""),
        "short_name": sdtm.get("shortName", ""),
    }

    rows = []
    for order, variable in enumerate(sdtm.get("variables", []), start=1):
        codelist = variable.get("codelist") or {}
        assigned_term = variable.get("assignedTerm") or {}
        relationship = variable.get("relationship") or {}
        rows.append(dict(
            base,
            order=order,
            sdtm_variable=variable.get("name", ""),
            dec_id=variable.get("dataElementConceptId", ""),
            nsv_flag=_yn(variable, "isNonStandard"),
            codelist=codelist.get("conceptId", ""),
            codelist_submission_value=codelist.get("submissionValue", ""),
            subset_codelist=variable.get("subsetCodelist", ""),
            value_list=_join(variable.get("valueList", [])),
            assigned_term=assigned_term.get("conceptId", ""),
            assigned_value=assigned_term.get("value", ""),
            role=variable.get("role", ""),
            subject=relationship.get("subject", ""),
            linking_phrase=relationship.get("linkingPhrase", ""),
            predicate_term=relationship.get("predicateTerm", ""),
            object=relationship.get("object", ""),
            data_type=variable.get("dataType", ""),
            length=variable.get("length"),
            format=variable.get("format", ""),
            significant_digits=variable.get("significantDigits"),
            mandatory_variable=_yn(variable, "mandatoryVariable"),
            mandatory_value=_yn(variable, "mandatoryValue"),
            origin_type=variable.get("originType", ""),
            origin_source=variable.get("originSource", ""),
            comparator=variable.get("comparator", ""),
            vlm_target=_yn(variable, "vlmTarget"),
        ))
    return rows


def crf_rows_from_json(crf):
    """One row per item, matching the CRF curation sheet's one-row-per-item convention."""
    base = {
        "package_date": crf.get("packageDate", ""),
        "bc_id": crf.get("biomedicalConceptId", ""),
        "vlm_group_id": crf.get("sdtmDatasetSpecializationId", ""),
        "standard": crf.get("standard", ""),
        "standard_start_version": crf.get("standardStartVersion", ""),
        "standard_end_version": crf.get("standardEndVersion", ""),
        "domain": crf.get("domain", ""),
        "crf_group_id": crf.get("crfSpecializationId", ""),
        "implementation_option": crf.get("implementationOption", ""),
        "scenario": crf.get("scenario", ""),
        "short_name": crf.get("shortName", ""),
    }

    rows = []
    for item in crf.get("items", []):
        codelist = item.get("codelist") or {}
        prepopulated = item.get("prepopulatedValue") or {}
        sdtm_target = item.get("sdtmTarget") or {}
        value_list = item.get("valueList") or []
        rows.append(dict(
            base,
            crf_item=item.get("name", ""),
            variable_name=item.get("variableName", ""),
            dec_id=item.get("dataElementConceptId", ""),
            question_text=item.get("questionText", ""),
            prompt=item.get("prompt", ""),
            completion_instructions=item.get("completionInstructions", ""),
            order_number=item.get("orderNumber"),
            mandatory_variable=_yn(item, "mandatoryVariable"),
            data_type=item.get("dataType", ""),
            length=item.get("length"),
            significant_digits=item.get("significantDigits"),
            display_hidden=_yn(item, "displayHidden"),
            derived_variable=_yn(item, "derivedVariable"),
            derivation_description=item.get("derivationDescription", ""),
            codelist=codelist.get("conceptId", ""),
            codelist_submission_value=codelist.get("submissionValue", ""),
            value_display_list=_join(v.get("displayValue", "") for v in value_list),
            value_list=_join(v.get("value", "") for v in value_list),
            selection_type=item.get("selectionType", ""),
            prepopulated_term=prepopulated.get("value", ""),
            prepopulated_code=prepopulated.get("conceptId", ""),
            sdtm_target_variable=_join(sdtm_target.get("sdtmVariables", [])),
            sdtm_annotation=sdtm_target.get("sdtmAnnotation", ""),
        ))
    return rows
