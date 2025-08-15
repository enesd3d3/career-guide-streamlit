
# -*- coding: utf-8 -*-
from typing import List, Tuple
LIKERT_BFI = ["Kesinlikle Katılmıyorum", "Katılmıyorum", "Kararsızım", "Katılıyorum", "Kesinlikle Katılıyorum"]
LIKERT_INTEREST = ["Hiç İlgilenmem", "Pek ilgilenmem", "Kararsızım", "İlgilenirim", "Çok ilgilenirim"]
INFO_QUESTIONS = {
    "age": "Lütfen yaşınızı giriniz.",
    "dept_self_choice": "Bilgisayar Mühendisliği bölümünü kendiniz mi seçtiniz?",
    "choice_influence": "Seçiminizde etkili olan kişi veya kurum neydi?",
    "grade_year": "Bu sene kaçıncı sınıfı bitirdiniz?",
}
GRADE_LABELS = [
    "AA–BA (çok iyi)",
    "BB–CB (iyi)",
    "CC–DC (orta)",
    "DD–FF/F1/F2 (zayıf)",
    "Bilmiyorum / Hatırlamıyorum",
    "Dersi henüz almadım",
]
COURSE_TO_ALIAS = {
    "Yapay Zeka": "grade_ai",
    "Kablosuz Ağlar": "grade_wireless",
    "Oyun Programlama": "grade_game",
    "Mobil Programlama": "grade_visual",
    "Bilgisayar ağ güvenliği": "grade_computer_net",
    "Operating Systems": "grade_os",
    "Visual Programming": "grade_visual",
    "Data Communication": "grade_datacom",
    "Introduction to Machine Learning": "grade_ml",
    "Software Engineering": "grade_software",
    "Object-Oriented Programming": "grade_oop",
    "Database Systems": "grade_database",
    "Internet Based Programming": "grade_ibp",
    "Programlama Dilleri 2": "grade_pd2",
    "Lineer Cebir": "grade_linear",
}
GRADES_BY_YEAR = {
    "4. Sınıf": ["Yapay Zeka", "Kablosuz Ağlar", "Oyun Programlama", "Mobil Programlama", "Bilgisayar ağ güvenliği"],
    "3. Sınıf": ["Operating Systems", "Visual Programming", "Data Communication", "Introduction to Machine Learning", "Software Engineering"],
    "2. Sınıf": ["Object-Oriented Programming", "Database Systems", "Internet Based Programming"],
    "1. Sınıf": ["Programlama Dilleri 2", "Lineer Cebir"],
}
BFI_ITEMS: List[Tuple[str, str, bool]] = [
    ("Sessiz olmaya eğilimli", "bfi_e_q1_r", False),
    ("Enerji dolu", "bfi_e_q6", False),
    ("Baskın, lider gibi davranan", "bfi_e_q11", False),
    ("Şefkatli, yumuşak kalpli", "bfi_a_q2", False),
    ("Zaman zaman başkalarına kaba davranan", "bfi_a_q7_r", False),
    ("Başkaları hakkında hep iyi düşünen", "bfi_a_q12", False),
    ("Sözünde duran, başkalarının güvenebildiği", "bfi_c_q3", False),
    ("Dağınık olma eğiliminde", "bfi_c_q8_r", False),
    ("İşe başlamakta zorlanan", "bfi_c_q13", True),
    ("Çok endişelenen", "bfi_n_q4", False),
    ("Depresif, hüzünlü hissetmeye eğilimli", "bfi_n_q9", False),
    ("Duygusal olarak dengeli, keyfi kolay kaçmayan", "bfi_n_q14_r", False),
    ("Sanat, müzik ya da edebiyatla çok ilgili", "bfi_o_q5", False),
    ("Soyut konulara az ilgi duyan", "bfi_o_q10_r", False),
    ("Özgün, yeni fikirler üreten", "bfi_o_q15", False),
]
INTEREST_ITEMS: List[Tuple[str, str]] = [
    ("Bir web sitesinin arka planda çalışan veritabanı ve sunucu yapısını tasarlama fikri", "int_backend_theo"),
    ("Türkiye’deki bir alışveriş sitesinin (ör. Trendyol) sipariş kayıtlarını yöneten kodu yazıp test etmek", "int_backend_prac"),
    ("Büyük indirim günlerinde milyonlarca kişi alışveriş yaptığında sitenin çökmemesini sağlamak", "int_backend_day"),
    ("Renkler ve buton düzeniyle kolay kullanılan ekranlar tasarlama ilkelerini öğrenmek", "int_frontend_theo"),
    ("WhatsApp benzeri bir sohbet uygulamasının görsel kısmını kodlamak", "int_frontend_prac"),
    ("Bir bankacılık uygulamasında (örn. İşCep) işlemleri en az dokunuşla yapmak için yeni arayüz fikirleri geliştirmek", "int_frontend_day"),
    ("Bilgi korumak için şifreleme mantığını ve temel güvenlik kavramlarını öğrenmek", "int_cyber_theo"),
    ("Bir sistemdeki tüm giriş-çıkış kayıtları size verildiğinde bu verilerden şüpheli bir hareketi fark etmeye çalışmak", "int_cyber_prac"),
    ("Bir yazılımın davranışını değiştirmeye çalışmak ve manipüle etmek, sistemi kandırmak", "int_cyber_day"),
    ("Büyük veri içindeki desenleri bulup modelleme mantığını öğrenmek", "int_ai_theo"),
    ("İstanbul trafik verisini kullanarak yoğunluk tahmini yapan küçük bir Python programı yazmak", "int_ai_prac"),
    ("Yemeksepeti veya Netflix’in kişiye özel önerilerinin nasıl çalıştığını incelemek", "int_ai_day"),
    ("Oyunlardaki karakterlerin nasıl hareket ettiğini, fiziğin ve grafiklerin nasıl oluştuğunu öğrenmek", "int_game_theo"),
    ("Unity’de 2‑boyutlu bir oyunda top sektiren basit bir mekanik kodlamak", "int_game_prac"),
    ("Popüler bir oyuna (örn. PUBG Mobile) hile engelleyici fikirler geliştirmek", "int_game_day"),
    ("Bilgisayarların içinde neler olduğunu, işletim sistemlerinin nasıl çalıştığını ve donanım‑yazılım ilişkisini öğrenmek", "int_system_theo"),
    ("Sunucu kurulumu yapmak, bilgisayar ağları kurmak ve sistem performansını iyileştirmek", "int_system_prac"),
    ("Okul laboratuvarındaki tüm bilgisayarları uzaktan güncelleyip bakım planı hazırlamak", "int_system_day"),
]
