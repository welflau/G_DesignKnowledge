# Freeciv(nation) · malawian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/malawian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的malawian定义

## 正文
```ruleset
[nation_malawian]

name = _("Malawian")
plural = _("?plural:Malawians")
groups="African", "Modern"
legend=_("Called Nyasaland by the British, Malawi adopted its current\
 name, referring to the old Maravi Empire upon independence in 1964.\
 The country's politics were dominated by Dr. Hastings Banda for three\
 decades, until he was stripped of his titles in 1993.")
leaders = {
 "name",               "sex"
 "Kanyama Chiume",     "Male"
 "Hastings Banda",     "Male"
 "Bingu wa Mutharika", "Male"
 "Joyce Banda",        "Female"
}

ruler_titles = {
 "government",      "male_title",    "female_title"
 "Fundamentalism",  _("Bishop %s"),     _("?female:Bishop %s")
}

flag = "malawi"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Zambian", "Zimbabwean"

cities =
 "Lilongwe",
 "Blantyre",
 "Mzuzu",
 "Mangochi",
 "Mzimba",
 "Dedza",
 "Kasungu",
 "Thyolo",
 "Dowa",
 "Mulanje",
 "Machinga",
 "Ntcheu",
 "Mchinji",
 "Chikwawa",
 "Salima",
 "Balaka",
 "Phalombe",
 "Nkhotakota",
 "Chiradzulu",
 "Karonga",
 "Nsanje",
 "Ntchisi",
 "Nkhata Bay (lake)",
 "Chitipa",
 "Rumphi",
 "Neno",
 "Mwanza",
 "Zomba",
 "Likoma",
 "Liwonde",
 "Mponela",
 "Luchenza",
 "Ngabu",
 "Livingstonia",
 "Chipoka"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
