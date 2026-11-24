# -*- coding: utf-8 -*-
"""Textes v2 (24/11/2026), appliqués par-dessus strings.py et families.py.

Consigne du client :
- ne jamais afficher combien d'engins l'entreprise possède : on parle de ce
  qu'elle PEUT FOURNIR (types, capacités, marques, délais) ;
- plus de programme AAPI sur le site ;
- mettre en avant la participation aux grands projets de l'État (ligne
  ferroviaire minière Est avec CRBC / CCCC, ouvrages de Mechroha, Tindouf) ;
- présenter la vision et les objectifs de l'entreprise face aux orientations
  de l'État.
Sources des faits : attachements CRBC « Section 3 » (121 km Bouchegouf – Souk
Ahras – Dréa), pointages grues 200 t / 280 t Mechroha (Engin Plus), facture
JIMS ON DJBILAT (grue 200 t, Tindouf) ; APS / Radio Algérie (ligne minière Est
422 km Annaba – Tébessa, projet de phosphate intégré ; ligne Béchar – Tindouf –
Gara Djebilet mise en service le 01/02/2026).
"""

# Catalogue « ce que nous pouvons fournir », par famille :
# (fr, ar, en, capacité fr, capacité ar, capacité en, marques, mobilisation "48" ou "mix")
CAT = {
 "levage": [
  ("Grues mobiles tout-terrain", "رافعات متنقلة لكل التضاريس", "All-terrain mobile cranes", "55 à 280 t", "من 55 إلى 280 طن", "55 to 280 t", "Liebherr", "mix"),
  ("Camions-grues", "شاحنات رافعة", "Truck-mounted cranes", "50 à 80 t", "من 50 إلى 80 طن", "50 to 80 t", "", "48"),
 ],
 "terrassement": [
  ("Pelles hydrauliques sur chenilles", "حفارات هيدروليكية على جنزير", "Crawler excavators", "jusqu'à la classe 50 t", "حتى فئة 50 طن", "up to the 50 t class", "Hyundai", "48"),
  ("Pelles hydrauliques sur pneus", "حفارات هيدروليكية على عجلات", "Wheeled excavators", "classe 14 à 15 t", "فئة 14 إلى 15 طن", "14 to 15 t class", "Doosan, Caterpillar", "48"),
  ("Pelles de manutention", "آليات مناولة", "Material handlers", "", "", "", "Liebherr", "48"),
  ("Niveleuses", "آلات تسوية (Niveleuse)", "Motor graders", "", "", "", "John Deere", "48"),
  ("Compacteurs", "مداحل", "Rollers", "", "", "", "XGMA", "48"),
 ],
 "transport": [
  ("Camions à benne 6x4", "شاحنات قلابة 6x4", "6x4 dump trucks", "", "", "", "PowerPlus", "48"),
  ("Porte-chars pour engins lourds", "ناقلات الآليات الثقيلة (Porte-char)", "Lowbeds for heavy machines", "40 t", "40 طن", "40 t", "", "48"),
  ("Semi-remorques porte-engins", "نصف مقطورات ناقلة آليات", "Lowbed semi-trailers", "charge utile 24 t", "حمولة 24 طن", "24 t payload", "ACTM", "48"),
  ("Semi-remorques benne", "نصف مقطورات قلابة", "Tipper semi-trailers", "charge utile 23,5 t", "حمولة 23,5 طن", "23.5 t payload", "SICAM", "48"),
  ("Semi-remorques plateau", "نصف مقطورات مسطحة", "Flatbed semi-trailers", "charge utile 25 t", "حمولة 25 طن", "25 t payload", "Comet", "48"),
  ("Semi-remorques citerne", "نصف مقطورات صهريج", "Tank semi-trailers", "", "", "", "", "48"),
  ("Camions-citernes arroseurs", "شاحنات صهريج للرش", "Water tanker trucks", "", "", "", "Dongfeng", "48"),
  ("Camions plateau", "شاحنات مسطحة", "Flatbed trucks", "", "", "", "Daewoo", "48"),
 ],
 "beton": [
  ("Camions malaxeurs (toupies)", "شاحنات خلاطة خرسانة", "Truck mixers", "9 m³", "9 م³", "9 m³", "Renault", "48"),
  ("Camions pompes à béton", "شاحنات مضخة خرسانة", "Concrete pump trucks", "", "", "", "MAN", "48"),
 ],
}

# Chiffre clé affiché en tête de chaque page famille : (valeur, libellé fr, ar, en)
FAM_FIG = {
 "levage":       ("280 <small>t</small>", "grues jusqu'à", "رافعات حتى", "cranes up to"),
 "terrassement": ("50 <small>t</small>", "pelles jusqu'à la classe", "حفارات حتى فئة", "excavators up to the class"),
 "transport":    ("40 <small>t</small>", "porte-chars pour engins lourds", "ناقلات للآليات الثقيلة", "lowbeds for heavy machines"),
 "beton":        ("9 <small>m³</small>", "camions malaxeurs", "شاحنات خلاطة", "truck mixers"),
}

T2 = {
"fr": {
 "dept":{"loc":("Location d'engins","Adel DRISSI, directeur technique"),"tp":("Travaux publics","Madani LATELLI, gérant")},
 "stats":[("280 <small>t</small>","grues mobilisables jusqu'à"),("48–72 <small>h</small>","délai de mobilisation"),("IV","catégorie de qualification TP"),("4","familles d'engins à louer")],
 "svc_txt":{
  "crane":"Grues tout-terrain et camions-grues de 50 à 280 t, livrés avec leur opérateur. Les plus grosses capacités se réservent quelques jours à l'avance.",
  "dig":"Pelles hydrauliques sur chenilles jusqu'à la classe 50 t et pelles sur pneus. Pour les plateformes, nous ajoutons niveleuses et compacteurs.",
  "truck":"Camions à benne 6x4 et semi-remorques benne, plateau ou citerne. Pour déplacer un engin lourd, nous fournissons des porte-chars de 40 t."},
 "fleet_k":"Notre capacité","fleet_h":"Nous fournissons l'engin dont votre chantier a besoin",
 "fleet_p":"Nos propres engins et ceux des propriétaires liés à nous par convention forment un seul parc. Vous passez commande, nous gérons le reste jusqu'à la facture.",
 "fleet_cards":[("Jusqu'à 280 t","Levage lourd","Des camions-grues de 50 t aux grues de 280 t, pour les poutres d'ouvrages d'art, les dalles préfabriquées et les équipements industriels."),
                ("48–72 h","Mobilisation","C'est notre délai habituel entre le bon de commande et l'arrivée de l'engin, où que soit le chantier. Les grues lourdes se planifient."),
                ("Un contrat","Un seul interlocuteur","L'opérateur et le pointage journalier restent à notre charge, comme l'assurance et la facture, même quand l'engin vient d'un partenaire.")],
 "fleet_btn":"Voir le matériel disponible",
 "ref_crbc":"Ligne ferroviaire minière Est, tronçon Bouchegouf – Souk Ahras – Dréa (121 km), section 3 : camions malaxeurs 9 m³, porte-chars 40 t, camions-grues de 50 à 80 t.",
 "ref_cccc":"Même chantier ferroviaire, en direct avec le groupe : camions malaxeurs 9 m³ et camion-grue 80 t.",
 "title_mat":"Matériel disponible à la location — ETPBH MAROUANE",
 "desc_mat":"Grues de 50 à 280 t, pelles, niveleuses, camions à benne, porte-chars, malaxeurs et pompes à béton : le matériel qu'ETPBH MAROUANE fournit avec opérateur.",
 "mat_h1":"Le matériel que nous pouvons fournir",
 "mat_lead":"Chaque engin part avec son chauffeur ou son opérateur. Les cartes grises, les assurances et les contrôles techniques accompagnent notre offre.",
 "th_cat":["Engin","Capacité / classe","Marques","Mobilisation"],
 "mob_48":"48 à 72 h","mob_mix":"48 à 72 h ; 140 t et plus sur planification",
 "mat_note":"Matériel fourni par ETPBH MAROUANE ou par des propriétaires partenaires liés par convention, toujours sous un seul contrat et une seule facture.",
 "prov_h":"Ce que nous pouvons fournir","mk":"Marques",
 # grands projets
 "pj_k":"Grands projets","pj_h":"Sur les chantiers structurants de l'État",
 "pj_p":"Nos engins travaillent pour les entreprises qui réalisent les grandes infrastructures du pays. Nous servons les groupes chinois comme les entreprises nationales.",
 "pj":[("rail","Ligne ferroviaire minière Est","Cette ligne de 422 km relie Annaba à Tébessa et sert le projet de phosphate intégré. Sur le tronçon Bouchegouf – Souk Ahras – Dréa, nous fournissons à CRBC, filiale du groupe CCCC, des camions-grues, des malaxeurs et des porte-chars."),
       ("crane","Ouvrages d'art à Mechroha","Des grues de 200 et 280 t ont levé, en 2026, les dalles préfabriquées des ouvrages de ce même tronçon, dans la wilaya de Souk Ahras."),
       ("pin","Jusqu'au Grand Sud","En 2026, une grue Liebherr de 200 t est partie travailler à Tindouf. Nous suivons nos clients là où l'État ouvre ses nouveaux chantiers.")],
 # vision
 "vi_k":"Notre vision","vi_h":"Grandir avec les priorités du pays",
 "vi_p":["L'Algérie investit dans le rail, les mines, l'eau et les routes. La ligne minière Est doit acheminer le phosphate de Tébessa jusqu'au port d'Annaba. Mise en service en février 2026, la ligne Béchar – Tindouf – Gara Djebilet ouvre le Sud au minerai de fer.",
         "Ces chantiers ont tous besoin de levage lourd et de transport, souvent loin des grandes villes. C'est là que nous voulons être utiles : fournir vite un engin fiable, avec un opérateur algérien qui connaît son métier."],
 "vi_goals_h":"Nos objectifs",
 "vi_goals":["Devenir un fournisseur de matériel de référence pour les grands groupes publics et pour leurs partenaires étrangers.",
             "Renforcer notre propre parc par l'investissement, en priorité en grues et en camions.",
             "Recruter et former des opérateurs dans les wilayas où nous travaillons.",
             "Monter en catégorie de qualification pour accéder à des marchés plus importants."],
},
"ar": {
 "dept":{"loc":("كراء الآليات","عادل دريسي، المدير التقني"),"tp":("الأشغال العمومية","لعطلي المداني، المسيّر")},
 "stats":[("280 <small>طن</small>","رافعات يمكن تعبئتها حتى"),("48–72 <small>ساعة</small>","أجل تعبئة العتاد"),("IV","صنف التأهيل في الأشغال العمومية"),("4","عائلات من الآليات للكراء")],
 "svc_txt":{
  "crane":"رافعات لكل التضاريس وشاحنات رافعة من 50 إلى 280 طن، تصلك مع مشغّلها. الحمولات الكبرى تُحجز قبل أيام.",
  "dig":"حفارات هيدروليكية على جنزير حتى فئة 50 طن، وحفارات على عجلات، وآليات مناولة، وآلات تسوية ومداحل.",
  "truck":"شاحنات قلابة 6x4 ونصف مقطورات قلابة أو مسطحة أو صهريج. ولنقل آلية ثقيلة نوفّر ناقلات آليات 40 طن."},
 "fleet_k":"قدرتنا","fleet_h":"نوفّر الآلية التي تحتاجها ورشتك",
 "fleet_p":"آلياتنا وآليات الملاك الذين تربطنا بهم اتفاقيات تشكّل حظيرة واحدة. ترسل طلبيتك، ونتكفّل بالباقي حتى الفاتورة.",
 "fleet_cards":[("حتى 280 طن","الرفع الثقيل","من شاحنات رافعة 50 طن إلى رافعات 280 طن، لرفع روافد المنشآت الفنية والبلاطات الجاهزة والتجهيزات الصناعية."),
                ("48–72 ساعة","التعبئة","هذا أجلنا المعتاد بين وصل الطلب ووصول الآلية إلى الورشة، أينما كانت. الرافعات الثقيلة تُبرمج مسبقًا."),
                ("عقد واحد","محاور واحد","المشغّل وورقة التشغيل اليومية على عاتقنا، ومعهما التأمين والفاتورة، حتى لو جاءت الآلية من أحد شركائنا.")],
 "fleet_btn":"العتاد المتوفّر",
 "ref_crbc":"خط السكة الحديدية المنجمي الشرقي، مقطع بوشقوف – سوق أهراس – الدريعة (121 كلم)، القسم 3: شاحنات خلاطة 9 م³، ناقلات آليات 40 طن، شاحنات رافعة من 50 إلى 80 طن.",
 "ref_cccc":"الورشة نفسها، مباشرة مع المجمّع: شاحنات خلاطة 9 م³ وشاحنة رافعة 80 طن.",
 "title_mat":"العتاد المتوفّر للكراء — ETPBH MAROUANE",
 "desc_mat":"رافعات من 50 إلى 280 طن، حفارات، آلات تسوية، شاحنات قلابة، ناقلات آليات، خلاطات ومضخات خرسانة: العتاد الذي توفّره ETPBH MAROUANE مع المشغّل.",
 "mat_h1":"العتاد الذي نوفّره",
 "mat_lead":"كل آلية تخرج مع سائقها أو مشغّلها. نرسل مع العرض البطاقات الرمادية وشهادات التأمين والمراقبة التقنية.",
 "th_cat":["الآلية","الحمولة / الفئة","العلامات","التعبئة"],
 "mob_48":"48 إلى 72 ساعة","mob_mix":"48 إلى 72 ساعة؛ 140 طن فما فوق حسب البرمجة",
 "mat_note":"عتاد توفّره ETPBH MAROUANE أو ملاك شركاء تربطنا بهم اتفاقيات، دائمًا بعقد واحد وفاتورة واحدة.",
 "prov_h":"ما الذي نوفّره","mk":"العلامات",
 "pj_k":"المشاريع الكبرى","pj_h":"في الورشات الهيكلية للدولة",
 "pj_p":"تعمل آلياتنا لحساب المؤسسات التي تنجز البنى التحتية الكبرى للبلاد، من المجمّعات الصينية إلى المؤسسات الوطنية.",
 "pj":[("rail","خط السكة الحديدية المنجمي الشرقي","يمتد هذا الخط على 422 كلم بين عنابة وتبسة، ويخدم مشروع الفوسفات المدمج. في مقطع بوشقوف – سوق أهراس – الدريعة نوفّر لشركة CRBC، فرع مجمّع CCCC، شاحنات رافعة وخلاطات خرسانة، وننقل لها آلياتها الثقيلة بناقلات 40 طن."),
       ("crane","المنشآت الفنية بالمشروحة","في 2026 رفعت رافعات بحمولة 200 و280 طن البلاطات الجاهزة لمنشآت المقطع نفسه، بولاية سوق أهراس."),
       ("pin","حتى الجنوب الكبير","في 2026 عبّأنا رافعة Liebherr بحمولة 200 طن في تندوف. نرافق زبائننا حيث تفتح الدولة ورشاتها الجديدة.")],
 "vi_k":"رؤيتنا","vi_h":"ننمو مع أولويات البلاد",
 "vi_p":["تستثمر الجزائر بقوة في السكك الحديدية والمناجم، وكذلك في المياه والطرق. خط السكة المنجمي الشرقي سينقل فوسفات تبسة إلى ميناء عنابة. وخط بشار – تندوف – غار جبيلات، الذي دخل الخدمة في فيفري 2026، يفتح الجنوب على خام الحديد.",
         "كل هذه الورشات تحتاج إلى رفع ثقيل ونقل، وغالبًا بعيدًا عن المدن الكبرى. هناك نريد أن نكون مفيدين: آلية موثوقة تصل بسرعة، مع مشغّل جزائري يتقن عمله."],
 "vi_goals_h":"أهدافنا",
 "vi_goals":["أن نصبح مورّد عتاد مرجعيًا للمجمّعات العمومية الكبرى ولشركائها الأجانب.",
             "أن نعزّز حظيرتنا الخاصة بالاستثمار، وفي مقدّمتها الرافعات والشاحنات.",
             "أن نوظّف المشغّلين ونكوّنهم في الولايات التي نعمل فيها.",
             "أن نرتقي في صنف التأهيل لنصل إلى صفقات أكبر."],
},
"en": {
 "dept":{"loc":("Equipment hire","Adel DRISSI, technical director"),"tp":("Public works","Madani LATELLI, managing director")},
 "stats":[("280 <small>t</small>","cranes available up to"),("48–72 <small>h</small>","mobilisation time"),("IV","public-works qualification class"),("4","equipment families for hire")],
 "svc_txt":{
  "crane":"All-terrain cranes and truck cranes from 50 to 280 t, delivered with their operator. The largest capacities are booked a few days ahead.",
  "dig":"Crawler excavators up to the 50 t class and wheeled excavators. For platforms, we add graders and rollers.",
  "truck":"6x4 dump trucks and semi-trailers for every kind of load. To move a heavy machine, we provide 40 t lowbeds."},
 "fleet_k":"Our capacity","fleet_h":"We supply the machine your site needs",
 "fleet_p":"Our own machines and those of owners bound to us by contract work as one fleet. You place the order and we handle the rest, down to the invoice.",
 "fleet_cards":[("Up to 280 t","Heavy lifting","From 50 t truck cranes to 280 t cranes, for bridge beams, precast slabs and industrial equipment."),
                ("48–72 h","Mobilisation","Our usual lead time from purchase order to the machine on site, wherever the site is. Heavy cranes are scheduled."),
                ("One contract","One contact","The operator and the daily timesheet stay with us, as do insurance and invoicing, even when the machine comes from a partner.")],
 "fleet_btn":"See available equipment",
 "ref_crbc":"Eastern mining railway, Bouchegouf – Souk Ahras – Dréa section (121 km), lot 3: 9 m³ truck mixers, 40 t lowbeds, 50 to 80 t truck cranes.",
 "ref_cccc":"Same railway site, directly with the group: 9 m³ truck mixers and an 80 t truck crane.",
 "title_mat":"Equipment available for hire — ETPBH MAROUANE",
 "desc_mat":"Cranes from 50 to 280 t, excavators, graders, dump trucks, lowbeds, truck mixers and concrete pumps: the equipment ETPBH MAROUANE supplies with operator.",
 "mat_h1":"The equipment we can supply",
 "mat_lead":"Every machine comes with its driver or operator. We send its registration papers with our quote, along with insurance and inspection certificates.",
 "th_cat":["Machine","Capacity / class","Makes","Mobilisation"],
 "mob_48":"48 to 72 h","mob_mix":"48 to 72 h; 140 t and above scheduled",
 "mat_note":"Equipment supplied by ETPBH MAROUANE or by partner owners under contract, always under one contract and one invoice.",
 "prov_h":"What we can supply","mk":"Makes",
 "pj_k":"Major projects","pj_h":"On the State's flagship infrastructure",
 "pj_p":"Our machines work for the companies building the country's major infrastructure, from Chinese groups to Algerian contractors.",
 "pj":[("rail","Eastern mining railway","This 422 km line links Annaba to Tébessa and serves the integrated phosphate project. On the Bouchegouf – Souk Ahras – Dréa section, we supply CRBC, a subsidiary of the CCCC group, with truck cranes, truck mixers and lowbeds."),
       ("crane","Structures at Mechroha","In 2026, 200 t and 280 t cranes lifted the precast slabs for the structures of that same section, in the wilaya of Souk Ahras."),
       ("pin","Down to the far south","In 2026, a 200 t Liebherr crane went to work in Tindouf. We follow our clients wherever the State opens new sites.")],
 "vi_k":"Our vision","vi_h":"Growing with the country's priorities",
 "vi_p":["Algeria is investing heavily in rail and mining, and in water and roads too. The Eastern mining line will carry phosphate from Tébessa to the port of Annaba. Opened in February 2026, the Béchar – Tindouf – Gara Djebilet line opens the south to iron ore.",
         "All of these sites need heavy lifting and haulage, often far from the big cities. That is where we want to be useful: a reliable machine that arrives fast, with an Algerian operator who knows the job."],
 "vi_goals_h":"Our goals",
 "vi_goals":["Become a go-to equipment supplier for large public groups and their foreign partners.",
             "Grow our own fleet through investment, starting with cranes and trucks.",
             "Hire and train operators in the wilayas where we work.",
             "Move up the qualification classes to reach larger contracts."],
},
}

F2 = {
"fr": {
 "faq_common_2":("Intervenez-vous en dehors d'Alger ?","Oui, partout en Algérie. Nous avons travaillé à Souk Ahras sur la ligne ferroviaire minière Est et mobilisé une grue de 200 t à Tindouf."),
 "all":"Tout le matériel",
 "fam":{
  "levage":{"desc":"Grues tout-terrain et camions-grues de 50 à 280 t à louer avec opérateur partout en Algérie. Mobilisation sous 48 à 72 h, grues lourdes sur planification.",
            "lead":"Camions-grues de 50 à 80 t et grues tout-terrain jusqu'à 280 t, toujours avec opérateur. Nous avons levé des dalles préfabriquées pour la ligne ferroviaire minière Est, à Mechroha.",
            "faq":[("Jusqu'à quelle capacité pouvez-vous lever ?","Jusqu'à 280 t. Les camions-grues de 50 à 80 t arrivent en 48 à 72 h. Au-delà de 140 t, nous planifions la grue avec vous quelques jours à l'avance.")]},
  "terrassement":{"desc":"Pelles hydrauliques sur chenilles et sur pneus, pelles de manutention, niveleuses et compacteurs à louer avec opérateur en Algérie.",
            "lead":"Pelles sur chenilles jusqu'à la classe 50 t et pelles sur pneus, avec des pelles de manutention Liebherr pour le chargement. Pour les plateformes, nous ajoutons niveleuses et compacteurs. Chaque engin arrive avec son opérateur.",
            "faq":[("Quels engins de terrassement pouvez-vous fournir ?","Des pelles hydrauliques sur chenilles (Hyundai, classe 50 t) et sur pneus (Doosan, Caterpillar), des pelles de manutention Liebherr, des niveleuses John Deere et des compacteurs.")]},
  "transport":{"desc":"Camions à benne 6x4, semi-remorques benne, plateau et citerne, camions-citernes et porte-chars 40 t avec chauffeur, partout en Algérie.",
            "lead":"Camions à benne 6x4 récents et semi-remorques pour tous types de charges, ainsi que des camions-citernes arroseurs. Pour transférer vos engins lourds, nous fournissons des porte-chars de 40 t.",
            "faq":[("Pouvez-vous mettre plusieurs camions sur un même chantier ?","Oui. Donnez-nous le volume à transporter et la distance. Nous fixons le nombre de camions et de semi-remorques, puis nous l'ajustons au fil du chantier.")]},
  "beton":{"lead":"Camions malaxeurs de 9 m³ et camions pompes à béton, avec chauffeur. Ils ont déjà alimenté les ouvrages de la ligne ferroviaire minière Est, entre Bouchegouf et Dréa.",
            "faq":[("Fournissez-vous aussi une pompe à béton ?","Oui. Un camion pompe MAN peut accompagner les malaxeurs pour couler en hauteur ou loin de l'accès.")]},
 }},
"ar": {
 "faq_common_2":("هل تعملون خارج الجزائر العاصمة؟","نعم، في كامل التراب الوطني. اشتغلنا في سوق أهراس على خط السكة الحديدية المنجمي الشرقي، وعبّأنا رافعة 200 طن في تندوف."),
 "all":"كل العتاد",
 "fam":{
  "levage":{"desc":"رافعات لكل التضاريس وشاحنات رافعة من 50 إلى 280 طن للكراء مع المشغّل في كامل التراب الوطني. تعبئة خلال 48 إلى 72 ساعة، والرافعات الثقيلة حسب البرمجة.",
            "lead":"شاحنات رافعة من 50 إلى 80 طن ورافعات لكل التضاريس حتى 280 طن، دائمًا مع المشغّل. رفعنا بلاطات جاهزة لخط السكة الحديدية المنجمي الشرقي في المشروحة.",
            "faq":[("ما أقصى حمولة يمكنكم رفعها؟","حتى 280 طن. الشاحنات الرافعة من 50 إلى 80 طن تصل خلال 48 إلى 72 ساعة. وما فوق 140 طن نبرمجه معك قبل أيام.")]},
  "terrassement":{"desc":"حفارات هيدروليكية على جنزير وعلى عجلات، وآليات مناولة، وآلات تسوية ومداحل للكراء مع المشغّل في كامل التراب الوطني، خلال 48 إلى 72 ساعة.",
            "lead":"حفارات على جنزير حتى فئة 50 طن، وحفارات على عجلات، وآليات مناولة Liebherr، وآلات تسوية ومداحل. كل آلية تصلك مع مشغّلها، جاهزة للعمل.",
            "faq":[("ما آليات الحفر والتسوية التي توفّرونها؟","حفارات هيدروليكية على جنزير (Hyundai، فئة 50 طن) وعلى عجلات (Doosan وCaterpillar)، وآليات مناولة Liebherr، وآلات تسوية John Deere، ومداحل.")]},
  "transport":{"desc":"شاحنات قلابة 6x4، ونصف مقطورات قلابة ومسطحة وصهريج، وشاحنات صهريج، وناقلات آليات 40 طن مع السائق في كامل التراب الوطني.",
            "lead":"شاحنات قلابة 6x4 حديثة ونصف مقطورات لكل أنواع الحمولة، إضافة إلى شاحنات صهريج للرش. ولنقل آلياتك الثقيلة نوفّر ناقلات آليات 40 طن.",
            "faq":[("هل يمكنكم وضع عدة شاحنات في ورشة واحدة؟","نعم. أخبرنا بالكمية المراد نقلها والمسافة، فنحدّد عدد الشاحنات ونصف المقطورات، ثم نعدّله حسب تقدّم الورشة.")]},
  "beton":{"lead":"شاحنات خلاطة سعة 9 م³ وشاحنات مضخة خرسانة مع السائق. سبق أن موّنت منشآت خط السكة الحديدية المنجمي الشرقي بين بوشقوف والدريعة.",
            "faq":[("هل توفّرون مضخة خرسانة أيضًا؟","نعم. ترافق شاحنة مضخة MAN الخلاطات للصبّ في العلو أو بعيدًا عن المدخل.")]},
 }},
"en": {
 "faq_common_2":("Do you work outside Algiers?","Yes, anywhere in Algeria. We have worked in Souk Ahras on the Eastern mining railway and sent a 200 t crane to Tindouf."),
 "all":"All equipment",
 "fam":{
  "levage":{"desc":"All-terrain cranes and truck cranes from 50 to 280 t for hire with operator anywhere in Algeria. Mobilised in 48 to 72 h; heavy cranes are scheduled.",
            "lead":"Truck cranes from 50 to 80 t and all-terrain cranes up to 280 t, always with an operator. We have lifted precast slabs for the Eastern mining railway at Mechroha.",
            "faq":[("What is the heaviest lift you can handle?","Up to 280 t. Truck cranes from 50 to 80 t arrive within 48 to 72 hours. Above 140 t, we schedule the crane with you a few days ahead.")]},
  "terrassement":{"desc":"Crawler and wheeled excavators, material handlers, graders and rollers for hire with an operator, anywhere in Algeria, within 48 to 72 hours.",
            "lead":"Crawler excavators up to the 50 t class and wheeled excavators, with Liebherr material handlers for loading. For platforms we add graders and rollers. Each machine arrives with its operator, ready to work.",
            "faq":[("Which earthmoving machines can you supply?","Crawler excavators (Hyundai, 50 t class) and wheeled excavators (Doosan, Caterpillar), Liebherr material handlers, John Deere graders and rollers.")]},
  "transport":{"desc":"6x4 dump trucks, tipper, flatbed and tank semi-trailers, water tankers and 40 t lowbeds with driver, anywhere in Algeria.",
            "lead":"Recent 6x4 dump trucks and semi-trailers for every kind of load, plus water tankers. To move your heavy machines, we provide 40 t lowbeds.",
            "faq":[("Can you put several trucks on one site?","Yes. Tell us the volume to move and the distance. We set the number of trucks and semi-trailers, then adjust it as the work progresses.")]},
  "beton":{"lead":"9 m³ truck mixers and concrete pump trucks, with driver. They have already supplied structures on the Eastern mining railway between Bouchegouf and Dréa.",
            "faq":[("Do you also supply a concrete pump?","Yes. A MAN pump truck can work with the mixers to pour at height or far from the access point.")]},
 }},
}


def appliquer(T, F):
    """Écrit les textes v2 dans les dictionnaires T (strings.py) et F (families.py)."""
    for l in ("fr", "ar", "en"):
        t, n = T[l], T2[l]
        for k in ("dept", "stats", "fleet_k", "fleet_h", "fleet_p", "fleet_cards", "fleet_btn", "title_mat", "desc_mat", "mat_h1", "mat_lead"):
            t[k] = n[k]
        t["svc"] = [(k, h, n["svc_txt"].get(k, p), li) for k, h, p, li in t["svc"]]
        t["ref_main"] = [(t["ref_main"][0][0], n["ref_crbc"]), (t["ref_main"][1][0], n["ref_cccc"])]
        t["v2"] = n
        f, m = F[l], F2[l]
        f["faq_common"] = [f["faq_common"][0], m["faq_common_2"]]
        f["all"] = m["all"]
        for fam, vals in m["fam"].items():
            f["fam"][fam].update(vals)
