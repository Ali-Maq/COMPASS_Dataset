
#	Exact file name	Type	Grain (one row =)	Rows × Cols*	What’s inside / why you keep it
Clinical DATA tables – CSV format					
1	MMRF_CoMMpass_IA14_PER_PATIENT.csv	Data	Patient	1 143 × 93	Baseline demographics, diagnosis metadata, high-level outcomes.
2	MMRF_CoMMpass_IA14_PER_PATIENT_VISIT.csv	Data	Scheduled visit	17 321 × 638	Longitudinal labs, disease status, vitals, response flags.
3	MMRF_CoMMpass_IA14_STAND_ALONE_ADMISSIONS.csv	Data	In-patient admission	11 595 × 8	Length of stay, admitting reason, discharge.
4	MMRF_CoMMpass_IA14_STAND_ALONE_EMERGENCY_DEPT.csv	Data	ED encounter	11 501 × 8	ED reason & disposition.
5	MMRF_CoMMpass_IA14_STAND_ALONE_AE.csv	Data	Adverse event	12 675 × 73	CTCAE-coded AE term, grade, onset/resolve days.
6	MMRF_CoMMpass_IA14_STAND_ALONE_FAMHX.csv	Data	Family-history item	1 327 × 13	Relative class & condition (adds hereditary-risk context).
7	MMRF_CoMMpass_IA14_STAND_ALONE_MEDHX.csv	Data	Medical-history item	2 270 × 11	Baseline comorbidities.
8	MMRF_CoMMpass_IA14_STAND_ALONE_SURVIVAL.csv	Data	Survival summary	1 143 × 56	Pre-calculated OS / PFS days, vital status.
9	MMRF_CoMMpass_IA14_STAND_ALONE_TREATMENT_REGIMEN.csv	Data	Therapy line / regimen	8 419 × 21	Drugs, line#, dates, SCT flag.
10	MMRF_CoMMpass_IA14_STAND_ALONE_TRTRESP.csv	Data	Response record	3 375 × 46	Best response (sCR/VGPR…), MRD, response/relapse dates.
Clinical DATA tables – XLSX duplicates (same content as CSV but in Excel; keep only if you prefer XLSX)					
11	MMRF_CoMMpass_IA14_PER_PATIENT.xlsx	Data (duplicate of #1)	Patient	1 143 × 93	Same rows as the CSV.
12	MMRF_CoMMpass_IA14_STAND_ALONE_ADMISSIONS.xlsx	Data dup. of #3	Admission	11 595 × 8	〃
13	MMRF_CoMMpass_IA14_STAND_ALONE_AE.xlsx	Data dup. of #5	AE	12 675 × 73	〃
14	MMRF_CoMMpass_IA14_STAND_ALONE_EMERGENCY_DEPT.xlsx	Data dup. of #4	ED	11 501 × 8	〃
15	MMRF_CoMMpass_IA14_STAND_ALONE_FAMHX.xlsx	Data dup. of #6	Fam-Hx	1 327 × 13	〃
16	MMRF_CoMMpass_IA14_STAND_ALONE_MEDHX.xlsx	Data dup. of #7	Med-Hx	2 270 × 11	〃
17	MMRF_CoMMpass_IA14_STAND_ALONE_SURVIVAL.xlsx	Data dup. of #8	Survival	1 143 × 56	〃
18	MMRF_CoMMpass_IA14_STAND_ALONE_TREATMENT_REGIMEN.xlsx	Data dup. of #9	Regimen	8 419 × 21	〃
19	MMRF_CoMMpass_IA14_STAND_ALONE_TRTRESP.xlsx	Data dup. of #10	Response	3 375 × 46	〃
20	MMRF_CoMMpass_IA14_PER_PATIENT_VISIT.xlsx	Metadata only	Variable dictionary	—	First sheet = column definitions for the massive VISIT CSV; no subject rows.
House-keeping & temporary					
21	MMRF_CoMMpass_IA14_PER_PATIENT.xlsx (second copy)	Duplicate of #11	—	—	Identical; safe to delete or ignore.
22	~$MMRF_CoMMpass_IA14_PER_PATIENT.xlsx	MS-Office lock file	—	—	Zero-byte temp created by Excel; delete.
