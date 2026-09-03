# -*- coding: utf-8 -*-
import sys
from reportlab.lib.units import inch
from reportlab.platypus import Spacer, PageBreak
from render import *

W = [0.26*inch, 2.35*inch, 4.29*inch]

def page(title, sub, rows, box_title, box):
    f = [P(title, 'h1'), P(sub, 'small'), Spacer(1,1),
         table(['', 'Do this', 'How / who to call / what to say'], [['☐', a, b] for a, b in rows], W, font='tight'),
         Spacer(1,4), callout(box, 'money', box_title)]
    return f

AU = [
 ('Get on the STAR+PLUS HCBS interest list (do this first).',
  'YourTexasBenefits.com, "Find Support Services" referral, AND call <b>844-438-5658</b>. Say: "Add [name] to the STAR+PLUS HCBS interest list; give me the request date." Write that date down.'),
 ('Open a Community Care intake and ask for CAS with CDS.',
  'Call <b>2-1-1, option 2</b> (or 877-541-7905). Say: "I want to apply for Community Attendant Services and be assessed for all Community Care programs. Open a Form 2110 intake. We want the Consumer Directed Services option."'),
 ('File the Medicaid application.',
  'Form <b>H1200</b> at YourTexasBenefits.com. Check the Medicare Savings Program box too (it pays your $202.90 Part B premium). Ask for a Form H1800 receipt.'),
 ('See your doctor this week.',
  'Ask them to complete <b>Form 3052</b> (Practitioner\'s Statement of Medical Need) and to chart every thing you need help with: bathing, dressing, toileting, transfers, walking, eating, medications, memory.'),
 ('Write a 7-day diary before the assessment.',
  'Every task, how long, how often, on your <b>worst</b> days, not your best. This is what sets your paid hours.'),
 ('Get countable money under the limit.',
  '$2,000 alone / $3,000 as a couple, on the 1st of the month. Home, one car, household goods and a prepaid funeral do not count. <b>Never gift money or add anyone to the deed.</b>'),
 ('If your income is over $2,982/month, set up a Miller trust.',
  'Free advice: Legal Hotline for Texans <b>800-622-2520, option 3</b>. Attorney cost is about $400-$500. HHSC has a model trust (MEPD Appendix XXXVI).'),
 ('Sign your legal papers while you are clearly competent.',
  'Durable Power of Attorney, Medical Power of Attorney, HIPAA release, Directive to Physicians, and a <b>Transfer on Death Deed</b> for the house. Free forms at TexasLawHelp.org. Record the deed with the county clerk.'),
 ('At the caseworker visit: answer for the worst days.',
  'They score you on <b>Form H2060</b>. Say clearly: "My daughter is not available to do this for free; she is being hired as the paid attendant." Do not let tasks be marked "C".'),
 ('Choose Consumer Directed Services and pick an FMSA.',
  'Sign <b>Form 1584</b>. You are the employer; the FMSA does payroll. <b>Do not name your daughter or her husband as Designated Representative</b> or they can never be paid.'),
 ('Set the wage as high as the budget allows.',
  'Ask the FMSA for the budget worksheet and set the hourly wage on <b>Form 1730</b> at the ceiling (about $15.05 now, $15.90 on the waiver).'),
 ('If either of you is a veteran, start that claim now.',
  'Texas Veterans Commission, free, <b>800-252-8387</b>. Ask for "Pension with Aid and Attendance."'),
 ('Answer every HHSC letter and call within 30 days.',
  'Most people who lose their place on the interest list lose it for not answering. Report any change to HHSC within 10 days.'),
]

CO = [
 ('Time your resignation. This one has a deadline.',
  'If you are quitting a job to do this, you must leave it within <b>30 days before or after</b> the CAS application date (CCSE 2433.2). Keep the separation letter. Otherwise HHSC can treat you as free help and cut the paid hours.'),
 ('Get authority to speak for them, but not the DR role.',
  'Have each of them sign HHSC <b>Form H1003</b> (authorized representative) plus a HIPAA release. <b>Never sign Form 1720 as Designated Representative</b> - a DR and the DR\'s spouse can never be paid.'),
 ('Make the calls in the aunt and uncle checklist today.',
  'Interest list <b>844-438-5658</b>; Community Care intake <b>2-1-1 option 2</b>; H1200 online for each of them. Log every call: date, name, reference number.'),
 ('Put your status in writing to the caseworker.',
  '"I am relocating to be hired as the paid CDS attendant. I am not available to provide unpaid care." Keep a copy for the assessment.'),
 ('Make the house your real home.',
  'Driver\'s license, voter registration, mail. This is what makes your pay federal-income-tax-free under IRS Notice 2014-7. Keeping a separate residence kills the exclusion.'),
 ('Pay no rent. Take no cash.',
  'Rent is countable income to them. Sign an expense-sharing agreement instead and pay your share of utilities and groceries <b>straight to the vendors</b>. No joint accounts with them, ever.'),
 ('Be the informant at both assessments.',
  'Bring the 7-day diaries, medication lists and doctor letters. Give minutes and frequency for each task. Ask for protective supervision hours if there is any memory loss.'),
 ('Complete the FMSA hiring packet for BOTH employers.',
  'Forms 1724, 1725, 1734, 1728, 1730, 1731, 1732, 1737, plus I-9 and W-4. Two separate files, one for the aunt, one for the uncle. <b>Do not work a single hour before Form 1729 comes back signed.</b>'),
 ('Negotiate the wage to the ceiling, then fill the rest with benefits.',
  'About $15.05/hr under CAS, $15.90 under the waiver. Put whatever is left into paid leave, a longevity bonus or a health stipend - unused budget is forfeited.'),
 ('Ask the FMSA three questions in writing.',
  '(1) Do you apply IRS Notice 2014-7 for live-in caregivers? (2) Do you apply it to CAS pay or only waiver pay? (3) How do you treat my combined hours across two employers for overtime?'),
 ('Install the EVV app and clock every single shift.',
  'HHAeXchange, support <b>833-430-1307</b>. Clock in and out separately for each person, never overlapping. A missed clock-in not fixed within <b>95 days</b> is pay you never get back.'),
 ('Register as the family caregiver for free help.',
  'Area Agency on Aging <b>800-252-9240</b>: caregiver training, respite vouchers, support groups. Alzheimer\'s helpline <b>800-272-3900</b>, 24/7.'),
 ('Appeal anything low, every time.',
  '90 days for CAS (before the effective date to keep hours); 60 days to the plan on STAR+PLUS, with continuation within 10 days. Stuck plan? Ombudsman <b>866-566-8989</b>.'),
]

HU = [
 ('Get hired as the second attendant.',
  'Same FMSA packet as your wife (Forms 1724, 1725, 1734, 1728, 1730, 1731, 1732, 1737, I-9, W-4). Nothing bars a daughter\'s husband. Add your license and auto insurance if you will drive them.'),
 ('Take the other spouse.',
  'Cleanest split: your wife is the main attendant for one, you for the other, and each of you picks up the other\'s remaining hours. This uses every authorized hour and avoids overtime eating the budget.'),
 ('Be the named backup on Form 1740.',
  'CDS requires a written backup plan. You back her up, she backs you up. That covers sick days without losing hours.'),
 ('Do not be the Designated Representative.',
  'While your wife is paid, you cannot be DR - and if you were DR, she could not be paid. Let the aunt and uncle be each other\'s DR, or use a relative who lives elsewhere.'),
 ('Know the two things you cannot be paid for.',
  'You cannot be the paid <b>respite</b> worker on the waiver (the provider must not live in the home), and you cannot be the AAA voucher respite worker. Recruit an outside person for those.'),
 ('Own the VA file if either of them served.',
  'Texas Veterans Commission <b>800-252-8387</b> (free). File <b>VA Form 21-0966</b> intent to file today to lock the back-pay date, then 21-2680 (doctor) and 21P-527EZ.'),
 ('Keep the ledger that protects the money.',
  'Every VA Aid and Attendance dollar, what it bought, with receipts. Unspent A&amp;A gets converted into hours and subtracted from their Medicaid authorization (CCSE 2531).'),
 ('Run home safety and equipment.',
  'CDC STEADI home checklist; ask the doctor for equipment orders; grab bars, ramps and bathroom work are covered up to $7,500 per person on the waiver. Never buy first - there is no reimbursement.'),
 ('Run logistics.',
  'Rides to appointments through the plan or <b>877-633-8747</b> (book 2 workdays ahead); you can be reimbursed mileage for driving them. Pharmacy, adult day care, respite scheduling.'),
 ('Keep the deadline calendar.',
  'Every notice, its appeal deadline, and the annual renewals. Photograph each letter the day it arrives.'),
 ('Watch her for burnout and schedule the breaks.',
  '30 respite days per person per year on the waiver, AAA vouchers, adult day care. Caregiver Action Network <b>855-227-3640</b>; 988 any hour.'),
 ('Think hard before you drop all outside income.',
  'Tax-free caregiver pay is not counted for marketplace health subsidies, and Texas has no Medicaid expansion. Some taxable income in the household keeps you eligible for coverage.'),
]

doc = Doc(sys.argv[1], 'Getting Started Checklists')
s = []
s += page('Checklist 1: The Aunt', 'Your case is separate from your husband\'s. Do all of this for yourself; he does the same for himself. Start today.', AU,
    'Your numbers', 'Income limit <b>$2,982/month</b> each. Countable savings <b>$2,000</b> alone or <b>$3,000</b> as a couple. Your home, one car and a prepaid funeral do not count. Decision due in <b>45 days</b>; caseworker visit within <b>14 days</b>.')
s += [PageBreak()]
s += page('Checklist 2: The Uncle', 'Same list, your own case. Two separate applications, two assessments, two sets of paid hours. Do not let anyone merge them.', AU,
    'Your numbers', 'Income limit <b>$2,982/month</b> each. Countable savings <b>$2,000</b> alone or <b>$3,000</b> as a couple. Veteran? Call <b>800-252-8387</b> this week - Aid and Attendance can add up to <b>$2,874/month</b> and Medicaid does not count it as income.')
s += [PageBreak()]
s += page('Checklist 3: The Daughter', 'You are the organizer now and the paid attendant later. Two rules decide whether you get paid at all: never be the Designated Representative, and time your job resignation.', CO,
    'What you can earn', 'CDS wage ceiling about <b>$15.05/hour</b> under CAS, <b>$15.90</b> under STAR+PLUS HCBS. Working both employers, that is roughly <b>$4,500 to $9,600 a month</b> for you and your husband together, and it is federal-income-tax-free if you live in the home.')
s += [PageBreak()]
s += page('Checklist 4: The Husband', 'You are the second paid attendant, the required backup, the VA claim, and the record keeper. The paperwork you keep is what protects everyone\'s hours.', HU,
    'Your numbers', 'You can be paid as an attendant for either spouse at the same rates. You cannot be paid for waiver respite while living in the home, and you cannot be the Designated Representative while your wife is paid.')
s += [PageBreak(), P('How high can the pay go?', 'h1'),
  P('The wage ceiling is set by the state rate minus employer payroll taxes. The hours are set by each person\'s Form H2060 assessment. Both spouses qualifying is what doubles the ceiling.', 'body'),
  table(['Stage', 'Household hours/week', 'Wage', 'Gross per month'], [
   ['CAS, one spouse only, moderate need', '35', '$15.05', '$2,283'],
   ['CAS, both spouses, moderate need', '70', '$15.05', '$4,565'],
   ['<b>CAS, both spouses at the 50-hour cap</b>', '100', '$15.05', '<b>$6,522</b>'],
   ['STAR+PLUS HCBS, both spouses, high need', '120', '$15.90', '$8,268'],
   ['<b>STAR+PLUS HCBS, both, very high need</b>', '140', '$15.90', '<b>$9,646</b>'],
   ['HCBS, near-continuous care (12 hrs/day each caregiver)', '168', '$15.90', '$11,575'],
  ], [2.7*inch, 1.3*inch, 0.9*inch, 2.0*inch]),
  Spacer(1,6),
  callout('<b>Realistic maximum from Medicaid alone: about $9,600 a month gross</b>, when both spouses are on STAR+PLUS HCBS with high assessed need and the two of you split the hours. '
   'The <b>$11,575</b> row is the practical outer edge: two people each working about 12 hours a day, every day, which needs the live-in overtime exemption confirmed by the FMSA in writing. '
   'On top of that, a married wartime veteran can add <b>up to $2,874/month</b> in VA Aid and Attendance (paid to him, spent on care), and if he is 70%+ service-connected the VA caregiver stipend pays the cousin '
   '<b>$3,034 to $3,499/month</b> directly - though the VA bars paying for care another program already covers, so get that in writing first. '
   'The legal ceiling behind all of it is 202% of what a nursing home would cost for that person; at typical Texas rates that is well above any of these rows, so <b>assessed need, not the cap, is what limits the money</b>.', 'money', 'The honest answer'),
  Spacer(1,4),
  P('Hours shown are what the assessment must support. Gross pay is before the 7.65% Social Security and Medicare withholding; there is no federal income tax on it if the caregivers live in the home (IRS Notice 2014-7) and no Texas income tax. Rates effective September 1, 2025; figures checked September 3, 2026.', 'small')]
doc._firstPageTemplateIndex = 1
doc.multiBuild(s)
print('ok')
