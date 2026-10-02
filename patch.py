with open('login.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '<button type="button"\n                        class="glass-input py-2 rounded-lg hover:bg-slate-50 transition-colors flex justify-center items-center opacity-50 cursor-not-allowed"\n                        title="Apple Login (Requires Paid Apple Developer Account)">'

replacement = '<button id="apple-login" type="button"\n                        class="glass-input py-2 rounded-lg hover:bg-slate-50 transition-colors flex justify-center items-center opacity-50 cursor-not-allowed"\n                        title="Apple Login (Requires Paid Apple Developer Account)">'

content = content.replace(target, replacement)

target2 = target.replace('\n', '\r\n')
replacement2 = replacement.replace('\n', '\r\n')
content = content.replace(target2, replacement2)

with open('login.html', 'w', encoding='utf-8') as f:
    f.write(content)
