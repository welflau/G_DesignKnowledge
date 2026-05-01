"""批量提取 KM 文章内容到文本文件"""
import sys
import re
import email
import quopri
import base64
from pathlib import Path

KM_BASE = "K:/iDisk/wilfredliu的同步盘/A_Works/Docs/KM"
OUT_DIR  = "F:/A_Works/G_DesignKnowledge/tools/extracted"

FILES = {
    # FPS
    "fps_gunplay":    "游戏设计/酣畅淋漓的Gunplay—做好FPS的射击手感 - KM平台.mhtml",
    "fps_3c":         "游戏设计/从TD角度谈谈射击与动作游戏的3C（上） - 腾讯游戏知识库 - KM平台.mhtml",
    "fps_cover":      "游戏设计/为什么你总想贴墙打？掩体系统浅析 - 腾讯游戏知识库 - KM平台.mhtml",
    "fps_diff":       "游戏/浅谈射击游戏的设计差异 - 腾讯游戏知识库 - KM平台.mhtml",
    "fps_apex":       "游戏/APEXM分析 - 腾讯游戏知识库 - KM平台.mhtml",
    # MOBA
    "moba_lol":       "游戏设计/英雄联盟英雄分类框架浅析 - KM平台.mhtml",
    # Roguelike
    "rl_balatro":     "游戏/【玩法研究】《小丑牌》测评：以低门槛和差异化切入肉鸽DBG赛道 - 腾讯游戏知识库 - KM平台.mhtml",
    # Casual/放置
    "casual_jiangnan":"游戏/【玩法研究】《江南百景图》测评：放置休闲难顶资源压力 - 腾讯游戏知识库 - KM平台.mhtml",
    # RPG / 动作
    "rpg_action":     "游戏设计/动作游戏的本质，与相关设计方法论 - KM平台.mhtml",
    "rpg_souls":      "游戏/从帧数出发——魂系列的战斗设计拆解 - 腾讯游戏知识库 - KM平台.mhtml",
    "rpg_sf6":        "游戏/聊聊《街霸6》的动作博弈 - 腾讯游戏知识库 - KM平台.mhtml",
    "rpg_zzz":        "游戏/浅析《绝区零》的沉浸感体验设计 - 腾讯游戏知识库 - KM平台.mhtml",
    "rpg_dmc5":       "游戏/鬼泣5拆解 - 腾讯游戏知识库 - KM平台.mhtml",
    "rpg_mhw":        "游戏/【玩法研究】《怪物猎人荒野》游戏测评：继往开来，老树新花 - 腾讯游戏知识库 - KM平台.mhtml",
    "rpg_metaphor":   "游戏/【玩法研究】《暗喻幻想》游戏测评：用P系列的方式参与一场王道旅行 - 腾讯游戏知识库 - KM平台.mhtml",
    "rpg_star_rail":  "GDC/2025/《崩坏：星穹铁道》：如何让RPG游戏走向大众【GDC精选】 - 腾讯游戏知识库 - KM平台.mhtml",
    # 开放世界/关卡
    "ow_poi":         "游戏设计/点线面基础与游戏中的POI规划 - KM平台.mhtml",
    "ow_zelda":       "游戏/《塞尔达传说：王国之泪》代表的SOC新方向深度研究.mhtml",
    "ow_genshin_map": "GDC/【GDC2024】米哈游演讲：《原神》开放世界地图设计的四个技巧 - 腾讯游戏知识库 - KM平台.mhtml",
    # 策略/模拟
    "strategy_albion":"游戏/很长但很爽！全网独一份的《阿尔比恩》沙盒式自由经济的设计拆解与解读.mhtml",
    "strategy_soc":   "游戏/【市场全景观察】SOC品类的诞生、发展与未来趋势 - 腾讯游戏知识库 - KM平台.mhtml",
    "strategy_rimw":  "游戏/【玩法研究】《Rimworld》测评：求生不易，最紧要开心 - 腾讯游戏知识库 - KM平台.mhtml",
    # 叙事/通用
    "narrative_myth": "游戏设计/八卦？九歌？塔罗？基于神话学的世界观构建 - 腾讯游戏知识库 - KM平台.mhtml",
    "narrative_xian": "游戏设计/【我欲成仙快乐齐天】修仙题材的创作参考指南 - KM平台.mhtml",
    "narrative_frost": "GDC/《冰汽时代2》主策教你用玩法来叙事，涌现式游戏的系统语言【GDC精选】 - 腾讯游戏知识库 - KM平台.mhtml",
    "narrative_story": "GDC/2025/创作可玩游戏故事：整合游戏机制和叙事的方法【GDC精选】 - 腾讯游戏知识库 - KM平台.mhtml",
    # 新手引导/F2P
    "ftue_f2p":       "GDC/【GDC2024腾讯游戏光子嘉宾演讲】正确的开始，有趣的开始_ F2P玩家上手路径体验研究 - KM平台.mhtml",
    # 社交
    "social_sky":     "游戏/下载量2.6亿、超70%为女性，陈星汉GDC分享《光·遇》友善社交的设计思考 - 腾讯游戏知识库 - KM平台.mhtml",
    # 运营/产品
    "ops_palworld":   "游戏/帕鲁过山车：起死回生丨GDC2025演讲烤制 - 腾讯游戏知识库 - KM平台.mhtml",
    # 小游戏
    "miniapp_game":   "游戏设计/微信小程序游戏 爆款设计分析 - KM平台.mhtml",
    # GDC策划向
    "gdc_ryugajoku":  "GDC/2025/《人中之龙》：叙事驱动与短周期开发的秘诀【GDC精选】 - 腾讯游戏知识库 - KM平台.mhtml",
    "gdc_tango":      "GDC/2025/《双影奇境》中所有游戏玩法的编写【GDC精选】 - 腾讯游戏知识库 - KM平台.mhtml",
    "gdc_icecoal":    "GDC/《冰汽时代2》主策教你用玩法来叙事，涌现式游戏的系统语言【GDC精选】 - 腾讯游戏知识库 - KM平台.mhtml",
}


def extract(mhtml_path: str, max_chars: int = 15000) -> str:
    try:
        with open(mhtml_path, 'rb') as f:
            raw = f.read()
        msg = email.message_from_bytes(raw)
        html_content = ""
        for part in msg.walk():
            ct = part.get_content_type()
            if ct not in ('text/html', 'text/plain'):
                continue
            enc = part.get('Content-Transfer-Encoding', '').strip().lower()
            charset = part.get_content_charset() or 'utf-8'
            payload = part.get_payload(decode=False)
            if payload is None:
                continue
            if isinstance(payload, str):
                payload_bytes = payload.encode('latin-1')
            else:
                payload_bytes = bytes(payload)
            try:
                if enc == 'quoted-printable':
                    decoded = quopri.decodestring(payload_bytes)
                elif enc == 'base64':
                    decoded = base64.b64decode(payload_bytes)
                else:
                    decoded = payload_bytes
            except Exception:
                decoded = payload_bytes
            for try_enc in [charset, 'utf-8', 'gbk', 'gb18030']:
                try:
                    text = decoded.decode(try_enc, errors='strict')
                    break
                except Exception:
                    continue
            else:
                text = decoded.decode('utf-8', errors='replace')
            if ct == 'text/html' and not html_content:
                html_content = text
            elif ct == 'text/plain' and not html_content:
                html_content = text
        if not html_content:
            return ""
        html = html_content
        html = re.sub(r'<script[^>]*>[\s\S]*?</script>', ' ', html, flags=re.I)
        html = re.sub(r'<style[^>]*>[\s\S]*?</style>', ' ', html, flags=re.I)
        html = re.sub(r'<(p|div|br|h[1-6]|li|tr)[^>]*>', '\n', html, flags=re.I)
        text = re.sub(r'<[^>]+>', '', html)
        text = text.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>') \
                   .replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', "'")
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r'[ \t]{2,}', ' ', text)
        # 过滤掉短行（UI噪声）
        lines = [l.strip() for l in text.split('\n') if len(l.strip()) > 15]
        return '\n'.join(lines)[:max_chars]
    except Exception as e:
        return f"ERROR: {e}"


Path(OUT_DIR).mkdir(parents=True, exist_ok=True)
ok, fail = 0, 0
for key, rel_path in FILES.items():
    full_path = f"{KM_BASE}/{rel_path}"
    out_path = f"{OUT_DIR}/{key}.txt"
    text = extract(full_path)
    if text and not text.startswith("ERROR"):
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"[OK] {key} ({len(text)} chars)")
        ok += 1
    else:
        print(f"[FAIL] {key}: {text[:80]}")
        fail += 1

print(f"\n完成: {ok} 成功, {fail} 失败")
