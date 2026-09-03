# -*- coding: utf-8 -*-
"""Sections 0-4 of the master plan: cover, how to use, the plan on one page, program map, aunt/uncle steps."""
from reportlab.lib.units import inch
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, KeepTogether
from render import *

def cover():
    return [
        Spacer(1, 1.6 * inch),
        P('Texas Family Caregiver Master Plan', 'title'),
        P('How your cousin and her husband get paid by Texas Medicaid to care for your aunt and uncle at home, '
          'at the highest legitimate pay, with the highest level of care', 'subtitle'),
        Spacer(1, 0.3 * inch),
        P('<b>Who this is for:</b> an elderly married couple (aunt and uncle) who own their home in Texas, and their niece '
          '(the cousin) and her husband, who will move in, give up outside work, live in the home, and become the paid attendants.', 'body'),
        P('<b>What is inside:</b> the exact Texas programs that pay relatives, 2026 dollar limits and hourly rates, '
          'an itemized step list for each of the four people, phone numbers and form numbers verified against HHSC and federal '
          'sources in September 2026, a 120-day timeline, an honest income model, the mistakes that cost families their pay, '
          'and a care-quality plan.', 'body'),
        Spacer(1, 0.2 * inch),
        callout('<b>The three-sentence version.</b> Put both names on the STAR+PLUS HCBS interest list today and apply for '
                'Community Attendant Services (CAS) the same day, because CAS has no waitlist and pays for up to 50 hours a week '
                'per person. Choose the Consumer Directed Services (CDS) option so the aunt and uncle are the employers and can '
                'legally hire the niece and her husband; never make the niece the Designated Representative. When STAR+PLUS HCBS '
                'opens (typically inside a year), move to it: no 50-hour cap, 30 days of respite per person per year, '
                'home modifications, adaptive aids, and dental, all on top of attendant hours.', 'money', 'Read this first'),
        Spacer(1, 0.25 * inch),
        P('Prepared September 3, 2026 from Texas HHSC handbooks, the Texas Administrative Code, HHSC rate schedules, IRS, VA and '
          'SSA sources. Rules change every September 1 and every January 1; confirm any figure before you rely on it. '
          'This is a planning guide, not legal, tax or medical advice.', 'small'),
        NextPageTemplate('main'), PageBreak(),
    ]

def how_to_use():
    return [
        H1('How to use this plan'),
        P('Each section is written for the person who has to do the work. Print the step tables for your person and check boxes as you go. '
          'Every phone number carries the words to say when someone answers. Every form has its number so you can ask for it by name.'),
        table(['Section', 'Who reads it', 'What you get'], [
            ['1. The plan on one page', 'Everyone', 'The strategy, the order of operations, and the money at stake'],
            ['2. The programs, in plain English', 'The organizer', 'Which Texas programs pay relatives, and which one to use when'],
            ['3. Aunt and uncle: itemized steps', 'Aunt, uncle, organizer', 'Every call, form, deadline and assessment, in order'],
            ['4. The cousin: itemized steps', 'The cousin', 'Getting hired, getting the wage set high, EVV, taxes, training'],
            ['5. The husband: itemized steps', 'The husband', 'Second attendant, respite provider, backup, VA role'],
            ['6. Money: how much and how to get more', 'Everyone', 'Rates, hours, budget math, income scenarios, tax-free rules'],
            ['7. 120-day timeline', 'The organizer', 'Week-by-week calendar with the legal deadlines that protect you'],
            ['8. Highest level of care', 'The cousin and husband', 'Free training, Medicaid-paid equipment, respite, oversight'],
            ['9. Pitfalls that cost families their pay', 'Everyone', 'The mistakes, with the rule that makes each one a mistake'],
            ['10. Directory', 'Everyone', 'Phone numbers, websites, search terms, form numbers, rule citations'],
        ], [1.9 * inch, 1.4 * inch, 3.6 * inch]),
        Spacer(1, 8),
        callout('Pick ONE organizer (probably the cousin) who keeps a binder or shared folder for EACH spouse. Texas treats the aunt and the uncle as two '
                'separate cases with two separate assessments, two service plans, two employer accounts and two sets of hours, even though they share a home. '
                'Log every call: date, time, person\'s name, what they said, reference number.', 'info', 'One rule for the whole plan'),
    ]

def one_page():
    return [
        H1('1. The plan on one page'),
        H2('The strategy'),
        P('Texas pays family caregivers through the <b>Consumer Directed Services (CDS)</b> option of its Medicaid attendant programs. The person receiving care '
          '(or their representative) becomes the legal employer, a state-contracted <b>Financial Management Services Agency (FMSA)</b> runs payroll, and the employer '
          'hires whoever they choose, including relatives, as long as the hire is not the care recipient\'s spouse, the employer, the Designated Representative, or '
          'those people\'s spouses (HHSC Form 1726, April 2026; 26 TAC Chapter 264). A niece and her husband who live in the home are eligible hires.'),
        P('There are two doors into paid hours for a couple over 65 who are not yet on Medicaid. You go through both at once:'),
        table(['', 'Door 1: Community Attendant Services (CAS)', 'Door 2: STAR+PLUS HCBS program'], [
            ['What it is', 'State-plan attendant program run by an HHSC caseworker. Not full Medicaid (no Medicaid card), just attendant hours.',
             'The full home-and-community waiver, run by a managed-care plan (MCO). Attendant hours plus respite, nursing, home mods, adaptive aids, meals, dental, emergency response.'],
            ['Waitlist', '<b>None.</b> Decision within 30 days of a signed application.', '<b>Interest list.</b> As of July 31, 2026, 13,519 names, 99.9% on it under one year; HHSC released 20,595 names since Sept. 1, 2025.'],
            ['Hours', 'Up to <b>50 hours/week per person</b> (42 if "priority"). Needs a score of 24+ on Form H2060 and 6+ hours/week of need.',
             '<b>No weekly cap and no minimum score.</b> Hours come straight from the Form H2060 task-and-minute math, limited only by a yearly cost ceiling of 202% of nursing-home cost.'],
            ['2026 money limits', 'Income $2,982/mo per person ($5,964 couple); resources $2,000 / $3,000; home exempt to $752,000 equity.', 'Same limits. Income over the cap is fixed with a Qualified Income Trust.'],
            ['CDS (hire family)?', 'Yes', 'Yes, for attendant hours, in-home respite, nursing and therapies'],
            ['Rate paid into the CDS budget (from Sept. 1, 2025)', '$16.33/hour (agency option $17.13)', '$17.24/hour for attendant time (CDS); respite $16.56/hour'],
            ['Use it as', 'The <b>bridge</b>: paid hours within about 6 to 10 weeks', 'The <b>destination</b>: more hours, more services, respite, home modifications'],
        ], [1.05 * inch, 2.9 * inch, 2.95 * inch]),
        Spacer(1, 6),
        H2('The order of operations'),
        numbered([
            '<b>Today:</b> add BOTH names to the STAR+PLUS HCBS interest list (YourTexasBenefits.com "Find Support Services", or call 844-438-5658). The request date is your place in line.',
            '<b>Today:</b> call 2-1-1 (option 2) or 877-541-7905 and open a Community Care intake for BOTH spouses, asking for Community Attendant Services with the CDS option. File Form H1200 online for each spouse.',
            '<b>This week:</b> doctor visit for each spouse; ask the practitioner to complete <b>Form 3052</b> (Practitioner\'s Statement of Medical Need) and to chart every ADL limitation. Get finances under the 2026 limits. Sign powers of attorney and a HIPAA release.',
            '<b>Within 14 days:</b> caseworker home visit. Each spouse is scored on Form H2060. Describe the worst days, task by task. Say the niece will NOT keep doing tasks for free, so tasks are coded "purchased," not "caregiver."',
            '<b>Within 30 days:</b> eligibility notice (Form 2065-A) with weekly hours. Elect CDS on Form 1584, pick an FMSA, and have the aunt and uncle each be their own employer. Cousin and husband complete the FMSA hiring packet.',
            '<b>Weeks 6 to 10:</b> first paychecks. Set the wage on Form 1730 as high as the budget allows. Clock every visit in EVV.',
            '<b>In parallel:</b> if either spouse served in wartime, file for VA Pension with Aid and Attendance; if the veteran has a 70%+ service-connected rating, file for the VA caregiver stipend, which is paid on top of Medicaid.',
            '<b>When the interest list releases (plan on 3 to 12 months):</b> return Form H1200 and the plan-choice form within 30 days, get the MN/LOC and H2060 done within the MCO\'s 45 days, move the CDS employer accounts to the STAR+PLUS HCBS plan, add respite, home modifications and adaptive aids.',
        ]),
        H2('What is at stake (summary; full model in Section 6)'),
        table(['Scenario', 'Hours / week', 'Wage', 'Household caregiver income per month (gross)'], [
            ['Bridge: CAS, both spouses, moderate needs (35 + 35)', '70', '$15.00', 'about $4,550'],
            ['Bridge: CAS, both spouses at the 50-hour cap, cousin and husband splitting each employer\'s hours', '100', '$15.00', 'about $6,500'],
            ['Destination: STAR+PLUS HCBS, both spouses, H2060 supports 60 hours each (dementia with protective supervision)', '120', '$15.50', 'about $8,060'],
            ['Add: VA Pension with Aid and Attendance for a married wartime veteran (paid to the veteran; must be spent on care, see 6.8)', '', '', '+ up to $2,874'],
            ['Add: VA caregiver stipend if the veteran is 70%+ service-connected (paid to the cousin)', '', '', '+ $3,034 to $3,499'],
        ], [3.3 * inch, 0.8 * inch, 0.7 * inch, 2.1 * inch]),
        P('Because the cousin and her husband live in the home, wages paid under a Medicaid home-and-community program are excludable from federal income tax under IRS Notice 2014-7, and Texas has no state income tax. The numbers above are therefore close to take-home apart from the 7.65% Social Security and Medicare tax. Details and the caveats (including which programs the IRS has ruled on) are in Section 6.7.', 'body'),
    ]
