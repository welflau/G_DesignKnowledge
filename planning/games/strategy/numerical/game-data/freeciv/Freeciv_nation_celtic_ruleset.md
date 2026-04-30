# Freeciv(nation) · celtic

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/celtic.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的celtic定义

## 正文
```ruleset
[nation_celtic]

translation_domain="freeciv"

name=_("Celtic")
plural=_("?plural:Celts")
groups="Ancient", "European", "Core"
legend=_("The Celts were an Indo-European ethno-linguistic complex in Western\
 Europe, probably originating from the area between the upper Rhine and\
 upper Danube, from the Urnfield culture and the western group of the\
 Hallstatt culture. The Celts were known as cruel and savage warriors\
 who terrorized the ancient civilized peoples of Europe and Asia Minor.\
 The Celts colonized much of Europe and had a large influence on the\
 development of European civilization.")
leaders = {
       "name",                "sex"
       "Noudentos",           "Male"         ;Nuada Airgetlám
       "Milesios",            "Male"         ;Míl Espáine
       "Talorgos",            "Male"         ;Talorc
       "Brennos",             "Male"         ;Brennus
       "Keretrios",           "Male"         ;Cerethrius
       "Bolgios",             "Male"         ;Bolgius
       "Wiridomaros",         "Male"         ;Viridomarus
       "Diwitiakos",          "Male"         ;Divitiacus
       "Werkingetorix",       "Male"         ;Vercingetorix
       "Boudikka",            "Female"       ;Boadicea
       "Rigotamos",           "Male"         ;Riothamus
       "Arktorios",           "Male"         ;Arthur Gernow
       "Windoseibara",        "Female"       ;Guinevere
}

flag="celtic"
flag_alt = "-"
style = "Celtic"

ruler_titles = {
  "government",     "male_title",          "female_title"
  "Despotism",      _("Great Warrior %s"), _("?female:Great Warrior %s")
  "Communism",      _("Brother %s"),       _("Sister %s")
  "Republic",       _("Spokesman %s"),     _("Spokeswoman %s")
  "Democracy",      _("Speaker %s"),       _("?female:Speaker %s")
  "Fundamentalism", _("High Druid %s"),    _("?female:High Druid %s")
}

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Boian", "Belgic", "Briton", "Gallic", "Helvetian", "Gaelic",
               "Scottish Gaelic", "Manx", "Welsh", "Cornish", "Breton", "Irish",
               "Celtiberian", "Indo-European" ; Galatian Noric
civilwar_nations = "Boian", "Belgic", "Briton", "Gallic", "Helvetian", "Gaelic",
                   "Scottish Gaelic", "Manx", "Welsh", "Cornish", "Breton", "Irish",
                   "Celtiberian" ; Galatian Noric Lusitanian

cities =
    ;Urnfield culture:
    "Knoviz",
    "Milavce",
    "Velatice",
    "Baierdorf",
    "Čaka",
    "Unstrut",
    "Châtenay",
    "Lingolsheim",
    "Marburg",
    "Hanau",
    "Friedberger",
    "Goloring",
    ;Halstatt culture:
    "Halstatt",
    "Gräfenbühl",
    "Hochmichele",
    "Hochdorf",
    "Heuneburg",
    "Châtillon-sur-Seine",
    "Vix",
    "Molpír",
    "Býčí Skála",
    "Frögg",
    "Hirschlanden",
    "Glauberg",
    ;La Téne culture:
    "La Téne",
    "Engehalbinsel",
    "Jolimont",
    "Manching",
    "Mormont",
    "Münsingen",
    "Petinesca",
    "Basel",
    "Bibracte",
    "Erstfeld",
    "Bopfingen",
    "Fellbach-Schmiden",
    "Kleinaspergle",
    "Waldalgesheim",
    "Dürrnberg",
    "Donnersberg",
    "Vill",
    "Sandberg",
    "Titelberg",
    "Reinheim"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
