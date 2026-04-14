"""
generate_cv.py
Generates Academic_CV_Josephine_Amponsah_Baah.docx using python-docx.

Install dependency if needed:
    pip install python-docx
"""

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ── Colour constants ───────────────────────────────────────────────────────────
GREEN = RGBColor(34, 139, 34)
BLACK = RGBColor(0, 0, 0)
DARK_GREY = RGBColor(64, 64, 64)

# ── Helper utilities ───────────────────────────────────────────────────────────

def set_run_font(run, name="Calibri", size_pt=10, bold=False, italic=False,
                 color=None):
    run.font.name = name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = color


def add_bottom_border(paragraph):
    """Add a thin bottom border (rule) beneath a paragraph."""
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "228B22")
    pBdr.append(bottom)
    pPr.append(pBdr)


def add_section_header(doc, title):
    """Bold, green, uppercase section header with bottom border."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(1)
    run = p.add_run(title.upper())
    set_run_font(run, size_pt=10.5, bold=True, color=GREEN)
    add_bottom_border(p)
    return p


def add_bullet(doc, text, indent_level=0, size_pt=10):
    """Add a bullet point paragraph."""
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.left_indent = Inches(0.25 + indent_level * 0.2)
    run = p.add_run(text)
    set_run_font(run, size_pt=size_pt)
    return p


def add_experience_header(doc, title, period, bold_title=True, space_before=3):
    """Bold role title + right-aligned period on same line."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(1)

    run_title = p.add_run(title)
    set_run_font(run_title, size_pt=10, bold=bold_title)

    # Tab + period right-aligned via tab stop
    tab_run = p.add_run("\t" + period)
    set_run_font(tab_run, size_pt=10, italic=True, color=DARK_GREY)

    # Right tab stop at 6.5 inches (within margins on letter paper)
    pPr = p._p.get_or_add_pPr()
    tabs = OxmlElement("w:tabs")
    tab = OxmlElement("w:tab")
    tab.set(qn("w:val"), "right")
    tab.set(qn("w:pos"), "9360")   # 6.5" × 1440 twips/inch
    tabs.append(tab)
    pPr.append(tabs)
    return p


def add_italic_label(doc, text, size_pt=10):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(text)
    set_run_font(run, size_pt=size_pt, italic=True, color=DARK_GREY)
    return p


def inline_bold_normal(paragraph, bold_text, normal_text, size_pt=10):
    r1 = paragraph.add_run(bold_text)
    set_run_font(r1, size_pt=size_pt, bold=True)
    r2 = paragraph.add_run(normal_text)
    set_run_font(r2, size_pt=size_pt)


# ── Document setup ─────────────────────────────────────────────────────────────

doc = Document()

# Margins – 0.65" top/bottom, 0.75" left/right
for section in doc.sections:
    section.top_margin = Inches(0.65)
    section.bottom_margin = Inches(0.65)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)

# ── NAME & CONTACT HEADER ─────────────────────────────────────────────────────

name_p = doc.add_paragraph()
name_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
name_p.paragraph_format.space_before = Pt(0)
name_p.paragraph_format.space_after = Pt(2)
name_run = name_p.add_run("Josephine Amponsah Baah")
set_run_font(name_run, size_pt=20, bold=True)

title_p = doc.add_paragraph()
title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
title_p.paragraph_format.space_before = Pt(0)
title_p.paragraph_format.space_after = Pt(2)
title_run = title_p.add_run("ML/AI Researcher")
set_run_font(title_run, size_pt=11, italic=True, color=GREEN)

contact_p = doc.add_paragraph()
contact_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
contact_p.paragraph_format.space_before = Pt(0)
contact_p.paragraph_format.space_after = Pt(4)
contact_run = contact_p.add_run(
    "josephine.amponsah98@gmail.com  |  "
    "github.com/josephine-amponsah  |  "
    "linkedin.com/in/josephine-amponsah-baah"
)
set_run_font(contact_run, size_pt=10, color=DARK_GREY)

# ── SECTION 1: RESEARCH INTERESTS ────────────────────────────────────────────

add_section_header(doc, "Research Interests")

research_text = (
    "My research focuses on NLP, deep learning, and LLM robustness — particularly bias "
    "mitigation in NLI/NLU systems — with applied interests in Financial AI including credit "
    "risk modelling, fraud detection, and domain-adapted LLMs (FinBERT) for financial "
    "document processing and validation."
)

ri_p = doc.add_paragraph()
ri_p.paragraph_format.space_before = Pt(2)
ri_p.paragraph_format.space_after = Pt(2)
ri_run = ri_p.add_run(research_text)
set_run_font(ri_run, size_pt=10)

# ── SECTION 2: EDUCATION ──────────────────────────────────────────────────────

add_section_header(doc, "Education")

# MSc
add_experience_header(
    doc,
    "MSc. Data Science  —  University of Texas, Austin, USA",
    "Aug 2024 – April 2026",
)

courses_p = doc.add_paragraph()
courses_p.paragraph_format.space_before = Pt(1)
courses_p.paragraph_format.space_after = Pt(0)
inline_bold_normal(
    courses_p,
    "Relevant Courses: ",
    "Machine Learning, Data Structures & Algorithms, Deep Learning, "
    "Advanced Predictive Modelling (Time-Series), Natural Language Processing, "
    "Advanced Deep Learning, Probability & Statistics",
)

# Azure Certification
add_experience_header(
    doc,
    "Azure Data Scientist Associate  —  Microsoft Certification",
    "Sept 2023 – Sept 2026",
)

# BSc
add_experience_header(
    doc,
    "BSc. Engineering (Chemical)  —  Kwame Nkrumah University of Science & Technology",
    "Sept 2015 – July 2019",
)

# ── SECTION 3: RESEARCH & ACADEMIC PROJECTS ───────────────────────────────────

add_section_header(doc, "Research & Academic Projects")

# ---- Project 1 ----
proj1_p = doc.add_paragraph()
proj1_p.paragraph_format.space_before = Pt(3)
proj1_p.paragraph_format.space_after = Pt(0)
r = proj1_p.add_run(
    "Improving NLU via Ensemble Debiasing and Data Cartography"
)
set_run_font(r, size_pt=10, bold=True)

proj1_meta_p = doc.add_paragraph()
proj1_meta_p.paragraph_format.space_before = Pt(0)
proj1_meta_p.paragraph_format.space_after = Pt(0)
r_meta = proj1_meta_p.add_run(
    "NLP Final Paper  |  github.com/josephine-amponsah/multi-nli-nlu-optimization  |  Dec 2025"
)
set_run_font(r_meta, size_pt=9.5, italic=True, color=DARK_GREY)

add_bullet(
    doc,
    "Authored research paper investigating dataset artifacts in MultiNLI; fine-tuned "
    "ELECTRA-small and implemented ensemble debiasing and data cartography, achieving up to "
    "4.6 pp robustness improvement on CheckList behavioral tests.",
)
add_bullet(
    doc,
    "Employed BiLSTM hypothesis-only baselines (InferSent, GloVe) alongside ELECTRA-small "
    "for controlled architecture comparison across negation, lexical overlap, and quantifier "
    "capabilities.",
)

# ---- Project 2 ----
proj2_p = doc.add_paragraph()
proj2_p.paragraph_format.space_before = Pt(3)
proj2_p.paragraph_format.space_after = Pt(0)
r = proj2_p.add_run("Neural Network Classifier with Loss Optimisation")
set_run_font(r, size_pt=10, bold=True)

proj2_meta_p = doc.add_paragraph()
proj2_meta_p.paragraph_format.space_before = Pt(0)
proj2_meta_p.paragraph_format.space_after = Pt(0)
r_meta = proj2_meta_p.add_run(
    "Deep Learning  |  github.com/josephine-amponsah/nnclassifier-loss-optimization  |  Mar 2026"
)
set_run_font(r_meta, size_pt=9.5, italic=True, color=DARK_GREY)

add_bullet(
    doc,
    "Designed and trained deep classification networks (MLP, Deep Residual MLP) in PyTorch, "
    "implementing residual connections and softmax log-likelihood loss; achieved >80% "
    "validation accuracy with TensorBoard-tracked training dynamics.",
)

# ---- Project 3 ----
proj3_p = doc.add_paragraph()
proj3_p.paragraph_format.space_before = Pt(3)
proj3_p.paragraph_format.space_after = Pt(0)
r = proj3_p.add_run("NLP Transformer Models & Sentiment Classifiers")
set_run_font(r, size_pt=10, bold=True)

proj3_meta_p = doc.add_paragraph()
proj3_meta_p.paragraph_format.space_before = Pt(0)
proj3_meta_p.paragraph_format.space_after = Pt(0)
r_meta = proj3_meta_p.add_run(
    "NLP  |  github.com/josephine-amponsah/nlp-transformer-models  |  Mar 2026"
)
set_run_font(r_meta, size_pt=9.5, italic=True, color=DARK_GREY)

add_bullet(
    doc,
    "Fine-tuned BERT/ELECTRA transformer models for sequence classification; built neural "
    "sentiment classifiers with custom optimization pipelines and investigated preprocessing "
    "strategies across multiple architectures.",
)

# ---- Project 4 ----
proj4_p = doc.add_paragraph()
proj4_p.paragraph_format.space_before = Pt(3)
proj4_p.paragraph_format.space_after = Pt(0)
r = proj4_p.add_run("LLM Fact-Checking Pipeline & ABSA Recommender")
set_run_font(r, size_pt=10, bold=True)

proj4_meta_p = doc.add_paragraph()
proj4_meta_p.paragraph_format.space_before = Pt(0)
proj4_meta_p.paragraph_format.space_after = Pt(0)
r_meta = proj4_meta_p.add_run(
    "NLP  |  github.com/josephine-amponsah/factchecking-llm-responses  |  github.com/josephine-amponsah/absa-based-recommender  |  Mar 2026"
)
set_run_font(r_meta, size_pt=9.5, italic=True, color=DARK_GREY)

add_bullet(
    doc,
    "Developed an LLM fact-checking pipeline for response validation; built BERT-based aspect "
    "sentiment analysis model (Word2vec + ABSA) for fine-grained customer sentiment "
    "extraction, applied in financial document and recommender contexts.",
)

# ── SECTION 4: EXPERIENCE ─────────────────────────────────────────────────────

add_section_header(doc, "Experience")

# Fido
add_experience_header(
    doc,
    "Data Analyst  —  Fido Microcredit (FinTech)",
    "July 2024 – Present",
    space_before=3,
)

add_italic_label(doc, "Statistical Analysis & ML Research")

add_bullet(
    doc,
    "Optimized statistical models behind fraud monitoring logics using central tendency "
    "measures and feature engineering techniques, reducing false fraud flags by 28%.",
)
add_bullet(
    doc,
    "Built a supervised learning model to automate flagging of newly discovered fraud "
    "patterns, replacing blanket geohash blocking at precision level 5.",
)
add_bullet(
    doc,
    "Analysed impact of new KYC requirements on risk performance via A/B testing cohort "
    "analysis; contributed features to new versions of risk behavioural models.",
)

# WeTheBrands
add_experience_header(
    doc,
    "Data Analyst  —  WeTheBrands (E-Commerce), Germany",
    "Jan 2024 – Nov 2024",
    space_before=3,
)

# Broadspectrum
add_experience_header(
    doc,
    "Data Analyst  —  Broadspectrum Digital Payments (FinTech)",
    "Jan 2022 – Jan 2024",
    space_before=3,
)

# ── SECTION 5: SKILLS ─────────────────────────────────────────────────────────

add_section_header(doc, "Skills")

skills_data = [
    (
        "Domains: ",
        "Supervised Learning, Unsupervised Learning, NLP & Transformers, Deep Learning, "
        "Statistical Analysis, Forecasting, Financial Risk Modelling, Data Visualisation, "
        "Recommender Systems",
    ),
    (
        "Frameworks/Tools: ",
        "PyTorch, TensorFlow/Keras, HuggingFace Transformers, Pandas, NumPy, Matplotlib, "
        "Scikit-learn, NLTK, Gensim, FastAPI, Flask, Docker, BigQuery, DBT, PowerBI, "
        "Tableau, GitHub",
    ),
    (
        "Languages: ",
        "Python, R, SQL, DAX, Azure, AWS",
    ),
]

for bold_part, normal_part in skills_data:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    inline_bold_normal(p, bold_part, normal_part)

# ── SECTION 6: PUBLICATIONS & PRESENTATIONS ───────────────────────────────────

add_section_header(doc, "Publications & Presentations")

pub_entries = [
    (
        "Improving Natural Language Understanding via Ensemble Debiasing and Data Cartography",
        " — NLP Final Paper, UT Austin, 2025. "
        "github.com/josephine-amponsah/multi-nli-nlu-optimization",
    ),
    (
        "Talk: ",
        "Statistical & ML-based Fraud Risk Prediction Methods — DevX 2025; "
        "Geospatial Segmentation for Risk Assessment — PyCon Ghana 2025.",
    ),
    (
        "Writing: ",
        "Publishing practical ML, mathematics and finance articles for intermediate data "
        "practitioners.",
    ),
]

for bold_part, normal_part in pub_entries:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    inline_bold_normal(p, bold_part, normal_part)

# ── Save ───────────────────────────────────────────────────────────────────────

output_path = "Academic_CV_Josephine_Amponsah_Baah.docx"
doc.save(output_path)
print(f"CV saved to {output_path}")
