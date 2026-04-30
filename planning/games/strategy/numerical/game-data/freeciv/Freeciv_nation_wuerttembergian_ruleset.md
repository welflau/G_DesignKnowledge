# Freeciv(nation) · wuerttembergian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/wuerttembergian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的wuerttembergian定义

## 正文
```ruleset
[nation_wuerttembergian]

name=_("Wuerttembergian")
plural=_("?plural:Wuerttembergians")
groups="Medieval", "Early Modern", "European"
legend=_("Wuerttemberg was a country in Swabia, in southwestern Germany.\
 After World War II it was merged with Baden and Hohenzollern to form\
 the land of Baden-Wuerttemberg.")

leaders = {
 "name",                        "sex"
 "Konrad I",                    "Male"
 "Ulrich der Stifter",          "Male"
 "Eberhard der Erlauchte",      "Male"
 "Eberhard III",                "Male"
 "Friedrich Wilhelm Karl",      "Male"
 "Eugen Bolz",                  "Male"
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Democracy", _("Minister-President %s"), _("?female:Minister-President %s")
 "Despotism",       _("Duke %s"),        _("Duchess %s")
 "Fundamentalism",  _("Bishop %s"),      _("?female:Bishop %s")
}

flag="wuerttemberg"
flag_alt = "germany"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "badian", "bavarian", "franconian", "swiss"

cities =
 "Stuttgart",
 "Ludwigsburg",
 "Urach",
 "Neuenstadt",
 "Winnental",
 "Mömpelgard",
 "Heilbronn",
 "Öhringen",
 "Calw",
 "Ulm",
 "Rottenburg",
 "Rottweil",
 "Ehingen",
 "Altdorf",
 "Schorndorf",
 "Ellwangen",
 "Neckarsulm",
 "Gmünd",
 "Tübingen",
 "Schwäbisch Hall",
 "Böblingen",
 "Besigheim",
 "Backnang",
 "Neuenstein",
 "Alpirsbach",
 "Balingen",
 "Hornberg",
 "Kirchheim",
 "Biberach",
 "Waldsee",
 "Aalen",
 "Cannstatt",
 "Bietigheim",
 "Beilstein",
 "Nitzenhausen",
 "Altensteig",
 "Herrenberg",
 "Spaichingen",
 "Münsingen",
 "Blaubeuren",
 "Göppingen",
 "Gaildorf",
 "Esslingen",
 "Köngen",
 "Leonberg",
 "Marbach",
 "Maulbronn",
 "Vaihingen",
 "Waiblingen",
 "Brackenheim",
 "Güglingen",
 "Kirchhausen",
 "Lauffen",
 "Möckmühl",
 "Weinsberg",
 "Schönthal",
 "Freudenstadt",
 "Herrenalb",
 "Nagold",
 "Neuenbürg",
 "Weil",
 "Horb",
 "Rosenfeld",
 "Sulz",
 "Stokach",
 "Tuttlingen",
 "Nürtingen",
 "Reutlingen",
 "Wiensteig",
 "Riedlingen",
 "Saulgau",
 "Urspring",
 "Zwiefalten",
 "Murrhardt",
 "Welzheim",
 "Winnenden",
 "Giegen",
 "Heidenheim",
 "Hohnhardt",
 "Nördlingen",
 "Schmidelfeld",
 "Vellberg"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
