import math, random
random.seed(7)
P,B,C,T = "#6a11cb","#2575fc","#00c6ff","#38BDAE"
def esc(s): return s.replace("&","&amp;")

def wave(base, amp, period, x0=-500, x1=1600):
    pts=[f"{x},{base+amp*math.sin(2*math.pi*x/period):.1f}" for x in range(x0,x1,10)]
    return "M"+" L".join(pts)+f" L{x1},400 L{x0},400 Z"

# ---------------- HEADER ----------------
lines=["AWS Certified Cloud & DevOps Engineer","AI / ML Engineer | Prompt Engineer",
"Data Analyst: Python, SQL, Power BI","Computer Vision with OpenCV",
"Docker | Kubernetes | Terraform | CI/CD","LLMs, RAG, LangChain & AI Tools","MLOps: where AI meets DevOps"]
N=len(lines); slot=3.6; Tt=N*slot; cw=13.2
parts=[]
for i,l in enumerate(lines):
    W=len(l)*cw; x0=500-W/2; y=232
    kt="0;0.06;0.12;"+f"{1/N:.4f};1"
    vals=f"0;{W:.1f};{W:.1f};0;0"
    xs=f"{x0:.1f};{x0+W:.1f};{x0+W:.1f};{x0:.1f};{x0:.1f}"
    parts.append(f'''<clipPath id="c{i}"><rect x="{x0-2:.1f}" y="205" height="40" width="0">
<animate attributeName="width" values="{vals}" keyTimes="{kt}" dur="{Tt}s" begin="{i*slot}s" repeatCount="indefinite"/></rect></clipPath>
<text x="{x0:.1f}" y="{y}" textLength="{W:.1f}" lengthAdjust="spacingAndGlyphs" clip-path="url(#c{i})" class="mono" font-size="22" fill="#fff">{esc(l)}</text>
<rect y="209" width="2.5" height="28" fill="#fff" opacity="0" x="{x0:.1f}">
<animate attributeName="x" values="{xs}" keyTimes="{kt}" dur="{Tt}s" begin="{i*slot}s" repeatCount="indefinite"/>
<animate attributeName="opacity" values="1;1;1;0;0" keyTimes="{kt}" dur="{Tt}s" begin="{i*slot}s" repeatCount="indefinite"/></rect>''')
parts="\n".join(parts)
stars="".join(f'<circle cx="{random.randint(20,980)}" cy="{random.randint(15,190)}" r="{random.choice([1,1.5,2,2.5])}" fill="#fff" opacity="0.2"><animate attributeName="opacity" values="0.1;0.9;0.1" dur="{random.uniform(2,5):.1f}s" begin="{random.uniform(0,3):.1f}s" repeatCount="indefinite"/><animate attributeName="cy" values="{(c:=random.randint(15,190))};{c-12};{c}" dur="{random.uniform(5,9):.1f}s" repeatCount="indefinite"/></circle>' for _ in range(26))
header=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="300" viewBox="0 0 1000 300" role="img" aria-label="Judson K - Cloud, DevOps, AI/ML Engineer">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{P}"/><stop offset="0.5" stop-color="{B}"/><stop offset="1" stop-color="{C}"/>
<animateTransform attributeName="gradientTransform" type="rotate" values="0 .5 .5;12 .5 .5;0 .5 .5" dur="10s" repeatCount="indefinite"/></linearGradient>
<linearGradient id="nm" x1="0" x2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#cfe3ff"/></linearGradient>
<filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<clipPath id="rr"><rect width="1000" height="300" rx="20"/></clipPath>
<style>.mono{{font-family:'Courier New',Consolas,monospace;font-weight:700}}.sans{{font-family:'Segoe UI',Verdana,Arial,sans-serif}}</style>
</defs>
<g clip-path="url(#rr)">
<rect width="1000" height="300" fill="url(#bg)"/>
{stars}
<path d="{wave(255,12,500)}" fill="#fff" opacity="0.07"><animateTransform attributeName="transform" type="translate" from="0 0" to="-500 0" dur="12s" repeatCount="indefinite"/></path>
<path d="{wave(268,10,250)}" fill="#fff" opacity="0.10"><animateTransform attributeName="transform" type="translate" from="-500 0" to="0 0" dur="9s" repeatCount="indefinite"/></path>
<path d="{wave(282,8,500)}" fill="#0d1117" opacity="0.35"><animateTransform attributeName="transform" type="translate" from="0 0" to="-500 0" dur="7s" repeatCount="indefinite"/></path>
<g class="sans" text-anchor="middle">
<text x="500" y="108" font-size="68" font-weight="800" fill="url(#nm)" filter="url(#glow)">Judson K
<animate attributeName="opacity" values="0;1" dur="1.2s"/>
<animateTransform attributeName="transform" type="translate" values="0 18;0 0" dur="1.2s"/></text>
<text x="500" y="154" font-size="20" fill="#e6efff">Cloud &amp; DevOps Engineer  •  AI / ML Engineer  •  Data Analyst
<animate attributeName="opacity" values="0;0;1" keyTimes="0;0.33;1" dur="1.8s"/></text>
</g>
<line x1="380" y1="176" x2="620" y2="176" stroke="#fff" stroke-opacity="0.5" stroke-width="2" stroke-linecap="round" stroke-dasharray="240"><animate attributeName="stroke-dashoffset" values="240;240;0" keyTimes="0;0.35;1" dur="2.2s"/></line>
{parts}
</g></svg>'''
open("assets/header.svg","w").write(header)

# ---------------- FOOTER ----------------
footer=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="170" viewBox="0 0 1000 170" role="img" aria-label="Open to opportunities">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{P}"/><stop offset="0.5" stop-color="{B}"/><stop offset="1" stop-color="{C}"/></linearGradient>
<clipPath id="r"><rect width="1000" height="170" rx="20"/></clipPath>
<style>.s{{font-family:'Segoe UI',Verdana,Arial,sans-serif}}</style></defs>
<g clip-path="url(#r)"><rect width="1000" height="170" fill="url(#g)"/>
<path d="{wave(120,10,500)}" fill="#fff" opacity="0.10"><animateTransform attributeName="transform" type="translate" from="0 0" to="-500 0" dur="10s" repeatCount="indefinite"/></path>
<path d="{wave(138,8,250)}" fill="#0d1117" opacity="0.30"><animateTransform attributeName="transform" type="translate" from="-500 0" to="0 0" dur="7s" repeatCount="indefinite"/></path>
<g class="s" text-anchor="middle" fill="#fff"><text x="500" y="62" font-size="26" font-weight="700">Open to Cloud, DevOps, AI &amp; Data opportunities</text>
<text x="500" y="94" font-size="17" fill="#e6efff">Let's build something intelligent together<animate attributeName="opacity" values="0.6;1;0.6" dur="3s" repeatCount="indefinite"/></text></g></g></svg>'''
open("assets/footer.svg","w").write(footer)

# ---------------- JOURNEY ----------------
nodes=[("AWS re/Start",P),("Cloud Practitioner",P),("DevOps Engineer",B),("Data Analytics",B),("AI / ML",C),("Computer Vision",C),("MLOps",T)]
w,g=128,10; tot=len(nodes)*w+(len(nodes)-1)*g; ox=(1000-tot)/2; y=50
out=[]
for i,(n,c) in enumerate(nodes):
    x=ox+i*(w+g)
    if i: out.append(f'<line x1="{x-g}" y1="{y+22}" x2="{x}" y2="{y+22}" stroke="#8b949e" stroke-width="2" stroke-dasharray="4 3"/>')
    tc="#000" if c==C or c==T else "#fff"
    out.append(f'''<g><rect x="{x}" y="{y}" width="{w}" height="44" rx="12" fill="{c}"><animate attributeName="opacity" values="0.75;1;0.75" dur="3s" begin="{i*0.4}s" repeatCount="indefinite"/></rect>
<text x="{x+w/2}" y="{y+27}" text-anchor="middle" font-size="12" font-weight="700" fill="{tc}" class="s">{esc(n)}</text></g>''')
dotx=f"{ox+w/2};{ox+tot-w/2}"
out.append(f'<circle r="5" cy="{y+22+44+14}" fill="{C}"><animate attributeName="cx" values="{dotx}" dur="7s" repeatCount="indefinite"/></circle>')
out.append(f'<line x1="{ox+w/2}" y1="{y+80}" x2="{ox+tot-w/2}" y2="{y+80}" stroke="#8b949e" stroke-opacity="0.4" stroke-width="2"/>')
journey=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="150" viewBox="0 0 1000 150" role="img" aria-label="Career journey">
<style>.s{{font-family:'Segoe UI',Verdana,Arial,sans-serif}}</style>{"".join(out)}</svg>'''
open("assets/journey.svg","w").write(journey)

# ---------------- MARQUEE ----------------
r1=[("Python","#3776AB"),("Pandas","#150458"),("NumPy","#013243"),("Scikit-learn","#F7931E"),("TensorFlow","#FF6F00"),("PyTorch","#EE4C2C"),("OpenCV","#5C3EE8"),("Keras","#D00000"),("Hugging Face","#B8860B"),("LangChain","#1C3C3C"),("Prompt Engineering","#D97757"),("Power BI","#B8960B"),("SQL","#4479A1"),("Tableau","#E97627"),("Streamlit","#FF4B4B")]
r2=[("AWS","#FF9900"),("EKS","#E07B00"),("Terraform","#7B42BC"),("Kubernetes","#326CE5"),("Docker","#2496ED"),("Helm","#0F1689"),("Ansible","#EE0000"),("GitHub Actions","#2088FF"),("Jenkins","#D24939"),("Prometheus","#E6522C"),("Grafana","#F46800"),("Linux","#8a6d00"),("Bash","#4EAA25"),("Git","#F05032"),("MLflow","#0194E2")]
def row(items,y,rev,dur):
    cw2=8.2;chips=[];x=0
    for n,c in items:
        wd=len(n)*cw2+30; chips.append((n,c,x,wd)); x+=wd+14
    RW=x
    def g(off): return "".join(f'<g transform="translate({off+cx:.1f},0)"><rect width="{wd:.1f}" height="32" rx="16" fill="{c}"/><text x="{wd/2:.1f}" y="21" text-anchor="middle" class="m" font-size="13" fill="#fff">{esc(n)}</text></g>' for n,c,cx,wd in chips)
    f,t=("-%.1f 0"%RW,"0 0") if rev else ("0 0","-%.1f 0"%RW)
    return f'<g transform="translate(0,{y})"><g><animateTransform attributeName="transform" type="translate" from="{f}" to="{t}" dur="{dur}s" repeatCount="indefinite"/>{g(0)}{g(RW)}</g></g>'
marq=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="96" viewBox="0 0 1000 96" role="img" aria-label="Skills marquee">
<defs><linearGradient id="fd"><stop offset="0" stop-color="#000"/><stop offset="0.08" stop-color="#fff"/><stop offset="0.92" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>
<mask id="mk"><rect width="1000" height="96" fill="url(#fd)"/></mask><style>.m{{font-family:'Courier New',Consolas,monospace;font-weight:700}}</style></defs>
<g mask="url(#mk)">{row(r1,8,False,45)}{row(r2,52,True,50)}</g></svg>'''
open("assets/skills-marquee.svg","w").write(marq)

# ---------------- SKILL BARS ----------------
sk=[("AWS & Cloud",80,P),("DevOps & IaC",85,B),("Python",80,"#3776AB"),("Data Analysis",75,T),("AI / ML",70,C),("OpenCV",70,"#5C3EE8"),("Prompt Engineering",85,"#D97757")]
rows=[]
for i,(n,v,c) in enumerate(sk):
    y=20+i*38
    rows.append(f'''<text x="10" y="{y+17}" class="s" font-size="15" font-weight="600" fill="#8b949e">{esc(n)}</text>
<rect x="210" y="{y}" width="400" height="22" rx="11" fill="#8b949e" fill-opacity="0.2"/>
<rect x="210" y="{y}" width="{4*v}" height="22" rx="11" fill="{c}"><animate attributeName="width" values="0;0;{4*v}" keyTimes="0;{(i*0.2)/(1.6+i*0.2):.3f};1" dur="{1.6+i*0.2:.1f}s"/></rect>
<text x="{620}" y="{y+17}" class="s" font-size="14" font-weight="700" fill="{c}">{v}%</text>''')
bars=f'''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="{20+len(sk)*38}" viewBox="0 0 700 {20+len(sk)*38}" role="img" aria-label="Skill proficiency"><style>.s{{font-family:'Segoe UI',Verdana,Arial,sans-serif}}</style>{"".join(rows)}</svg>'''
open("assets/skill-bars.svg","w").write(bars)

# ---------------- DIVIDER ----------------
div=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="14" viewBox="0 0 1000 14"><defs><linearGradient id="d"><stop offset="0" stop-color="{P}" stop-opacity="0"/><stop offset="0.3" stop-color="{P}"/><stop offset="0.5" stop-color="{B}"/><stop offset="0.7" stop-color="{C}"/><stop offset="1" stop-color="{C}" stop-opacity="0"/></linearGradient></defs>
<rect x="0" y="6" width="1000" height="2" rx="1" fill="url(#d)"/><circle cy="7" r="5" fill="#fff"><animate attributeName="cx" values="0;1000" dur="4s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.1;0.9;1" dur="4s" repeatCount="indefinite"/></circle></svg>'''
open("assets/divider.svg","w").write(div)
print("ok")
