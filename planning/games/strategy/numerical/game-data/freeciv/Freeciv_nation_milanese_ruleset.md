# Freeciv(nation) · milanese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/milanese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的milanese定义

## 正文
```ruleset
[nation_milanese]

name = _("Milanese")
plural = _("?plural:Milanese")
groups="European", "Medieval", "Early Modern"
legend=_("Milan is the capital of Lombardy, a region in Northern Italy. From\
 1395 to 1797 it was the seat of the Duchy of Milan. Lombardy came under\
 Austrian domination after the Napoleonic War. In 1859 it was annexed by\
 Italy.")

leaders = {
 "name",                        "sex"
 "Alberto da Giussano",         "Male"
 "Matteo I Visconti",           "Male"
 "Gian Galeazzo Visconti",      "Male"
 "Beatrice d'Este",             "Female"
 "Francesco Sforza",            "Male"
 "Ludovico il Moro",            "Male"
 "Francesco Maria Sforza",      "Male"
 "Giuseppe Radetzky",           "Male"
 "Umberto Bossi",               "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism",       _("Condottiere %s"),  _("Condottiera %s")
 "Fundamentalism",  _("Fra %s"),          _("Mother Superior %s")
 "Monarchy",        _("Grand Duke %s"),   _("Grand Duchess %s")
 "Republic",        _("Captain %s"),      _("?female:Captain %s")
}

flag = "milan"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="piedmontese", "venetian", "swiss"

cities =
 "Milano",
 "Parma",
 "Verona",
 "Novara",
 "Pavia",
 "Alessandria",
 "Agnadello",
 "Piacenza",
 "Marignano",
 "Vicenza",
 "Piacenza",
 "Bellinzona",
 "Este",
 "Fornuovo",
 "Como",
 "Tortona",
 "Lodi",
 "Cremona",
 "Brescia",
 "Borgo San Donnino",
 "Bobbio",
 "Lecco",
 "Reggio nell'Emilia",
 "Cassamo",
 "Bergamo",
 "Feltre",
 "Ossola",
 "Asti",
 "Carrara",
 "Belluno",
 "Vercelli",
 "Bormio",
 "Novi Ligure",
 "Bassano del Grappa",
 "Riva del Garda",
 "Crema",
 "Lugano",
 "Tortona",
 "Pontremoli",
 "Saló",
 "Rocca d'Arazzo",
 "Locarno",
 "Sarzana",
 "Soncino",
 "Sesto San Giovanni",
 "Busto Arsizio",
 "Monza",
 "Mendrisio",
 "Cinisello Balsamo"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
