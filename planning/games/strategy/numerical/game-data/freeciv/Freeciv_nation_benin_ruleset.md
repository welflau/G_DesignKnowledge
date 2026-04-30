# Freeciv(nation) · benin

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/benin.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的benin定义

## 正文
```ruleset
[nation_benin] 

name=_("Benin") 
plural=_("?plural:Benin") 
groups="Medieval", "Early Modern", "African" 
legend=_("Not to be confused with the modern republic of Benin,\
 the Kingdom of Benin was founded by Edo speakers sometime between\
 the 12th and 14th centuries. Benin united a large area of land\
 west of the Niger river delta, reaching its peak in the 16th\
 century. Eweka I founded the Uzama, or Councilors of State, to\
 aid in the accession of a new Oba, or king. Its fortunes waned as\
 Europeans chose other kingdoms to trade with after Benin's main\
 port silted up. The Kingdom finally ended in 1897 when the\
 British assumed control.")

leaders = {
 "name",        "sex"
 "Obagodo",     "Male"
 "Owodo",       "Male"
 "Evian",       "Male"
 "Ogiamne",     "Male"
 "Oranmiyan",   "Male"
 "Eweka I",     "Male"
 "Ornogbua",    "Male"
}

ruler_titles = {
 "government",  "male_title",       "female_title"
 "Democracy",   _("Councillor %s"), _("?female:Councillor %s") 
}

flag= "benin_ancient" 
flag_alt = "-" 
style = "Tropical" 

init_techs="" 
init_buildings="" 
init_units="" 

civilwar_nations = "Malian", "Kongo", "Dahomean"

cities = 
"Benin", 
"Gwatto", 
"Ego", 
"Usama", 
"Warri", 
"Ikara", 
"Oka", 
"Isebu-Ode", 
"Owo", 
"Akure", 
"Lagos", 
"Idah", 
"Uromi", 
"Ifon", 
"Siluko", 
"Auchi", 
"Ilushi", 
"Agbor Bojiboji", 
"Supele", 
"Asaba", 
"Ore", 
"Ughelli", 
"Ihiala", 
"Okitipupa", 
"Ikorodu", 
"Oudo"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
