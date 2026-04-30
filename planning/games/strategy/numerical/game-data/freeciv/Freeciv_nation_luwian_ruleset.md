# Freeciv(nation) · luwian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/luwian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的luwian定义

## 正文
```ruleset
[nation_luwian]

name=_("Luwian")
plural=_("?plural:Luwians")
groups="Ancient", "Asian"
legend=_("The Luwians were an ancient Indo-European Anatolian people who \
lived in the late Bronze Age. For a time after the fall of the Hittite Empire\
 they took a dominant role in the region. One of the most important\
 Neo-Hittite states was Tabal (biblical Tubal), located in Syria and\
 Southeastern Anatolia.")
leaders = {
 "name",                "sex"
 "Pariyawatri",         "Male"
 "Isputahsu",           "Male"
 "Paddatisu",           "Male"
 "Piliya",              "Male"
 "Šunaššura I",         "Male"
 "Talzu",               "Male"
 "Šunaššura II",        "Male"
;Neo-Hittite Luwian kings:
 "Burutash",            "Male"
 "Tibe",                "Male"
 "Ura-Tarhundas",       "Male"
 "Ambaris",             "Male"
 "Hidi",                "Male"
 "Mugallu",             "Male"
}
flag="luwian"
flag_alt = "-"
style = "Babylonian"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="ottoman", "turkish", "byzantine", "roman", "arab", "armenian",
 "syrian", "seleucid", "palmyrene"
civilwar_nations = "hittite", "aramean", "mitanni" ; lycian, carian

cities =
 "Kummanni",
 "Tarhuntassa",
 "Adana",
 "Milid",
 "Hupisna",
 "Tuwana",
 "Qarqar",
 "Karatepe",
 "Kinalua",
 "Arpad",
 "Hamath",
 "Zincirli",
 "Marqasi",
 "Carchemiš",
 "Tunna",
 "Halab",
 "Nampigi",
 "Hatarikka",
 "Til-Barsip",
 "Guzana",
 "Pozanti",
 "Ikkuwaniya"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
