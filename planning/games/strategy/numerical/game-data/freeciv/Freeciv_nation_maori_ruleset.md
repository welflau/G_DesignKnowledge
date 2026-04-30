# Freeciv(nation) · maori

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/maori.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的maori定义

## 正文
```ruleset
[nation_maori]

name=_("Maori")
plural=_("?plural:Maori")
groups="Oceanian"
legend=_("The Maori are a Polynesian people that migrated to and settled the\
 island group that is now New Zealand. According to archeological evidence,\
 the migration commenced in the 900s and continued until the 1400s.")

leaders = {
 "name",                "sex"
 "Te Kooti",            "Male"
 "Hone Heke",           "Male"
 "Potatau",             "Male"
 "Tawhiao",             "Male"
 "Apirana Ngata",       "Male"
 "Te Atairangi Kaahu",  "Female"
 "Te Puea Herangi",     "Female"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Monarchy",        _("Paramount Chief %s"), _("?female:Paramount Chief %s")
 "Republic",        _("Spokesman %s"),       _("Spokeswoman %s")
 "Democracy",       _("Principal Chief %s"), _("?female:Principal Chief %s")
 "Fundamentalism",  _("Elder %s"),           _("?female:Elder %s")
}

flag="maori"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="new zealand", "papuan"

cities =
 "Tamaki (hills, ocean)",	; Auckland (Maorification: Ākarana)
 "Rotorua (swamp, river, !ocean)",
 "Ngaruawahia",
 "Manukau (grassland, ocean)",
 "Whakatane",
 "Wairoa (ocean, plains)",
 "Kataia",
 "Whangarei", 
 "Te Puke",
 "Te Whanganui (hills, ocean)",	; Wellington; alt. Maori: Poneke
 "Otautahi (plains, ocean)",	; Christchurch
 "Otepoti (ocean)",		; Dunedin
 "Waitakere",
 "Waiheke (ocean)",
 "Matakana",
 "Hokianga (ocean)",
 "Manawatu (river, plains)",
 "Waikato",
 "Kawerau (hills)",
 "Wairarapa",
 "Te Aroha (grassland)",
 "Urewera",
 "Mahia",
 "Waihi (ocean, mountains)",
 "Kaipara (ocean)",
 "Hikurangi (mountains)",
 "Heretaunga (plains)",
 "Hikurangi",
 "Kamo",
 "Tangiwai",
 "Takapuna",
 "Waitemata",
 "Papatoetoe",
 "Papakura",
 "Tamaki",
 "Porirua",
 "Ngaio",
 "Opotiki"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
