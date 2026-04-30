# Freeciv(nation) · greek

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/greek.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的greek定义

## 正文
```ruleset
[nation_greek]

translation_domain="freeciv"

name=_("Greek")
plural=_("?plural:Greeks")
groups="Ancient", "European", "Core"
legend=_("The ancient Greeks, between Mycenae and the Roman conquest.")

leaders = {
 "name",                "sex"
 "Alexandros Molossus", "Male"
 "Perikles",            "Male"
 "Leonidas",            "Male"
 "Solon",               "Male"
 "Alkibiades",          "Male"
 "Megas Alexandros",    "Male" ; Alexander the Great
 "Gorgo",               "Female"
}

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Anarchy",         _("Usurper %s"),        _("?female:Usurper %s")
 "Despotism",       _("Despot %s"),         _("?female:Despot %s")
 "Fundamentalism",  _("Elder %s"),          _("?female:Elder %s")
}

flag="greece_ancient"
flag_alt = "greece"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="macedon", "epirote", "Byzantine", "Cretan", "Pontic", "italian greek"

cities =
; Original city list with native Greek orthography
 "Athinai",
 "Sparti",
 "Thivai",
 "Korinthos",
 "Konstandinoupolis",
 "Militos",
 "Efesos",
 "Peiraiefs (ocean)",
 "Argos",
 "Megalopolis",
 "Elefsis",
 "Chalkis",
 "Eretreia",
 "Thessaloniki (ocean)",
 "Edessa",
 "Nikopolis",
 "Nafpaktos",
 "Patrai (ocean)",
 "Olymbia (mountains)",
 "Pylos",
 "Nafplion (ocean)",
 "Mykinai",
 "Epidavros (ocean)",
 "Avlis",
 "Orchomenos",
 "Marathon",
 "Delfoi",
 "Thermopylai (hills)",
 "Faliron",
 "Nikaia",
 "Iraklion (ocean)",
 "Potidaia",
 "Stagira",
 "Olynthos",
 "Kolofon",
 "Fokaia",
 "Amfissa",
 "Atalanti",
 "Oropos",
 "Livadeia",
 "Larisa (river)", 
 "Iolkos",
 "Amfiklaia",
 "Kyzikos",
 "Alikarnassos",
 "Pergamos",
 "Pydna",
 "Filadelfeia",
 "Thermi",
 "Amfipolis",
 "Kerkyra (ocean)",
 "Ithaki",
 "Thira (ocean)",
 "Panormos",
 "Ortygia",
 "Milos (ocean)", 
 "Lykosoura",
 "Amyklai",
 "Klazomenai",
 "Kynos Kefalai",
 "Distomon (hills, mountains)",
; Additional cities sorted in joint population/chronology order
 "Smyrni (ocean)",
 "Alexandreia (ocean)", 
 "Nikomideia",
 "Trapezous (ocean)",
 "Chania", 
 "Knossos", 
 "Pafos",
 "Mitylini (ocean)",
 "Chios", 
 "Sinopi",
 "Rodos (ocean)",
 "Adrianoupolis (river)",
 "Volos", 
 "Neapolis",
 "Ammostochos",
 "Arta (river)", 
 "Serrai",
 "Katerini",
 "Trikala",
 "Lamia",
 "Agrinion", 
 "Xanthi",
 "Veroia",
 "Drama",
 "Komotini", 
 "Troia",
 "Kozani", 
 "Karditsa (!ocean)",
 "Samos",
 "Pirgos", 
 "Tripolis (mountains)",
 "Rethymnon",
 "Kastoria",
 "Ioannina (river)",
 "Florina",
 "Preveza",
 "Kilkis",
 "Ayios Nikolaos",
 "Zakynthos (ocean)", 
 "Igoumenotsa",
 "Mesolongion",
 "Lefkosia", 
 "Grevena",
 "Argostolion (ocean)",
 "Karpenisi",
 "Lefkas", 
 "Militos",
 "Polygyros",
 "Kalamai", 
 "Kariai (mountains)",
 "Ermoupolis",
 "Ydra (ocean)",
 "Kavala (ocean)",
 "Alexandroupolis (ocean)",
 "Tembi (river)"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
