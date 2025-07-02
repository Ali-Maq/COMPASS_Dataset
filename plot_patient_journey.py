import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def load_csv(name):
    return pd.read_csv(
        Path('clinical_data/actual_data_') / name,
        encoding='latin1',
        low_memory=False
    )

def get_patient_data(patient_id):
    data = {}
    data['per_patient'] = load_csv('MMRF_CoMMpass_IA14_PER_PATIENT.csv')
    data['per_patient'] = data['per_patient'][data['per_patient']['PUBLIC_ID']==patient_id]

    data['visits'] = load_csv('MMRF_CoMMpass_IA14_PER_PATIENT_VISIT.csv')
    data['visits'] = data['visits'][data['visits']['PUBLIC_ID']==patient_id][['VISITDY','VJ_INTERVAL']]

    data['admissions'] = load_csv('MMRF_CoMMpass_IA14_STAND_ALONE_ADMISSIONS.csv')
    data['admissions'] = data['admissions'][data['admissions']['public_id']==patient_id][['visitdy','ADM_PRIMARYREASON']]

    data['emergency'] = load_csv('MMRF_CoMMpass_IA14_STAND_ALONE_EMERGENCY_DEPT.csv')
    data['emergency'] = data['emergency'][data['emergency']['public_id']==patient_id][['visitdy','ED_PRIMARYREASON']]

    data['ae'] = load_csv('MMRF_CoMMpass_IA14_STAND_ALONE_AE.csv')
    data['ae'] = data['ae'][data['ae']['public_id']==patient_id][['visdy','aeterm']]

    data['regimen'] = load_csv('MMRF_CoMMpass_IA14_STAND_ALONE_TREATMENT_REGIMEN.csv')
    data['regimen'] = data['regimen'][data['regimen']['public_id']==patient_id][['startday','MMTX_THERAPY']]

    data['trtresp'] = load_csv('MMRF_CoMMpass_IA14_STAND_ALONE_TRTRESP.csv')
    data['trtresp'] = data['trtresp'][data['trtresp']['public_id']==patient_id][['trtstdy','trtname','trtshnm']]

    data['survival'] = load_csv('MMRF_CoMMpass_IA14_STAND_ALONE_SURVIVAL.csv')
    data['survival'] = data['survival'][data['survival']['public_id']==patient_id][['deathdy','lstalive']]

    return data

def build_timeline(data):
    events = []
    for dy, interval in data['visits'].itertuples(index=False):
        events.append({'day': dy, 'type': 'Visit', 'detail': interval})
    for dy, reason in data['admissions'].itertuples(index=False):
        events.append({'day': dy, 'type': 'Admission', 'detail': reason})
    for dy, reason in data['emergency'].itertuples(index=False):
        events.append({'day': dy, 'type': 'Emergency', 'detail': reason})
    for dy, term in data['ae'].itertuples(index=False):
        events.append({'day': dy, 'type': 'AE', 'detail': term})
    for dy, therapy in data['regimen'].itertuples(index=False):
        events.append({'day': dy, 'type': 'Regimen', 'detail': therapy})
    for dy, trtname, short in data['trtresp'].itertuples(index=False):
        events.append({'day': dy, 'type': 'Treatment', 'detail': trtname})
    surv = data['survival'].iloc[0]
    if pd.notna(surv['lstalive']):
        events.append({'day': surv['lstalive'], 'type': 'LastAlive', 'detail': ''})
    if pd.notna(surv['deathdy']):
        events.append({'day': surv['deathdy'], 'type': 'Death', 'detail': ''})
    df = pd.DataFrame(events)
    return df.dropna(subset=['day'])

def plot_journey(timeline, patient_id):
    fig, ax = plt.subplots(figsize=(10,5))
    types = timeline['type'].unique()
    y_map = {t:i for i,t in enumerate(types)}
    colors = {
        'Visit':'blue',
        'Admission':'orange',
        'Emergency':'red',
        'AE':'purple',
        'Regimen':'green',
        'Treatment':'brown',
        'LastAlive':'black',
        'Death':'black'
    }
    for t in types:
        subset = timeline[timeline['type']==t]
        ax.scatter(subset['day'], [y_map[t]]*len(subset), color=colors.get(t,'gray'), label=t)
    ax.set_yticks(list(y_map.values()))
    ax.set_yticklabels(list(y_map.keys()))
    ax.set_xlabel('Study Day')
    ax.set_title(f'Patient Journey for {patient_id}')
    ax.legend(bbox_to_anchor=(1.05,1), loc='upper left')
    fig.tight_layout()
    plt.show()

def main(patient_id='MMRF_1014'):
    data = get_patient_data(patient_id)
    timeline = build_timeline(data)
    print(timeline.sort_values('day'))
    plot_journey(timeline.sort_values('day'), patient_id)

if __name__ == '__main__':
    main()
