# -*- coding: utf-8 -*-
"""Section 7 timeline and Section 9 pitfalls."""
from reportlab.lib.units import inch
from reportlab.platypus import Spacer, PageBreak
from render import *

def timeline():
    return [
        PageBreak(), H1('7. The 120-day timeline (and what happens after)'),
        P('Dates count from the day you make the first calls. The legal clocks in the right column are the ones that protect you; write each one on a calendar the day it starts.'),
        table(['When', 'Aunt and uncle', 'Cousin', 'Husband', 'Legal clocks running'], [
            ['<b>Day 1</b>', 'Interest list, both names (844-438-5658 / YourTexasBenefits). 2-1-1 option 2: Community Care intake for both, CAS with CDS. Form H1200 online for both.', 'Make the calls, keep the log. Sign nothing as DR.', 'Locate DD-214; call TVC 800-252-8387; VA Form 21-0966 intent to file.', 'Interest-list request date = place in line. CCSE home visit due within 14 days. MEPD 45-day clock starts on the signed H1200.'],
            ['<b>Days 2 to 7</b>', 'Doctor visits: Form 3052 signed, ADL limits charted, home-health referral if any skilled need. Financial snapshot. Sign SDPOA, MPOA, HIPAA, Directive, record the Transfer on Death Deed.', 'Written question to the Community Care office and two FMSAs about the Form 1726 "primary caregiver" line. Expense-sharing agreement drafted. Legal Hotline 800-622-2520.', 'VA net-worth inventory; physician appointment for 21-2680; 10-10EZ enrollment.', 'Form 3052 correction turnaround: 5 business days.'],
            ['<b>Days 7 to 21</b>', 'Caseworker visit: Form H2060 for each. Worst days, every task, no "C" codes. Elect CDS (Form 1584), pick FMSA, Forms 1735/1736/1740. Ask for meals, DAHS, ERS, Family Care interest list.', 'Present as informant with the 7-day diaries. Start FMSA new-hire packet.', 'Same packet. Named backup on Form 1740.', 'CCSE decision due within 30 days of the signed application. QIT must exist before MEPD can certify (if income over $2,982).'],
            ['<b>Days 21 to 45</b>', 'Form 2065-A arrives with hours. Form 2101 to the FMSA within 5 business days. Set wages on Form 1730 at the ceiling. Approve the budget in writing.', 'FMSA orientation done; Form 1729 back; EVV training and app; first shifts.', 'Same. File 21P-527EZ with 21-2680 and 21P-8416.', 'Fair hearing on low hours: 90 days (before the effective date to keep hours). FMSA: up to 3 weeks from meeting to first workday.'],
            ['<b>Days 45 to 70</b>', 'First CDS payroll. Report any change to MEPD within 10 days. MSP (QMB) approval: confirm SSA stops the $202.90 deduction.', 'First paycheck (pay at least twice monthly). Register with the AAA caregiver program 800-252-9240.', 'Ledger started: A&amp;A spending, receipts, notices.', 'EVV visit maintenance: 95 days per visit.'],
            ['<b>Days 70 to 120</b>', 'Reassessment request if needs changed. Home safety fixes. Dental, DME via Medicare and MCO.', 'CPR class; dementia training; care plan and log in place.', 'Home mods bids ready for the HCBS day; NEMT set up.', 'MEPD redetermination annually; CCSE reassessment annually.'],
            ['<b>Months 3 to 12: interest-list release</b>', 'Answer the HHSC call or Form H2118 within 30 days. Return H1200 + H2053-B within 30 days. MN/LOC + H2060 + ISP within the MCO\'s 45 days. Form H2065-D with start date.', 'Move CDS accounts to the MCO\'s FMSA; new budget at $17.24. Ask for protective supervision, respite (outside provider), aids, home mods, dental.', 'Same hiring under the HCBS budget. PCAFC application if 70%+ rated.', 'Start of care = 1st of the month after the last approval. MN valid 120 days. MCO appeal 60 days, continuation within 10 days, fair hearing 120 days after MCO decision.'],
            ['<b>Every year</b>', 'ISP and MN/LOC renewal (12 months); MEPD renewal; registry rechecks on employees; new Form 1730 after any rate change (next rate action expected Sept. 1, 2027).', 'Training log (Form 1732) and annual evaluation; tax filing with the 2014-7 exclusion.', 'VA Form 21P-8416 annual medical-expense report; ledger.', 'Interest-list annual contact if still waiting (inactive after 120 days of no response).'],
        ], [0.85 * inch, 1.75 * inch, 1.45 * inch, 1.3 * inch, 1.55 * inch], font='cell'),
    ]

def pitfalls():
    return [
        PageBreak(), H1('9. Pitfalls that cost families their pay (with the rule that makes each one a mistake)'),
        table(['Mistake', 'What it costs', 'The rule', 'Do this instead'], [
            ['Naming the cousin (or her husband) as CDS Designated Representative', 'Neither can be paid by that employer', 'Form 1726; 26 TAC 264.205', 'Aunt and uncle are their own employers, or each other\'s DR, or use an outside adult'],
            ['Letting the assessor record the cousin as the unpaid "primary caregiver," or answering "we manage fine"', 'Tasks coded "C" are not purchased; in CAS/PHC/FC the primary caregiver may not be the paid attendant', 'CCSE 2432-2433; Form 1726', 'State that unpaid help is not available; the cousin is the hired attendant'],
            ['Paying the cousin cash, back pay, or "under the table" before approval; adding her to the deed or accounts', 'Transfer penalty: $262.37 per day of ineligibility; a $20,000 gift = 76 days', 'MEPD I-1000, I-4100, I-5100', 'Written prospective Personal Care Agreement, checks, logs; Transfer on Death Deed instead of a deed change'],
            ['Charging the cousin rent', 'Countable income to the couple; can push over $2,982 and force a trust or co-payment', 'MEPD E-3000/E-3300', 'Written expense-sharing agreement, paid to vendors'],
            ['Expecting Community First Choice', 'Not available to the 300%-income (MAO) group most retirees are in', 'STAR+PLUS Handbook 1100, 6118; LTSS comparison footnote 15', 'CAS now, STAR+PLUS HCBS later; SSI route only if income is at SSI level'],
            ['Missing the HHSC interest-list contact or Form H2118', 'Removed from the list; start over at the bottom (44.6% of FY26-27 closures were "no response")', '1 TAC 353.1153; PSU Handbook 3300', 'Answer within 30 days; keep address and phone current'],
            ['Missing the 30-day window to return H1200 + H2053-B after release', 'Default plan assignment; can close the release', 'PSU Handbook 3311', 'Calendar it the day the packet arrives'],
            ['Physician does not sign the MN/LOC or Form 3052, or charts only "dementia"', '617 medical-necessity denials and 251 "unable to obtain MD signature" closures in FY26-27', 'PSU 1250; CCSE 4600', 'Line up a responsive PCP now; ask for physical conditions causing the limits'],
            ['Accepting priority status when live-in help is present', 'Cap drops from 50 to 42 hours for $0.18/hour more', '26 TAC 271.81', 'Decline unless truly needed for safety'],
            ['Overlapping or missed EVV clock-ins; billing time merely present in the home', 'Unpaid visits; locked after 95 days; possible fraud referral', 'EVV Handbook 7000, 9000, 17000', 'Separate clock-ins per spouse; sequential shifts; daily log'],
            ['One person over 40 hours for a single employer with no overtime plan', 'Overtime at 1.5x eats the fixed budget and lowers the wage', '26 TAC 264.241, 264.505', 'Split hours between the cousin and husband; ask about the live-in exemption'],
            ['Counting on the husband for paid HCBS respite or the AAA voucher', 'Not payable to someone living in the home', 'STAR+PLUS Handbook 7300; HHSC respite voucher guidelines', 'Hire an outside respite worker; husband takes attendant hours instead'],
            ['Both spouses apply at once when assets are well above $3,000', 'No community-spouse protection; spend-down to $3,000', 'MEPD J-1300', 'Ask an elder-law attorney about staging the applications (SPRA up to $162,660)'],
            ['Unspent VA Aid and Attendance', 'Converted to hours and subtracted from CAS authorizations', 'CCSE 2531', 'Ledger every A&amp;A dollar to medications, supplies, equipment and non-Medicaid care hours'],
            ['Depositing A&amp;A into the Qualified Income Trust', 'Becomes countable for the co-payment', 'MEPD E-4315; Appendix XXXVI', 'Keep A&amp;A out of the trust'],
            ['Choosing the agency option', 'Attendant paid near the $13.00 assumption; family loses control', 'PFD rate methodology', 'CDS: the family controls $16.33 to $17.24 per hour'],
            ['Not appealing low hours, or appealing late', 'Hours stay low; benefits stop during appeal', 'CCSE 2900 (90 days); MCO 60 days; continuation within 10 days', 'Appeal every low authorization; ask for continuation'],
            ['Keeping a separate residence while claiming the tax exclusion', 'Back taxes and penalties', 'IRS Q&amp;A 3 on Notice 2014-7', 'Move in fully; change license and voter registration'],
            ['Ignoring the health-coverage cliff', 'No marketplace subsidy if household MAGI is below 100% of poverty in Texas', '26 USC 36B', 'Keep some taxable income or plan coverage first'],
            ['Buying equipment or home modifications out of pocket before asking', 'No retroactive reimbursement', 'STAR+PLUS Handbook 6400, 6600', 'PCP order, MCO service coordinator, then the waiver pays'],
            ['Forgetting to record the Transfer on Death Deed, or only one spouse signing', 'Void; home goes through probate and MERP', 'Est. Code 114.055', 'Record with the county clerk now; both owners sign'],
            ['Assuming CAS gives a Medicaid card', 'No drug or medical coverage; only attendant hours', 'MEPD A-4100', 'File for the Medicare Savings Program and Extra Help on the same H1200'],
            ['Using stale plan lists (Aetna, BCBSTX, Amerigroup)', 'Wrong phone numbers; wrong plan choice', 'HHSC service-area chart effective Sept. 1, 2024', 'Use the chart in Section 10 or call 800-964-2777'],
        ], [1.75 * inch, 1.55 * inch, 1.35 * inch, 2.25 * inch]),
    ]
