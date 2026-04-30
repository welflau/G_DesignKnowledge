# Freeciv(nation) · kuna

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/kuna.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的kuna定义

## 正文
```ruleset
[nation_kuna]

name=_("Kuna")
plural=_("?plural:Kunas")
groups="American"
legend=_("The Kunas are a Chibchan people living on the Isthmus of Darien,\
 where North and South America meet. In 1925 Kuna chief Nele Kantule led\
 a revolt against the Panamanian authorities. Since then Panama has granted\
 significant autonomy to Kuna Yala, the Kuna homeland. Currently Kuna Yala\
 (also known as San Blas) is known worldwide as a tourist center and the\
 Kunas have established something of a reputation for managing to combine\
 tradition and modernity.")
leaders = {
 "name",                "sex"
 "Olokintipipilele",    "male"
 "Nele Kantule",	"male"
 "Waga Ebinkili",       "female"
}
ruler_titles = {
 "government",     "male_title",        "female_title"
 "Fundamentalism", _("Shaman %s"),      _("?female:Shaman %s")
 "Monarchy",       _("Great Chief %s"), _("?female:Great Chief %s")
 "Republic",       _("Governor %s"),    _("?female:Governor %s")
} 

flag="kuna_yala"
flag_alt = "-"
style = "tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "miskito", "mwiska"

cities =
 "Gaigirgordup",
 "Ailigandi",
 "Yandup",
 "Tubuala",
 "Mulatupu",
 "Akua Yala",
 "Nurra",
 "Ukupseni",
 "Sasardi",
 "Mormakedup",
 "Mansucun",
 "Sukunya",
 "Orosdup",
 "Arridup",
 "Narasgandup Dummad",
 "Magebgandi",
 "Yansipdiwar",
 "Urgandi",
 "Carti Yandup",
 "Nabagandi",
 "Carti Mamidup",
 "Nabagandi",
 "Ailidup",
 "Carti Mulatupu",
 "Digir",
 "Dubpak",
 "Ukupa",
 "Narasgandup Bipi",
 "Tikantiki",
 "Dad Nakue Dupbir",
 "Mamitupu",
 "Uargandup",
 "Carti Sugdupu",
 "Mamardup",
 "Irgandi",
 "Wichupwala",
 "Uargandup",
 "Dupir",
 "Carti Tupile",
 "Ustupu",
 "Goedupu",
 "Gorbiski",
 "Achutupu",
 "Anachukuna",
 "Armila",
 "Akwanusadup",
 "Sasardi",
 "Mirya Ubgigandup",
 "Aidirgandi",
 "Ogobsucun",
 "Mandi Ubgigandup",
 "Ukupseni",
 "Akwadup",
 "Nusadup",
 "Nalunega"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
