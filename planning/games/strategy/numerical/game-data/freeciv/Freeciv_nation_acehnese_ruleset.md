# Freeciv(nation) · acehnese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/acehnese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的acehnese定义

## 正文
```ruleset
[nation_acehnese]

name=_("Acehnese")
plural=_("?plural:Acehnese")
groups="Asian", "Early Modern"
legend=_("The Sultanate of Aceh located on the western tip of the island of\
 Sumatra was a regional power in the 16th and 17th centuries, controlling\
 much of the trade through the Strait of Malacca. Aceh was subjugated by\
 the Dutch in the bloody Aceh War of 1873-1903.")

leaders = {
 "name",                "sex"
 "Ali Mughayat Syah",   "Male"
 "Alauddin al-Kahar",   "Male"
 "Iskandar Muda",       "Male"
 "Iskandar Thani",      "Male"
 "Taj ul-Alam",         "Female"
 "Zainatuddin",         "Female"
 "Tuanku Ibrahim",      "Male"
 "Muhammad Daud Syah",  "Male"
 "Cut Nyak Meutia",     "Female"
 "Hasan di Tiro",       "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Monarchy",        _("Sultan %s"),          _("Sultana %s")
 "Republic",        _("Governor %s"),        _("?female:Governor %s")
 "Fundamentalism",  _("Imam %s"),            _("Imama %s")
}

flag="aceh"
flag_alt="-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Indonesian", "Malaysian"

cities =
 "Kutaraja",
 "Pasai",
 "Peureulak",
 "Weh (ocean)",
 "Simeulue (ocean)",
 "Pariaman",
 "Padang",
 "Indrapura",
 "Muko-muko",
 "Siberut (ocean)",
 "Aru",
 "Deli",
 "Kedah",
 "Penang (ocean)",
 "Pahang",
 "Trengganu",
 "Siak",
 "Rengat",
 "Indragiri",
 "Nias (ocean)",
 "Perlak",
 "Lhokseumawe",
 "Langsa",
 "Sabang",
 "Subulussalam",
 "Lhoksukon",
 "Takengon",
 "Meulaboh",
 "Simpang Tiga Redelong",
 "Nias",
 "Bireun",
 "Dewantara",
 "Kuala Simpang",
 "Siglo",
 "Alaban",
 "Blangpidie",
 "Calang",
 "Garot",
 "Jantho",
 "Kuta Reh",
 "Leupung",
 "Lhoknga",
 "Tapaktuan",
 "Teunom"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
