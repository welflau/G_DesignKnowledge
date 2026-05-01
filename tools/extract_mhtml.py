"""从 mhtml 文件中提取纯文本内容"""
import sys
import re
import email
import quopri
import base64


def extract_text_from_mhtml(mhtml_path: str, max_chars: int = 8000) -> str:
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

        # 获取原始 payload bytes
        payload = part.get_payload(decode=False)
        if payload is None:
            continue
        if isinstance(payload, str):
            payload_bytes = payload.encode('latin-1')
        else:
            payload_bytes = bytes(payload)

        # 解码传输编码
        try:
            if enc == 'quoted-printable':
                decoded = quopri.decodestring(payload_bytes)
            elif enc == 'base64':
                decoded = base64.b64decode(payload_bytes)
            else:
                decoded = payload_bytes
        except Exception:
            decoded = payload_bytes

        # 解码字符集
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
    text = text.strip()

    return text[:max_chars]


if __name__ == '__main__':
    path = sys.argv[1]
    print(extract_text_from_mhtml(path))
