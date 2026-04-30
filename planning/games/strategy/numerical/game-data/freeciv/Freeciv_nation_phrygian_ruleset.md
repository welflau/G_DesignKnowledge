# Freeciv(nation) · phrygian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/phrygian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的phrygian定义

## 正文
```ruleset
[nation_phrygian]

name=_("Phrygian")
plural=_("?plural:Phrygians")
groups="Ancient", "Asian"
legend=_("The Phrygians were an ancient Indo-European people, probably\
 related to the Greeks or Thracians. They arrived in Anatolia around the\
 twelfth century BCE, at the time of the invasion of the Sea Peoples in the\
 Eastern Mediterranean region. The arrival of the Phrygians has been\
 associated by some historians with the fall of the Hittite State. After the\
 Macedonian conquest of the Achaemenid Empire and after the arrival of the\
 Galatians to Anatolia, the Phrygians succumbed to Hellenization.")
leaders = {
 "name",                "sex"
 "Barsine",             "Female"
 "Niobe",               "Female"
 "Midas I",             "Male"
 "Dymas",               "Male"
 "Mygdon",              "Male"
 "Gordias",             "Male"
 "Midas V",             "Male"
 "Artabazos",           "Male"
}
flag="phrygian"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Turkish", "Ottoman", "Seljuk", "Byzantine",
               "Latin" ; Galatian
civilwar_nations = "Thracian", "Greek" ; Galatian, Carian, Lycian, Lydian

cities =
 "Gordion",
 "Abydos",
 "Ankyra",
 "Pepuza",
 "Tymion",
 "Tripolis",
 "Kerkenes",
 "Darieion",
 "Synnada",
 "Kelainai",
 "Abbassos",
 "Apameia",
 "Laodikeia me tis Lykos",
 "Laodikeia Kombusta",
 "Mossyna",
 "Cotyseion",
 "Kolossai",
 "Dorylaion",
 "Kibyra",
 "Philomedion",
 "Ipsos",
 "Pessinos"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
