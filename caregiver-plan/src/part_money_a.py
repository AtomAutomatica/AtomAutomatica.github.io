# -*- coding: utf-8 -*-
"""Section 6 part A: eligibility numbers, spend-down, QIT, staging, protecting the home, Medicare savings."""
from reportlab.lib.units import inch
from reportlab.platypus import Spacer, PageBreak
from render import *

def money_a():
    return [
        PageBreak(), H1('6. Money: getting eligible, protecting the home, and how much the caregivers earn'),
        H2('6.1 The 2026 numbers that decide eligibility (MEPD Handbook Appendix XXXI; CMS bulletin April 27, 2026)'),
        table(['Test', 'One spouse applying', 'Both spouses applying', 'Notes'], [
            ['Monthly income cap (300% of SSI)', '<b>$2,982</b>', '<b>$5,964</b> combined', 'Gross income before deductions. Over the cap? A Qualified Income Trust fixes it. VA Aid and Attendance is not counted (MEPD G-4100, E-4300).'],
            ['Countable resources', '<b>$2,000</b>', '<b>$3,000</b>', 'Tested on the first day of each month. Both spouses\' assets count even if one applies.'],
            ['Home', 'Exempt as principal residence', 'Exempt', '2026 equity cap $752,000, and the cap does not apply while a spouse lives there (F-3600).'],
            ['Vehicle', 'One, any value', 'One, any value', 'F-4221'],
            ['Life insurance', 'Face value up to $1,500 per person exempt', 'Same', 'Over $1,500 face: the whole cash value counts. Term insurance is fine.'],
            ['Burial', 'Irrevocable prepaid funeral: exempt, any value; $1,500 designated burial fund; burial plots exempt', 'Same', 'The cleanest spend-down item.'],
            ['Spousal protection when only ONE spouse is on the program', 'Community spouse keeps <b>$32,532 to $162,660</b> in resources (SPRA) and an income allowance up to <b>$4,066.50</b>/month', 'Not available: with both on the program there is no community spouse (J-1300)', 'This is why application timing matters; see 6.2.'],
            ['Look-back', '60 months', '60 months', 'Gifts are penalized at <b>$262.37 per day</b> of ineligibility (I-5100). A $20,000 gift = 76 days.'],
            ['Family Care (Title XX) backup resource limit', '$5,000', '$6,000', 'Same income limits; regional interest list.'],
            ['SSI level (opens CFC immediately)', '$994', '$1,491', 'If income is this low, apply for SSI first.'],
        ], [1.55 * inch, 1.7 * inch, 1.55 * inch, 2.1 * inch]),
        H2('6.2 Getting under the limits without losing anything'),
        bullets([
            '<b>Take a snapshot first.</b> Every account, policy, title, deed, award letter, and any gift in the last 60 months. Nothing moves until you know the numbers.',
            '<b>Income over $2,982?</b> A Qualified Income Trust (Miller trust) is routine in Texas: irrevocable, income only, Texas named as residuary beneficiary, deposit in the month received. HHSC publishes a model trust (MEPD Appendix XXXVI). Elder-law attorneys typically charge about $400 to $500. The husband can be the trustee. It can be made effective up to 3 months before the application date.',
            '<b>Resources over $3,000?</b> Spend down on exempt things that help the care: irrevocable prepaid funerals for both, home repairs and accessibility work, a reliable vehicle, a hospital bed or lift Medicare will not cover, paying off debt. <b>Never</b> gift cash or add the cousin to the deed.',
            '<b>Ask an elder-law attorney about staging.</b> If the couple holds more than $3,000 but less than roughly $165,000 in countable assets, applying for the <b>needier spouse first</b> makes the other a "community spouse" who may keep up to $162,660 (SPRA) instead of spending down to $3,000. Whether and when to add the second spouse is a planning decision; get it in writing. Free advice: Legal Hotline for Texans <b>800-622-2520, option 3</b> (age 60+). Referral to a paid attorney: State Bar <b>800-252-9690</b>; Texas NAELA directory at naela.org.',
            '<b>The cousin\'s and husband\'s money does not count.</b> Texas deems income only spouse-to-spouse and parent-to-minor (MEPD E-7100), and waiver budgets ignore in-kind support (O-1000). But <b>rent paid to the aunt and uncle IS countable income</b> to them (E-3000). So: no rent. Sign a written expense-sharing agreement and have the cousin\'s household pay its share of utilities, groceries and repairs <b>directly to the vendors</b>. No joint accounts with the aunt and uncle, ever.',
            '<b>Any private pay to the cousin before Medicaid starts</b> must be under a written, prospective Personal Care Agreement at a fair hourly wage for genuine personal care (bathing, toileting, transfers), paid by check, with daily logs. Texas treats payment for "chores a family member would normally do" (cleaning, laundry, meals, shopping, driving) as a gift even with a contract (MEPD I-4100).',
        ]),
        H2('6.3 Protecting the house from Medicaid Estate Recovery (MERP)'),
        P('Texas recovers the cost of STAR+PLUS long-term care and CAS received at age 55+ from the <b>probate estate</b> after death (1 TAC Chapter 373; HHSC "Your Guide to MERP"). No claim is filed while a spouse survives. The cousin, as a niece, gets <b>no</b> caregiver-child exemption. These are the tools that work:'),
        table(['Tool', 'What it does', 'How'], [
            ['<b>Transfer on Death Deed</b> (Tex. Est. Code ch. 114) or Lady Bird deed', 'Passes the home outside probate, so MERP has nothing to claim against. Not a penalized transfer during life (MEPD I-3100). Revocable.', 'Free statutory form and instructions at TexasLawHelp.org; record it with the county clerk (about $30). Do it this week while both are competent.'],
            ['<b>Care-cost deduction</b> (1 TAC 373.213)', 'MERP\'s claim is reduced by documented costs of care that kept the person out of a nursing home, plus taxes, insurance, utilities and repairs paid by heirs. No dollar cap.', 'Keep a receipts binder from day one. File within 60 days of the Form 8001 notice.'],
            ['<b>Undue hardship waiver</b> (1 TAC 373.209; Form 5006)', 'No recovery if the homestead is appraised under $100,000 and heirs\' income is below 300% of poverty (about $47,880 single / $64,920 couple in 2026), or recovery would push heirs onto public assistance.', 'Request within 60 days of Form 8001; decided in 40 days.'],
            ['Automatic exemptions', 'No claim if estate is $10,000 or less, Medicaid cost is $3,000 or less, or a surviving spouse or disabled child exists.', 'MERP contractor <b>800-641-9356</b>; merp@hhs.texas.gov'],
        ], [1.7 * inch, 2.8 * inch, 2.4 * inch]),
        H2('6.4 Money the couple gets back the day Medicaid says yes'),
        table(['Benefit', '2026 limits', 'Worth'], [
            ['Medicare Savings Program (QMB) on the same Form H1200', 'Income $1,330 single / $1,804 couple; resources $9,950 / $14,910 (MEPD Q-2500, Q-1300)', 'Pays the <b>$202.90/month Part B premium</b> for each spouse ($4,869.60 a year for the couple) and all Medicare copays and deductibles. SLMB and QI-1 pay the premium at higher incomes (up to $2,435 couple).'],
            ['Part D Extra Help', 'Automatic with Medicaid or MSP; otherwise income $23,940 / $32,460', '$0 plan premium and deductible; copays no more than $5.10 generic / $12.65 brand'],
            ['Full Medicaid (STAR+PLUS)', 'When HCBS starts', 'Covers what Medicare does not; STAR+PLUS HCBS adds dental, home mods, adaptive aids, respite'],
            ['Over-65 homestead exemption and tax ceiling', 'Any income', 'Check the county appraisal district has the over-65 exemption and school-tax ceiling on file; Tax Code 33.06 also allows deferral of property taxes entirely.'],
        ], [1.9 * inch, 2.3 * inch, 2.7 * inch]),
        callout('Apply for BOTH spouses. Each one who qualifies is a separate assessment and a separate set of paid hours. Under CAS that is up to 100 hours a week for the household; under STAR+PLUS HCBS there is no weekly cap at all. Getting the second spouse eligible is the single biggest pay lever in this plan.', 'money', 'The biggest lever'),
    ]
