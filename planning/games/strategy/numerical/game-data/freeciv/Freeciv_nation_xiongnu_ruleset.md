# Freeciv(nation) · xiongnu

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/xiongnu.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的xiongnu定义

## 正文
```ruleset
[nation_xiongnu]

name=_("Xiongnu")
plural=_("?plural:Xiongnu")
groups="Ancient", "Asian"
legend=_("The Xiongnu, also known as Asiatic Huns, were an ancient tribal\
 confederation of mixed origin. Their language is unknown; it may have\
 belonged to the Altaic or Yeniseian language family. The Xiongnu created\
 a strong state in the plains of the eastern part of Central Asia, which\
 was an important threat to China. From the second century onwards the\
 northern wing of the Xiongnu was known as Xianbei, while another group of\
 the Xiongnu emigrated to the west.")
leaders = {
 "name",                  "sex"
 "Touman",                "Male"
 "Modu",                  "Male"
 "Laoshang",              "Male"
 "Junchen",               "Male"
 "Yizhixie",              "Male"
 "Wuwei",                 "Male"
 "Zhanshilu",             "Male"
 "Goulihu",               "Male"
 "Judihou",               "Male"
 "Hulugu",                "Male"
 "Xulüquanqu",            "Male"
 "Woyenqudi",             "Male"
 "Huduershidaogao Ruodi", "Male"
 "Yuchujian",             "Male"
 "Zhizhi",                "Male"
 "Huahanye",              "Male"
 "Cheniu",                "Male"
 }
flag="xiongnu"
flag_alt = "-"
style = "Asian"

ruler_titles = {
 "government",      "male_title",    "female_title"
 "Despotism",       _("%s Khan"),    _("%s Khatan")
 "Monarchy",        _("%s Khagan"),  _("?female:%s Khagan")
}

init_techs=""
init_buildings=""
init_units=""

conflicts_with= "Russian", "Soviet", "Manchu", "Kazakh", "Gokturk",
                "Uyghur", "Buryat", "Chinese", "Tuvan"
civilwar_nations = "Gokturk", "Saka", "Mongol", "Han", "Tocharian"

cities =
 "Tongwancheng",
 "Luut Hot",
 "Longcheng",
 "Shule",
 "Qiuci",
 "Yutian",
 "Jingbian",
 "Gaocheng",
 "Gansu",
 "Mayi",
 "Pingcheng",
 "Taraz",
 "Chaoyang",
 "Jiaohe",
 "Hohhot",
 "Liqjan",
 "Yiwu",
 "Boroogiin Suurin",
 "Shanggui",
 "Noin Ula",
 "Lishi",
 "Liting",
 "Puzi",
 "Chang'an",
 "Jiankang",
 "Zhangye",
 "Guzang",
 "Jiquan",
 "Dunhuang",
 "Shanshan",
 "Zhizhi",
 "Yiwulu",
 "Mayi",
 "Mobei",
 "Loulan",
 "Baideng",
 "Ikh Bayan",
 "Jushi"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
