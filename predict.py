
# -*- coding: utf-8 -*-
import pandas as pd

DOMAINS = ["ai", "cyber", "backend", "frontend", "game", "systems"]
DISPLAY = {
    "ai": "Yapay Zekâ / Veri Bilimi",
    "cyber": "Siber Güvenlik",
    "backend": "Backend / DevOps",
    "frontend": "Frontend / Mobil",
    "game": "Oyun Geliştirme",
    "systems": "Sistem Mühendisliği",
}
def recommend_career(df_row: pd.DataFrame):
    scores = df_row.iloc[0][[f'domain_{d}_score' for d in DOMAINS]]
    order = list(scores.sort_values(ascending=False).index.str.extract(r'domain_(.*)_score')[0])
    top3  = [(DISPLAY[d], round(scores[f'domain_{d}_score'], 2)) for d in order[:3]]
    return top3, df_row
