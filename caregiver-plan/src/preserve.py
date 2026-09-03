# -*- coding: utf-8 -*-
import sys
from reportlab.lib.units import inch
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate
from render import *

def build(out):
    doc = Doc(out, 'Keeping the Estate and Getting the Care')
    s = []
    s += [Spacer(1, 1.5*inch),
      P('Keeping the Estate<br/>and Getting the Care', 'title'),
      P('A Texas plan for an elderly couple with substantial assets, and for their daughter and her husband who will move in and be paid to care for them', 'subtitle'),
      Spacer(1, 0.3*inch),
      callout('<b>The headline: they do not spend down to $3,000.</b> That figure applies only to the spouse who applies, and only after the other spouse\'s protections are carved out. '
        'A married Texas couple keeps the homestead at <b>any value</b>, one car at <b>any value</b>, household goods, prepaid funerals, up to <b>$162,660</b> in other resources, and up to <b>$4,066.50</b> a month in income. '
        'Most of an ordinary estate survives without a trust. What needs planning is the part above that line: non-homestead land and retirement savings.', 'money', 'Read this first'),
      Spacer(1, 0.15*inch),
      callout('This edition assumes: both spouses living at home, community property owned equally, <b>no veteran status</b>, and a firm goal of preserving the estate rather than spending it down. '
        'It replaces the earlier plan\'s advice to apply for both spouses at once, which is wrong for a couple with assets.', 'info', 'What changed'),
      Spacer(1, 0.2*inch),
      P('Prepared September 3, 2026 from Texas HHSC handbooks (MEPD, CCSE, STAR+PLUS), the Texas Administrative Code, HHSC rate schedules, IRS and CMS sources. '
        'Rules change every September 1 and January 1. This is a planning guide, not legal or tax advice - and this particular plan genuinely requires an elder law attorney.', 'small'),
      NextPageTemplate('main'), PageBreak()]

    s += [H1('Contents'), toc(), PageBreak()]

    # 1
    s += [H1('1. What they keep'),
      P('Texas Medicaid counts the resources of <b>both</b> spouses no matter whose name is on them. MEPD J-2200 says it outright: "regardless of any state laws relating to community property... all the resources held by either... shall be considered available." '
        'Retitling assets between them accomplishes nothing. What does the work is the set of protections the law gives the spouse who stays home, called the community spouse.'),
      table(['What', 'Protected amount', 'Rule'], [
        ['The homestead', '<b>Any value.</b> The $752,000 equity cap does not apply while a spouse lives in the home.', 'MEPD F-3600, J-4400'],
        ['One automobile', '<b>Any value</b>', 'MEPD F-4221'],
        ['Household goods and personal effects', 'All', 'MEPD F-4222'],
        ['Irrevocable prepaid funeral contracts', 'Both spouses', 'MEPD F-4200'],
        ['Other countable resources (the SPRA)', '<b>$32,532 minimum to $162,660 maximum</b>', 'MEPD Appendix XXXI (rev. June 1, 2026)'],
        ['Community spouse monthly income', 'Up to <b>$4,066.50</b>', 'MMMNA, Appendix XXXI'],
        ['The applying spouse keeps', '$2,000', 'MEPD Appendix XXXI'],
      ], [1.9*inch, 3.3*inch, 1.7*inch]),
      Spacer(1, 6),
      callout('<b>Only one spouse applies.</b> This is the whole strategy in one line. The moment both are on the waiver there is no community spouse, the couple is budgeted together against $3,000, and every protection above disappears. '
        'The needier spouse applies. The other may apply years later, or never.', 'warn', 'The rule that decides everything'),
      H2('What is still exposed'),
      bullets([
        '<b>Non-homestead real property</b> - second homes, raw land, rental or ranch property, mineral interests - counts at equity value (F-4210).',
        '<b>Retirement accounts</b> - his and hers, counted in full. Be careful here: many elder law articles claim Texas exempts IRAs once they are in required-minimum-distribution status. <b>That rule appears nowhere in the MEPD Handbook or 1 TAC 358.</b> It traces to a 2018 verbal HHSC announcement that was never formalized, and the related claim that a community spouse\'s IRA is excluded entirely contradicts J-2200. Plan on them counting.',
        '<b>Bank and brokerage accounts, cash value life insurance</b> over $1,500 face value.',
        'The "essential to self-support" exclusion (F-4310) sounds useful but is capped at <b>$6,000 of equity returning at least 6%</b>, and it is all-or-nothing: if the return dips below 6%, the entire equity counts.',
      ]),
      H2('The timing lever'),
      P('The snapshot that sets the SPRA is taken in the <b>application month</b> (J-4310), not at some earlier date. Combined with the tools in Section 2, that means the month they file genuinely matters, and it is a decision to make with an attorney rather than by accident.')]

    # 2
    s += [PageBreak(), H1('2. The tools for everything above the line'),
      P('Ranked by how well they actually work for this family.'),
      table(['#', 'Tool', 'How it works', 'Watch out for'], [
        ['1', '<b>Caregiver child exception</b><br/>MEPD I-3100', 'A son or daughter who lived in the parent\'s home for at least <b>two years</b> before the parent\'s institutionalization, and provided care that allowed the parent to stay out of a nursing facility, may receive <b>the home itself</b> as a transfer with <b>no penalty at all</b>. Not a reduced penalty - none. This exists only because she is their daughter.',
         'Requires all three: two full years living there, documented care that prevented institutionalization, and an institutionalization event. Confirm with the attorney how it applies when the parent enters the waiver rather than a facility.'],
        ['2', '<b>Community spouse annuity</b><br/>MEPD F-7230', 'A single-premium immediate annuity - irrevocable, non-assignable, actuarially sound, level payments, State named as remainder beneficiary - converts excess countable savings into the healthy spouse\'s protected income stream. No transfer penalty when structured correctly. This is the main lever for retirement savings above the SPRA.',
         '<b>F-7240 is punitive.</b> An annuity that fails any requirement makes the <b>entire purchase price</b> a penalized transfer, not just the excess. Never buy one without an elder law attorney.'],
        ['3', '<b>Accessibility remodeling of the homestead</b>', 'Quietly the best tool in the box. Unlimited dollars, no look-back, and HHSC\'s own handbook example blesses it. Ramps, roll-in shower, widened doors, a ground-floor suite, lifts, HVAC, generator. Countable cash becomes better care AND preserved value inside an asset that is exempt in life and outside probate at death.',
         'Do the work before applying, keep invoices, and use licensed contractors. Improvements to a non-homestead property do not get this treatment.'],
        ['4', '<b>Lady Bird or Transfer on Death deed</b><br/>Tex. Est. Code ch. 114', 'Estate recovery reaches only the <b>probate</b> estate. A recorded deed passes the homestead outside probate with <b>zero look-back</b> - strictly better than putting the home into a trust.',
         'Must be recorded before death or it is void (114.055). Both owners sign. Est. Code 114.106 lets a personal representative reach the property within 2 years if the probate estate cannot pay claims.'],
        ['5', '<b>Irrevocable trust</b><br/>MEPD F-6500', 'If no circumstance permits payment of principal back to the grantor, the trust corpus is a transfer rather than a resource - and transfers made more than 60 months before applying carry no penalty at all (I-2130). About $7,000 to $12,000 and 4 to 10 weeks to draft and fund.',
         '<b>The 60-month clock is why this is a this-month decision.</b> No access to principal, however remote - F-6610 counts a $50,000 payout contingent on a heart transplant as fully countable. IRAs generally cannot go in. The homestead usually should not go in either; use the deed instead.'],
        ['6', '<b>Non-homestead property listed for sale</b><br/>MEPD F-3130, F-4211', 'Real property genuinely on the market is exempt outright, with no time limit, "until the proceeds of the sale are available."',
         'They must accept any offer at two-thirds of market value or better. Once it sells, the cash counts.'],
        ['7', '<b>Business property</b><br/>MEPD F-4330', 'Property of a genuine trade or business is excluded <b>regardless of value or rate of return</b>, including land, livestock and equipment. The only unlimited real-property exclusion in Texas.',
         'It has to be a real operation - a Schedule F or C filing, not land that happens to have cattle on it.'],
        ['8', 'Ordinary exempt spend-down', 'Irrevocable prepaid funerals for both, paying off the mortgage, a newer vehicle, prepaying taxes and insurance, replacing a failing roof or HVAC on the homestead.',
         'All legitimate, none are penalized transfers. Confirm current funeral-contract limits with HHSC.'],
        ['9', 'Long-term care Partnership insurance<br/>MEPD Chapter P', 'A qualified policy protects a dollar of assets for every dollar it pays out, at eligibility AND from estate recovery (P-1200).',
         '<b>Too late here.</b> At 65+ it runs roughly $7,030 a year per couple with full underwriting, and it protects only the applying spouse\'s resources, not the SPRA (P-1220).'],
      ], [0.22*inch, 1.5*inch, 3.1*inch, 2.08*inch]),
      Spacer(1, 6),
      callout('The caregiver child exception and Money Follows the Person fit together. The 30-day nursing facility stay that skips the interest list (Section 3) is also an <b>institutionalization event</b> - the trigger the exception needs. '
        'If their daughter has already banked two documented years of live-in care by then, the same admission that gets them onto the waiver can also let the home transfer to her penalty-free. '
        '<b>That means the two-year clock should start now, and every month of care should be documented from day one.</b> Have the attorney confirm the sequencing before anything is signed.', 'money', 'The two tools that work together'),
      Spacer(1, 4),
      callout('<b>Never gift or retitle anything to family.</b> The 60-month look-back penalizes transfers at <b>$262.37 per day</b> of ineligibility (unchanged as of September 1, 2026; next review September 1, 2027). '
        'Deeding property to their daughter is the single most expensive mistake available - But see the caregiver child exception below - as their daughter, she has a route the law gives to no one else.', 'warn', 'The one thing that ruins the plan')]

    # 3
    s += [PageBreak(), H1('3. Money Follows the Person: skipping the waiting list'),
      P('The STAR+PLUS HCBS waiver is the program worth having - it is the one that carries spousal impoverishment protection, and it has no 50-hour weekly cap on attendant hours. '
        'Its problem is the interest list, with roughly <b>15,850 people</b> waiting.'),
      P('Elder law practitioners routinely bypass it. A planned <b>nursing facility admission of at least 30 days</b>, followed by a <b>Money Follows the Person</b> transition, moves the person onto the waiver and back home on Consumer Directed Services without ever reaching the front of the queue. '
        'This is a recognized HHSC pathway, not a trick - the program exists specifically to move people out of institutions.'),
      table(['Route', 'How long', 'What it costs', 'When it fits'], [
        ['Interest list, wait your turn', 'Months to a year or more, then 3 to 5 months of processing', 'Nothing', 'Needs are stable and there is time'],
        ['<b>Nursing facility stay + Money Follows the Person</b>', 'About 30 days inpatient, then transition home', 'A month of facility care, and the emotional cost of a placement', 'Care needs have already spiked, or a hospital discharge is being planned anyway'],
      ], [2.2*inch, 1.7*inch, 1.6*inch, 1.4*inch]),
      Spacer(1,6),
      P('The practical version: put both names on the interest list today anyway (it costs nothing and the request date sets their place), and if either spouse is ever hospitalized, <b>tell the hospital discharge planner immediately that the family wants a Medicaid nursing-facility stay with a Money Follows the Person transition home.</b> '
        'That single sentence at the right moment can save a year. Ask the elder law attorney to brief the family on it in advance so nobody has to improvise it during a crisis.'),
      Spacer(1,4),
      callout('Community Attendant Services - the no-waitlist program the earlier plan recommended as a bridge - <b>does not carry spousal impoverishment protection.</b> It is a state-plan program under Social Security Act 1929(b), and Texas has not elected those protections for it, so the couple is budgeted together against $3,000. '
        'For a family with assets, CAS is not the bridge. The waiver is the destination and Money Follows the Person is the road.', 'warn', 'Why the earlier plan\'s bridge does not work here')]

    # 4
    s += [PageBreak(), H1('4. Paying their daughter: what actually works in Texas'),
      P('This is where the earlier plan was too optimistic, and it matters enough to correct in detail. Texas is <b>hostile</b> to family caregiver contracts as a spend-down device.'),
      table(['What people try', 'What Texas does', 'Rule'], [
        ['Pay a large lump sum up front for a lifetime of care', '<b>Rejected.</b> "Future compensation does not satisfy the compensation requirement." Only commercial annuities and assumption of a legal debt are excepted.', 'MEPD I-4130'],
        ['Pay a relative hourly for help with cleaning, laundry, cooking, shopping, driving to appointments', '<b>Treated as a gift.</b> These are "services normally provided by a family member." The handbook example gives a grandson <b>$200 of credit against $40,000 paid</b>.', 'MEPD I-4140, I-4160'],
        ['Pay a relative for genuine hands-on personal care under a written, prospective, fair-market agreement with daily logs and checks', 'Allowed, but narrowly - and only for the personal-care portion.', 'MEPD I-4140'],
        ['Compensate a relative for <b>documented lost wages</b> from leaving a job to provide care', '<b>Recognized.</b> This is the version the handbook example actually credits.', 'MEPD I-4160, Example 1'],
      ], [2.0*inch, 3.3*inch, 1.6*inch]),
      Spacer(1,6),
      callout('If they are going to pay their daughter privately, the agreement must be drafted by the elder law attorney and built around <b>documented lost wages plus hands-on personal care</b>, not around household help. '
        'Get her current pay stubs and a written offer letter or separation letter now - that documentation is the evidence the whole arrangement rests on.', 'money', 'How to structure it'),
      H2('4.1 Private pay versus Medicaid pay, side by side'),
      table(['', 'Medicaid CDS (once approved)', 'Private pay (now)'], [
        ['Hourly to the attendant', '<b>$13.00 to $15.90</b> - the state\'s rate assumes a $13.00 average wage; the FMSA budget workbook can support up to about $15.90 on the waiver. The binding number is whatever the FMSA approves in writing.', 'Whatever the family agrees, at fair market value'],
        ['Federal income tax', '<b>None</b>, if the caregiver lives in the home (IRS Notice 2014-7 covers 1915(c) waiver payments to a co-resident provider)', '<b>Fully taxable.</b> Notice 2014-7 does not reach private pay'],
        ['To match $15.90/hr tax-free, private pay must be', '-', '<b>$18.07 to $20.38/hr</b>, plus about 8.25% in employer taxes on top'],
        ['Social Security and Medicare', 'Withheld; she earns credits', 'Same - the couple becomes a household employer (IRS Pub. 926) once wages hit $3,000, plus Texas unemployment at $1,000 per quarter'],
        ['Effect on the estate', 'Paid by Medicaid; recoverable from the probate estate at death', 'Paid from their savings - which is the point, if spend-down is the goal'],
        ['Hours', 'Only what the Form H2060 assessment authorizes', 'Whatever they want'],
      ], [1.5*inch, 2.9*inch, 2.5*inch]),
      H2('4.2 What Texas care actually costs (2024 market data)'),
      table(['Option', 'Texas cost'], [
        ['Homemaker services (agency)', '$5,339 per month'],
        ['Home health aide (agency)', '$5,720 per month'],
        ['Nursing facility, semi-private room', '$5,475 per month'],
        ['<b>Private live-in family caregiver</b>', '<b>$3,300 to $5,000 per month</b>'],
      ], [3.4*inch, 3.4*inch]),
      P('The comparison that matters: paying their daughter privately costs roughly what an agency aide costs, delivers far better continuity of care, and keeps the money in the family instead of sending it to a facility or, eventually, to an estate recovery claim.', 'body')]

    # 5
    s += [PageBreak(), H1('5. The sequence practitioners actually use'),
      table(['Stage', 'What happens', 'How long', 'Why'], [
        ['<b>Now: month 1</b>', 'Elder law attorney engaged. Full asset inventory. Decide trust versus annuity. Record the Lady Bird or Transfer on Death deed. Put both names on the STAR+PLUS HCBS interest list (it costs nothing). Sign powers of attorney, medical powers of attorney, HIPAA releases and directives while both are clearly competent.',
         '2 to 6 weeks', 'The 60-month trust clock only runs once the trust is funded. Every month of delay is a month of exposure.'],
        ['<b>Months 1 to 3</b>', 'Fund the irrevocable trust with what should be protected long-term. Start accessibility remodeling of the homestead. Buy irrevocable prepaid funerals. List any non-homestead property they are willing to sell. Niece and husband move in; the written care agreement (lost wages plus personal care) starts.',
         '1 to 3 months', 'Converts countable assets into exempt ones and into better care, with no look-back on the remodeling.'],
        ['<b>Years 1 through 5</b>', 'Private pay for care. The trust clock runs. Reassess annually. Keep every receipt - care costs and home upkeep reduce an estate recovery claim later (1 TAC 373.213).',
         '5 years, ideally', 'This is the normal path. Most families with assets private-pay for years before Medicaid is relevant at all.'],
        ['<b>When care needs spike</b>', 'The needier spouse applies for STAR+PLUS HCBS. The community spouse annuity absorbs whatever countable savings remain. If a hospitalization happens, use the 30-day nursing facility stay plus Money Follows the Person to skip the interest list.',
         '45 days to 5 months', 'The SPRA snapshot is taken in the application month, so the timing is chosen, not accidental.'],
        ['<b>After approval</b>', 'Choose Consumer Directed Services, pick a financial management agency, hire their daughter and her husband as the paid attendants. Their pay becomes federal-income-tax-free because they live in the home.',
         '3 to 8 weeks to first paycheck', 'Now Medicaid pays for the care the family has been funding.'],
        ['<b>At death</b>', 'Estate recovery reaches the probate estate only. The homestead passed by deed is outside it. Anything in the trust past 60 months was never countable.',
         '-', 'This is where the earlier work pays off.'],
      ], [1.15*inch, 3.25*inch, 0.95*inch, 1.55*inch]),
      Spacer(1,6),
      callout('<b>Estate recovery, honestly.</b> A large estate clears every small-estate exemption and loses the under-$100,000 homestead hardship waiver. Because their daughter is a lineal descendant, the under-$100,000 homestead hardship waiver IS potentially available to her (1 TAC 373.209), alongside the family farm or ranch waiver. '
        'Recovery is probate-only and sits at Class 7 priority, which is why the deed in Section 2 does so much work.', 'info', 'What happens at the end')]

    # 6
    s += [PageBreak(), H1('6. Who does what'),
      H2('The aunt and uncle'),
      table(['', 'Step'], [['☐', x] for x in [
        'Engage an elder law attorney <b>before filing anything or moving any money</b>. Texas NAELA directory at naela.org; State Bar referral <b>800-252-9690</b>. Free advice line for 60+: <b>800-622-2520, option 3</b>.',
        'Build the full inventory: every account, every parcel, deeds, retirement statements, life insurance, vehicle titles, and any transfer in the last 60 months.',
        'Decide together which spouse is the likely applicant. That choice drives everything else.',
        'Record a Lady Bird or Transfer on Death deed on the homestead. Both sign. Record it with the county clerk.',
        'Sign the durable power of attorney (with express gifting and Medicaid-planning powers), medical power of attorney, HIPAA release and directive to physicians.',
        'Put <b>both</b> names on the STAR+PLUS HCBS interest list: <b>844-438-5658</b> and the YourTexasBenefits.com "Find Support Services" referral. Costs nothing, sets the request date.',
        'Start the accessibility remodeling. It is the best dollar-for-dollar move available.',
        'Buy irrevocable prepaid funeral contracts for both.',
        'Sign the written care agreement with their daughter, drafted by the attorney.',
        'Keep a receipts binder from day one - care costs and home upkeep reduce an estate recovery claim later.',
      ]], [0.3*inch, 6.6*inch]),
      H2('The cousin'),
      table(['', 'Step'], [['☐', x] for x in [
        'Gather proof of what you are giving up: pay stubs, offer letter, separation letter. <b>Documented lost wages are the strongest basis for being paid</b> under Texas rules.',
        'Do not accept cash, gifts, or any transfer of property. Not a car, not a share of land, nothing. It creates a penalty at $262.37 per day.',
        'Make the house your legal home - license, voter registration, mail. This is what makes Medicaid pay tax-free later.',
        'Pay no rent to them. Sign an expense-sharing agreement and pay your share directly to the vendors.',
        'Work under the written care agreement, at the agreed hourly rate, by check, with daily logs of hands-on personal care tasks.',
        'Expect to pay income tax on private-pay wages. Set aside roughly a quarter of it. This changes once Medicaid starts.',
        'Never let anyone name you or your husband as Designated Representative on Medicaid paperwork - it permanently blocks you from being paid.',
        'Learn the Money Follows the Person sentence in Section 3 and be ready to say it at any hospital discharge.',
      ]], [0.3*inch, 6.6*inch]),
      H2('The husband'),
      table(['', 'Step'], [['☐', x] for x in [
        'Be the second paid caregiver under the same agreement, with your own rate, logs and documented lost wages.',
        'Own the records: the receipts binder, the remodeling invoices, every notice and its deadline.',
        'Manage the accessibility remodeling - bids, licensed contractors, invoices kept.',
        'Keep the calendar: the 60-month trust date, annual reviews, and any application deadlines.',
        'Keep some outside taxable income if you can. It protects your household\'s health-insurance subsidy eligibility, which tax-free caregiver pay does not support.',
      ]], [0.3*inch, 6.6*inch])]

    # 7
    s += [PageBreak(), H1('7. What to ask the attorney'),
      P('Bring this page. These are the decisions only a Texas elder law attorney should make, and asking them directly will save an hour of billable time.'),
      table(['#', 'Question'], [[str(i+1), q] for i, q in enumerate([
        'Given our numbers, which spouse should be the applicant, and in which month should we file so the SPRA snapshot lands well?',
        'Trust, annuity, or both? How much goes into an irrevocable trust now to start the 60-month clock, and how much stays liquid for the community spouse annuity later?',
        'Is any of our land a genuine trade or business under MEPD F-4330? If not, can we make it one, or should we list it for sale under F-3130?',
        'How should the retirement accounts be handled - annuitized under F-7230, drawn down, or left alone? Confirm that no RMD exemption applies in Texas.',
        'Draft the care agreement with our daughter around documented lost wages plus hands-on personal care. What hourly rate is defensible as fair market value in our county?',
        'Lady Bird deed or Transfer on Death deed for the homestead - which do you prefer in this county, and what about Est. Code 114.106 exposure?',
        'Walk us through the Money Follows the Person route in advance so we can act on it during a hospitalization instead of improvising.',
        'What is our realistic estate recovery exposure, and does the family farm or ranch hardship waiver apply to us?',
        'Should we expand the SPRA through Form H1275 or a fair hearing, or does the income-first rule make that pointless in our case?',
        'What should we NOT do in the next 60 months?',
      ])], [0.3*inch, 6.6*inch]),
      Spacer(1, 10),
      H2('Key numbers, one place'),
      table(['Item', '2026 figure'], [
        ['Community spouse resource allowance (SPRA)', '$32,532 minimum / $162,660 maximum'],
        ['Community spouse monthly income allowance (MMMNA)', '$4,066.50'],
        ['Applying spouse resource limit', '$2,000'],
        ['Both spouses applying (avoid this)', '$3,000 combined'],
        ['Monthly income limit per applicant', '$2,982 (a Qualified Income Trust fixes income above it)'],
        ['Homestead equity cap', '$752,000 - and waived entirely while a spouse lives there'],
        ['Transfer penalty divisor', '$262.37 per day, 60-month look-back'],
        ['Medicaid CDS attendant pay', '$13.00 to $15.90 per hour; get the FMSA budget in writing'],
        ['Irrevocable trust', '$7,000 to $12,000; 4 to 10 weeks to fund; 60 months to protect'],
        ['Texas home health aide, agency', '$5,720 per month'],
        ['Texas nursing facility, semi-private', '$5,475 per month'],
      ], [3.4*inch, 3.4*inch]),
      Spacer(1, 8),
      H2('Phone numbers'),
      table(['Who', 'Number', 'For'], [
        ['STAR+PLUS HCBS interest list', '<b>844-438-5658</b>', 'Add both names today; get the request date'],
        ['2-1-1 Texas', '<b>2-1-1, option 2</b> (877-541-7905)', 'Applications, program questions, case status'],
        ['Legal Hotline for Texans', '<b>800-622-2520, option 3</b>', 'Free advice for 60+ (orientation, not the planning itself)'],
        ['State Bar of Texas referral', '800-252-9690', 'Find the elder law attorney'],
        ['Texas NAELA', 'naela.org', 'Elder law attorney directory'],
        ['HHS Managed Care Ombudsman', '866-566-8989', 'Plan delays, low hours, denials'],
        ['Aging and Disability Resource Center', '855-937-2372', 'Options counseling'],
        ['Area Agencies on Aging', '800-252-9240', 'Free caregiver training, respite vouchers'],
        ['Medicaid Estate Recovery Program', '800-641-9356', 'Recovery questions (contractor changed Sept. 1, 2026)'],
        ['Adult Protective Services', '800-252-5400', '24/7'],
      ], [2.1*inch, 1.7*inch, 3.0*inch]),
      Spacer(1, 8),
      P('Sources: Texas HHSC MEPD Handbook (F-3600, F-4200 series, F-6500, F-7200 series, I-2130, I-4130, I-4140, I-4160, J-2200, J-4310, J-4400, J-6100, J-6200, Chapter P, Appendix XXXI rev. June 1 2026), CCSE and STAR+PLUS Handbooks, 1 TAC 358 and 373, Texas Estates Code ch. 114, HHSC Provider Finance rate schedules effective September 1 2025, IRS Notice 2014-7 and Publication 926, CareScout Cost of Care data for Texas. Compiled and cross-checked September 3, 2026.', 'tiny')]

    doc.multiBuild(s)
    print('ok')

build(sys.argv[1])
