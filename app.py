
# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd

from form_schema import (
    INFO_QUESTIONS, GRADE_LABELS, GRADES_BY_YEAR, COURSE_TO_ALIAS,
    BFI_ITEMS, LIKERT_BFI, INTEREST_ITEMS, LIKERT_INTEREST
)
from preprocess import build_features_from_alias
from predict import recommend_career

st.set_page_config(page_title="Kariyer Öneri Sistemi (Form Entegrasyonlu)", page_icon="🎓", layout="wide")
st.title("🎓 Bilgisayar Mühendisliği Alan Rehberi  — Google Form Entegrasyonlu")
st.caption("Google Form’daki **aynı** sorular Streamlit arayüzüne taşınmıştır.")

with st.form("user_form"):
    cols = st.columns([1,1,1])
    age = cols[0].number_input(INFO_QUESTIONS["age"], min_value=15, max_value=80, value=21, step=1)
    dept_self = cols[1].radio(INFO_QUESTIONS["dept_self_choice"], ["Evet","Hayır"], horizontal=True)
    influence = cols[2].selectbox(INFO_QUESTIONS["choice_influence"],
                                  ["Aile","Rehber öğretmen","Arkadaş / Çevre","Yerleştirme puanım","Diğer"])

    st.markdown("---")
    st.subheader("📚 DERS NOT BİLGİSİ")
    st.caption("Lütfen **aldığın** dersler için seç; bilmediğin/almadığınlar **etkisiz** sayılır.")
    grade_inputs = {}
    for year, courses in GRADES_BY_YEAR.items():
        st.markdown(f"**{year}**")
        gcols = st.columns(2) if len(courses) > 3 else [st]
        for i, course in enumerate(courses):
            widget_col = gcols[i%len(gcols)]
            grade_inputs[course] = widget_col.selectbox(course, GRADE_LABELS, index=2)

    st.markdown("---")
    st.subheader("🧠 Kişilik Özellikleri Testi (Big Five)")
    st.caption("1 = Kesinlikle Katılmıyorum ... 5 = Kesinlikle Katılıyorum")
    bfi_values = {}
    for text, alias, reverse_ui in BFI_ITEMS:
        v = st.slider(text, 1, 5, 3, key=f"bfi_{alias}")
        if reverse_ui and not alias.endswith("_r"):
            v = 6 - v
        bfi_values[alias] = v

    st.markdown("---")
    st.subheader("🎯 İlgi Alanları")
    st.caption("1 = Hiç ilgilenmem ... 5 = Çok ilgilenirim")
    interest_values = {}
    for text, alias in INTEREST_ITEMS:
        v = st.slider(text, 1, 5, 3, key=f"int_{alias}")
        interest_values[alias] = v

    submitted = st.form_submit_button("📊 Alanımı Öner")

if submitted:
    alias_row = {"age": age, "dept_self_choice": 1 if dept_self == "Evet" else 0, "choice_influence": influence}
    for course, label in grade_inputs.items():
        alias = COURSE_TO_ALIAS.get(course)
        if alias:
            alias_row[alias] = label
    alias_row.update(bfi_values)
    alias_row.update(interest_values)

    df_alias = pd.DataFrame([alias_row])
    feats = build_features_from_alias(df_alias)
    top3, full = recommend_career(feats)

    st.success("Öneri hazır!")
    st.subheader("⭐ Önerilen İlk 3 Alan")
    c1, c2, c3 = st.columns(3)
    for col, (name, sc) in zip([c1,c2,c3], top3):
        col.metric(label=name, value=f"{sc:.2f}")

    st.subheader("🔎 Detaylı skorlar")
    tbl = (feats.filter(regex="^domain_.*_score$").T.reset_index(names="Alan").rename(columns={feats.index[0]:"Skor"}))
    st.dataframe(tbl, hide_index=True, use_container_width=True)

    st.download_button("⬇️ Tüm skorları CSV indir", feats.to_csv(index=False).encode("utf-8-sig"),
                       file_name="features_and_scores.csv", mime="text/csv")
