import os
import re
from datetime import datetime

def generate_rss():
    html_file = 'index.html'
    rss_file = 'feed.xml'
    base_url = "https://ophiroren.github.io/"
    
    if not os.path.exists(html_file):
        return

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # חילוץ הנתונים מהטבלה בעזרת Regex
    pattern = r'<a href="(.*?)".*?class="t-link">.*?<span class="t-tag.*?">(.*?)</span>.*?<span class="t-title">(.*?)</span>.*?<span class="t-meta">(.*?)</span>'
    items = re.findall(pattern, content, re.DOTALL)

    rss_items = ""
    for link, tag, title, meta in items:
        rss_items += f"""
        <item>
            <title>[{tag.strip()}] {title.strip()}</title>
            <link>{link}</link>
            <description>{meta.strip()}</description>
            <pubDate>{datetime.now().strftime("%a, %d %b %Y 00:00:00 +0000")}</pubDate>
            <guid>{link}</guid>
        </item>"""

    rss_template = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
    <title>Ophir Oren - Cyber &amp; AI Security Updates</title>
    <link>{base_url}</link>
    <description>Latest milestones and professional impact from Ophir Oren's portfolio</description>
    <language>en-us</language>
    <image>
        <url>{base_url}logo.png</url>
        <title>Ophir Oren</title>
        <link>{base_url}</link>
    </image>
    <atom:link href="{base_url}feed.xml" rel="self" type="application/rss+xml" />
    {rss_items}
</channel>
</rss>"""

    with open(rss_file, 'w', encoding='utf-8') as f:
        f.write(rss_template)

if __name__ == "__main__":
    generate_rss()