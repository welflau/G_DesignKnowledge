# Freeciv(nation) · rapanui

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/rapanui.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的rapanui定义

## 正文
```ruleset
[nation_rapanui]

name=_("Rapa Nui")
plural=_("?plural:Rapa Nui")
groups="Oceanian", "Medieval", "Early Modern"
legend=_("The Rapa Nui are the native Polynesian inhabitants of Easter\
 Island. They have inhabited the island since the end of the first\
 millennium CE. They are famous for having built large statues called\
 moai. This civilization was destroyed due to internal conflicts; in 1888\
 the island was annexed by Chile. Their script Rongorongo has never been\
 deciphered.")

leaders = {
 "name",                          "sex"
 "Hotu Matu'a",                   "Male"
 "Vakai",                         "Female"
 "Tu'u Maheke",                   "Male"
 "Aturaugi",                      "Male"
 "Atahega'a Miru",                "Male"
 "Mahuta Ariiki",                 "Male"
 "Uru Kenu",                      "Male"
 "Te Tuhunga",                    "Male"
 "Tangaroa Tatarara",             "Male"
 "Toko Te Rangi",                 "Male"
 "Hotu Iti",                      "Male"
 "Nga'ara",                       "Male"
 "Koreto",                        "Female"
 "Rukunga",                       "Male"


}
flag="rapa_nui"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="chilean"
civilwar_nations = "tahitian", "chilean"

cities =
 "Hanga Roa",
 "Orongo",
 "Mataveri",
 "Ana Kai Tongata",
 "Vinapu",
 "Hanga Piko",
 "Tongariki",
 "Vai Mata",
 "A Tanga",
 "Papa Tekena",
 "Vai Tara Kai Ua",
 "Nau Nau",
 "Te Pito Kura",
 "Hekii",
 "Tau A Ure",
 "Taharoa",
 "One Mahiki",
 "Tu'u Tahi",
 "Hanga Tetenga",
 "Runga Va'e",
 "Oroi",
 "Akahanga",
 "Ura Uranga Te Mahina",
 "Hanga Te'e",
 "Tarakiu",
 "Hanga Poukura",
 "Hanga Hahave",
 "Tahai",
 "A Kivi",
 "Te Peu",
 "Maikati Te Moa",
 "Motu Tautara",
 "Motu Ko Hepoko",
 "Huri A Urenga",
 "One Makihi",
 "Tau A Ure",
 "Te Pito Kura",
 "Motu Nui",
 "Motu Motiro Hiva"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
