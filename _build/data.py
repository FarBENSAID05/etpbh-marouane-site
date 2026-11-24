# -*- coding: utf-8 -*-
"""Données du site ETPBH MAROUANE — source : Liste_materiel_ETPBH_MAROUANE.xlsx (situation au 26/10/2026)
et Fiche_signaletique_ETPBH_MAROUANE.docx (dossier « Prospection grands comptes »)."""

PHONE = "0661 34 82 73"
PHONE_INTL = "+213661348273"
WA = "213661348273"
EMAIL = "marouanlatelli@gmail.com"   # à remplacer par contact@etpbh-marouane.dz quand le MX sera en place
DOMAIN = "https://etpbh-marouane.dz"

# Formulaires Tally « Demande de devis » (compte Tally de Farouk, créés le 24/11/2026)
TALLY = {"fr": "zE7g2a", "ar": "gb9gJl", "en": "EqxANX"}
def tally(lang): return "https://tally.so/r/" + TALLY[lang]

# Désignations (fr, ar, en)
D = {
 "grue":      ("Grue mobile tout-terrain", "رافعة متنقلة لكل التضاريس", "All-terrain mobile crane"),
 "pelle_ch":  ("Pelle hydraulique sur chenilles", "حفارة هيدروليكية على جنزير", "Crawler excavator"),
 "pelle_pn":  ("Pelle hydraulique sur pneus", "حفارة هيدروليكية على عجلات", "Wheeled excavator"),
 "manut":     ("Pelle de manutention", "آلية مناولة", "Material handler"),
 "niv":       ("Niveleuse", "آلة تسوية (Niveleuse)", "Motor grader"),
 "comp":      ("Compacteur mixte", "مدحلة مختلطة", "Combination roller"),
 "malax":     ("Camion malaxeur (toupie)", "شاحنة خلاطة خرسانة", "Truck mixer"),
 "pompe":     ("Camion pompe à béton", "شاحنة مضخة خرسانة", "Concrete pump truck"),
 "citerne":   ("Camion-citerne arroseur", "شاحنة صهريج للرش", "Water tanker truck"),
 "plateau":   ("Camion plateau", "شاحنة مسطحة", "Flatbed truck"),
 "benne":     ("Camion à benne 6x4", "شاحنة قلابة 6x4", "6x4 dump truck"),
 "sr_engin":  ("Semi-remorque porte-engins", "نصف مقطورة ناقلة آليات", "Lowbed semi-trailer"),
 "sr_benne":  ("Semi-remorque benne", "نصف مقطورة قلابة", "Tipper semi-trailer"),
 "sr_plat":   ("Semi-remorque plateau à ridelles", "نصف مقطورة مسطحة بجوانب", "Dropside flatbed semi-trailer"),
 "sr_cit":    ("Semi-remorque citerne", "نصف مقطورة صهريج", "Tank semi-trailer"),
 "portechar": ("Camion porte-engins (porte-char)", "ناقلة آليات (Porte-char)", "Heavy equipment transporter"),
 "camgrue":   ("Camion-grue", "شاحنة رافعة", "Truck-mounted crane"),
 "gruem":     ("Grue mobile", "رافعة متنقلة", "Mobile crane"),
}

# Caractéristiques traduisibles
C = {
 "55t":   ("Capacité 55 t", "حمولة 55 طن", "55 t capacity"),
 "50tc":  ("Classe 50 t", "فئة 50 طن", "50 t class"),
 "14tc":  ("Classe 14 t", "فئة 14 طن", "14 t class"),
 "15tc":  ("Classe 15 t", "فئة 15 طن", "15 t class"),
 "45":    ("PTAC 45 t", "الوزن الإجمالي 45 طن", "GVW 45 t"),
 "35":    ("PTAC 35 t", "الوزن الإجمالي 35 طن", "GVW 35 t"),
 "149":   ("PTAC 14,9 t", "الوزن الإجمالي 14,9 طن", "GVW 14.9 t"),
 "neuf":  ("Neuf", "جديدة", "New"),
 "cu241": ("Charge utile 24,1 t", "الحمولة 24,1 طن", "Payload 24.1 t"),
 "cu235": ("Charge utile 23,5 t", "الحمولة 23,5 طن", "Payload 23.5 t"),
 "cu25":  ("Charge utile 25 t", "الحمولة 25 طن", "Payload 25 t"),
 "":      ("—", "—", "—"),
}

# Parc propre : (clé désignation, marque, modèle, caractéristique, année, statut) — statut "ok" = carte grise, "enc" = immatriculation en cours
PARC = [
 ("grue","LIEBHERR","LTM 1055-3.2","55t",2009,"ok"),
 ("pelle_ch","HYUNDAI","R520LC-9S","50tc",2018,"ok"),
 ("pelle_pn","DOOSAN","DX140W","14tc",2017,"enc"),
 ("pelle_pn","CATERPILLAR","M315D","15tc",2016,"enc"),
 ("manut","LIEBHERR","926","",2014,"enc"),
 ("manut","LIEBHERR","926","",2013,"enc"),
 ("manut","LIEBHERR","932","",2014,"enc"),
 ("niv","JOHN DEERE","670D","",2005,"ok"),
 ("comp","XGMA","6121","",2008,"ok"),
 ("malax","RENAULT","34FPA","45",2014,"ok"),
 ("malax","RENAULT","34FPA","45",2014,"ok"),
 ("pompe","MAN","TGS 33.360","35",2016,"ok"),
 ("citerne","DONGFENG","SGZ5200GSS","149",2008,"ok"),
 ("plateau","DAEWOO","K7CEF","",2014,"ok"),
 ("benne","POWERPLUS","PD680Z-II","neuf",2026,"enc"),
 ("benne","POWERPLUS","PD680Z-II","neuf",2026,"enc"),
 ("benne","POWERPLUS","PD680Z-II","neuf",2026,"enc"),
 ("benne","POWERPLUS","PD680Z-II","neuf",2026,"enc"),
 ("benne","POWERPLUS","PD680Z-II","neuf",2026,"enc"),
 ("sr_engin","ACTM","S46315CHC","cu241",2004,"ok"),
 ("sr_benne","SICAM","SRBA2S32T","cu235",2014,"ok"),
 ("sr_plat","COMET","SRPR2S","cu25",2012,"ok"),
 ("sr_cit","MONTENEGRO","VST002269","",2009,"ok"),
]

# Parc mobilisable (partenaires conventionnés) : (clé, capacité, nombre, délai "48" ou "plan")
MOBIL = [
 ("portechar","40 t",4,"48"),
 ("camgrue","50 t",1,"48"),
 ("camgrue","70 t",1,"48"),
 ("camgrue","80 t",1,"48"),
 ("gruem","140 t",1,"plan"),
 ("gruem","200 t",1,"plan"),
 ("gruem","250 t",1,"plan"),
 ("gruem","280 t",1,"plan"),
]

# Programme d'acquisition (familles, résumé) : (fr, ar, en, quantité)
ACQ = [
 ("Camions à benne 6x4 et 8x4", "شاحنات قلابة 6x4 و8x4", "6x4 and 8x4 dump trucks", 10),
 ("Tracteurs routiers et semi-remorques à benne", "جرارات طرقية ونصف مقطورات قلابة", "Road tractors and tipper semi-trailers", 14),
 ("Grues mobiles 50 t et grues sur chenilles 250 t", "رافعات متنقلة 50 طن ورافعات على جنزير 250 طن", "50 t mobile cranes and 250 t crawler cranes", 5),
 ("Pelles sur chenilles, rétro-chargeurs, bulldozer, foreuses", "حفارات على جنزير، جرافات خلفية، بلدوزر، آلات حفر", "Crawler excavators, backhoe loaders, bulldozer, drill rigs", 13),
 ("Camions malaxeurs, citernes à eau, compacteurs, niveleuses", "شاحنات خلاطة، صهاريج مياه، مداحل، آلات تسوية", "Truck mixers, water tankers, rollers, graders", 14),
 ("Matériel routier et béton (finisher, répandeuse, enrobage, centrale)", "عتاد الطرق والخرسانة (فينيشر، رشاشة، محطة زفت، محطة خرسانة)", "Road and concrete plant (paver, sprayer, asphalt and batching plants)", 4),
 ("Divers (plateaux, auto-bétonnières, mini-pelle, brise-roches…)", "متنوع (شاحنات مسطحة، خلاطات ذاتية، حفارة صغيرة، كاسرات صخور…)", "Miscellaneous (flatbeds, self-loading mixers, mini excavator, breakers…)", 15),
]
