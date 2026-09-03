# -*- coding: utf-8 -*-
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('DV', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('DV', normal='DV', bold='DVB', italic='DV', boldItalic='DVB')
H1 = ParagraphStyle('h1', fontName='DVB', fontSize=15, leading=19, spaceBefore=14, spaceAfter=6)
H2 = ParagraphStyle('h2', fontName='DVB', fontSize=11.5, leading=15, spaceBefore=12, spaceAfter=4)
B  = ParagraphStyle('b', fontName='DV', fontSize=10.2, leading=14.5, spaceAfter=6)
LI = ParagraphStyle('li', parent=B, leftIndent=16, bulletIndent=4, spaceAfter=3)
S=[]
def h1(t): S.append(Paragraph(t,H1))
def h2(t): S.append(Paragraph(t,H2))
def p(t): S.append(Paragraph(t,B))
def li(items):
    for i in items: S.append(Paragraph(i, LI, bulletText='-'))

h1('Getting the Daughter paid to care for Mom and Dad, without giving away what they own')
p('Texas. Written September 2026. Plain language. Not legal advice; an elder law attorney is part of this plan.')

h2('Who is who')
li(['<b>Mom and Dad.</b> Married. Both elderly. They own the house, other property and retirement savings. Everything is 50/50 between them. They have done no wills, trusts or deeds.',
    '<b>The Daughter.</b> Their daughter. She is moving in to take care of them and wants to be paid for it.',
    '<b>The Son-in-law.</b> The Daughter\'s husband. Also moving in. He can be paid too.',
    'Nobody is a veteran, so nothing here involves the VA.'])

h1('1. Read this first: Medicaid gets paid back from the estate')
p('If Medicaid ever pays for Mom\'s or Dad\'s care, including paying the Daughter to give that care, Texas keeps a running tab of every dollar spent after age 55. Nothing is collected while either of them is alive. After the second one dies, the state sends the family a bill and collects it from whatever goes through probate.')
p('Only from probate. A house that passes by a recorded Lady Bird deed or Transfer on Death deed does not go through probate. Accounts with a named beneficiary do not go through probate. Life insurance does not. None of that can be touched.')
p('So Medicaid is a loan. If the estate is left the way it is now (no deeds, no beneficiaries), the state takes the tab out of the estate later. If the house and accounts are set up to pass outside probate, there is little for the state to collect. Same Medicaid, same tab, very different ending. This is the reason the deed in Section 7 matters more than anything else in this document.')

h1('2. Who can pay the Daughter')
p('There are exactly two sources of money for a family caregiver in Texas:')
li(['<b>Mom and Dad themselves</b>, out of their own money. Available today.',
    '<b>Medicaid</b>. Available only after Mom or Dad qualifies, which means their countable money has to be low.'])
p('There is no third option. No Texas or federal program pays a daughter to care for her parents while the parents keep substantial assets.')

h1('3. What Medicaid counts, with things exactly as they are')
p('<b>Does not count:</b> the house, at any value, as long as Mom or Dad lives in it. One car, at any value. Furniture and belongings. Prepaid funerals.')
p('<b>Counts:</b> the other property. The retirement accounts. Bank accounts, CDs, stocks. Cash value of life insurance.')
p('The 50/50 split changes nothing. Texas adds up everything either of them owns, no matter whose name is on it.')

h1('4. The rule for a married couple: only one of them applies')
p('Whoever needs care more applies. The other one does not. The one who does NOT apply keeps:')
li(['The house.', 'One car.', 'Half of the countable money. At least $32,532. At most $162,660.', 'Income of up to $4,066.50 a month.'])
p('The one who applies has to be down to $2,000 of countable money.')
p('If both of them apply, every one of those protections disappears and the two of them together may keep $3,000. That is why they never both apply at the same time.')

h1('5. So can Medicaid pay the Daughter today?')
p('Only if Mom and Dad\'s countable money (not the house, not one car) is under about $34,500 in total. Above that, the applying parent\'s half has to be spent or converted first. If Mom and Dad have real money, the honest answer is: not today.')

h1('6. Where the applying parent\'s half can go without a penalty')
p('"Spending down" does not mean throwing money away. It means moving it into things Medicaid does not count:')
li(['Fixing the house for their care: ramps, a walk-in shower, a downstairs bedroom, better lighting. No dollar limit and no waiting period.',
    'Paying off the mortgage. Replacing the car. Prepaying both funerals.',
    'Putting land on the market. While it is genuinely listed for sale, it does not count.',
    'Paying the Daughter under a written agreement (Section 8).',
    'Buying a special annuity that pays the non-applying parent a monthly income. Attorney only; done wrong, the whole purchase is penalized.',
    'Putting money in an irrevocable trust. It works, but only five years after the trust is funded.'])
p('<b>What is not allowed:</b> giving money or property to the Daughter, the Son-in-law, or anyone else. Texas looks back five years and charges a penalty of $262.37 per day of lost coverage for every gift.')

h1('7. The plan that fits this family')
h2('Now')
li(['<b>Mom and Dad pay the Daughter and the Son-in-law themselves.</b> A live-in caregiver in Texas costs $3,300 to $5,000 a month. It is taxable income to her. If a doctor writes a plan of care, Mom and Dad can deduct it as a medical expense.',
    '<b>Record a Lady Bird deed or Transfer on Death deed on the house.</b> The house then passes to whoever they choose (for example the Daughter) outside probate. About $30 to record. No penalty, no waiting. This one step keeps the biggest asset away from Medicaid recovery.',
    '<b>Name beneficiaries on the retirement and bank accounts.</b> Also outside probate.',
    '<b>Sign powers of attorney and medical powers of attorney</b> while both are clear-headed.',
    '<b>The Daughter starts a dated log of the care she gives</b> and gets a letter from their doctor saying they would need a nursing home without her. Section 9 explains why.'])
h2('Later, if care gets heavy')
li(['One parent applies for Medicaid. Half the countable money is protected for the other.',
    'Medicaid then pays the Daughter directly. Because she lives in the house, that pay has no federal income tax, and Texas has no income tax.',
    'The tab starts. It is repaid from probate after both have died, and by then probate is small because of the deed and the beneficiaries.'])

h1('8. Paying the Daughter the right way')
li(['A written agreement, signed before the work starts. Hourly pay, paid by check, with a daily log.',
    'Texas counts it as real pay only for hands-on care (bathing, dressing, toileting, moving them, medications) and for the wages she gave up by leaving her job. It does not count cooking, cleaning, shopping or driving.',
    'No lump sums up front. Texas does not recognize them.',
    'Mom and Dad become household employers: a W-2 for the Daughter, Social Security and Medicare tax withheld.',
    'Have the elder law attorney draft it.'])

h1('9. Why the Daughter\'s two-year log matters')
p('Texas has a rule written for exactly this situation. A son or daughter who lived in the parent\'s home for two years, and whose care kept the parent out of a nursing home, can be given the house with no penalty when the parent does go to a nursing home. Only a child can use it. It needs proof: the two years, the dated log, the doctor\'s letter. The clock starts on move-in day.')

h1('10. What the Daughter earns')
li(['<b>While Mom and Dad pay:</b> whatever they agree. $3,300 to $5,000 a month is the market. Taxable.',
    '<b>Once one parent is on Medicaid:</b> about $13 to $15.90 an hour, no federal income tax. Hours are set by a nurse\'s assessment; 40 to 50 hours a week for one parent is a realistic range, which is roughly $2,300 to $3,400 a month for that parent\'s care. The Son-in-law can be paid for hours she does not cover.',
    'The second parent goes on Medicaid only after the first has died or the countable money is gone. Until then the second parent\'s care is private pay.'])

h1('11. The first five calls')
li(['<b>An elder law attorney.</b> State Bar referral 800-252-9690. Directory at naela.org. Free advice line for anyone 60+: 800-622-2520, option 3.',
    '<b>844-438-5658.</b> Put both Mom and Dad on the STAR+PLUS HCBS waiting list. Free. Commits them to nothing. Holds their place.',
    '<b>The county clerk</b>, to record the deed once the attorney drafts it.',
    '<b>Their doctor</b>, for the plan of care letter and the "would need a nursing home without her" letter.',
    '<b>Area Agency on Aging, 800-252-9240.</b> Free caregiver training for the Daughter, and respite money to pay an outside helper so she can rest.'])

h1('12. What we do not know yet, and what changes the answer')
li(['<b>How much countable money there is.</b> Under about $34,500: Medicaid can pay the Daughter now. Over: Mom and Dad pay first.',
    '<b>Whether any of the land is a working farm or ranch business.</b> A real business is excluded from the count regardless of value.',
    '<b>Whether they have a long-term care insurance policy.</b> Many pay family caregivers and none care about assets.',
    '<b>How much care they need today.</b> That sets the Medicaid hours later.'])

doc = SimpleDocTemplate(sys.argv[1], pagesize=letter, leftMargin=0.9*inch, rightMargin=0.9*inch, topMargin=0.8*inch, bottomMargin=0.8*inch, title='Getting the Daughter paid')
doc.build(S); print('ok')
