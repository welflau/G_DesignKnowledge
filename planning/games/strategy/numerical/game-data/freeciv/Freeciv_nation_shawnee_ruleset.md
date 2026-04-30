# Freeciv(nation) · shawnee

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/shawnee.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的shawnee定义

## 正文
```ruleset
[nation_shawnee] 

name=_("Shawnee") 
plural=_("?plural:Shawnee") 
groups="American" 
legend=_("An Algonquian people, the Shawnee were led by Tikamthi (better\
 known as Tecumseh) and his brother Tenskwatawa in trying to create a\
 pan-native alliance against American expansionism but were ultimately\
 unsuccessful and made to resettle in the Indian Territory (modern Oklahoma).")

leaders = {
 "name",                "sex"
"Paxinos",              "Male"
"Tenskwatawa",          "Male"
"Tikamthi",             "Male"
"Nererahhe",            "Male"
"Waweyapiersenwaw",     "Male"
"Tanacharison",         "Male"
}
ruler_titles = {
 "government",      "male_title",            "female_title"
 "Monarchy",        _("Great Chief %s"),     _("?female:Great Chief %s")
 "Republic",        _("Spokesman %s"),       _("Spokeswoman %s")
 "Democracy",       _("Principal Chief %s"), _("?female:Principal Chief %s")
 "Fundamentalism",  _("Shaman %s"),          _("?female:Shaman %s")
}

flag = "shawnee" 
flag_alt = "-" 
style = "Celtic" 

init_techs="" 
init_buildings="" 
init_units="" 
civilwar_nations="iroquois", "anishinaabe", "cree" 

cities = 
"Chalahgawtha", 
"Kittanning", 
"Shamokin", 
"Sonnioto", 
"Chalahgawtha", ; Chillicothe 
"Wakatomika", 
"Kagoughsage", 
"Kymulga", 
"Wakatawicks", 
"Mequachake", 
"Sawanogi", 
"Piqua", 
"Peixtan", 
"Nawake", 
"Wapaughkonetta", 
"Kickenapawling", 
"Conedogwinit", 
"Scoutash", 
"Chililisuagi", 
"Wakarusa"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
