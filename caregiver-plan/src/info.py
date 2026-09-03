# -*- coding: utf-8 -*-
import sys
from reportlab.pdfgen import canvas as cv
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.utils import simpleSplit
import render  # registers DV/DVB fonts

W, H = letter
M = 40
INK   = colors.HexColor('#0b0b0b')
INK2  = colors.HexColor('#52514e')
NAVY  = colors.HexColor('#12233a')
SURF  = colors.HexColor('#fcfcfb')
LINE  = colors.HexColor('#d8d6d0')
S1 = colors.HexColor('#2a78d6')   # blue   - stays exempt
S2 = colors.HexColor('#1baf7a')   # aqua   - protected for spouse
S3 = colors.HexColor('#eda100')   # yellow - converted
S4 = colors.HexColor('#4a3aa7')   # violet - moved early
GREY  = colors.HexColor('#9a9891')

def tint(c, a):
    return colors.Color(1-(1-c.red)*a, 1-(1-c.green)*a, 1-(1-c.blue)*a)

def page_bg(c):
    c.setFillColor(SURF); c.rect(0, 0, W, H, fill=1, stroke=0)

def header(c, kicker, title, n):
    c.setFillColor(NAVY); c.rect(0, H-92, W, 92, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#8fb3d9')); c.setFont('DVB', 8.5)
    c.drawString(M, H-38, kicker.upper())
    c.setFillColor(colors.white); c.setFont('DVB', 21)
    c.drawString(M, H-66, title)
    c.setFillColor(colors.HexColor('#5f7fa3')); c.setFont('DVB', 26)
    c.drawRightString(W-M, H-64, str(n))

def footer(c, note=''):
    c.setStrokeColor(LINE); c.setLineWidth(0.7); c.line(M, 46, W-M, 46)
    c.setFont('DV', 7.2); c.setFillColor(GREY)
    c.drawString(M, 34, note or 'Texas rules, 2026 figures. Not legal or tax advice - this plan needs an elder law attorney.')

def para(c, txt, x, y, w, size=9.2, lead=12, font='DV', fill=INK):
    c.setFont(font, size); c.setFillColor(fill)
    for ln in simpleSplit(txt, font, size, w):
        c.drawString(x, y, ln); y -= lead
    return y

def card(c, x, y, w, h, accent, num, title, body, tsize=11, bsize=8.8):
    c.setFillColor(tint(accent, 0.10)); c.setStrokeColor(tint(accent, 0.45)); c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, 7, fill=1, stroke=1)
    c.setFillColor(accent); c.roundRect(x, y, 5.5, h, 2.5, fill=1, stroke=0)
    tx = x + 20
    if num:
        c.setFillColor(accent); c.circle(x+30, y+h-19, 10.5, fill=1, stroke=0)
        c.setFillColor(colors.white); c.setFont('DVB', 11)
        c.drawCentredString(x+30, y+h-23, str(num)); tx = x + 50
    c.setFillColor(NAVY); c.setFont('DVB', tsize)
    c.drawString(tx, y+h-24, title)
    para(c, body, tx, y+h-40, w-(tx-x)-16, bsize, bsize+3.2, 'DV', INK2)

def arrow_down(c, x, y0, y1, col=GREY):
    c.setStrokeColor(col); c.setLineWidth(1.6); c.line(x, y0, x, y1+7)
    c.setFillColor(col)
    p = c.beginPath(); p.moveTo(x-5, y1+8); p.lineTo(x+5, y1+8); p.lineTo(x, y1); p.close()
    c.drawPath(p, fill=1, stroke=0)

# ---------------------------------------------------------------- page 1
def p1(c):
    page_bg(c); header(c, 'The whole plan in one picture', 'Nothing has to be given away', 1)
    y = H-118
    c.setFillColor(NAVY); c.setStrokeColor(NAVY); c.setLineWidth(1.2)
    c.roundRect(M, y-34, W-2*M, 34, 6, fill=1, stroke=1)
    c.setFillColor(colors.white); c.setFont('DVB', 12.5)
    c.drawCentredString(W/2, y-22, 'EVERYTHING YOUR PARENTS OWN TODAY')
    y -= 34
    arrow_down(c, W/2, y-2, y-20)
    y -= 26

    items = [
        (S1, 1, 'It is already exempt', 'The homestead counts for nothing - at ANY value - as long as a spouse lives there. So does one car, at any value, plus household goods. For most families this is the largest piece of the estate, and it never had to be protected. It already is.'),
        (S2, 2, 'It is protected for the spouse who stays home', 'Only ONE spouse applies. The other becomes the "community spouse" and keeps up to $162,660 in savings plus up to $4,066.50 a month of income. That protection exists only while there is a spouse at home - which is why they never both apply at once.'),
        (S3, 3, 'It gets turned into care', 'Money spent making the house work for them - ramps, a roll-in shower, wider doors, a ground-floor suite, lifts - is unlimited, has no waiting period, and Texas blesses it by name. Cash becomes care AND stays in an asset that is exempt for life.'),
        (S4, 4, 'It gets turned into income', 'Retirement savings above the protected amount can be converted into a properly structured annuity paying the spouse at home a monthly income for life. Done right there is no penalty. Done wrong the whole purchase is penalized - attorney work.'),
        (S4, 5, 'It moves early, and legally', 'Assets placed in an irrevocable trust are outside the test once five years have passed - so the clock is worth starting now. And because the caregiver is their DAUGHTER, the house itself can pass to her penalty-free after two years of live-in care. See page 3.'),
    ]
    ch = 78
    for col, n, t, b in items:
        card(c, M, y-ch, W-2*M, ch, col, n, t, b)
        y -= ch + 9
    y += 9
    arrow_down(c, W/2, y-4, y-22)
    y -= 30
    c.setFillColor(tint(GREY, 0.18)); c.setStrokeColor(GREY); c.setLineWidth(0.9)
    c.roundRect(M, y-40, W-2*M, 40, 6, fill=1, stroke=1)
    c.setFillColor(NAVY); c.setFont('DVB', 10.5)
    c.drawCentredString(W/2, y-17, 'Only what is left after all five is what Medicaid ever looks at.')
    c.setFillColor(INK2); c.setFont('DV', 8.6)
    c.drawCentredString(W/2, y-31, 'For most families that remainder is small - and it is spent on their own care, not forfeited.')
    footer(c)

# ---------------------------------------------------------------- page 2
def p2(c):
    page_bg(c); header(c, 'The single most important decision', 'One spouse applies. Never both.', 2)
    y = H-118
    y = para(c, 'Everything else in this plan is optional. This one is not. Texas protects the spouse who stays at home - but that protection exists only while there IS a spouse at home. The day the second one applies, it vanishes and the couple is measured together against $3,000.',
             M, y, W-2*M, 9.6, 13)
    y -= 12

    base = 296
    colw = (W-2*M-30)/2
    lx, rx = M, M+colw+30
    top = y

    # left: both apply
    c.setStrokeColor(LINE); c.setFillColor(colors.white); c.setLineWidth(0.8)
    c.roundRect(lx, base-14, colw, top-base+14, 7, fill=1, stroke=1)
    c.setFillColor(colors.HexColor('#9B2226')); c.setFont('DVB', 11.5)
    c.drawCentredString(lx+colw/2, top-24, 'IF BOTH APPLY')
    c.setFillColor(INK2); c.setFont('DV', 8.6)
    c.drawCentredString(lx+colw/2, top-38, 'They are budgeted as a couple')
    bh = 4
    c.setFillColor(colors.HexColor('#9B2226'))
    c.rect(lx+30, base+10, colw-60, bh, fill=1, stroke=0)
    c.setFillColor(NAVY); c.setFont('DVB', 15)
    c.drawCentredString(lx+colw/2, base+24, '$3,000')
    c.setFillColor(INK2); c.setFont('DV', 8.4)
    c.drawCentredString(lx+colw/2, base+1, 'total, between the two of them')
    c.setFillColor(colors.HexColor('#9B2226')); c.setFont('DVB', 9.5)
    c.drawCentredString(lx+colw/2, base+120, 'Everything above this line')
    c.drawCentredString(lx+colw/2, base+106, 'must be spent down first.')
    c.setFillColor(INK2); c.setFont('DV', 8.4)
    c.drawCentredString(lx+colw/2, base+88, 'The house is still exempt while')
    c.drawCentredString(lx+colw/2, base+76, 'they live in it - but the savings,')
    c.drawCentredString(lx+colw/2, base+64, 'the land and the retirement')
    c.drawCentredString(lx+colw/2, base+52, 'accounts are all on the table.')

    # right: one applies - stacked blocks
    c.setStrokeColor(LINE); c.setFillColor(colors.white); c.setLineWidth(0.8)
    c.roundRect(rx, base-14, colw, top-base+14, 7, fill=1, stroke=1)
    c.setFillColor(colors.HexColor('#1baf7a')); c.setFont('DVB', 11.5)
    c.drawCentredString(rx+colw/2, top-24, 'IF ONLY ONE APPLIES')
    c.setFillColor(INK2); c.setFont('DV', 8.6)
    c.drawCentredString(rx+colw/2, top-38, 'The other is the "community spouse"')

    by = base + 8
    blocks = [
        (S2, 30, 'Savings kept', 'up to $162,660'),
        (S2, 26, 'Income kept', 'up to $4,066.50/mo'),
        (S1, 26, 'One car', 'any value'),
        (S1, 74, 'The homestead', 'ANY value'),
    ]
    for col, bh2, lab, val in blocks:
        c.setFillColor(tint(col, 0.55)); c.setStrokeColor(col); c.setLineWidth(0.8)
        c.roundRect(rx+22, by, colw-44, bh2, 4, fill=1, stroke=1)
        c.setFillColor(NAVY); c.setFont('DVB', 9)
        c.drawString(rx+30, by+bh2-15, lab)
        c.setFillColor(INK); c.setFont('DVB', 10.5)
        c.drawRightString(rx+colw-30, by+bh2-15, val)
        by += bh2 + 6
    c.setDash(3, 3); c.setStrokeColor(S1); c.setLineWidth(1.2)
    c.line(rx+22, by+2, rx+colw-22, by+2); c.setDash()
    c.setFillColor(INK2); c.setFont('DVI', 8)
    c.drawCentredString(rx+colw/2, by+8, 'no ceiling on the home')

    c.setFillColor(NAVY); c.setFont('DVB', 10)
    c.drawCentredString(W/2, base-46, 'Same couple. Same assets. The only difference is how many applications get filed.')
    c.setFillColor(INK2); c.setFont('DV', 8.8)
    c.drawCentredString(W/2, base-62, 'The needier parent applies. The other may apply years later, or never at all.')
    footer(c, 'MEPD Appendix XXXI (rev. June 1, 2026); F-3600; J-2200; J-4400. The $752,000 home equity cap does not apply while a spouse lives there.')

# ---------------------------------------------------------------- page 3
def p3(c):
    page_bg(c); header(c, 'Why it matters that she is their daughter', 'The house can pass to her, penalty-free', 3)
    y = H-118
    y = para(c, 'Texas penalizes almost every transfer made within five years of applying - at $262.37 for each day of ineligibility. There is one exception written for exactly this situation, and it is available to a son or daughter and to nobody else. A niece, a nephew, a friend, a paid aide: none of them can use it.',
             M, y, W-2*M, 9.6, 13)
    y -= 16

    c.setFillColor(tint(S4, 0.10)); c.setStrokeColor(tint(S4, 0.5)); c.setLineWidth(1)
    c.roundRect(M, y-70, W-2*M, 70, 7, fill=1, stroke=1)
    c.setFillColor(S4); c.setFont('DVB', 11)
    c.drawString(M+16, y-22, 'THE CAREGIVER CHILD EXCEPTION')
    para(c, 'A son or daughter who lived in the parent\'s home for at least two years before the parent moved to a nursing facility - and whose care is what kept the parent out of one - may receive the home itself with NO penalty. Not a reduced penalty. None.',
         M+16, y-38, W-2*M-32, 9, 11.5, 'DV', INK)
    y -= 86

    c.setFillColor(NAVY); c.setFont('DVB', 11.5)
    c.drawString(M, y, 'The three things that have to be true')
    y -= 12
    steps = [
        ('1', 'She lives there', 'Two full years, in the home, as her residence. The clock starts the day she moves in - not the day someone thinks to write it down.'),
        ('2', 'Her care is what keeps them home', 'Documented, month by month: what she does, how often, and what would have happened without her. A doctor\'s letter saying the parent would otherwise need facility care is the most valuable page in the file.'),
        ('3', 'A nursing facility admission happens', 'The exception is written around the parent entering a facility. This is the piece most families do not plan for - and it is also the piece that solves a different problem entirely. See below.'),
    ]
    for n, t, b in steps:
        card(c, M, y-62, W-2*M, 62, S4, n, t, b, 10.5, 8.6)
        y -= 70

    y -= 4
    c.setFillColor(tint(S3, 0.16)); c.setStrokeColor(tint(S3, 0.6)); c.setLineWidth(1)
    c.roundRect(M, y-104, W-2*M, 104, 7, fill=1, stroke=1)
    c.setFillColor(colors.HexColor('#8a6000')); c.setFont('DVB', 11)
    c.drawString(M+16, y-22, 'THE TWO PIECES FIT TOGETHER')
    para(c, 'The waiting list for the good Medicaid program is about 15,850 people deep. Families skip it with a planned nursing facility stay of about 30 days followed by a "Money Follows the Person" transition back home. That same admission is the institutionalization event the caregiver child exception needs.',
         M+16, y-38, W-2*M-32, 9.1, 12, 'DV', INK)
    para(c, 'So one hospital discharge, handled correctly, can do both jobs at once: it moves a parent onto the waiver without the wait, and - if the two years are already banked and documented - it opens the door for the house to transfer to their daughter free of penalty. Sequencing this is exactly what the attorney is for.',
         M+16, y-78, W-2*M-32, 9.1, 12, 'DVB', INK)
    footer(c, 'MEPD I-3100 (caregiver child exception); I-5100 (penalty divisor $262.37/day); Money Follows the Person, HHSC.')

# ---------------------------------------------------------------- page 4
def p4(c):
    page_bg(c); header(c, 'What happens when', 'The clocks that are already running', 4)
    y = H-118
    y = para(c, 'Two of these tools only work if time has already passed. That makes this month, not next year, the moment that matters.', M, y, W-2*M, 9.6, 13)
    y -= 14

    lane = M + 26
    top_y = y
    rows = [
        (S1, 'THIS MONTH', 'Elder law attorney engaged. Full asset inventory. Decide trust vs annuity. Record the deed on the homestead. Put both names on the waiting list - it is free and the date holds their place. Sign powers of attorney while both are clearly competent.'),
        (S1, 'MONTHS 1-3', 'Fund the trust. Start the accessibility remodeling. Buy the prepaid funerals. Daughter and her husband move in - and the two-year caregiver clock starts. Begin documenting care from day one.'),
        (S3, 'YEAR 2', 'The caregiver child clock is satisfied. From here, a nursing facility admission can carry the house to her without penalty.'),
        (S4, 'YEAR 5', 'The trust clock is satisfied. Everything in it is now invisible to Medicaid, permanently.'),
        (S2, 'WHEN CARE NEEDS SPIKE', 'The needier parent applies. The annuity absorbs whatever countable savings are left. If a hospital stay happens, ask for a Medicaid nursing facility stay with a Money Follows the Person transition home - that skips the waiting list.'),
        (S2, 'AFTER APPROVAL', 'Consumer Directed Services chosen; daughter and her husband hired as the paid attendants. Because they live in the home, that pay carries no federal income tax.'),
    ]
    rh = 68
    c.setStrokeColor(LINE); c.setLineWidth(2)
    c.line(lane, top_y-12, lane, top_y-len(rows)*rh+6)
    for i, (col, t, b) in enumerate(rows):
        yy = top_y - i*rh
        c.setFillColor(col); c.circle(lane, yy-22, 7.5, fill=1, stroke=0)
        c.setFillColor(SURF); c.circle(lane, yy-22, 3, fill=1, stroke=0)
        c.setFillColor(NAVY); c.setFont('DVB', 10.5)
        c.drawString(lane+20, yy-18, t)
        para(c, b, lane+20, yy-32, W-lane-M-24, 8.7, 11.3, 'DV', INK2)
    y = top_y - len(rows)*rh - 4

    c.setFillColor(tint(S4, 0.12)); c.setStrokeColor(tint(S4, 0.5)); c.setLineWidth(1)
    c.roundRect(M, y-68, W-2*M, 68, 7, fill=1, stroke=1)
    c.setFillColor(S4); c.setFont('DVB', 10.5)
    c.drawString(M+16, y-20, 'The one thing that undoes all of it')
    para(c, 'Do not gift money, add anyone to a deed, or move assets to family outside these structures. Any of it inside five years creates a penalty at $262.37 per day - and unlike everything above, that damage cannot be undone.',
         M+16, y-34, W-2*M-32, 9, 11.5, 'DV', INK)
    footer(c)

# ---------------------------------------------------------------- page 5
def p5(c):
    page_bg(c); header(c, 'What their daughter earns', 'Paid now, and paid tax-free later', 5)
    y = H-118
    y = para(c, 'There are two phases, and the money is real in both. What changes between them is who pays and how it is taxed.',
             M, y, W-2*M, 9.6, 13)
    y -= 14

    colw = (W-2*M-24)/2
    lx, rx = M, M+colw+24
    bh = 250
    for x, ttl, sub, col, rows_ in [
        (lx, 'PHASE 1 - PRIVATE PAY', 'From their parents, starting now', S3, [
            ('Rate', 'Fair market, by written agreement'),
            ('Taxed?', 'Yes - fully taxable to her'),
            ('Who pays', 'Her parents, from savings'),
            ('Hours', 'Whatever the family agrees'),
            ('Why do it', 'It is also the spend-down - money leaves the countable pile and stays in the family'),
            ('Careful', 'Texas credits only hands-on personal care and documented lost wages - not cooking, cleaning or driving'),
        ]),
        (rx, 'PHASE 2 - MEDICAID PAYS', 'Once a parent is approved', S2, [
            ('Rate', '$13.00 to $15.90 per hour'),
            ('Taxed?', 'NO federal income tax, and Texas has none'),
            ('Who pays', 'Medicaid, through a payroll agency'),
            ('Hours', 'What the assessment authorizes'),
            ('Why do it', 'Her pay stops draining the estate entirely'),
            ('Careful', 'She must live in the home for tax-free treatment, and never be named "Designated Representative"'),
        ])]:
        c.setFillColor(tint(col, 0.10)); c.setStrokeColor(tint(col, 0.5)); c.setLineWidth(1)
        c.roundRect(x, y-bh, colw, bh, 7, fill=1, stroke=1)
        c.setFillColor(col); c.roundRect(x, y-bh, colw, 5.5, 2.5, fill=1, stroke=0)
        c.setFillColor(NAVY); c.setFont('DVB', 11)
        c.drawString(x+14, y-22, ttl)
        c.setFillColor(INK2); c.setFont('DV', 8.3)
        c.drawString(x+14, y-34, sub)
        yy = y-52
        for k, v in rows_:
            c.setFillColor(col); c.setFont('DVB', 7.8)
            c.drawString(x+14, yy, k.upper())
            yy = para(c, v, x+14, yy-11, colw-28, 8.6, 10.8, 'DV', INK) - 5
    y -= bh + 16

    c.setFillColor(NAVY); c.setFont('DVB', 11.5)
    c.drawString(M, y, 'What the household can earn once Medicaid is paying')
    y -= 10
    bars = [
        ('Both parents, moderate need - 70 hrs/week', 4550, S2),
        ('Both parents at high need - 120 hrs/week', 8268, S2),
        ('Both parents, very high need - 140 hrs/week', 9646, S2),
    ]
    mx = 10500; bx = M+232; bw = W-M-70-bx
    for lab, val, col in bars:
        y -= 26
        c.setFillColor(INK); c.setFont('DV', 8.6)
        c.drawString(M, y+4, lab)
        c.setFillColor(tint(col, 0.22)); c.rect(bx, y, bw, 13, fill=1, stroke=0)
        c.setFillColor(col); c.roundRect(bx, y, bw*val/mx, 13, 3, fill=1, stroke=0)
        c.setFillColor(NAVY); c.setFont('DVB', 9.5)
        c.drawString(bx+bw*val/mx+6, y+3.5, '${:,}/mo'.format(val))
    y -= 22
    c.setFillColor(INK2); c.setFont('DV', 8.2)
    para(c, 'Gross, before the 7.65% Social Security and Medicare withholding. Hours are whatever the assessment supports, split between her and her husband.', M, y, W-2*M, 8.2, 10.5, 'DV', INK2)
    footer(c, 'HHSC rate schedules effective September 1, 2025; IRS Notice 2014-7; MEPD I-4130, I-4140, I-4160.')

# ---------------------------------------------------------------- page 6
def p6(c):
    page_bg(c); header(c, 'Where to start', 'The next 30 days', 6)
    y = H-118
    y = para(c, 'In order. The first one unlocks the rest - and nothing should be sold, moved, gifted or signed before it.', M, y, W-2*M, 9.6, 13)
    y -= 14
    acts = [
        (S4, '1', 'Hire a Texas elder law attorney', 'Not a general practitioner. Texas NAELA directory at naela.org, or the State Bar referral line at 800-252-9690. Free orientation for anyone 60+: the Legal Hotline for Texans, 800-622-2520, option 3. Bring this packet with you.'),
        (S1, '2', 'Put BOTH parents on the waiting list', 'Call 844-438-5658 or use the "Find Support Services" referral at YourTexasBenefits.com. It costs nothing, commits them to nothing, and the request date holds their place. Do this today - it is the one step with no downside.'),
        (S1, '3', 'Record the deed on the homestead', 'A Lady Bird or Transfer on Death deed moves the house outside probate - which is the only place Texas can recover from - with no waiting period at all. Both owners sign. It must be recorded before death or it is void.'),
        (S2, '4', 'Sign the papers while both are clearly competent', 'Durable power of attorney with express Medicaid-planning powers, medical power of attorney, HIPAA release, directive to physicians. Free Texas forms at TexasLawHelp.org. If capacity slips first, the whole plan gets harder and more expensive.'),
        (S3, '5', 'Move in, and start documenting on day one', 'The two-year caregiver clock starts the day their daughter moves in - but only if it can be proved later. A dated log of care, a doctor\'s letter about what would happen without her, and her pay stubs from the job she is leaving.'),
        (S3, '6', 'Start the remodeling', 'Ramps, a roll-in shower, wider doors, better lighting, a ground-floor bedroom. Unlimited, no waiting period, and it makes her job safer and their lives better from the first week. Keep every invoice.'),
    ]
    ch = 68
    for col, n, t, b in acts:
        card(c, M, y-ch, W-2*M, ch, col, n, t, b, 11, 8.7)
        y -= ch + 8

    y -= 6
    c.setFillColor(NAVY); c.setStrokeColor(NAVY)
    c.roundRect(M, y-82, W-2*M, 82, 7, fill=1, stroke=1)
    c.setFillColor(colors.white); c.setFont('DVB', 11)
    c.drawString(M+16, y-22, 'The sentence to remember at any hospital')
    c.setFillColor(colors.HexColor('#cfe0f2')); c.setFont('DVBI', 10.5)
    para(c, '"We want a Medicaid nursing facility stay with a Money Follows the Person transition home."',
         M+16, y-40, W-2*M-32, 10.5, 13, 'DVBI', colors.HexColor('#cfe0f2'))
    para(c, 'Said to the discharge planner at the right moment, it can save a year of waiting - and it is the same event the caregiver child exception needs.',
         M+16, y-62, W-2*M-32, 8.4, 11, 'DV', colors.HexColor('#9fb8d0'))
    footer(c)

def build(out):
    c = cv.Canvas(out, pagesize=letter)
    c.setTitle('How This Works')
    for fn in (p1, p2, p3, p4, p5, p6):
        fn(c); c.showPage()
    c.save(); print('ok')

build(sys.argv[1])
