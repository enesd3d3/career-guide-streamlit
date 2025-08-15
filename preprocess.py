
# -*- coding: utf-8 -*-
from typing import Dict, List, Tuple
import pandas as pd
import numpy as np

W_I = 0.6
W_P = 0.3
W_G_BASE = 0.1
COVERAGE_MIN = 0.30
LOW_GRADE_THRESHOLD = 2.0
LOW_GRADE_PENALTY = 0.00

GRADE_BINS = {
    "AA–BA (çok iyi)": 4,
    "BB–CB (iyi)": 3,
    "CC–DC (orta)": 2,
    "DD–FF/F1/F2 (zayıf)": 1,
    "Bilmiyorum / Hatırlamıyorum": np.nan,
    "Dersi henüz almadım": np.nan,
}
def norm_label(s):
    if pd.isna(s): return s
    return str(s).strip().replace('—','-').replace('–','-')
GRADE_BINS_NORM = {norm_label(k): v for k, v in GRADE_BINS.items()}

DOMAIN_GRADE_GROUPS = {
    'cyber':   ['grade_computer_net_num','grade_os_num','grade_wireless_num','grade_datacom_num'],
    'ai':      ['grade_ai_num','grade_ml_num','grade_linear_num','grade_database_num'],
    'backend': ['grade_software_num','grade_oop_num','grade_database_num','grade_ibp_num','grade_pd2_num','grade_os_num'],
    'frontend':['grade_visual_num','grade_ibp_num'],
    'game':    ['grade_game_num','grade_visual_num','grade_oop_num'],
    'systems': ['grade_os_num','grade_computer_net_num','grade_datacom_num','grade_wireless_num'],
}

PERS_W = {
    'ai':      dict(openness=.35, conscientiousness=.30, extraversion=.10, agreeableness=.05, stability=.20),
    'cyber':   dict(openness=.20, conscientiousness=.30, extraversion=.10, agreeableness=.05, stability=.35),
    'backend': dict(openness=.20, conscientiousness=.30, extraversion=.10, agreeableness=.15, stability=.25),
    'frontend':dict(openness=.30, conscientiousness=.20, extraversion=.20, agreeableness=.20, stability=.10),
    'game':    dict(openness=.40, conscientiousness=.20, extraversion=.15, agreeableness=.15, stability=.10),
    'systems': dict(openness=.20, conscientiousness=.30, extraversion=.10, agreeableness=.10, stability=.30),
}
DOMAINS = ['ai','cyber','backend','frontend','game','systems']

def map_grades_alias_texts_to_numeric(df: pd.DataFrame) -> pd.DataFrame:
    grade_cols = [c for c in df.columns if c.startswith('grade_') and not c.endswith('_num')]
    for c in grade_cols:
        df[c + '_num'] = df[c].map(norm_label).map(GRADE_BINS_NORM)
    return df

def aggregate_domain_grades(df: pd.DataFrame) -> pd.DataFrame:
    for dom, cols in DOMAIN_GRADE_GROUPS.items():
        use = [c for c in cols if c in df.columns]
        if use:
            df[f'grade_{dom}_score'] = df[use].mean(axis=1, skipna=True)
            df[f'grade_{dom}_coverage'] = df[use].notna().mean(axis=1)
    return df

def compute_personality_dimension_scores(df: pd.DataFrame) -> pd.DataFrame:
    groups = {
        'openness_score': ['bfi_o_q5','bfi_o_q10_r','bfi_o_q15'],
        'conscientiousness_score': ['bfi_c_q3','bfi_c_q8_r','bfi_c_q13'],
        'extraversion_score': ['bfi_e_q1_r','bfi_e_q6','bfi_e_q11'],
        'agreeableness_score': ['bfi_a_q2','bfi_a_q7_r','bfi_a_q12'],
        'neuroticism_score': ['bfi_n_q4','bfi_n_q9','bfi_n_q14_r'],
    }
    for dim, cols in groups.items():
        use = [c for c in cols if c in df.columns]
        if use:
            df[dim] = df[use].mean(axis=1, skipna=True)
    df['stability_score'] = 6 - df['neuroticism_score']
    return df

def compute_interest_scores(df: pd.DataFrame) -> pd.DataFrame:
    interest_groups = {
        'frontend': ['int_frontend_theo', 'int_frontend_prac', 'int_frontend_day'],
        'ai':       ['int_ai_theo', 'int_ai_prac', 'int_ai_day'],
        'cyber':    ['int_cyber_theo', 'int_cyber_prac', 'int_cyber_day'],
        'backend':  ['int_backend_theo', 'int_backend_prac', 'int_backend_day'],
        'game':     ['int_game_theo', 'int_game_prac', 'int_game_day'],
        'system':   ['int_system_theo', 'int_system_prac', 'int_system_day'],
    }
    for cat, cols in interest_groups.items():
        use = [c for c in cols if c in df.columns]
        if use:
            df[f'interest_{cat}_score'] = df[use].mean(axis=1, skipna=True)
    return df

def personality_weighted(row: pd.Series, dom: str) -> float:
    w = PERS_W[dom]
    vals, weights = [], []
    mapping = {
        'openness':'openness_score',
        'conscientiousness':'conscientiousness_score',
        'extraversion':'extraversion_score',
        'agreeableness':'agreeableness_score',
        'stability':'stability_score',
    }
    for trait, wt in w.items():
        col = mapping[trait]
        if col in row and not pd.isna(row[col]):
            vals.append(row[col]); weights.append(wt)
    if not weights: return np.nan
    weights = np.asarray(weights, float); weights /= weights.sum()
    return float(np.dot(vals, weights))

def compute_domain_scores(df: pd.DataFrame) -> pd.DataFrame:
    for d in DOMAINS:
        col_i   = f"interest_{'system' if d=='systems' else d}_score"
        col_g   = f"grade_{d}_score"
        col_cov = f"grade_{d}_coverage"
        i_norm = df[col_i]/5 if col_i in df else pd.Series(np.nan, df.index)
        g_norm = df[col_g]/4 if col_g in df else pd.Series(np.nan, df.index)
        cov    = df[col_cov]  if col_cov in df else pd.Series(0.0, df.index)
        p_norm = df.apply(lambda r: personality_weighted(r, d), axis=1) / 5

        w_g = (W_G_BASE * cov).where((cov >= COVERAGE_MIN) & g_norm.notna(), 0)
        wi  = pd.Series(W_I, df.index).where(i_norm.notna(), 0)
        wp  = pd.Series(W_P, df.index).where(p_norm.notna(), 0)
        wg  = w_g.where(g_norm.notna(), 0)

        num = wi*i_norm.fillna(0) + wp*p_norm.fillna(0) + wg*g_norm.fillna(0)
        den = wi + wp + wg
        df[f'domain_{d}_score'] = (num / den).fillna(0)
    return df

def build_features_from_alias(df_alias: pd.DataFrame) -> pd.DataFrame:
    df = df_alias.copy()
    df = map_grades_alias_texts_to_numeric(df)
    df = aggregate_domain_grades(df)
    df = compute_personality_dimension_scores(df)
    df = compute_interest_scores(df)
    df = compute_domain_scores(df)
    return df
