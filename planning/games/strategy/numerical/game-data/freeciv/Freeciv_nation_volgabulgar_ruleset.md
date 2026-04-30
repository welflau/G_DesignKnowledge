# Freeciv(nation) · volgabulgar

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/volgabulgar.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的volgabulgar定义

## 正文
```ruleset
[nation_volgabulgar] 

name=_("Volga Bulgar") 
plural=_("?plural:Volga Bulgars") 
groups="European", "Medieval" 
legend=_("The Volga Bulgars were Medieval Turkic people inhabiting the\
 middle Volga region. They may have been descendants of European Huns\
 who migrated from the Ukrainian Steppe to the North. Their descendants\
 are the modern Chuvashes and Volga Tatars.")
leaders = {
 "name",                 "sex"
 "Şilki",                "male"
 "Almış",                "male"
 "Mikail bine Cäğfär",   "male"
 "Mö'mim bine Äxmäd",    "male"
 "Mö'min bine âl-Xäsän", "male"
 "Talib bine Äxmäd",     "male"
 "Abdullah Chelbir",     "male"
}

flag= "volga_bulgar" 
flag_alt = "-" 
style = "celtic" 

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Despotism",       _("Tarkhan %s"),     _("?female:Tarkhan %s")
 "Fundamentalism",  _("Grand Mufti %s"), _("?female:Grand Mufti %s")
 "Monarchy",        _("%s Khagan"),      _("?female:%s Khagan")
}

init_techs="" 
init_buildings="" 
init_units="" 

conflicts_with="tatar", "russian", "soviet"
civilwar_nations="gokturk", "khazar", "mordvin", "tatar", "chuvash"

;Cities names taken from http://www.s155239215.onlinehome.us/turkic/70_Dateline/KhazardatelineEn.htm

cities=

"Bulgar",
"Bilär",
"Nur-Suvar",
"Qaşan",
"Saratau",
"Saran",
"Astarkhan",
"Samar",
"Ufa",
"Sabakul",
"Kargaly",
"Moskha",
"Kolyn",
"Nukrat",
"Djunne Kala",
"Hin",
"Madjara Suba",
"Ardjam",
"Bustym",
"Djama",
"Ermek",
"Samis",
"Nazykh",
"Kaek",
"Tomek",
"Tim",
"Changhay",
"Menkhaz",
"Chyby",
"Yamalyak",
"Taz",
"Baduk",
"Iber-Bolgar",
"Kaik",
"Surgut",
"Djinesh",
"Gaskar",
"Sherkala",
"Totkarak",
"Tura Kala",
"Kargadan",
"Sarychin",
"Kyzyl Yar",
"Yauchy",
"Galich",
"Vologda",
"Talib",
"Ustyug",
"Iren",
"Bizek",
"Kerken",
"Shimal",
"Kadim Yul",
"Omek",
"Kozgun",
"Yabyn",
"Yalbak",
"Kasim",
"Masim",
"Tansu",
"Uel",
"Menkesh",
"Nuksa",
"Esegel",
"Churtan",
"Tselym-Balyn",
"Uchel",
"Kan",
"Djir",
"Khazar",
"Karatayak",
"Khalik Yar",
"Yar Chally",
"Karga",
"Lyakin",
"Yargaly",
"Buysyn",
"Ysta Kala",
"Baltavar",
"Abi Tura",
"Kostroma",
"Makhdi",
"Leybat",
"Baygul",
"Gasmankatay"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
