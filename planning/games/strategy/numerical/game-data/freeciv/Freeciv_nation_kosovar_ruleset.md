# Freeciv(nation) · kosovar

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/kosovar.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的kosovar定义

## 正文
```ruleset
[nation_kosovar]

name=_("Kosovar")
plural=_("?plural:Kosovars")
groups="European", "Modern"
legend=_("Kosovo is a country on the Balkans. It declared independence in\
 2008. Serbia claims Kosovo as a province and its independence is not\
 universally recognized.")

leaders = {
 "name",                        "sex"
 "Mahmud Shevket Pasha",        "Male"
 "Bajram Curri",                "Male"
 "Isa Boletini",                "Male"
 "Fadil Hoxha",                 "Male"
 "Ibrahim Rugova",              "Male"
 "Fatmir Sejdiu",               "Male"
}

flag="kosovo"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "albanian", "serbian"

cities =
 "Prishtinë",	;Priština
 "Prizreni",	;Prizren
 "Ferizaji",	;Uroševac
 "Gjakovë",	;Đakovica
 "Mitrovica",	;Kosovska Mitrovica
 "Pejë",	;Peć
 "Gjilan",	;Gnjilane
 "Vushtrri",	;Vučitrn
 "Podujevë",	;Podujevo
 "Rahoveci",	;Orahovac
 "Fushë Kosovë", ;Kosovo Polje
 "Suharekë",	;Suva Reka
 "Kaçaniku",	;Kačanik
 "Klinë",	;Klina
 "Kamenicë",	;Kosovska Kamenica
 "Deçan",	;Dečani
 "Gllogovc",	;Glogovac
 "Dragash",	;Dragaš
 "Istog",	;Istok
 "Leposaviq",	;Leposavić
 "Lipjan",	;Lipljan
 "Obiliq",	;Obilić
 "Skënderaj",	;Srbica
 "Shtime",	;Štimlje
 "Shtërpcë",	;Štrpce
 "Viti",	;Vitina
 "Zubin Potok",	;Zubin Potok
 "Zveçan",	;Zvečan
 "Malishevë",	;Mališevo
 "Novobërdë",	;Novo Brdo
 "Junik",	;Junik
 "Hani i Elezit", ;Đeneral Janković
 "Mamushë",	;Mamuša
 "Graçanica",	;Gračanica
 "Ranillug",	;Ranilug
 "Partesh",	;Parteš
 "Kllokot"	;Klokot

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
