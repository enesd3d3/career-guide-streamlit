
# Kariyer Öneri Sistemi — Google Form Entegrasyonlu (Streamlit)

Çalıştır:
```
pip install streamlit pandas numpy
streamlit run app.py
```

- Form soru metinleri `form_schema.py` içinde.
- Alias → pipeline işleyişi `preprocess.py` içinde.
- Top-3 öneri `predict.py` içinde.
- `bfi_c_q13` maddesi formda olumsuz olduğu için UI tarafında 6-x çevrildi; alias adında `_r` yok, bu yüzden EDA ile çakışmaz.
