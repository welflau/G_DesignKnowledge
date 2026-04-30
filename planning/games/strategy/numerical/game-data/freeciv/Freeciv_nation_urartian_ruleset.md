# Freeciv(nation) · urartian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/urartian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的urartian定义

## 正文
```ruleset
[nation_urartian]

name=_("Urartian")
plural=_("?plural:Urartians")
groups="Ancient", "Asian"
legend=_("Urartu was an ancient Hurrian state located around Lake Van in\
 the eastern part of Anatolia. The earliest historical mention of Urartu\
 comes from texts of the Assyrian king Shalmaneser I dating from the 13th\
 century BCE. It is thought that Urartu was a multiethnic state in which\
 Hurrian tribes likely formed the dominant element. Urartu played an\
 important role in shaping the modern Armenian people.")
leaders = {
 "name",                "sex"
 "Arame",               "Male"
 "Lutipri",             "Male"
 "Sarduri I",           "Male"
 "Ishpuini",            "Male"
 "Menua",               "Male"
 "Argishti I",          "Male"
 "Sarduri II",          "Male"
 "Rusa I",              "Male"
 "Argishti II",         "Male"
 "Rusa II",             "Male"
 "Sarduri III",         "Male"
 "Eriména",             "Male"
 "Rusa III",            "Male"
 "Sarduri IV",          "Male"
 "Rusa IV",             "Male"
}
flag="urartu"
flag_alt = "-"
style = "Babylonian"

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Anarchy",         _("Pretender %s"),    _("?female:Pretender %s")
 "Despotism",       _("Prince %s"),       _("Princess %s")
 "Communism",       _("Brother %s"),      _("Sister %s")
 "Republic",        _("Spokesman %s"),    _("Spokeswoman %s")
 "Democracy",       _("Speaker %s"),      _("?female:Speaker %s")
}

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Mitanni", "Armenian", "Kurdish", "Seleucid", "Turkish",
               "Ottoman"
civilwar_nations = "Mitanni", "Assyrian", "Median", "Armenian"

cities =
 "Tushpa",
 "Ardini",
 "Rusahinili",
 "Charduriqurda",
 "Marmos",
 "Erebuni",
 "Argishtihinili",
 "Archuqiuni",
 "Teishebaini",
 "Isuwa",
 "Anachi",
 "Argichtiqiui",
 "Gurgum",
 "Kummukh",
 "Samallu",
 "Milid",
 "Kauri",
 "Chupa",
 "Arqanis",
 "Tumeichki",
 "Akhuriani",
 "Kipani",
 "Touchan",
 "Ichqugulu",
 "Ulliba",
 "Diaueqi",
 "Khate",
 "Etiuni",
 "Arpad",
 "Eriaki",
 "Ordaklou",
 "Alzi",
 "Zogalu",
 "Qaria",
 "Amimu",
 "Menouaini",
 "Souhmi",
 "Urmeniuqini",
 "Kubuchkia",
 "Kurchi",
 "Luqiuni",
 "Biaini",
 "Arzachkun",
 "Uchnu",
 "Tachtepe",
 "Manna",
 "Delibala",
 "Zenziun",
 "Uelikuqi",
 "Tuliku",
 "Argukiu",
 "Qiequni",
 "Maqaltu",
 "Ichtamani",
 "Gilzan"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
