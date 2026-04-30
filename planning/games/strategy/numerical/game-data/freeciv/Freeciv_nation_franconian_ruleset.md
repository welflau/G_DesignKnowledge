# Freeciv(nation) · franconian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/franconian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的franconian定义

## 正文
```ruleset
[nation_franconian] 

name=_("Franconian") 
plural=_("?plural:Franconians") 
groups="European", "Medieval" 
legend=_("Franconia was one of the stem duchies of the Holy Roman\
 Empire. Founded in the 9th century, unlike the other stem duchies it\
 didn't manage to consolidate itself and by the 12th century it had\
 completely disappeared. Franconia continues to exist as a cultural\
 region in the modern states of Bavaria, Thuringia and Baden-Wuerttemberg.")

leaders = {
 "name",                                "sex"
 "Eberhard",                            "Male"
 "Konrad III von Bibra",                "Male"
 "Lorenz von Bibra",                    "Male"
 "Julius Echter von Mespelbrunn",       "Male"
 "Franz Ludwig von Erthal",             "Male"
 "Johann Gottfried von Guttenberg",     "Male"
}

ruler_titles = {
 "government",       "male_title",          "female_title"
 "Despotism",        _("Duke %s"),          _("Duchess %s")
 "Fundamentalism",   _("Prince-Bishop %s"), _("Mother Superior %s")  
}

flag= "franconia" 
flag_alt = "-" 
style = "Celtic" 
init_techs="" 
init_buildings="" 
init_units="" 

conflicts_with="indonesian" ;similar flag
civilwar_nations="wuerttembergian", "bavarian", "hessian", "saxon"

cities=
"Nürnberg",
"Bayreuth",
"Ansbach",
"Bamberg",
"Würzburg",
"Coburg",
"Aschaffenburg",
"Hof",
"Erlangen",
"Fürth",
"Schweinfurt",
"Suhl",
"Hassfurt",
"Kitzingen",
"Höchstadt",
"Kronach",
"Heilbronn",
"Kulmbach",
"Neustadt an der Aisch",
"Bad Windsheim",
"Feuchtwangen",
"Rothenburg ob der Tauber",
"Wassertrüdingen",
"Gunzenhausen",
"Weissenburg",
"Solnhofen",
"Hilpoltstein",
"Forchheim",
"Pegnitz",
"Pyrbaum",
"Roth",
"Schwabach",
"Neckarsulm",
"Lohr",
"Karlstadt",
"Gemünden",
"Bad Kissingen",
"Lichtenfels",
"Sonneberg",
"Hildburghausen",
"Meiningen",
"Schmalkalden",
"Gersfeld",
"Schwäbisch Hall",
"Hilders",
"Naila",
"Münchberg",
"Selb",
"Bad Neustadt an der Saale",
"Creussen",
"Wunsiedel",
"Lauf",
"Wertheim",
"Hersbruck",
"Marktredwitz",
"Tauberbischofsheim"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
