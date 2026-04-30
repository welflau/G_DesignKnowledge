# Freeciv(default) · nation_intelligence_effects

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/default/nation_intelligence_effects.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, default

## 概述
Freeciv default规则集的nation_intelligence_effects定义

## 正文
```ruleset
; /* <-- avoid gettext warnings
; This file contains the Nation_Intelligence effects used in most rulesets.
; Include it in effects.ruleset with:
;
; *include "default/nation_intelligence_effects.ruleset"
;
; You'll also want to add the +Nation_Intelligence option to effects.ruleset.
; */ <-- avoid gettext warnings

[effect_ni_multipliers_embassy]
type  = "Nation_Intelligence"
value = 1
reqs  =
    { "type",                 "name",         "range",  "present"
      "NationalIntelligence", "Multipliers",  "Player", TRUE
      "DiplRel",              "Has embassy",  "Local",  TRUE
    }

[effect_ni_wonders]
type  = "Nation_Intelligence"
value = 1
reqs  =
    { "type",                 "name",     "range",  "present"
      "NationalIntelligence", "Wonders",  "Player", TRUE
    }

[effect_ni_score_contact]
type  = "Nation_Intelligence"
value = 1
reqs  =
    { "type",                 "name",         "range",  "present"
      "NationalIntelligence", "Score",        "Player", TRUE
      "DiplRel",              "Has Contact",  "Local",  TRUE
    }

[effect_ni_score_embassy]
type  = "Nation_Intelligence"
value = 1
reqs  =
    { "type",                 "name",         "range",  "present"
      "NationalIntelligence", "Score",        "Player", TRUE
      "DiplRel",              "Has embassy",  "Local",  TRUE
    }

[effect_ni_gold_contact]
type  = "Nation_Intelligence"
value = 1
reqs  =
    { "type",                 "name",         "range",  "present"
      "NationalIntelligence", "Gold",         "Player", TRUE
      "DiplRel",              "Has Contact",  "Local",  TRUE
    }

[effect_ni_gold_embassy]
type  = "Nation_Intelligence"
value = 1
reqs  =
    { "type",                 "name",         "range",  "present"
      "NationalIntelligence", "Gold",         "Player", TRUE
      "DiplRel",              "Has embassy",  "Local",  TRUE
    }

[effect_ni_gov_contact]
type  = "Nation_Intelligence"
value = 1
reqs  =
    { "type",                 "name",         "range",  "present"
      "NationalIntelligence", "Government",   "Player", TRUE
      "DiplRel",              "Has Contact",  "Local",  TRUE
    }

[effect_ni_gov_embassy]
type  = "Nation_Intelligence"
value = 1
reqs  =
    { "type",                 "name",         "range",  "present"
      "NationalIntelligence", "Government",   "Player", TRUE
      "DiplRel",              "Has embassy",  "Local",  TRUE
    }

[effect_ni_diplomacy_contact]
type  = "Nation_Intelligence"
value = 1
reqs  =
    { "type",                 "name",         "range",  "present"
      "NationalIntelligence", "Diplomacy",    "Player", TRUE
      "DiplRel",              "Has Contact",  "Local",  TRUE
    }

[effect_ni_diplomacy_embassy]
type  = "Nation_Intelligence"
value = 1
reqs  =
    { "type",                 "name",         "range",  "present"
      "NationalIntelligence", "Diplomacy",    "Player", TRUE
      "DiplRel",              "Has embassy",  "Local",  TRUE
    }

[effect_ni_techs_embassy]
type  = "Nation_Intelligence"
value = 1
reqs  =
    { "type",                 "name",         "range",  "present"
      "NationalIntelligence", "Techs",        "Player", TRUE
      "DiplRel",              "Has embassy",  "Local",  TRUE
    }

[effect_ni_tax_embassy]
type  = "Nation_Intelligence"
value = 1
reqs  =
    { "type",                 "name",         "range",  "present"
      "NationalIntelligence", "Tax Rates",    "Player", TRUE
      "DiplRel",              "Has embassy",  "Local",  TRUE
    }

[effect_ni_culture_embassy]
type  = "Nation_Intelligence"
value = 1
reqs  =
    { "type",                 "name",         "range",  "present"
      "NationalIntelligence", "Culture",      "Player", TRUE
      "DiplRel",              "Has embassy",  "Local",  TRUE
    }

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
