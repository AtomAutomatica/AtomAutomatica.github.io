# -*- coding: utf-8 -*-
"""Section 6 part B: rates, budget math, income model, taxes, VA."""
from reportlab.lib.units import inch
from reportlab.platypus import Spacer, PageBreak
from render import *

def money_b():
    return [
        H2('6.5 What Texas pays per hour, and how much reaches the caregiver'),
        P('Since September 1, 2025 (Senate Bill 1, Rider 23, 89th Legislature) HHSC rates assume an average attendant wage of $13.00 an hour plus 14% payroll costs. '
          'Under the agency option the agency keeps the difference. Under CDS the aunt and uncle receive the whole CDS rate into a budget the FMSA administers, the FMSA is paid its fee '
          'separately ($120.55/month for CAS, $210.08/month for STAR+PLUS HCBS), and the employer sets the wage. HHSC\'s own budget workbook requires at least 66.36% of the budget to go to employee compensation; in practice about 92% can.'),
        table(['Program and service', 'CDS rate into the budget', 'Agency rate (for comparison)', 'Wage ceiling after employer taxes*'], [
            ['CAS / PHC / Family Care attendant, non-priority', '<b>$16.33/hour</b>', '$17.13', 'about <b>$15.05</b>'],
            ['CAS / PHC / Family Care attendant, priority (42-hour cap)', '$16.51/hour', '$17.31', 'about $15.20'],
            ['STAR+PLUS HCBS attendant (PAS), incl. protective supervision', '<b>$17.24/hour</b> ($4.31 per 15 min)', '$17.60', 'about <b>$15.90</b>'],
            ['STAR+PLUS HCBS in-home respite (outside provider only)', '$16.56/hour', '$17.56', 'about $15.25'],
            ['CFC attendant / CFC habilitation (only if SSI-level Medicaid)', '$17.04 / $17.68', '$17.84', 'about $15.70 / $16.30'],
            ['Support consultation (coach for the employer, from the budget)', '$26.52/hour', '', 'use briefly, if at all'],
        ], [2.4 * inch, 1.6 * inch, 1.3 * inch, 1.6 * inch]),
        P('*Ceiling assumes nothing reserved for benefits or bonuses; employer FICA 7.65%, FUTA 0.6% on the first $7,000, Texas unemployment 2.7% on the first $9,000. Source: HHSC PHC CDS budget workbook (rev. 9/1/2025) and PFD rate sheets effective 9/1/2025. The former $10.60 base-wage rule ended August 31, 2025.', 'small'),
        H2('6.6 The income model: low, typical, high'),
        P('Assumptions: both spouses qualify; the cousin and husband are each hired by both employers; hours are split so no one exceeds 40 hours for a single employer; wage set at $15.00 (CAS) or $15.50 (HCBS). Gross pay is before the 7.65% Social Security and Medicare withholding. Multiply weekly hours by 52 and divide by 12 for the monthly figure.'),
        table(['Scenario', 'Hours / week', 'Wage', 'Gross per month', 'Who is paid'], [
            ['<b>Floor:</b> only one spouse qualifies for CAS at 30 hours', '30', '$15.00', '<b>$1,950</b>', 'Cousin alone'],
            ['<b>Bridge (CAS), both spouses, moderate needs</b> (35 + 35)', '70', '$15.00', '<b>$4,550</b>', 'Cousin 40, husband 30'],
            ['<b>Bridge (CAS), both at the 50-hour cap</b>', '100', '$15.00', '<b>$6,500</b>', 'Cousin 50, husband 50 (40 + 10 each)'],
            ['<b>Destination (STAR+PLUS HCBS), both, H2060 supports 50 each</b>', '100', '$15.50', '<b>$6,717</b>', 'Same split'],
            ['<b>Destination, high need</b> (60 + 60 incl. protective supervision for dementia)', '120', '$15.50', '<b>$8,060</b>', 'Cousin 60, husband 60 (40 + 20 each)'],
            ['<b>Destination, very high need</b> (70 + 70; inside the 202% cost ceiling)', '140', '$15.50', '<b>$9,403</b>', 'Same, or a third part-time attendant'],
        ], [2.6 * inch, 0.95 * inch, 0.6 * inch, 1.2 * inch, 1.55 * inch]),
        P('What the Texas rules actually authorize is driven by the Form H2060 minutes, so the "typical" row is the one to plan a budget around until the assessments are done. '
          'Honest ranges for a 65+ adult needing help with 3 to 5 activities of daily living run 25 to 50 hours a week; dementia with protective supervision can push HCBS hours well above that. Every hospitalization or decline is a reassessment trigger.', 'body'),
        table(['Add-on', 'Monthly value', 'Notes'], [
            ['Federal income tax saved by IRS Notice 2014-7 (live-in) on a $6,500/month household', 'about $400 to $500', 'See 6.7. Texas has no income tax. Social Security and Medicare tax still withheld.'],
            ['Earned Income Tax Credit if the couple elects to count excluded wages (Feigh election)', 'up to $8,231/year with 3+ children; $664 with none', 'Refundable; all-or-nothing election; 2026 figures (Rev. Proc. 2025-32)'],
            ['STAR+PLUS HCBS extras paid to vendors, not the family, but replacing household costs', 'ERS $37.61; meals; up to $10,000/yr aids; $7,500 home mods; $5,000/yr dental per spouse', 'Section 8.2'],
            ['QMB paying both Part B premiums', '$405.80', 'Plus deductibles and copays'],
            ['VA Pension with Aid and Attendance, married wartime veteran (paid to the veteran)', 'up to $2,874', 'Section 6.8; must be spent on care or it offsets CAS hours'],
            ['VA caregiver stipend (PCAFC) if the veteran is 70%+ service-connected (paid to the cousin)', '$3,034 to $3,499 (Level 2) or $1,896 to $2,187 (Level 1)', 'Section 6.8; overlap with Medicaid hours must be cleared with the VA'],
            ['AAA Lifespan Respite voucher', 'about $300/quarter guideline, often $800 to $1,000 per award', 'Paid to an outside respite provider'],
            ['SNAP for the couple (elderly simplified application), CEAP utility help, Lifeline phone', 'SNAP up to $546 for two; CEAP $400 to $1,200/yr; Lifeline $9.25 to $12.75/mo', 'Section 6.4; the cousin\'s wages count for the cousin\'s own SNAP household, not the couple\'s'],
        ], [2.6 * inch, 1.9 * inch, 2.4 * inch]),
        callout('The pay does not come from the aunt and uncle. It comes from Medicaid through the FMSA, so it never counts as a gift, never triggers a transfer penalty, and never touches their eligibility. '
                'Any money the couple pays the cousin directly must be under a written, prospective Personal Care Agreement for genuine personal care (Section 6.2).', 'money', 'Why this is safe money'),
        H2('6.7 Taxes for the cousin and husband'),
        table(['Question', 'Answer', 'Source'], [
            ['Is the pay federal-income-tax-free?', 'Yes, if you live in the aunt and uncle\'s home as your own home (no separate residence) and the pay is a "Medicaid waiver payment." STAR+PLUS HCBS pay clearly qualifies. For CAS/PHC pay the IRS says it depends on the program\'s nature; most FMSAs apply the exclusion to live-in CDS attendants; get the FMSA\'s written position and, if in doubt, a tax preparer\'s.', 'IRS Notice 2014-7; IRS Q&amp;A (reviewed April 29, 2026), Q1 to Q4'],
            ['How is it reported?', 'You sign the FMSA\'s live-in difficulty-of-care statement. W-2 Box 1 shows $0 (or the excluded amount appears in Box 12, Code II). If any excluded pay lands in Box 1, back it out on Schedule 1, line 8s.', 'IRS W-2 instructions; IRS Q&amp;A'],
            ['Do I still pay Social Security and Medicare tax?', 'Yes, 7.65% withheld and matched by the employer budget. The family exemption covers only a spouse, parent or child. You earn Social Security credits.', '26 USC 3121(b)(3); IRS Pub. 926'],
            ['Can I still get the Earned Income Tax Credit?', 'Yes. You may elect to count all the excluded pay as earned income for the EITC and Additional Child Tax Credit. 2026 maximums: $664 (no children), $4,427 (1), $7,316 (2), $8,231 (3+).', 'Feigh v. Commissioner (2019); IRS AOD 2020-02; Rev. Proc. 2025-32'],
            ['Texas income tax?', 'None. Constitutionally prohibited.', 'Tex. Const. art. VIII, sec. 24-a'],
            ['Unemployment insurance?', 'Covered. Texas excludes only a spouse, parent or child under 21 from domestic employment coverage. If the job ends (nursing-home placement, death), file with TWC 800-939-6631.', 'Tex. Labor Code 201.065'],
            ['Health insurance trap', 'Excluded wages are not in MAGI. In Texas (no Medicaid expansion) a household whose only income is excluded pay can fall below 100% of poverty and lose marketplace subsidies entirely. Keep some taxable income in the household or plan coverage before you rely on the exclusion.', '26 USC 36B(d)(2)(B); IRS premium tax credit Q&amp;A'],
            ['SNAP for the cousin\'s household', 'Counts the gross wages even though they are income-tax-free.', '7 CFR 273.9(b)(1)(i)'],
            ['Overtime', 'Over 40 hours for one employer is 1.5x and comes out of the fixed budget. Avoid it by splitting hours, or ask the FMSA whether the household live-in exemption applies (live-in 5 days/120 hours a week, written sleep and meal agreement). The 2025 federal "no tax on overtime" deduction (up to $12,500 single / $25,000 joint through 2028) needs the FMSA to report qualified overtime separately.', '29 CFR 552.102; 29 CFR 785.22; 26 TAC 264.241'],
            ['Workers\' compensation', 'Optional in Texas; without it the employer is personally liable for injuries. Buy a policy from the CDS budget (Form 1728).', '26 TAC 264.223'],
        ], [1.6 * inch, 3.6 * inch, 1.7 * inch]),
        H2('6.8 If the uncle (or aunt) served: the VA stack'),
        P('VA money stacks on top of Medicaid, but Texas has one trap you must plan around. All figures effective December 1, 2025 through November 30, 2026.'),
        table(['Benefit', 'Who qualifies', '2026 amount', 'How it interacts with Texas Medicaid'], [
            ['<b>VA Pension with Aid and Attendance</b> (needs-based)', '65+, 90 days active duty with 1 day in a wartime period (WWII, Korea, Vietnam, Gulf War), net worth under $163,699 (home and 2 acres excluded), non-dishonorable discharge, needs help with daily living', 'Veteran with spouse: <b>$34,488/yr = $2,874/month</b>; veteran alone $29,093; surviving spouse $18,697 ($1,558/mo); both spouses veterans, both A&amp;A: $46,143', 'The A&amp;A portion is NOT counted as income by Texas Medicaid (MEPD E-4315); the base pension is counted. <b>Trap:</b> CCSE Handbook 2531 treats A&amp;A as the primary fund for attendant care; unspent A&amp;A, or A&amp;A spent on the same tasks Medicaid covers, is converted to hours and subtracted from CAS authorizations (a full $2,874 divided by $16.33 = 176 hours a month). Fix: document every A&amp;A dollar spent on medications, supplies, equipment, therapy copays and privately paid care hours OUTSIDE the Medicaid plan (nights, weekends) under a written care agreement.'],
            ['Family caregiver wages as VA medical expenses', 'Once the veteran is A&amp;A-rated or a physician documents custodial need; the aunt\'s care counts too as a household relative', 'Payments above 5% of the basic rate ($1,141/yr for veteran with spouse) reduce countable income dollar for dollar', 'This is how a near-zero pension becomes the maximum: the couple pays the cousin under a care agreement for non-Medicaid hours and reports it on Form 21P-8416 (38 CFR 3.278). Those wages are taxable to the cousin (Notice 2014-7 does not cover VA-funded private pay).'],
            ['<b>VA Program of Comprehensive Assistance for Family Caregivers (PCAFC)</b>', 'Veteran with a 70%+ service-connected rating (any era), needs in-person care 6+ months; the cousin qualifies as an extended family member and as a live-in', 'Monthly stipend to the cousin: Level 2 $3,499 Houston, $3,299 DFW, $3,119 Austin, $3,079 San Antonio, $3,034 rest of Texas; Level 1 is 62.5% of that. Plus CHAMPVA health coverage, 30+ respite days, training', 'Paid to the caregiver, so it does not touch the couple\'s Medicaid budget. But 38 CFR 71.20(a)(5) bars care "simultaneously and regularly provided by another entity": get the VA Caregiver Support Coordinator\'s written answer on how Medicaid CDS hours for the same veteran are treated. Husband can be Secondary Family Caregiver.'],
            ['Veteran-Directed Care', 'Enrolled VA patient; referral by the VA social worker; offered through Central Texas (Temple) 855-937-2372, San Antonio AACOG 888-724-8387, DFW REACH 817-870-9082, Houston Harris County AAA', 'A VA-funded monthly budget the veteran uses to hire and pay workers, family included', 'Useful for hours Medicaid will not authorize.'],
            ['VA Homemaker/Home Health Aide and Respite', 'Enrolled VA patient with clinical need', 'Agency aide hours; up to 30 days/year respite', 'Covers the cousin\'s time off without unpaid gaps.'],
            ['Disability compensation (if any service-connected condition, incl. PACT Act presumptives)', 'Any rating', 'Not needs-based; A&amp;A can be added as Special Monthly Compensation', 'Counted by Medicaid except its A&amp;A portion; a 70%+ rating unlocks PCAFC and free State Veterans Home care.'],
        ], [1.45 * inch, 1.6 * inch, 1.65 * inch, 2.2 * inch]),
        bullets([
            '<b>Sequence:</b> Texas Veterans Commission claims advisor <b>800-252-8387</b> (free, Mon-Fri 7:30-5:30) and VA Form 21-22; file <b>VA Form 21-0966</b> Intent to File today to lock the retroactive date; physician completes <b>21-2680</b>; file <b>21P-527EZ</b> with <b>21P-8416</b> (medical expenses) and 3 months of bank statements; enroll in VA health care (10-10EZ, 877-222-8387); ask the VA social worker about Veteran-Directed Care and aide hours; if 70%+ rated, file <b>10-10CG</b>. VA status line 800-827-1000; Caregiver Support Line 855-260-3274.',
            '<b>Never</b> route A&amp;A through the Qualified Income Trust (it becomes countable for the co-payment). Give HHSC the VA award letter showing the A&amp;A breakdown; HHSC verifies quarterly with the VA (Form 1240).',
            'Avoid "pension poachers" who sell annuities to qualify for A&amp;A; the 36-month VA look-back penalizes transfers at $2,874 a month per covered dollar, and the Medicaid 60-month look-back runs alongside.',
        ]),
    ]
