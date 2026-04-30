# Freeciv(nation) · mikmaq

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/mikmaq.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的mikmaq定义

## 正文
```ruleset
[nation_mikmaq] 

name=_("Mi'kmaq") 
plural=_("?plural:Mi'kmaq") 
groups="American" 
legend=_("Today numbering roughly 25,000, the Mi'kmaq inhabited (and\
 largely continue to) Nova Scotia. The first Mi'kmaq to convert to\
 Christianity did so in 1610 under French suzerainty. French\
 rule gave way to English and English to Canadian.")

leaders = {
 "name",                "sex"
 "Membertou",           "Male"
 "Matiew Plansue",      "Male"
 "So'sep Ku'l",         "Male"
 "Sa'n Teni",           "Male"
}
ruler_titles = {
 "government",      "male_title",            "female_title"
 "Democracy",       _("Principal Chief %s"), _("?female:Principal Chief %s")
 "Fundamentalism",  _("Shaman %s"),          _("?female:Shaman %s")
 "Monarchy",        _("Great Chief %s"),     _("?female:Great Chief %s")
 "Republic",        _("Spokesman %s"),       _("Spokeswoman %s")
}


flag = "mikmaq" 
flag_alt = "-" 
style = "Celtic" 

init_techs="" 
init_buildings="" 
init_units="" 
civilwar_nations="cree", "iroquois", "inuit" 

cities = 
"Miawpukwek", 
"Epekwitk", 
"Malikiaq", 
"Ulustuk", 
"L’setkuk", 
"Puktusk", 
"Eskinuopitijk", 
"Waqmitkuk", 
"Potlotek", 
"Natuaqanek", 
"Keskapekiaq", 
"Puksaqtéknékatik", 
"Oqpíkanjik", 
"Lsipuktuk", 
"Eskisoqnik", 
"Amlamkuk Kwesawék", 
"Kespék", 
"Pesikitk", 
"Listikujk", 
"Maupeltuk", 
"Wékopekwitk", 
"Kampalijek", 
"Kékwapskuk", 
"Paqtnkek", 
"Sipekníkatik", 
"Wékoqmáq", 
"Metepnákiaq"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
