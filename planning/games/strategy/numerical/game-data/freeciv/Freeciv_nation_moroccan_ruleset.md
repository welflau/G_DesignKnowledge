# Freeciv(nation) · moroccan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/moroccan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的moroccan定义

## 正文
```ruleset
[nation_moroccan]

name=_("Moroccan")
plural=_("?plural:Moroccans")
groups="Medieval", "Early Modern", "Modern", "African"
legend=_("Modern Morocco gained independence in 1956. However, the area\
 has been inhabited since at least 8000 BCE. In classical times the region\
 was known as Mauretania.")

leaders = {
 "name",                        "sex"
 "Uqba ibn Nafi",               "Male" ; A general of the Umayyads, d. 683.
 "Tariq ibn Ziyad",             "Male" ; An Amazigh general of the Umayyads,
                                       ; d. 720.
 "Idris I",                     "Male" ; Founder of the Idrisid Dynasty,
                                       ; ruled 788 - 791.
 "Youssef Ibn Tachafine",       "Male" ; Reigned 1009-1106, founder of.
                                       ; The Almoravide Amazigh Dynasty.
 "Ismail Ibn Sharif",           "Male" ; Reigned 1672 - 1727.
 "Mohammed ben Abdallah",       "Male" ; Reigned 1757 - 1790.
 "Mohammed V",                  "Male" ; Reigned 1927 - 1953, 1957 - 1961.
 "Hassan II",                   "Male" ; Reigned 1961 - 1999.
 "Fatima Al-Fihriya",           "Female" ; Prominent educator, d 880.
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Despotism",       _("Sheikh %s"),          _("Shaykha %s")
 "Fundamentalism",  _("Caliph %s"),          _("Calipha %s")
 "Republic",        _("Vizier %s"),          _("?female:Vizier %s")
}

flag="morocco"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="Amazigh", "Riffian", "Sahrawi"

cities =
 "Rabat",
 "Casablanca", ; Dar al-Beida
 "Fès",
 "Marrakech",
 "Béni Mellal",
 "Agadir",
 "Meknès",
 "Oujda",
 "Kenitra",
 "Tétouan",
 "Essaouira",
 "Mohammadia",
 "Ouarzazat",
 "Safi",
 "Salé",
 "Tangier",
 "Nador",
 "Taourirt",
 "Settat",
 "Guelmim",
 "Laayoun",
 "Dakhla",
 "Figuig", 
 "Ifrane",
 "Azrou",
 "Imouzzar",
 "Chichaoua",
 "Chefchaouen",
 "Assila",
 "Taza",
 "El Hajeb",
 "Errachidia",
 "Amizmiz",
 "Tameslouht",
 "Tamesna",
 "Tan-Tan",
 "Smara",
 "Boujdour",
 "Lagouira",
 "Sidi Kacem",
 "Ben Slimane",
 "Khouribga",
 "El Jadida",
 "Moulay Yacoub",
 "Bhalil",
 "Boulemane",
 "Assa",
 "Zag",
 "Berkane",
 "Jerada",
 "Temara",
 "Khemisset",
 "Tiznit",
 "Zagora",
 "Taroudant",
 "Azilal",
 "Chefchaouen",
 "Larache",
 "Tarfaya",
 "Erfoud",
 "Midelt",
 "Al Hoceima",
 "Tétouan",
 "Ouarzazate",
 "Er Rachidia",
 "Saidia",
 "Zagora",
 "Walili" ; Volubilis

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
