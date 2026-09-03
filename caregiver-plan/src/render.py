"""Rendering helpers for the Texas caregiver plan PDF (reportlab platypus)."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                PageBreak, Table, TableStyle, KeepTogether, ListFlowable, ListItem,
                                NextPageTemplate)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('DV', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DVI', '/usr/share/fonts/truetype/dejavu/../liberation/LiberationSans-Italic.ttf'))
pdfmetrics.registerFont(TTFont('DVBI', '/usr/share/fonts/truetype/dejavu/../liberation/LiberationSans-BoldItalic.ttf'))
pdfmetrics.registerFontFamily('DV', normal='DV', bold='DVB', italic='DVI', boldItalic='DVBI')

NAVY = colors.HexColor('#1F3A5F')
TEAL = colors.HexColor('#2A7F7F')
GOLD = colors.HexColor('#B8860B')
LIGHT = colors.HexColor('#EEF3F8')
LIGHT2 = colors.HexColor('#F7F9FB')
RED = colors.HexColor('#9B2226')
GREEN = colors.HexColor('#2D6A4F')
GRID = colors.HexColor('#C9D3DE')

S = {}
S['title'] = ParagraphStyle('title', fontName='DVB', fontSize=26, leading=32, textColor=NAVY, alignment=TA_CENTER, spaceAfter=10)
S['subtitle'] = ParagraphStyle('subtitle', fontName='DV', fontSize=13, leading=18, textColor=TEAL, alignment=TA_CENTER, spaceAfter=6)
S['h1'] = ParagraphStyle('h1', fontName='DVB', fontSize=18, leading=22, textColor=NAVY, spaceBefore=6, spaceAfter=8, keepWithNext=1)
S['h2'] = ParagraphStyle('h2', fontName='DVB', fontSize=13.5, leading=17, textColor=TEAL, spaceBefore=10, spaceAfter=5, keepWithNext=1)
S['h3'] = ParagraphStyle('h3', fontName='DVB', fontSize=11, leading=14, textColor=NAVY, spaceBefore=7, spaceAfter=3, keepWithNext=1)
S['body'] = ParagraphStyle('body', fontName='DV', fontSize=9.6, leading=13.2, spaceAfter=5)
S['small'] = ParagraphStyle('small', fontName='DV', fontSize=8.2, leading=10.8, spaceAfter=3, textColor=colors.HexColor('#333333'))
S['tiny'] = ParagraphStyle('tiny', fontName='DV', fontSize=7.4, leading=9.4, textColor=colors.HexColor('#444444'))
S['tight'] = ParagraphStyle('tight', fontName='DV', fontSize=7.5, leading=9.3)
S['tighth'] = ParagraphStyle('tighth', fontName='DVB', fontSize=7.7, leading=9.5, textColor=colors.white)
S['cell'] = ParagraphStyle('cell', fontName='DV', fontSize=8.4, leading=10.8)
S['cellb'] = ParagraphStyle('cellb', fontName='DVB', fontSize=8.4, leading=10.8)
S['cellh'] = ParagraphStyle('cellh', fontName='DVB', fontSize=8.6, leading=11, textColor=colors.white)
S['callout'] = ParagraphStyle('callout', fontName='DV', fontSize=9.4, leading=13, textColor=colors.black)
S['toc1'] = ParagraphStyle('toc1', fontName='DVB', fontSize=10.5, leading=15, leftIndent=0)
S['toc2'] = ParagraphStyle('toc2', fontName='DV', fontSize=9.2, leading=13, leftIndent=14)

def P(text, style='body'):
    return Paragraph(text, S[style])

def H1(text):
    return Paragraph(text, S['h1'])

def H2(text):
    return Paragraph(text, S['h2'])

def H3(text):
    return Paragraph(text, S['h3'])

def bullets(items, style='body', bullet='•'):
    return ListFlowable([ListItem(Paragraph(i, S[style]), leftIndent=12, value=bullet) for i in items],
                        bulletType='bullet', start=bullet, leftIndent=12, bulletFontName='DV', bulletFontSize=8)

def numbered(items, style='body', start=1):
    return ListFlowable([ListItem(Paragraph(i, S[style]), leftIndent=16) for i in items],
                        bulletType='1', start=start, leftIndent=16, bulletFontName='DVB', bulletFontSize=9)

def callout(text, kind='info', title=None):
    color = {'info': TEAL, 'warn': RED, 'money': GOLD, 'ok': GREEN}[kind]
    bg = {'info': LIGHT, 'warn': colors.HexColor('#FBEDEE'), 'money': colors.HexColor('#FBF5E4'), 'ok': colors.HexColor('#E9F5EE')}[kind]
    rows = []
    if title:
        rows.append([Paragraph(f'<b>{title}</b>', ParagraphStyle('ct', parent=S['callout'], textColor=color, fontName='DVB'))])
    rows.append([Paragraph(text, S['callout'])])
    t = Table(rows, colWidths=[6.9 * inch])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), bg), ('LINEBEFORE', (0, 0), (0, -1), 3, color),
                           ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
                           ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5)]))
    return KeepTogether([Spacer(1, 3), t, Spacer(1, 6)])

def table(header, rows, widths, zebra=True, header_bg=NAVY, font='cell'):
    hs = S['tighth'] if font == 'tight' else S['cellh']
    data = [[Paragraph(h, hs) for h in header]]
    for r in rows:
        data.append([Paragraph(str(c), S[font]) if not hasattr(c, 'wrap') else c for c in r])
    t = Table(data, colWidths=widths, repeatRows=1)
    style = [('BACKGROUND', (0, 0), (-1, 0), header_bg), ('GRID', (0, 0), (-1, -1), 0.4, GRID),
             ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
             ('TOPPADDING', (0, 0), (-1, -1), 2 if font == 'tight' else 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 2 if font == 'tight' else 3)]
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0:
                style.append(('BACKGROUND', (0, i), (-1, i), LIGHT2))
    t.setStyle(TableStyle(style))
    return t

def steps_table(rows, widths=(0.35 * inch, 2.35 * inch, 2.6 * inch, 1.6 * inch)):
    """rows: list of (n, what, how/where, timing)"""
    return table(['#', 'What to do', 'How / where / who to call', 'When / how long'],
                 [[f'<b>{n}</b>', w, h, t] for n, w, h, t in rows], list(widths))

def checkbox_list(items):
    return table(['', 'Checklist item'], [['☐', i] for i in items], [0.3 * inch, 6.6 * inch], zebra=False)

class Doc(BaseDocTemplate):
    def __init__(self, filename, title, **kw):
        super().__init__(filename, pagesize=letter, leftMargin=0.8 * inch, rightMargin=0.8 * inch,
                         topMargin=0.85 * inch, bottomMargin=0.8 * inch, title=title, author='Family caregiving plan', **kw)
        self.doc_title = title
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id='f')
        self.addPageTemplates([PageTemplate(id='cover', frames=[frame], onPage=self._cover),
                               PageTemplate(id='main', frames=[frame], onPage=self._decorate)])

    def _cover(self, canv, doc):
        canv.saveState()
        canv.setFillColor(NAVY)
        canv.rect(0, letter[1] - 1.1 * inch, letter[0], 1.1 * inch, fill=1, stroke=0)
        canv.setFillColor(TEAL)
        canv.rect(0, 0, letter[0], 0.5 * inch, fill=1, stroke=0)
        canv.restoreState()

    def _decorate(self, canv, doc):
        canv.saveState()
        canv.setStrokeColor(NAVY); canv.setLineWidth(1.2)
        canv.line(doc.leftMargin, letter[1] - 0.6 * inch, letter[0] - doc.rightMargin, letter[1] - 0.6 * inch)
        canv.setFont('DVB', 8); canv.setFillColor(NAVY)
        canv.drawString(doc.leftMargin, letter[1] - 0.52 * inch, self.doc_title)
        canv.setFont('DV', 8); canv.setFillColor(colors.HexColor('#555555'))
        canv.drawRightString(letter[0] - doc.rightMargin, letter[1] - 0.52 * inch, 'Texas · prepared September 2026')
        canv.drawRightString(letter[0] - doc.rightMargin, 0.5 * inch, f'Page {doc.page}')
        canv.drawString(doc.leftMargin, 0.5 * inch, 'Not legal, tax, or medical advice. Verify figures with HHSC before acting.')
        canv.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            st = flowable.style.name
            if st == 'h1':
                key = 'h1-%d' % id(flowable)
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(flowable.getPlainText(), key, level=0, closed=False)
                self.notify('TOCEntry', (0, flowable.getPlainText(), self.page, key))
            elif st == 'h2':
                key = 'h2-%d' % id(flowable)
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(flowable.getPlainText(), key, level=1, closed=True)
                self.notify('TOCEntry', (1, flowable.getPlainText(), self.page, key))

def toc():
    t = TableOfContents()
    t.levelStyles = [S['toc1'], S['toc2']]
    t.dotsMinLevel = 0
    return t
