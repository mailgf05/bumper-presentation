#!/usr/bin/env python3
"""Build bumper-presentation.html — 11-slide Pop Art slideshow."""

import base64, os

DIR = os.path.dirname(os.path.abspath(__file__))

def b64(path):
    full = os.path.join(DIR, path)
    ext = path.rsplit('.', 1)[-1].lower()
    mime = {'png': 'image/png', 'jpg': 'image/jpeg', 'jpeg': 'image/jpeg'}
    with open(full, 'rb') as f:
        return f"data:{mime.get(ext, 'image/png')};base64,{base64.b64encode(f.read()).decode()}"

IMG1 = b64("img/magasin_interieur.jpg")
IMG2 = b64("img/mannequin_smartphones.jpg")
IMG3 = b64("img/magasin_rayons.jpg")
IMG4 = b64("img/mur_coques.jpg")
IMG5 = b64("img/plan_espace_new.jpg")
IMG6 = b64("img/magazines_bumper.jpg")
IMG7 = b64("img/bumper_lab_photo.jpg")
IMG8 = b64("img/post_insta.jpg")

HTML = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>BUMPER — Bachelor RAC 2025/2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cherry+Bomb+One&family=Poppins:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --navy:#232F3E;--teal:#00C9AF;--blue:#39B0FF;--yellow:#FAC900;
  --purple:#9400C9;--black:#000;--white:#FFF;--gray:#F4F6F8;
  --red:#E53935;
}}
html,body{{width:100%;height:100%;overflow:hidden;font-family:'Poppins',sans-serif;background:var(--navy);min-width:1024px}}

/* SLIDESHOW */
.ss{{position:relative;width:100%;height:100vh}}
.slide{{position:absolute;inset:0;width:100%;height:100vh;display:none;overflow:hidden;flex-direction:column;justify-content:center;align-items:center;padding:40px 60px}}
.slide.active{{display:flex}}

/* TYPOGRAPHY */
.stitle{{font-family:'Cherry Bomb One',cursive;font-size:2.6rem;margin-bottom:24px;text-align:center;line-height:1.2;text-shadow:2px 2px 0 #000,-1px -1px 0 #000,1px -1px 0 #000,-1px 1px 0 #000}}
body,p,li,span,td,th{{font-family:'Poppins',sans-serif}}
.kpi{{font-family:'Cherry Bomb One',cursive;font-size:2.6rem;text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
.kpi-sm{{font-family:'Cherry Bomb One',cursive;font-size:1.4rem;text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}

/* NAVIGATION */
.nbtn{{position:fixed;z-index:900;width:46px;height:46px;background:var(--navy);color:var(--teal);border:2px solid var(--teal);font-size:1.5rem;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:.15s}}
.nbtn:hover{{background:var(--teal);color:var(--black)}}
.nprev{{bottom:30px;right:72px}}
.nnext{{bottom:30px;right:20px}}
.dots{{position:fixed;bottom:18px;left:50%;transform:translateX(-50%);display:flex;gap:10px;z-index:900}}
.dot{{width:12px;height:12px;background:var(--gray);border:2px solid var(--navy);cursor:pointer;transition:.15s;border-radius:50%}}
.dot.active{{background:var(--teal);border-color:var(--teal)}}
.pbar{{position:fixed;top:0;left:0;height:4px;background:linear-gradient(90deg,var(--teal),var(--blue));z-index:900;transition:width .3s}}
.scount{{position:fixed;top:12px;right:24px;color:var(--white);font-size:.8rem;z-index:900;background:rgba(0,0,0,.4);padding:4px 14px;border:1px solid var(--teal);border-radius:4px}}

/* CARDS */
.c{{background:rgba(255,255,255,0.8);border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.5);padding:20px;position:relative}}
.ct-teal{{border-top:5px solid var(--teal)}}
.ct-blue{{border-top:5px solid var(--blue)}}
.ct-yellow{{border-top:5px solid var(--yellow)}}
.ct-purple{{border-top:5px solid var(--purple)}}
.cl-teal{{border-left:5px solid var(--teal)}}
.cl-yellow{{border-left:5px solid var(--yellow)}}
.cl-blue{{border-left:5px solid var(--blue)}}
.cl-red{{border-left:5px solid var(--red)}}
.cw{{background:rgba(255,255,255,0.8);border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.5);padding:20px}}

/* BADGE */
.badge{{display:inline-block;background:var(--yellow);color:var(--black);font-weight:800;padding:5px 16px;font-size:.85rem;border:2px solid var(--black);border-radius:4px}}
.badge-teal{{background:var(--teal);color:var(--black);border-color:var(--black)}}
.badge-blue{{background:var(--blue);color:var(--black);border-color:var(--black)}}
.badge-purple{{background:var(--purple);color:var(--white);border-color:var(--black)}}

/* GEO SHAPES */
.geo{{position:absolute;z-index:0;pointer-events:none}}

/* IMG FRAME */
.imgframe{{border:3px solid var(--navy);border-radius:4px;overflow:hidden}}
.imgframe-teal{{border-color:var(--teal)}}

/* POP ART BG ON ALL SLIDES */
.pabg{{position:absolute;inset:0;width:100%;height:100%;background-size:cover;background-position:center;z-index:0}}
.slide>*:not(.pabg):not(.geo):not(.foot){{position:relative;z-index:2}}

/* ===== SLIDE 1 COVER ===== */
#s1{{color:var(--white);text-align:center;position:relative;overflow:hidden}}
#s1 .content{{position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;justify-content:center}}
#s1 .logo-txt{{font-family:'Cherry Bomb One',cursive;font-size:5.5rem;color:var(--white);letter-spacing:6px;text-shadow:2px 2px 0 #000,-1px -1px 0 #000,1px -1px 0 #000,-1px 1px 0 #000}}
#s1 .loc{{font-size:1.5rem;color:var(--teal);margin-top:2px}}
#s1 .tagline{{font-size:1.1rem;color:var(--white);margin-top:10px;letter-spacing:1px;text-shadow:2px 2px 0 #000,-1px -1px 0 #000,1px -1px 0 #000,-1px 1px 0 #000}}
#s1 .sep{{width:80px;height:4px;background:var(--teal);margin:18px auto}}
#s1 .sub2{{font-size:1rem;color:var(--white);opacity:.85;text-shadow:2px 2px 0 #000,-1px -1px 0 #000,1px -1px 0 #000,-1px 1px 0 #000}}
#s1 .foot{{position:absolute;bottom:20px;font-size:.8rem;color:rgba(255,255,255,.5);z-index:2}}
#s1 .g1{{top:-40px;left:-40px;width:180px;height:180px;background:var(--teal);border-radius:50%;opacity:.12}}
#s1 .g2{{bottom:-50px;right:-50px;width:200px;height:200px;background:var(--yellow);border-radius:50%;opacity:.10}}
#s1 .g3{{top:20%;right:5%;width:100px;height:100px;background:var(--purple);border-radius:50%;opacity:.10}}
#s1 .g4{{bottom:15%;left:8%;width:120px;height:120px;background:var(--blue);border-radius:50%;opacity:.08}}

/* ===== SLIDE 2 CONTEXTE ===== */
#s2 .stitle{{color:var(--navy);text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s2 .grid{{display:flex;gap:30px;width:100%;max-width:1200px}}
#s2 .left{{flex:1;display:flex;flex-direction:column;gap:14px}}
#s2 .right{{flex:1;display:flex;flex-direction:column;gap:14px}}
#s2 .txt{{font-size:.88rem;line-height:1.6;color:var(--navy)}}
#s2 .srow{{display:flex;gap:12px;flex-wrap:wrap;margin-top:6px}}
#s2 .sc{{flex:1;min-width:120px;text-align:center;padding:20px 14px;background:rgba(255,255,255,0.8);border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.5)}}
#s2 .sc .kpi{{display:block;margin-bottom:4px;text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s2 .sc .slbl{{font-size:.72rem;color:var(--navy);font-weight:600}}

/* ===== SLIDE 3 SWOT ===== */
#s3 .stitle{{color:var(--navy);text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s3 .swot{{display:grid;grid-template-columns:1fr 1fr;gap:16px;width:100%;max-width:1100px}}
#s3 .sw{{background:rgba(255,255,255,0.8);border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.5);padding:22px}}
#s3 .sw h3{{font-family:'Cherry Bomb One',cursive;font-size:1.2rem;margin-bottom:8px;text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s3 .sw ul{{list-style:none;padding:0}}
#s3 .sw li{{font-size:.82rem;padding:3px 0 3px 16px;position:relative;line-height:1.4;color:var(--navy)}}
#s3 .sw li::before{{content:'';position:absolute;left:0;top:10px;width:6px;height:6px;border-radius:50%}}

/* ===== SLIDE 4 PERSONAS ===== */
#s4 .stitle{{color:var(--navy);text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s4 .prow{{display:flex;gap:24px;width:100%;max-width:1200px}}
#s4 .pc{{flex:1;padding:24px;background:rgba(255,255,255,0.8);border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.5)}}
#s4 .pc h3{{font-family:'Cherry Bomb One',cursive;font-size:1.3rem;margin-bottom:4px;text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s4 .pc .meta{{font-size:.75rem;font-weight:600;color:#555;margin-bottom:10px}}
#s4 .pc ul{{list-style:none;padding:0}}
#s4 .pc li{{font-size:.8rem;padding:3px 0 3px 14px;position:relative;line-height:1.4;color:var(--navy)}}
#s4 .pc li::before{{content:'';position:absolute;left:0;top:10px;width:5px;height:5px;border-radius:50%}}
#s4 .pc .lev{{margin-top:10px;padding:8px 12px;font-size:.75rem;font-weight:700;border:2px solid;border-radius:4px}}
#s4 .pc .plat{{display:flex;gap:6px;margin-top:8px;flex-wrap:wrap}}
#s4 .pc .ptag{{font-size:.7rem;padding:3px 10px;border:2px solid var(--black);border-radius:20px;font-weight:600}}

/* ===== SLIDE 5 ESPACE ===== */
#s5 .stitle{{color:var(--navy);text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s5 .imgs{{display:flex;gap:20px;justify-content:center;width:100%;max-width:1200px;margin-bottom:18px}}
#s5 .imgs .imgframe{{flex:1;max-height:35vh;display:flex;align-items:center;justify-content:center;background:var(--gray)}}
#s5 .imgs img{{max-width:100%;max-height:35vh;object-fit:contain}}
#s5 .zones{{display:flex;gap:12px;width:100%;max-width:1200px;justify-content:center}}
#s5 .zone{{flex:1;padding:14px;text-align:center;color:var(--navy);background:rgba(255,255,255,0.8);border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.5)}}
#s5 .zone .zn{{display:inline-block;width:28px;height:28px;line-height:28px;background:var(--teal);color:var(--black);font-family:'Cherry Bomb One',cursive;font-size:.9rem;border-radius:50%;margin-bottom:4px;text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s5 .zone h4{{font-family:'Cherry Bomb One',cursive;font-size:.9rem;margin-bottom:2px;text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s5 .zone p{{font-size:.68rem;color:var(--navy);line-height:1.3}}
#s5 .flux{{font-size:.78rem;color:var(--navy);margin-top:14px;font-weight:600;text-align:center}}

/* ===== SLIDE 6 BUMPER LAB ===== */
#s6{{color:var(--white);text-align:center}}
#s6 .stitle{{font-size:3.2rem;color:var(--white);margin-bottom:4px;text-shadow:2px 2px 0 #000,-1px -1px 0 #000,1px -1px 0 #000,-1px 1px 0 #000}}
#s6 .sub6{{color:var(--teal);font-size:1rem;margin-bottom:16px;text-shadow:2px 2px 0 #000,-1px -1px 0 #000,1px -1px 0 #000,-1px 1px 0 #000}}
#s6 .labimg{{margin:0 auto 18px;display:block;max-width:100%;max-height:40vh;object-fit:contain}}
#s6 .steps{{display:flex;gap:12px;width:100%;max-width:1100px;justify-content:center;margin-bottom:14px}}
#s6 .stp{{flex:1;padding:14px;text-align:center;color:var(--navy);background:rgba(255,255,255,0.8);border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);backdrop-filter:blur(6px);border:3px solid}}
#s6 .stp h4{{font-family:'Cherry Bomb One',cursive;font-size:.95rem;margin-bottom:4px;text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s6 .stp p{{font-size:.72rem;color:var(--navy);line-height:1.3}}
#s6 .kpirow{{display:flex;gap:12px;width:100%;max-width:1100px;justify-content:center;margin-bottom:10px}}
#s6 .kb{{padding:12px 16px;text-align:center;flex:1;color:var(--navy);background:rgba(255,255,255,0.8);border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);backdrop-filter:blur(6px);border:3px solid}}
#s6 .kb .kpi{{display:block;margin-bottom:2px;text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s6 .kb .klbl{{font-size:.7rem;color:var(--navy)}}
#s6 .invest{{font-size:.82rem;color:var(--teal);margin-top:6px}}

/* ===== SLIDE 7 DIFF ===== */
#s7 .stitle{{color:var(--navy);text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s7 .quote{{color:var(--navy);border-left:5px solid var(--teal);padding:18px 24px;font-size:1.05rem;font-style:italic;max-width:1100px;width:100%;text-align:center;margin-bottom:18px;background:rgba(255,255,255,0.8);border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.5)}}
#s7 .pills{{display:flex;gap:14px;width:100%;max-width:1100px;margin-bottom:18px}}
#s7 .pill{{flex:1;padding:16px;text-align:center;background:rgba(255,255,255,0.8);border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.5)}}
#s7 .pill h4{{font-family:'Cherry Bomb One',cursive;font-size:1rem;margin-bottom:4px;text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s7 .pill p{{font-size:.78rem;color:#555;line-height:1.35}}
#s7 .tbl{{width:100%;max-width:1100px;border-collapse:collapse;font-size:.82rem}}
#s7 .tbl th{{background:rgba(255,255,255,0.8);color:var(--navy);padding:10px 14px;text-align:left;font-weight:600;backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.5)}}
#s7 .tbl td{{padding:8px 14px;border-bottom:1px solid rgba(0,0,0,0.06);background:rgba(255,255,255,0.7)}}
#s7 .tbl tr:nth-child(even) td{{background:var(--gray)}}

/* ===== SLIDE 8 RS ===== */
#s8 .stitle{{color:var(--navy);text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s8 .rsimg{{max-height:30vh;object-fit:contain;display:block;margin:0 auto 14px}}
#s8 .rule80{{text-align:center;margin-bottom:14px}}
#s8 .pcards{{display:flex;gap:12px;width:100%;max-width:1200px;margin-bottom:16px}}
#s8 .pc2{{flex:1;color:var(--navy);padding:16px;border-top:4px solid;background:rgba(255,255,255,0.8);border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.5)}}
#s8 .pc2 h4{{font-family:'Cherry Bomb One',cursive;font-size:1rem;margin-bottom:4px;text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s8 .pc2 p{{font-size:.72rem;color:var(--navy);line-height:1.35}}

/* ===== SLIDE 9 COMMUNITY ===== */
#s9 .stitle{{color:var(--navy);text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}

/* ===== SLIDE 10 STORY ===== */
#s10 .stitle{{color:var(--navy);text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s10 .arc{{display:flex;gap:14px;width:100%;max-width:1200px;margin-bottom:16px}}
#s10 .ab{{flex:1;color:var(--navy);padding:18px;border-left:5px solid;background:rgba(255,255,255,0.8);border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.5)}}
#s10 .ab h4{{font-family:'Cherry Bomb One',cursive;font-size:.95rem;margin-bottom:6px;text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s10 .ab p{{font-size:.78rem;color:var(--navy);line-height:1.4}}

/* ===== SLIDE 11 BILAN ===== */
#s11 .stitle{{color:var(--navy);text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s11 .krow{{display:flex;gap:12px;width:100%;max-width:1200px;margin-bottom:16px}}
#s11 .kc{{flex:1;color:var(--navy);padding:16px;text-align:center;border-top:4px solid;background:rgba(255,255,255,0.8);border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.5)}}
#s11 .kc .kpi{{display:block;margin-bottom:2px;text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s11 .kc .klbl{{font-size:.7rem;color:var(--navy)}}
#s11 .brow{{display:flex;gap:16px;width:100%;max-width:1200px;margin-bottom:14px}}
#s11 .brow .c{{flex:1}}
#s11 .brow h4{{font-family:'Cherry Bomb One',cursive;font-size:1rem;margin-bottom:8px;color:var(--teal);text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s11 .brow p{{font-size:.8rem;margin-bottom:3px;color:var(--navy)}}
#s11 .rtbl{{width:100%;border-collapse:collapse;font-size:.8rem}}
#s11 .rtbl th{{background:rgba(255,255,255,0.8);color:var(--navy);padding:8px 12px;text-align:left;font-weight:600;backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,0.5)}}
#s11 .rtbl td{{padding:7px 12px;border-bottom:1px solid rgba(0,0,0,0.06);background:rgba(255,255,255,0.7)}}
#s11 .closing{{font-family:'Cherry Bomb One',cursive;font-size:1.6rem;color:var(--navy);margin-top:14px;text-align:center;text-shadow:2px 2px 0 #fff,-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff}}
#s11 .foot10{{font-size:.8rem;color:#555;margin-top:8px}}
</style>
</head>
<body>
<div class="ss" id="ss">
<div class="pbar" id="pbar"></div>
<div class="scount" id="scount"></div>

<!-- SLIDE 1 — COVER (bg normal, dark overlay) -->
<div class="slide active" id="s1">
  <div class="pabg" style="background-image:url('/popart-yellow.jpg')"></div>
  <div class="geo g1" style="border-radius:50%"></div>
  <div class="geo g2" style="border-radius:50%"></div>
  <div class="geo g3" style="border-radius:50%"></div>
  <div class="geo g4" style="border-radius:50%"></div>
  <div class="content">
    <div class="logo-txt">BUMPER</div>
    <div class="loc">Avenue 83 &mdash; Var</div>
    <div class="tagline">Coques &bull; R&eacute;parations &bull; Accessoires</div>
    <div class="sep"></div>
    <div class="sub2">Strat&eacute;gie Commerciale &amp; Animation du Point de Vente</div>
  </div>
  <div class="foot">Bachelor RAC &bull; Promotion 2025/2026</div>
</div>

<!-- SLIDE 2 — CONTEXTE (bg sepia, light overlay) -->
<div class="slide" id="s2">
  <div class="pabg" style="background-image:url('/popart-purple.jpg')"></div>
  <div class="stitle">Contexte de l&rsquo;enseigne</div>
  <div class="grid">
    <div class="left">
      <div class="imgframe" style="max-height:45vh;display:flex;align-items:center;justify-content:center;background:var(--gray)">
        <img src="{IMG3}" alt="Rayons Bumper" style="max-width:100%;max-height:45vh;object-fit:contain">
      </div>
      <p class="txt">Bumper est une enseigne ind&eacute;pendante sp&eacute;cialis&eacute;e dans la <strong>r&eacute;paration de smartphones</strong>, la vente de <strong>coques</strong> et d&rsquo;<strong>accessoires t&eacute;l&eacute;phoniques</strong>, implant&eacute;e au c&oelig;ur de la zone commerciale Avenue 83, dans le Var.</p>
      <p class="txt">Face &agrave; l&rsquo;essor des SAV en ligne et &agrave; la mont&eacute;e des grandes enseignes, Bumper doit renforcer son positionnement physique et num&eacute;rique.</p>
    </div>
    <div class="right">
      <div class="srow">
        <div class="sc ct-teal">
          <span class="kpi" style="color:var(--teal)">27&thinsp;&euro;</span>
          <div class="slbl">Panier moyen</div>
        </div>
        <div class="sc ct-blue">
          <span class="kpi" style="color:var(--blue)">150&ndash;300</span>
          <div class="slbl">Trafic quotidien</div>
        </div>
      </div>
      <div class="srow">
        <div class="sc ct-yellow">
          <span class="kpi" style="color:var(--yellow)">33%</span>
          <div class="slbl">Taux de transformation</div>
        </div>
        <div class="sc ct-purple">
          <span class="kpi" style="color:var(--purple)">4,8&thinsp;★</span>
          <div class="slbl">Note Google</div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 3 — SWOT (bg purple, light overlay) -->
<div class="slide" id="s3">
  <div class="pabg" style="background-image:url('/popart-teal.jpg')"></div>
  <div class="stitle">Diagnostic SWOT</div>
  <div class="swot">
    <div class="sw cl-teal">
      <h3 style="color:var(--teal)">FORCES</h3>
      <ul>
        <li style="color:var(--navy)">R&eacute;paration express garantie 30 min</li>
        <li style="color:var(--navy)">Coques exclusives disponibles en ligne</li>
        <li style="color:var(--navy)">Note Google 4,8&thinsp;★ &mdash; bonne r&eacute;putation</li>
        <li style="color:var(--navy)">Ancrage local fort, relation client personnalis&eacute;e</li>
        <li style="color:var(--navy)">Garantie SAV 1 an</li>
      </ul>
    </div>
    <div class="sw cl-yellow">
      <h3 style="color:var(--yellow)">FAIBLESSES</h3>
      <ul>
        <li style="color:var(--navy)">Visibilit&eacute; digitale &agrave; renforcer</li>
        <li style="color:var(--navy)">R&eacute;seaux sociaux insuffisamment exploit&eacute;s</li>
        <li style="color:var(--navy)">Pas d&rsquo;animation distinctive en boutique</li>
      </ul>
    </div>
    <div class="sw cl-blue">
      <h3 style="color:var(--blue)">OPPORTUNIT&Eacute;S</h3>
      <ul>
        <li style="color:var(--navy)">Zone Avenue 83 &agrave; fort trafic quotidien</li>
        <li style="color:var(--navy)">Tendance personnalisation et exp&eacute;rience client</li>
        <li style="color:var(--navy)">Potentiel contenu UGC</li>
      </ul>
    </div>
    <div class="sw cl-red">
      <h3 style="color:var(--red)">MENACES</h3>
      <ul>
        <li style="color:var(--navy)">Concurrence r&eacute;parateurs en ligne et cha&icirc;nes</li>
        <li style="color:var(--navy)">Pression prix grande distribution (FNAC, Darty)</li>
        <li style="color:var(--navy)">Baisse fr&eacute;quentation p&eacute;riodes creuses</li>
      </ul>
    </div>
  </div>
</div>


<!-- SLIDE 4 — PERSONAS (bg teal, light overlay) -->
<div class="slide" id="s4">
  <div class="pabg" style="background-image:url('/popart-yellow.jpg')"></div>
  <div class="stitle">Nos clients types</div>
  <div class="prow">
    <div class="pc ct-teal">
      <h3 style="color:var(--teal)">LUCAS &mdash; 22 ans</h3>
      <div class="meta">&Eacute;tudiant &bull; Toulon &bull; Budget 600&ndash;800&thinsp;&euro;/mois</div>
      <ul>
        <li>Usage intensif : 6&ndash;8h/jour</li>
        <li>Besoin : r&eacute;paration rapide, coque tendance unique</li>
        <li>Digital : Instagram, TikTok actifs</li>
        <li>Levier conversion : exp&eacute;rience Bumper Lab</li>
        <li>Levier fid&eacute;lisation : #MaBumperCoque, parrainage -10%</li>
      </ul>
      <div class="plat">
        <span class="ptag">📸 Instagram</span>
        <span class="ptag">🎵 TikTok</span>
      </div>
      <div class="lev" style="border-color:var(--teal);background:rgba(0,201,175,.08)">
        Leviers : Bumper Lab &bull; UGC &bull; Parrainage
      </div>
    </div>
    <div class="pc ct-yellow">
      <h3 style="color:var(--yellow)">MARIE &mdash; 42 ans</h3>
      <div class="meta">Cadre &bull; 2 enfants &bull; Var</div>
      <ul>
        <li>Besoin : r&eacute;paration fiable avec garantie</li>
        <li>D&eacute;clencheur : enfant casse &eacute;cran, recommandation amie</li>
        <li>Digital : Facebook, Google Maps</li>
        <li>Levier conversion : garantie 1 an, avis Google</li>
        <li>Levier fid&eacute;lisation : SMS suivi, newsletter famille</li>
      </ul>
      <div class="plat">
        <span class="ptag">📍 Google Maps</span>
        <span class="ptag">📘 Facebook</span>
      </div>
      <div class="lev" style="border-color:var(--yellow);background:rgba(250,201,0,.08)">
        Leviers : Garantie &bull; Avis &bull; Newsletter famille
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 5 — ESPACE SCENARISE (bg sepia, light overlay) -->
<div class="slide" id="s5">
  <div class="pabg" style="background-image:url('/popart-purple.jpg')"></div>
  <div class="stitle">Espace de vente sc&eacute;naris&eacute;</div>
  <div class="imgs">
    <div class="imgframe">
      <img src="{IMG5}" alt="Plan espace Bumper">
    </div>
    <div class="imgframe">
      <img src="{IMG2}" alt="Mannequin smartphones Bumper">
    </div>
  </div>
  <div class="zones">
    <div class="zone">
      <div class="zn">1</div>
      <h4>VITRINE</h4>
      <p>Coques tendance &bull; QR Code Instagram &bull; Rotation mensuelle</p>
    </div>
    <div class="zone">
      <div class="zn">2</div>
      <h4>ACCUEIL</h4>
      <p>D&eacute;monstration live &bull; Bornes diagnostic</p>
    </div>
    <div class="zone">
      <div class="zn">3</div>
      <h4>BUMPER LAB</h4>
      <p>Borne 24&Prime; &bull; Imprimante UV &bull; Mur UGC</p>
    </div>
    <div class="zone">
      <div class="zn">4</div>
      <h4>FID&Eacute;LISATION</h4>
      <p>Programme fid&eacute;lit&eacute; &bull; Borne QR avis</p>
    </div>
  </div>
  <div class="flux">Flux : Vitrine &rarr; Accueil &rarr; Bumper Lab &rarr; Produits &rarr; Caisse</div>
</div>


<!-- SLIDE 6 — BUMPER LAB (bg purple, dark overlay) -->
<div class="slide" id="s6">
  <div class="pabg" style="background-image:url('/popart-teal.jpg')"></div>
  <div class="stitle">BUMPER LAB</div>
  <div class="sub6">Seule boutique du Var avec personnalisation en direct</div>
  <div style="text-align:center;margin-bottom:14px">
    <img src="{IMG7}" alt="Bumper Lab" class="labimg imgframe-teal" style="border:3px solid var(--teal);border-radius:4px">
  </div>
  <div class="steps">
    <div class="stp" style="border-color:var(--teal)">
      <h4 style="color:var(--teal)">ARRIV&Eacute;E</h4>
      <p>Le client remarque le corner lumineux et la borne tactile</p>
    </div>
    <div class="stp" style="border-color:var(--blue)">
      <h4 style="color:var(--blue)">CHOIX</h4>
      <p>Il s&eacute;lectionne mod&egrave;le, couleur, motif sur la borne interactive</p>
    </div>
    <div class="stp" style="border-color:var(--yellow)">
      <h4 style="color:var(--yellow)">CR&Eacute;ATION</h4>
      <p>L&rsquo;imprimante UV imprime la coque sous ses yeux en 15&ndash;30 min</p>
    </div>
    <div class="stp" style="border-color:var(--purple)">
      <h4 style="color:var(--purple)">PARTAGE</h4>
      <p>Il poste en story #BumperLab et re&ccedil;oit -10%</p>
    </div>
  </div>
  <div class="kpirow">
    <div class="kb" style="border-color:var(--teal)">
      <span class="kpi" style="color:var(--teal)">+28%</span>
      <div class="klbl">Panier moyen</div>
    </div>
    <div class="kb" style="border-color:var(--blue)">
      <span class="kpi" style="color:var(--blue)">30%</span>
      <div class="klbl">UGC g&eacute;n&eacute;r&eacute;</div>
    </div>
    <div class="kb" style="border-color:var(--yellow)">
      <span class="kpi" style="color:var(--yellow)">20/sem</span>
      <div class="klbl">Coques personnalis&eacute;es</div>
    </div>
    <div class="kb" style="border-color:var(--purple)">
      <span class="kpi" style="color:var(--purple)">x5</span>
      <div class="klbl">ROI</div>
    </div>
  </div>
  <div class="invest">Investissement : 480&thinsp;&euro; &rarr; Marge 3 mois : 2 820&thinsp;&euro; &rarr; ROI x5</div>
</div>

<!-- SLIDE 7 — DIFFERENCIATION (bg teal, light overlay) -->
<div class="slide" id="s7">
  <div class="pabg" style="background-image:url('/popart-yellow.jpg')"></div>
  <div class="stitle">Notre avantage concurrentiel</div>
  <div class="quote">&laquo; Votre t&eacute;l&eacute;phone r&eacute;par&eacute; en 30 min, avec une coque unique &mdash; ici, maintenant, par des experts. &raquo;</div>
  <div class="pills">
    <div class="pill ct-teal">
      <h4 style="color:var(--teal)">RAPIDIT&Eacute;</h4>
      <p>30 min chrono &bull; Devis imm&eacute;diat &bull; Stock pi&egrave;ces disponible</p>
    </div>
    <div class="pill ct-blue">
      <h4 style="color:var(--blue)">EXCLUSIVIT&Eacute;</h4>
      <p>Coques non vendues en ligne &bull; Personnalisation &bull; Collections limit&eacute;es</p>
    </div>
    <div class="pill ct-yellow">
      <h4 style="color:var(--yellow)">PROXIMIT&Eacute;</h4>
      <p>&Eacute;quipe locale &bull; Relation personnalis&eacute;e &bull; Conseils honn&ecirc;tes</p>
    </div>
    <div class="pill ct-purple">
      <h4 style="color:var(--purple)">CONFIANCE</h4>
      <p>Garantie 1 an &bull; Pi&egrave;ces certifi&eacute;es &bull; Devis transparent</p>
    </div>
  </div>
  <table class="tbl">
    <thead><tr><th>Crit&egrave;re</th><th>Bumper</th><th>iSmash</th><th>FNAC / Darty</th></tr></thead>
    <tbody>
      <tr><td>Note Google</td><td style="color:var(--teal);font-weight:700">4,8&thinsp;★</td><td>4.2&thinsp;★</td><td>3.8&thinsp;★</td></tr>
      <tr><td>D&eacute;lai</td><td style="color:var(--teal);font-weight:700">30 min</td><td>1&ndash;2h</td><td>3&ndash;7 jours</td></tr>
      <tr><td>Coques exclusives</td><td style="color:var(--teal);font-weight:700">✓</td><td>✗</td><td>✗</td></tr>
      <tr><td>Personnalisation</td><td style="color:var(--teal);font-weight:700">✓ Lab</td><td>✗</td><td>✗</td></tr>
      <tr><td>Garantie SAV</td><td style="color:var(--teal);font-weight:700">✓ 1 an</td><td>✓ 1 an</td><td>Constructeur</td></tr>
    </tbody>
  </table>
</div>


<!-- SLIDE 8 — RESEAUX SOCIAUX (bg sepia, light overlay) -->
<div class="slide" id="s8">
  <div class="pabg" style="background-image:url('/popart-purple.jpg')"></div>
  <div class="stitle">Strat&eacute;gie R&eacute;seaux Sociaux</div>
  <div style="display:flex;gap:24px;width:100%;max-width:1200px;align-items:stretch">
    <div style="flex:1;display:flex;flex-direction:column;gap:10px">
      <div style="text-align:center">
        <span class="badge">80% utile &amp; divertissant</span>
        <span class="badge badge-teal" style="margin-left:6px">20% promotionnel</span>
      </div>
      <div style="display:flex;gap:10px">
        <div class="pc2" style="border-color:var(--teal);flex:1;background:rgba(255,255,255,0.8);backdrop-filter:blur(6px);color:var(--navy);padding:14px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);border:1px solid rgba(255,255,255,0.5);border-top:4px solid var(--teal)">
          <h4 style="color:var(--teal);font-family:'Cherry Bomb One',cursive;font-size:1rem;margin-bottom:4px">INSTAGRAM</h4>
          <p style="font-size:.72rem;color:var(--navy);line-height:1.35">5&times;/sem &bull; Reels &bull; Stories &bull; UGC #BumperLab<br>Objectif 1 000 abos</p>
        </div>
        <div class="pc2" style="border-color:var(--blue);flex:1;background:rgba(255,255,255,0.8);backdrop-filter:blur(6px);color:var(--navy);padding:14px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);border:1px solid rgba(255,255,255,0.5);border-top:4px solid var(--blue)">
          <h4 style="color:var(--blue);font-family:'Cherry Bomb One',cursive;font-size:1rem;margin-bottom:4px">TIKTOK</h4>
          <p style="font-size:.72rem;color:var(--navy);line-height:1.35">3&times;/sem &bull; Avant/apr&egrave;s 60s &bull; POV boutique<br>#MaBumperCoque &bull; 500 abos</p>
        </div>
      </div>
      <div style="display:flex;gap:10px">
        <div class="pc2" style="border-color:var(--yellow);flex:1;background:rgba(255,255,255,0.8);backdrop-filter:blur(6px);color:var(--navy);padding:14px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);border:1px solid rgba(255,255,255,0.5);border-top:4px solid var(--yellow)">
          <h4 style="color:var(--yellow);font-family:'Cherry Bomb One',cursive;font-size:1rem;margin-bottom:4px">FACEBOOK</h4>
          <p style="font-size:.72rem;color:var(--navy);line-height:1.35">3&times;/sem &bull; Promos locales &bull; &Eacute;v&eacute;nements<br>Avis Google &bull; Rayon 15 km</p>
        </div>
        <div class="pc2" style="border-color:var(--purple);flex:1;background:rgba(255,255,255,0.8);backdrop-filter:blur(6px);color:var(--navy);padding:14px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);border:1px solid rgba(255,255,255,0.5);border-top:4px solid var(--purple)">
          <h4 style="color:var(--purple);font-family:'Cherry Bomb One',cursive;font-size:1rem;margin-bottom:4px">GOOGLE</h4>
          <p style="font-size:.72rem;color:var(--navy);line-height:1.35">2&times;/sem &bull; Posts offres &bull; Photos HD<br>R&eacute;ponse avis &lt; 24h &bull; Top 3 local</p>
        </div>
      </div>
    </div>
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:10px">
      <img src="{IMG8}" alt="Post Instagram Bumper" style="max-height:55vh;object-fit:contain;border:3px solid var(--teal);border-radius:4px">
      <div style="background:rgba(255,255,255,0.8);backdrop-filter:blur(6px);color:var(--navy);padding:10px 16px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);border:1px solid rgba(255,255,255,0.5);width:100%;text-align:center">
        <p style="font-weight:700;margin-bottom:2px">&Eacute;cran cass&eacute; ? On s&rsquo;en occupe.</p>
        <p style="font-size:.75rem;color:var(--navy)">30 min chrono &mdash; garanti 1 an &mdash; Sans RDV</p>
        <p style="color:var(--teal);font-size:.72rem">#BumperAv83 #R&eacute;parationT&eacute;l&eacute;phone #Var</p>
        <p style="font-size:.7rem;color:var(--yellow)">200 impressions &bull; 15 likes &bull; 5 enregistrements</p>
      </div>
    </div>
  </div>
</div>


<!-- SLIDE 9 — ANIMATION COMMUNAUTÉ (bg purple, light overlay) -->
<div class="slide" id="s9">
  <div class="pabg" style="background-image:url('/popart-teal.jpg')"></div>
  <div class="stitle">Animation d&rsquo;une communaut&eacute;</div>
  <div style="display:flex;gap:8px;flex-wrap:wrap;width:100%;max-width:1200px;justify-content:center;margin-bottom:18px">
    <div style="background:rgba(255,255,255,0.8);backdrop-filter:blur(6px);color:var(--navy);padding:8px 14px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);border:1px solid rgba(255,255,255,0.5);text-align:center;border-top:3px solid var(--teal)"><strong>JAN</strong><br><span style="font-size:.68rem;color:var(--teal)">Soldes -20%</span></div>
    <div style="background:rgba(255,255,255,0.8);backdrop-filter:blur(6px);color:var(--navy);padding:8px 14px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);border:1px solid rgba(255,255,255,0.5);text-align:center;border-top:3px solid var(--yellow)"><strong>F&Eacute;V</strong><br><span style="font-size:.68rem;color:var(--yellow)">St-Valentin duo</span></div>
    <div style="background:rgba(255,255,255,0.8);backdrop-filter:blur(6px);color:var(--navy);padding:8px 14px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);border:1px solid rgba(255,255,255,0.5);text-align:center;border-top:3px solid var(--teal)"><strong>MAR</strong><br><span style="font-size:.68rem;color:var(--teal)">Printemps nature</span></div>
    <div style="background:rgba(255,255,255,0.8);backdrop-filter:blur(6px);color:var(--navy);padding:8px 14px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);border:1px solid rgba(255,255,255,0.5);text-align:center;border-top:3px solid var(--yellow)"><strong>AVR</strong><br><span style="font-size:.68rem;color:var(--yellow)">P&acirc;ques surprise</span></div>
    <div style="background:rgba(255,255,255,0.8);backdrop-filter:blur(6px);color:var(--navy);padding:8px 14px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);border:1px solid rgba(255,255,255,0.5);text-align:center;border-top:3px solid var(--purple)"><strong>MAI</strong><br><span style="font-size:.68rem;color:var(--purple)">F&ecirc;te des M&egrave;res gravure</span></div>
    <div style="background:rgba(255,255,255,0.8);backdrop-filter:blur(6px);color:var(--navy);padding:8px 14px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);border:1px solid rgba(255,255,255,0.5);text-align:center;border-top:3px solid var(--blue)"><strong>JUIN</strong><br><span style="font-size:.68rem;color:var(--blue)">&Eacute;t&eacute; plage</span></div>
    <div style="background:rgba(255,255,255,0.8);backdrop-filter:blur(6px);color:var(--navy);padding:8px 14px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);border:1px solid rgba(255,255,255,0.5);text-align:center;border-top:3px solid var(--teal)"><strong>SEP</strong><br><span style="font-size:.68rem;color:var(--teal)">Rentr&eacute;e &eacute;tudiant</span></div>
    <div style="background:rgba(255,255,255,0.8);backdrop-filter:blur(6px);color:var(--navy);padding:8px 14px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);border:1px solid rgba(255,255,255,0.5);text-align:center;border-top:3px solid var(--yellow)"><strong>OCT</strong><br><span style="font-size:.68rem;color:var(--yellow)">Halloween limited</span></div>
    <div style="background:rgba(255,255,255,0.8);backdrop-filter:blur(6px);color:var(--navy);padding:8px 14px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);border:1px solid rgba(255,255,255,0.5);text-align:center;border-top:3px solid var(--blue)"><strong>NOV</strong><br><span style="font-size:.68rem;color:var(--blue)">Black Friday -30%</span></div>
    <div style="background:rgba(255,255,255,0.8);backdrop-filter:blur(6px);color:var(--navy);padding:8px 14px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.08);border:1px solid rgba(255,255,255,0.5);text-align:center;border-top:3px solid var(--purple)"><strong>D&Eacute;C</strong><br><span style="font-size:.68rem;color:var(--purple)">No&euml;l cadeaux</span></div>
  </div>
  <div style="display:flex;gap:14px;width:100%;max-width:1200px;margin-bottom:14px">
    <div class="c ct-teal" style="flex:1;text-align:center">
      <h4 style="font-family:'Cherry Bomb One',cursive;font-size:1rem;color:var(--teal);margin-bottom:4px">Club VIP</h4>
      <p style="font-size:.8rem;color:var(--navy)">1&thinsp;&euro; = 1 point<br>Avantages exclusifs</p>
    </div>
    <div class="c ct-blue" style="flex:1;text-align:center">
      <h4 style="font-family:'Cherry Bomb One',cursive;font-size:1rem;color:var(--blue);margin-bottom:4px">UGC #MaBumperCoque</h4>
      <p style="font-size:.8rem;color:var(--navy)">-15% sur prochaine commande<br>Contenu client valoris&eacute;</p>
    </div>
    <div class="c ct-yellow" style="flex:1;text-align:center">
      <h4 style="font-family:'Cherry Bomb One',cursive;font-size:1rem;color:var(--yellow);margin-bottom:4px">Parrainage</h4>
      <p style="font-size:.8rem;color:var(--navy)">-10% pour le parrain<br>-10% pour le filleul</p>
    </div>
    <div class="c ct-purple" style="flex:1;text-align:center">
      <h4 style="font-family:'Cherry Bomb One',cursive;font-size:1rem;color:var(--purple);margin-bottom:4px">Live Instagram</h4>
      <p style="font-size:.8rem;color:var(--navy)">Session mensuelle<br>D&eacute;mo &amp; questions en direct</p>
    </div>
  </div>
  <div style="text-align:center">
    <img src="{IMG4}" alt="Mur coques Bumper" style="max-height:20vh;object-fit:contain;border:3px solid var(--navy);border-radius:4px">
  </div>
</div>


<!-- SLIDE 10 — MESSAGE ET STORY TELLING (bg teal, light overlay) -->
<div class="slide" id="s10">
  <div class="pabg" style="background-image:url('/popart-yellow.jpg')"></div>
  <div class="stitle">Notre histoire, votre histoire</div>
  <div class="arc">
    <div class="ab" style="border-color:var(--yellow)">
      <h4 style="color:var(--yellow)">LE PROBL&Egrave;ME</h4>
      <p>&Eacute;cran cass&eacute;, chargeur HS, coque ray&eacute;e. Les SAV en ligne sont lents, les grandes enseignes impersonnelles. Tu cherches rapide, local, humain.</p>
    </div>
    <div class="ab" style="border-color:var(--teal)">
      <h4 style="color:var(--teal)">LE H&Eacute;ROS : TOI</h4>
      <p>Tu veux une solution rapide et humaine. Tu m&eacute;rites un expert qui te comprend, sans jargon, sans attente.</p>
    </div>
    <div class="ab" style="border-color:var(--blue)">
      <h4 style="color:var(--blue)">LA SOLUTION : BUMPER</h4>
      <p>En 30 minutes, ton t&eacute;l&eacute;phone est r&eacute;par&eacute;. Une coque unique t&rsquo;attend. Une &eacute;quipe souriante t&rsquo;accueille.</p>
    </div>
    <div class="ab" style="border-color:var(--purple)">
      <h4 style="color:var(--purple)">LA TRANSFORMATION</h4>
      <p>Tu repars avec un t&eacute;l&eacute;phone neuf, une protection styl&eacute;e, et l&rsquo;adresse d&rsquo;un commerce de confiance &agrave; partager.</p>
    </div>
  </div>
</div>

<!-- SLIDE 11 — BILAN & PERSPECTIVES (bg sepia, light overlay) -->
<div class="slide" id="s11">
  <div class="pabg" style="background-image:url('/popart-purple.jpg')"></div>
  <div class="stitle">Bilan &amp; Perspectives</div>
  <div class="krow">
    <div class="kc" style="border-color:var(--teal)">
      <span class="kpi" style="color:var(--teal)">≥ 4.7</span>
      <div class="klbl">Note Google</div>
    </div>
    <div class="kc" style="border-color:var(--blue)">
      <span class="kpi" style="color:var(--blue)">+15%</span>
      <div class="klbl">CA annuel</div>
    </div>
    <div class="kc" style="border-color:var(--yellow)">
      <span class="kpi" style="color:var(--yellow)">+20%/mois</span>
      <div class="klbl">Abonn&eacute;s RS</div>
    </div>
    <div class="kc" style="border-color:var(--purple)">
      <span class="kpi" style="color:var(--purple)">&gt; 40%</span>
      <div class="klbl">Taux fid&eacute;lisation</div>
    </div>
    <div class="kc" style="border-color:var(--teal)">
      <span class="kpi" style="color:var(--teal)">&gt; 45&thinsp;&euro;</span>
      <div class="klbl">Panier moyen</div>
    </div>
  </div>
  <div class="brow">
    <div class="c ct-teal">
      <h4>Budget Bumper Lab</h4>
      <p>Investissement : 480&thinsp;&euro; (borne 300&thinsp;&euro; + coques 100&thinsp;&euro; + signal&eacute;tique 80&thinsp;&euro;)</p>
      <p>Marge nette 3 mois : 2 820&thinsp;&euro; &bull; ROI : x5</p>
      <p>Imprimante UV &agrave; commission : 0&thinsp;&euro; charge fixe</p>
    </div>
    <div class="c ct-blue">
      <table class="rtbl">
        <thead><tr><th>Risque</th><th>Criticité</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Avis viral</td><td style="color:var(--red);font-weight:700">&Eacute;LEV&Eacute;E</td><td>R&eacute;ponse &lt; 2h + geste commercial</td></tr>
          <tr><td>Panne fournisseur</td><td style="color:var(--yellow);font-weight:700">MOYENNE</td><td>2 backup + stock 15 jours</td></tr>
          <tr><td>Faible trafic</td><td style="color:var(--red);font-weight:700">&Eacute;LEV&Eacute;E</td><td>Meta Ads local + offre -10%</td></tr>
          <tr><td>Baisse CA creuse</td><td style="color:var(--purple);font-weight:700">CRITIQUE</td><td>Offres saisonni&egrave;res anticip&eacute;es</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="closing">Bumper : l&rsquo;expert local qui allie rapidit&eacute;, cr&eacute;ativit&eacute; et proximit&eacute;.</div>
  <div class="foot10">Merci pour votre attention</div>
</div>

<!-- Navigation -->
<button class="nbtn nprev" onclick="go(-1)">&lsaquo;</button>
<button class="nbtn nnext" onclick="go(1)">&rsaquo;</button>
<div class="dots" id="dots"></div>

</div><!-- /ss -->

<script>
(function(){{
  var S=document.querySelectorAll('.slide'),T=S.length,C=0;
  var P=document.getElementById('pbar'),K=document.getElementById('scount'),D=document.getElementById('dots');
  function show(n){{
    S[C].classList.remove('active');
    C=(n+T)%T;
    S[C].classList.add('active');
    P.style.width=((C+1)/T*100)+'%';
    K.textContent=(C+1)+' / '+T;
    var dd=D.querySelectorAll('.dot');
    for(var i=0;i<dd.length;i++) dd[i].classList.toggle('active',i===C);
  }}
  for(var i=0;i<T;i++){{
    var d=document.createElement('div');
    d.className='dot'+(i===0?' active':'');
    d.setAttribute('data-i',i);
    d.onclick=function(){{ show(parseInt(this.getAttribute('data-i'))); }};
    D.appendChild(d);
  }}
  window.go=function(dir){{ show(C+dir); }};
  document.addEventListener('keydown',function(e){{
    if(e.key==='ArrowRight'||e.key==='ArrowDown') go(1);
    else if(e.key==='ArrowLeft'||e.key==='ArrowUp') go(-1);
  }});
  P.style.width=(100/T)+'%';
  K.textContent='1 / '+T;
}})();
</script>
</body>
</html>"""

out = os.path.join(DIR, "bumper-presentation.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"Wrote {out} ({len(HTML):,} bytes)")
