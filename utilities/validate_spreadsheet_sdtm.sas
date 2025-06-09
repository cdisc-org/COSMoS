%let root=C:/_github/cdisc-org/COSMoS;
%include "&root/utilities/config.sas";

%let _debug=0;
%let print_html=0;

title01 "&now";


/* Package 1*/

%let excel_file=&root/curation/BC_Package_2022_10_26.xlsx;

%ReadExcel(file=&excel_file, range=Conceptual VS BC$, dsout=bc1_1);
%ReadExcel(file=&excel_file, range=%str(Conceptual LB (Common) BC)$, dsout=bc1_2);

%ReadExcel(file=&excel_file, range=SDTM VS BC$, dsout=sdtm1_1);
%ReadExcel(file=&excel_file, range=%str(SDTM LB BC)$, dsout=sdtm1_2);


/* Package 2 */

%let excel_file=&root/curation/BC_Package_2023_02_13.xlsx;

%ReadExcel(file=&excel_file, range=%str(BC LB (Common))$, dsout=bc2_1);
%ReadExcel(file=&excel_file, range=%str(BC LB (TIG Biomarkers))$, dsout=bc2_2);

%ReadExcel(file=&excel_file, range=%str(SDTM LB)$, dsout=sdtm2_1);
%ReadExcel(file=&excel_file, range=%str(SDTM LB (TIG Biomarkers))$, dsout=sdtm2_2);

%get_Subset_Codelists(file=&excel_file, range=Subset Codelists$, dsout=subsets);


/* Package 3 */

%let excel_file=&root/curation/BC_Package_2023_03_31.xlsx;

%ReadExcel(file=&excel_file, range=%str(BC_DM)$, dsout=bc3_1);
%ReadExcel(file=&excel_file, range=%str(BC_VS)$, dsout=bc3_2);
%ReadExcel(file=&excel_file, range=%str(BC_LB)$, dsout=bc3_3);
%ReadExcel(file=&excel_file, range=%str(BC_MB)$, dsout=bc3_4);
%ReadExcel(file=&excel_file, range=%str(BC_AE)$, dsout=bc3_5);
%ReadExcel(file=&excel_file, range=%str(BC_MH)$, dsout=bc3_7);
%ReadExcel(file=&excel_file, range=%str(BC_CM)$, dsout=bc3_8);
%ReadExcel(file=&excel_file, range=%str(BC_RE)$, dsout=bc3_9);
%ReadExcel(file=&excel_file, range=%str(BC_PR)$, dsout=bc3_10);
%ReadExcel(file=&excel_file, range=%str(BC_BE)$, dsout=bc3_11);
%ReadExcel(file=&excel_file, range=%str(BC_EG)$, dsout=bc3_12);
%ReadExcel(file=&excel_file, range=%str(BC_DS)$, dsout=bc3_13);


/* Package 4 - Oncology */

%let excel_file=&root/curation/BC_Package_R4_Oncology_RECIST11_2023_07_06.xlsx;

%ReadExcel(file=&excel_file, range=%str(BC TU_TR_RS)$, dsout=bc4_onco_1);

%ReadExcel(file=&excel_file, range=%str(SDTM_TU)$, dsout=sdtm4_onco_1, drop=%str(drop=significant_digits));
%ReadExcel(file=&excel_file, range=%str(SDTM_TR)$, dsout=sdtm4_onco_2, drop=%str(drop=length significant_digits));
%ReadExcel(file=&excel_file, range=%str(SDTM_RS)$, dsout=sdtm4_onco_3, drop=%str(drop=length significant_digits));


/* Package 4 - Non-oncology*/

%let excel_file=&root/curation/BC_Package_R4_2023_07_06.xlsx;

%ReadExcel(file=&excel_file, range=%str(BC_AE)$, dsout=bc4_1);
%ReadExcel(file=&excel_file, range=%str(BC_BE)$, dsout=bc4_2);
%ReadExcel(file=&excel_file, range=%str(BC_BE_EDITS)$, dsout=bc4_3);
%ReadExcel(file=&excel_file, range=%str(BC_DS)$, dsout=bc4_4);
%ReadExcel(file=&excel_file, range=%str(BC_EG)$, dsout=bc4_5);
%ReadExcel(file=&excel_file, range=%str(BC_EG_EDITS)$, dsout=bc4_6);
%ReadExcel(file=&excel_file, range=%str(BC_LB_(TIG)_Biomarkers)$, dsout=bc4_7);
%ReadExcel(file=&excel_file, range=%str(BC_LB_EDITS)$, dsout=bc4_8);
%ReadExcel(file=&excel_file, range=%str(BC_MH)$, dsout=bc4_9);
%ReadExcel(file=&excel_file, range=%str(BC_PR_EDITS)$, dsout=bc4_10);
%ReadExcel(file=&excel_file, range=%str(BC_VS_EDITS)$, dsout=bc4_11);

%ReadExcel(file=&excel_file, range=%str(SDTM_AE)$, dsout=sdtm4_1, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_BE)$, dsout=sdtm4_2, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_DS)$, dsout=sdtm4_3, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_EG)$, dsout=sdtm4_4, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_LB)$, dsout=sdtm4_5, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_LB_EDITS)$, dsout=sdtm4_6, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_LB_EDITS_2)$, dsout=sdtm4_7, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_MB)$, dsout=sdtm4_8, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_MH)$, dsout=sdtm4_9, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_PR)$, dsout=sdtm4_10, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_VS)$, dsout=sdtm4_11, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_VS_EDITS)$, dsout=sdtm4_12, drop=%str(drop=length significant_digits format));


/* Package 5 - */

%let excel_file=&root/curation/BC_Package_R5_LZZT.xlsx;

%ReadExcel(file=&excel_file, range=%str(BC_AE_EDITS)$, dsout=bc5_1); 
%ReadExcel(file=&excel_file, range=%str(BC_CM_EDITS)$, dsout=bc5_2); 
%ReadExcel(file=&excel_file, range=%str(BC_DS_EDITS)$, dsout=bc5_3); 
%ReadExcel(file=&excel_file, range=%str(BC_EC)$, dsout=bc5_4); 
%ReadExcel(file=&excel_file, range=%str(BC_LB)$, dsout=bc5_5); 
%ReadExcel(file=&excel_file, range=%str(BC_LB_EDITS)$, dsout=bc5_6); 
%ReadExcel(file=&excel_file, range=%str(BC_MB)$, dsout=bc5_7); 
%ReadExcel(file=&excel_file, range=%str(BC_MH_EDITS)$, dsout=bc5_8); 
%ReadExcel(file=&excel_file, range=%str(BC_PR_EDITS)$, dsout=bc5_9); 

%ReadExcel(file=&excel_file, range=%str(SDTM_AE_EDITS)$, dsout=sdtm5_1, drop=%str(drop=length significant_digits format)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_CM)$, dsout=sdtm5_2, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_DS_EDITS)$, dsout=sdtm5_3, drop=%str(drop=length significant_digits format)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_EC)$, dsout=sdtm5_4, drop=%str(drop=length significant_digits format)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_LB)$, dsout=sdtm5_5, drop=%str(drop=length significant_digits format)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_LB_EDITS)$, dsout=sdtm5_6, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_MB)$, dsout=sdtm5_7, drop=%str(drop=length significant_digits format)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_MH)$, dsout=sdtm5_8, drop=%str(drop=length significant_digits format)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_PR_EDITS)$, dsout=sdtm5_9, drop=%str(drop=length significant_digits format));

%get_Subset_Codelists(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);


/* Package 6 - */

%let excel_file=&root/curation/BC_Package_R6_LZZT.xlsx;

%ReadExcel(file=&excel_file, range=%str(BC_CM_EDITS)$, dsout=bc6_01); 
%ReadExcel(file=&excel_file, range=%str(BC_DS)$, dsout=bc6_02); 
%ReadExcel(file=&excel_file, range=%str(BC_EG_EDITS)$, dsout=bc6_03); 
%ReadExcel(file=&excel_file, range=%str(BC_EX)$, dsout=bc6_04); 
%ReadExcel(file=&excel_file, range=%str(BC_IE)$, dsout=bc6_05); 
%ReadExcel(file=&excel_file, range=%str(BC_LB)$, dsout=bc6_06); 
%ReadExcel(file=&excel_file, range=%str(BC_LB_EDITS)$, dsout=bc6_07); 
%ReadExcel(file=&excel_file, range=%str(BC_MH_EDITS)$, dsout=bc6_08); 
%ReadExcel(file=&excel_file, range=%str(BC_PR)$, dsout=bc6_09); 
%ReadExcel(file=&excel_file, range=%str(BC_QS)$, dsout=bc6_10); 
%ReadExcel(file=&excel_file, range=%str(BC_SC)$, dsout=bc6_11); 
%ReadExcel(file=&excel_file, range=%str(BC_SU)$, dsout=bc6_12); 
%ReadExcel(file=&excel_file, range=%str(BC_VS_EDITS)$, dsout=bc6_13); 

%ReadExcel(file=&excel_file, range=%str(SDTM_CM_EDITS)$, dsout=sdtm6_01, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_DS)$, dsout=sdtm6_02, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_EG_EDITS)$, dsout=sdtm6_03, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_EX)$, dsout=sdtm6_04, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_IE)$, dsout=sdtm6_05, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_LB)$, dsout=sdtm6_06, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_LB_EDITS)$, dsout=sdtm6_07, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_MH)$, dsout=sdtm6_08, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_PR)$, dsout=sdtm6_09, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_QS)$, dsout=sdtm6_10, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_SC)$, dsout=sdtm6_11, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_SU)$, dsout=sdtm6_12, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_VS_EDITS)$, dsout=sdtm6_13, drop=%str(drop=length significant_digits format));

%get_Subset_Codelists(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);


/* Package 7 - */

%let excel_file=&root/curation/BC_Package_R7_GF.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_GF)$, dsout=bc7_01, drop=%str(drop=change_history)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_GF)$, dsout=sdtm7_01, drop=%str(drop=length significant_digits format));

%let excel_file=&root/curation/BC_Package_R7_FACV.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_FACV)$, dsout=bc7_02, drop=%str(drop=change_history)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_FACV)$, dsout=sdtm7_02, drop=%str(drop=length significant_digits format));

%let excel_file=&root/curation/BC_Package_R7_DD.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_DD)$, dsout=bc7_03, drop=%str(drop=change_history)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_DD)$, dsout=sdtm7_03, drop=%str(drop=length significant_digits format));

%let excel_file=&root/curation/BC_Package_R7_BC_updates.xlsx;
%ReadExcel(file=&excel_file, range=%str(Biomedical Concepts)$, dsout=bc7_04, drop=%str(drop=change_history)); 

%let excel_file=&root/curation/BC_Package_R7_SDTM_updates.xlsx;
%ReadExcel(file=&excel_file, range=%str(SDTM Dataset Specializations)$, dsout=sdtm7_04, drop=%str(drop=length significant_digits format)); 


/* Package 8 - */

%let excel_file=&root/curation/BC_Package_R8_LUGANO_RS.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_RS)$, dsout=bc8_01, drop=%str(drop=change_history)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_RS)$, dsout=sdtm8_01, drop=%str(drop=length significant_digits format));

%let excel_file=&root/curation/BC_Package_R8_RANO_RS.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_RS)$, dsout=bc8_02, drop=%str(drop=change_history)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_RS)$, dsout=sdtm8_02, drop=%str(drop=length significant_digits format));

%let excel_file=&root/curation/BC_Package_R8_BC_updates.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_Onco_Corrections)$, dsout=bc8_03, drop=%str(drop=change_history)); 
%ReadExcel(file=&excel_file, range=%str(BC_New)$, dsout=bc8_04, drop=%str(drop=change_history));

%let excel_file=&root/curation/BC_Package_R8_SDTM_updates.xlsx;
%ReadExcel(file=&excel_file, range=%str(SDTM_Corrections)$, dsout=sdtm8_03, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_Corrections_1)$, dsout=sdtm8_04, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_Corrections_2)$, dsout=sdtm8_05, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_New)$, dsout=sdtm8_06, drop=%str(drop=length significant_digits format));


/* Package 9 - */

%let release=9;
%let excel_file=&root/curation/BC_Package_R9_public_review_updates.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_Corrections)$, dsout=bc9_01, drop=%str(drop=History_of_Change)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_Corrections)$, dsout=sdtm9_01, drop=%str(drop=length significant_digits format));


/* Package 10 - */

%let release=10;
%let excel_file=&root/curation/BC_Package_R10.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_RP)$, dsout=bc10_01, drop=%str(drop=History_of_Change)); 
%ReadExcel(file=&excel_file, range=%str(BC_SR)$, dsout=bc10_02, drop=%str(drop=change_history));
%ReadExcel(file=&excel_file, range=%str(SDTM_RP)$, dsout=sdtm10_01, drop=%str(drop=length significant_digits format)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_SR)$, dsout=sdtm10_02, drop=%str(drop=length significant_digits format));

%let excel_file=&root/curation/BC_Package_R10_Breast_Cancer.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_MI)$, dsout=bc10_03, drop=%str(drop=change_history)); 
%ReadExcel(file=&excel_file, range=%str(BC_PR)$, dsout=bc10_04, drop=%str(drop=change_history));
%ReadExcel(file=&excel_file, range=%str(SDTM_MI)$, dsout=sdtm10_03, drop=%str(drop=length significant_digits format)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_PR)$, dsout=sdtm10_04, drop=%str(drop=length significant_digits format));
%ReadExcel(file=&excel_file, range=%str(SDTM_CM)$, dsout=sdtm10_05, drop=%str(drop=length significant_digits format));

%let excel_file=&root/curation/BC_Package_R10_ECG.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_EG)$, dsout=bc10_05); 

%let excel_file=&root/curation/BC_Package_R10_ECG_SDTM.xlsx;
%ReadExcel(file=&excel_file, range=%str(SDTM_EG)$, dsout=sdtm10_06, drop=%str(drop=length significant_digits format)); 


/* Package 11 - */

%let release=11;
%let excel_file=&root/curation/BC_Package_R11_BC_Lindus Health.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_Breast_Cancer)$, dsout=bc11_01, drop=%str(drop=change_history)); 

%let excel_file=&root/curation/BC_Package_R11_UR.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_UR)$, dsout=bc11_02, drop=%str(drop=History_of_Change)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_UR)$, dsout=sdtm11_01, drop=%str(drop=length significant_digits format)); 

%let excel_file=&root/curation/BC_Package_R11_LB_GF_Edits.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_LB)$, dsout=bc11_03); 
%ReadExcel(file=&excel_file, range=%str(BC_GF)$, dsout=bc11_04, drop=%str(drop=change_history)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_LB)$, dsout=sdtm11_02, drop=%str(drop=length significant_digits format)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_GF)$, dsout=sdtm11_03, drop=%str(drop=length significant_digits format)); 

%let excel_file=&root/curation/BC_Package_R11_DM.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_DM)$, dsout=bc11_05, drop=%str(drop=change_history)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_DM)$, dsout=sdtm11_04, drop=%str(drop=length significant_digits format)); 

%let excel_file=&root/curation/BC_Package_R11_MK.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_MK)$, dsout=bc11_06, drop=%str(drop=change_history)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_MK)$, dsout=sdtm11_05, drop=%str(drop=length significant_digits format)); 

%let excel_file=&root/curation/BC_Package_R11_VS.xlsx;
%ReadExcel(file=&excel_file, range=%str(SDTM_VS)$, dsout=sdtm11_06, drop=%str(drop=length significant_digits format)); 

%let excel_file=&root/curation/BC_Package_R11_AE_Edit.xlsx;
%ReadExcel(file=&excel_file, range=%str(SDTM_AE)$, dsout=sdtm11_07, drop=%str(drop=length significant_digits format)); 


/* Package 12 - */

%let release=12;
%let excel_file=&root/curation/draft/package12/R12_6MWT.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_6MWT)$, dsout=bc12_01); 
%ReadExcel(file=&excel_file, range=%str(SDTM_6MWT)$, dsout=sdtm12_01, drop=%str(drop=length significant_digits format change_history)); 

%let excel_file=&root/curation/draft/package12/R12_BC_New.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_Test_Occurrence)$, dsout=bc12_02); 
%ReadExcel(file=&excel_file, range=%str(BC_BRTHDTC)$, dsout=bc12_03); 

%let excel_file=&root/curation/draft/package12/R12_BC_Edits.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_EDITS)$, dsout=bc12_04); 

%let excel_file=&root/curation/draft/package12/R12_BC_IE.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_IE)$, dsout=bc12_05); 

%let excel_file=&root/curation/draft/package12/R12_LB.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_LB_EDITS)$, dsout=bc12_06); 
%ReadExcel(file=&excel_file, range=%str(SDTM_LB_EDITS)$, dsout=sdtm12_02, drop=%str(drop=length significant_digits format)); 

%let excel_file=&root/curation/draft/package12/R12_SDTM_Misc.xlsx;
%ReadExcel(file=&excel_file, range=%str(SDTM_brthdtc_new)$, dsout=sdtm12_03, drop=%str(drop=length significant_digits format)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_linking_phrase_edits)$, dsout=sdtm12_04, drop=%str(drop=length significant_digits format)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_Edits)$, dsout=sdtm12_05, drop=%str(drop=length significant_digits format)); 

%let excel_file=&root/curation/draft/package12/R12_TS.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_TS)$, dsout=bc12_07); 
%ReadExcel(file=&excel_file, range=%str(SDTM_TS)$, dsout=sdtm12_06, drop=%str(drop=length significant_digits format)); 

%let excel_file=&root/curation/draft/package12/R12_BC_QRS_ADAS-Cog.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_ADAS-Cog)$, dsout=bc12_08); 

%let excel_file=&root/curation/draft/package12/R12_SDTM_QRS_ADAS-Cog.xlsx;
%ReadExcel(file=&excel_file, range=%str(SDTM_ADAS-Cog)$, dsout=sdtm12_07, drop=%str(drop=length significant_digits format)); 

%let excel_file=&root/curation/draft/package12/R12_BC_Event_Occurrence.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_Indicators)$, dsout=bc12_09); 

%let excel_file=&root/curation/draft/package12/R12_BC_SDTM_LB_Japan_Group.xlsx;
%ReadExcel(file=&excel_file, range=%str(NEW_BC_LAB_2025.04.24)$, dsout=bc12_10); 
%ReadExcel(file=&excel_file, range=%str(NEW_SDTM_LAB_2025.04.24)$, dsout=sdtm12_08, drop=%str(drop=length significant_digits format)); 

%let excel_file=&root/curation/draft/package12/R12_BC_SDTM_MK_Part2.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_MK)$, dsout=bc12_11); 
%ReadExcel(file=&excel_file, range=%str(BC_MK_Edits)$, dsout=bc12_12); 
%ReadExcel(file=&excel_file, range=%str(SDTM_MK)$, dsout=sdtm12_09, drop=%str(drop=length significant_digits format)); 
%ReadExcel(file=&excel_file, range=%str(SDTM_MK_Edits)$, dsout=sdtm12_10, drop=%str(drop=length significant_digits format)); 

%let excel_file=&root/curation/draft/package12/R12_BC_SDTM_QRS_APACHE.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_APACHE II)$, dsout=bc12_13); 
%ReadExcel(file=&excel_file, range=%str(SDTM_APACHE II)$, dsout=sdtm12_11, drop=%str(drop=length significant_digits format)); 

%let excel_file=&root/curation/draft/package12/R12_BC_SDTM_QRS_AIMS.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_AIMS)$, dsout=bc12_14); 
%ReadExcel(file=&excel_file, range=%str(SDTM_AIMS)$, dsout=sdtm12_12, drop=%str(drop=length significant_digits format)); 

%let excel_file=&root/curation/draft/package12/R12_SDTM_EC_Linking_Edits.xlsx;
%ReadExcel(file=&excel_file, range=%str(SDTM_EC_EDITS)$, dsout=sdtm12_13, drop=%str(drop=length significant_digits format)); 

%let excel_file=&root/curation/draft/package12/R12_BC_SDTM_MH_AE_CM_SU.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_MH_AE_CM_SU)$, dsout=bc12_15);
%ReadExcel(file=&excel_file, range=%str(SDTM_MH_AE_CM_SU)$, dsout=sdtm12_14, drop=%str(drop=length significant_digits format));

%let excel_file=&root/curation/draft/package12/R12_SDTM_TU_TULOC_Linking_Edits.xlsx;
%ReadExcel(file=&excel_file, range=%str(SDTM_TU)$, dsout=sdtm12_15, drop=%str(drop=length significant_digits format));

%let excel_file=&root/curation/draft/package12/R12_BC_SDTM_GF.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_GF)$, dsout=bc12_16); 
%ReadExcel(file=&excel_file, range=%str(SDTM_GF)$, dsout=sdtm12_16, drop=%str(drop=length significant_digits format));

%let excel_file=&root/curation/draft/package12/R12_BC_SDTM_QRS_ATLAS.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_ATLAS)$, dsout=bc12_17); 
%ReadExcel(file=&excel_file, range=%str(SDTM_ATLAS)$, dsout=sdtm12_17, drop=%str(drop=length significant_digits format));

%let excel_file=&root/curation/draft/package12/R12_BC_SDTM_QRS_HAM-A.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_HAM-A)$, dsout=bc12_18); 
%ReadExcel(file=&excel_file, range=%str(SDTM_HAM-A)$, dsout=sdtm12_18, drop=%str(drop=length significant_digits format));

%let excel_file=&root/curation/draft/package12/R12_BC_QRS.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_QRS)$, dsout=bc12_19); 

/************************************************************************************************************************/

data bc(drop=change_history F1: F2: i vname vvalue);
  length package_date $64 bc_id ncit_code parent_bc_id dec_id ncit_dec_code $64 bc_categories synonyms result_scales definition 
         system	system_name	code change_history $5124 short_name dec_label data_type $512 example_set vvalue $32000 vname $32;
  retain _excel_file_ _tab_ package_date bc_id ncit_code parent_bc_id bc_categories short_name 
         synonyms result_scales definition system system_name code dec_id ncit_dec_code dec_label data_type example_set;
  set bc:(where=(not missing(bc_id)));
  
  array carray{*} _character_;
  * if missing(bc_id) then delete;
  do i=1 to dim(carray);
    vname = vname(carray[i]);
    vvalue = (translate (carray[i], "", cats(collate (1, 31), collate (128, 255))));
    if vvalue ne carray[i] then do;
     put '### CHARACTER CODING ISSUE: ' _excel_file_= _tab_= vname= bc_id= short_name= dec_id= dec_label= / @10 carray[i] / @10 vvalue;
    end; 
  end;
  package_date = upcase(package_date);
run;  

%if &_debug gt 1 %then %do;
  proc freq data=bc;
    tables bc_id * package_date / nopercent norow nocol;
  run;  
%end;  

%if &print_html=1 %then %do;
  ods listing close;
  ods html5 file="&root/utilities/reports/validate_spreadsheet_bc_R&release._&todays..html";
  ods excel options(sheet_name="BC &todays" flow="tables" autofilter = 'all') file="&root/utilities/reports/validate_spreadsheet_bc_R&release._&todays..xlsx";

    proc print data=bc;
    run;

  ods html5 close;
  ods excel close;
  ods listing;
%end;

/************************************************************************************************************************/

data sdtm(drop=change_history F3: F4:  i vname vvalue);
  length order 8 package_date $64 sdtmig_start_version sdtmig_end_version bc_id dec_id $64 domain vlm_group_id vlm_source sdtm_variable $128
         codelist subset_codelist value_list assigned_value assigned_term subject linking_phrase predicate_term object 
         short_name role format data_type origin_type origin_source vlm_target change_history vvalue $32000 vname $32;
  retain _excel_file_ _tab_ order package_date sdtmig_start_version sdtmig_end_version bc_id domain vlm_group_id short_name vlm_source  
         sdtm_variable dec_id nsv_flag codelist codelist_submission_value assigned_term subset_codelist value_list assigned_value 
         subject linking_phrase predicate_term object format 
         vlm_target role data_type length significant_digits mandatory_variable mandatory_value origin_type origin_source comparator;
  set sdtm:(where=(not missing(vlm_group_id)));
  order=_n_;
  package_date = upcase(package_date);
  array carray{*} _character_;
  do i=1 to dim(carray);
    vname = vname(carray[i]);
    vvalue = (translate (carray[i], "", cats(collate (1, 31), collate (128, 255))));
    if vvalue ne carray[i] then do;
     put '### CHARACTER CODING ISSUE: ' _excel_file_= _tab_= vname= vlm_group_id= short_name= sdtm_variable= bc_id= dec_id= / @10 carray[i] / @10 vvalue ;
    end; 
  end;
run;  

%if &_debug gt 1 %then %do;
  proc freq data=sdtm;
    tables vlm_group_id * package_date / nopercent norow nocol;
    tables linking_phrase / nopercent norow nocol;
    tables predicate_term / nopercent norow nocol;
  run;  
%end;  

proc sql;
  create table sdtm_merged(drop=order)
  as select
    sdtm.*,
    ss.subset_value_list
  from work.sdtm sdtm
    left join subsets ss
  on sdtm.subset_codelist = ss.subset_short_name
  order by _excel_file_, _tab_, vlm_group_id, order
  ;
quit;     

%if &print_html=1 %then %do;
  ods listing close;
  ods html5 file="&root/utilities/reports/validate_spreadsheet_sdtm_R&release._&todays..html";
  ods excel options(sheet_name="SDTM &todays" flow="tables" autofilter = 'all') file="&root/utilities/reports/validate_spreadsheet_sdtm_R&release._&todays..xlsx";

    proc print data=sdtm_merged;
    run;

  ods html5 close;
  ods excel close;
  ods listing;
%end;


/************************************************************************************************************************/

ods listing close;
ods html5 file="&root/utilities/reports/validate_spreadsheet_sdtm_bc_issues_R&release._&todays..html";

  /* Unresolved BC Parent BCs */
  proc sql;
    title02 "Missing BC parent_bc_id link to BC bc_id";
      select _excel_file_, _tab_, package_date, bc_categories, bc_id, short_name, parent_bc_id
      from bc
      where 
        parent_bc_id not in (select bc_id from bc)
        and not missing(parent_bc_id)
      order by _excel_file_, _tab_, bc_categories, bc_id
      ;
  quit;

  /* Unresolved SDTM BCs */
  proc sql;
    title02 "Missing SDTM Specialization bc_id link to BC bc_id";
      select _excel_file_, _tab_, package_date, vlm_group_id, sdtm_variable, sd.bc_id
      from sdtm_merged sd
      where 
        sd.bc_id not in (select bc_id from bc)
      order by _excel_file_, _tab_, vlm_group_id, sdtm_variable
      ;
  quit;

  /* Unresolved SDTM BCs/DECs */
  proc sql;
    title02 "Missing SDTM Specialization bc_id/dec_id link to BC bc_id/dec_id";
    create table sdtm_bc_dec as
      select unique catx('-', bc_id, dec_id) as bc_dec
      from sdtm_merged
      where not missing(dec_id);

      select sbdi._excel_file_, sbdi._tab_, sbdi.package_date, sbdi.vlm_group_id, sbdi.sdtm_variable, sbdi.bc_id, sbdi.dec_id
      from sdtm_bc_dec sbd, sdtm_merged sbdi
      where 
        sbd.bc_dec not in (select unique catx('-', bc_id, dec_id) from bc) and
        catx('-', sbdi.bc_id, sbdi.dec_id) = sbd.bc_dec
      order by _excel_file_, _tab_, vlm_group_id, sdtm_variable
      ;
  quit;

  /* Duplicate BC records */
  proc sql;
    title02 "Duplicate BC records (package_date, bc_id, dec_id)";
      select _excel_file_, _tab_, package_date, bc_categories, bc_id, short_name, dec_id, dec_label
      from bc
      group by package_date, bc_id, dec_id
      having count(*) > 1
      ;
  run;

  /* Duplicate SDTM records */
  proc sql;
    title02 "Duplicate SDTM Specialization records (package_date, vlm_group_id, sdtm_variable)";
      select _excel_file_, _tab_, package_date, sdtmig_start_version,	sdtmig_end_version, vlm_group_id, sdtm_variable
      from sdtm_merged
      group by package_date, vlm_group_id, sdtm_variable
      having count(*) > 1
      ;
  run;

ods html5 close;
ods listing;
