# Freeciv(nation) · swahili

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/swahili.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的swahili定义

## 正文
```ruleset
[nation_swahili]

name=_("Swahili")
plural=_("?plural:Swahili")
groups="African", "Medieval"
legend=_("The Swahili are a Bantu ethnic group living along the Eastern\
 Coast of Africa. From about the 9th century onwards the region, at the\
 crossroads of Islamic and African cultural influences, saw the rise of\
 Swahili city states, including Zanzibar, Kilwa Kisiwani, Mozambique and\
 Sofala. The cities grew to prominence thanks to their ivory, gold, slave\
 and spice trade. The arrival of the Portuguese around 1500 coincided with\
 the decline of the Swahili polities, but the Swahili remained a dominant\
 cultural element in Eastern Africa. Today, the Swahili language\
 (Kiswahili) is used as lingua franca by more than 50 million people in\
 Eastern Africa and is an official language of Kenya, Tanzania, Uganda,\
 the Comoros and the African Union.")

leaders = {
 "name",                   "sex"
 "Fumo Liyongo",           "Male"
 "Mwana Mkisi",            "Female"
 "Al-Hasan ibn Sulaiman",  "Male"
 "Bwana Mkuu",             "Male"
 "Fumo Madi ibn Abi Bakr", "Male"
 "Abushiri",               "Male"
 "Tippu Tip",              "Male"
}

flag ="swahili"
style = "babylonian"

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Fundamentalism",  _("Mullah %s"),          _("?female:Mullah %s")
 "Monarchy",        _("Sultan %s"),          _("Sultana %s")
}

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "zanzibari", "comorian", "mozambican", "tanganyikan", "kenyan"
conflicts_with = "zanzibari", "comorian", "mozambican", "tanganyikan", "kenyan",
 "tanzanian", "ugandan"

cities =
 "Kilwa Kisiwani",
 "Mvita", ; Mombasa
 "Zanzibar",
 "Sofala",
 "Msumbiji", ; Ilha de Moçambique
 "Moroni",
 "Gedi",
 "Malindi",
 "Songo Mnara",
 "Lamu",
 "Mzizima", ; Dar es Salaam
 "Pangani",
 "Manda",
 "Shanga",
 "Jumba la Mtwana",
 "Bagamoyo",
 "Kilwa Kivinje",
 "Chake Chake",
 "Mutsamudu",
 "Mwiini", ; Baraawe
 "Witu",
 "Kivinja",
 "Takwe",
 "Msasani",
 "Ujiji",
 "Makunduchi",
 "Sofala",
 "Pate",
 "Shela",
 "Kilwa Masoko",
 "Kua",
 "Quelimane",
 "Fomboni",
 "Husuni Kubwa",
 "Mamoudzou",
 "Faza",
 "Shanga",
 "Mahilaka",
 "Mikindani",
 "Saadani",
 "Kiwayu",
 "Tanga",
 "Wete",
 "Siyu",
 "Matondoni",
 "Ungwana"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
