# -*- coding: utf-8 -*-
"""Section 8: Highest level of care."""
from reportlab.lib.units import inch
from reportlab.platypus import Spacer, PageBreak
from render import *

def care():
    return [
        PageBreak(), H1('8. Delivering the highest level of care'),
        P('Paid hours are the floor. What separates good care from great care is training, the right equipment (which Medicaid will buy if you ask by name), '
          'scheduled relief for the caregiver, and knowing the legal line for medical tasks. Everything below is free or Medicaid-paid unless a price is shown.'),
        H2('8.1 Free and low-cost training for the cousin and her husband'),
        table(['Training', 'Where', 'Cost', 'Why it matters'], [
            ['Family Caregiver Support Program (Title III-E): caregiver education, counseling, support groups, respite vouchers', 'Local Area Agency on Aging, <b>800-252-9240</b>. A niece caring for an aunt or uncle 60+ is an eligible caregiver (AAA Caregiver Eligibility Guide, Appendix VI).', 'Free', 'Enrolls you as the recognized family caregiver and unlocks vouchers'],
            ['Dementia care: UCLA Alzheimer\'s and Dementia Care caregiver videos; Teepa Snow Positive Approach to Care videos; Alzheimer\'s Association classes and 24/7 helpline', 'uclahealth.org (search "caregiver training videos"); teepasnow.com; <b>800-272-3900</b>', 'Free', 'Bathing, agitation, wandering, repetitive questions, safe redirection'],
            ['Fall prevention: CDC STEADI caregiver brochure and "Check for Safety" home checklist', 'cdc.gov/steadi', 'Free', 'Falls are the number one reason a home placement fails. Do the checklist before the H2060 visit and after every fall.'],
            ['AARP Prepare to Care workbook', 'learn.aarp.org/prepare-to-care-guide', 'Free', 'Team, plan, records, self-care'],
            ['CPR / AED / First Aid (American Heart Association Heartsaver or Red Cross)', 'Local training centers; Red Cross <b>800-733-2767</b>; ask the AAA about free classes', 'About $70 to $120', 'Not required for CDS, but expected of a professional-quality caregiver'],
            ['Certified Nurse Aide (Texas NATCEP): 60 classroom hours (HHSC online course is free) + 40 clinical hours + Prometric exam', 'hhs.texas.gov (search "NATCEP"); Prometric <b>800-488-5787</b>. Nursing facilities often train free in exchange for work ("train-to-hire").', 'Exam $120 ($31 written + $89 skills); tuition $0 to $1,500', 'Does not change the CDS budget, but justifies paying the top wage in it and opens agency shifts if ever needed. Lapses after 24 months without verified paid aide work.'],
            ['Pressure-injury prevention basics (NPIAP); medication reconciliation checklist (AHRQ)', 'npiap.com; ahrq.gov', 'Free', 'Reposition every 2 hours; skin checks; one current medication list'],
        ], [2.0 * inch, 2.1 * inch, 0.9 * inch, 1.9 * inch]),
        H2('8.2 What Medicaid and Medicare will buy to make care better (ask by name)'),
        table(['Item', 'Source', 'Limit', 'How to get it'], [
            ['Skilled nursing, physical/occupational/speech therapy, home health aide (while skilled care is active)', 'Medicare home health', '$0; must be homebound with an intermittent skilled need', 'Ask the PCP for a home-health referral after every hospitalization, fall or new diagnosis. Runs alongside Medicaid attendant hours.'],
            ['Hospital bed, pressure mattress, wheelchair, walker, shower chair, lift, incontinence supplies', 'Medicare Part B and Texas Medicaid state-plan DME first; then STAR+PLUS HCBS adaptive aids', 'HCBS adaptive aids and medical supplies: <b>$10,000 per person per ISP year</b> (MCO may exceed)', 'PCP writes the order with medical necessity; MCO service coordinator routes it. Never buy out of pocket first; there is no retroactive reimbursement.'],
            ['Grab bars, ramps, roll-in shower, widened doors, bathroom and kitchen modifications', 'STAR+PLUS HCBS minor home modifications', '<b>$7,500 lifetime per person</b> + $300/year repairs; done within 90 business days of the ISP', 'Each spouse has a separate $7,500. Ask at the first ISP meeting.'],
            ['Dentures, extractions, routine and emergency dental', 'STAR+PLUS HCBS dental', '<b>$5,000 per person per ISP year</b>; MCO can waive for oral surgery; referral within 90 days of request', 'Adult Medicaid otherwise covers almost no dental. Ask.'],
            ['Emergency response pendant', 'STAR+PLUS HCBS ERS (or CAS/CCSE ERS)', '12 units per plan year', 'Justified for the hours the caregivers are out of the house; document that schedule.'],
            ['Home-delivered meals', 'STAR+PLUS HCBS (no limit) or Title XX (H2060 score 20+, no means test)', 'Minimum 5 hot meals/week', 'Frees attendant minutes for hands-on care.'],
            ['Nursing, therapies, cognitive rehabilitation', 'STAR+PLUS HCBS', 'No dollar cap; based on need; inside the 202% cost ceiling', 'Skilled nursing can also be delivered through CDS.'],
            ['Rides or mileage to medical appointments', 'MCO transportation line; Medical Transportation Program <b>877-633-8747</b>', 'Book 2 workdays ahead (5 days out of county)', 'The Individual Transportation Participant program pays a relative mileage for driving; separate from CDS wages.'],
            ['Adult day center (Day Activity and Health Services)', 'MCO (Medicaid) or caseworker (Title XX)', 'Up to 10 units/week; physician order Form 3055', 'Structured respite; note it reduces attendant hours for those blocks.'],
            ['Hospice and palliative care at home', 'Medicare', 'No STAR+PLUS disenrollment; waiver hours continue for non-duplicative needs', 'STAR+PLUS Handbook 3200.'],
        ], [1.8 * inch, 1.5 * inch, 1.6 * inch, 2.0 * inch]),
        H2('8.3 Respite: the relief that keeps the plan alive'),
        bullets([
            '<b>STAR+PLUS HCBS respite:</b> up to <b>30 days (720 hours) per person per ISP year</b>, in-home or out-of-home, and in-home respite can be delivered through CDS by a hired backup attendant (STAR+PLUS Handbook 7300 and 8212). Respite exists to relieve the unpaid caregiving (nights, weekends), so document those unpaid hours; confirm the MCO\'s policy on respite when the same person is also the paid attendant.',
            '<b>AAA respite vouchers:</b> HHSC guideline $300 per quarter; many AAAs award more. The voucher provider must be 18+ and "anyone except immediate family living in the home," so the husband cannot be the voucher worker; a friend, neighbor or agency can.',
            '<b>Texas Lifespan Respite / Take Time Texas:</b> HHSC\'s searchable respite-provider directory (respite.hhs.state.tx.us) for in-home and out-of-home providers by county.',
            '<b>Support:</b> AAA and Alzheimer\'s Association support groups (free); Caregiver Action Network help desk 855-227-3640; 988 crisis line, call or text, any hour.',
        ]),
        H2('8.4 The legal line for medical tasks (Texas Board of Nursing, 22 TAC Chapter 225)'),
        table(['An unlicensed attendant MAY do (with written RN delegation, or as a "health maintenance activity" the client can direct)', 'An unlicensed attendant may NEVER do'], [
            ['Oral, sublingual, topical, eye, ear, nose and inhaler medications; pill-organizer medications; insulin and other subcutaneous diabetes injections; medications through an established feeding tube; intermittent catheterization; tube irrigation; tracheostomy care and suctioning; routine oxygen; vital signs and glucose checks (225.8, 225.10, 225.11).',
             'Nursing assessments or care planning; dose calculations (other than measuring a prescribed liquid or splitting a pre-calculated tablet); injections other than the diabetes exceptions; taking verbal or telephone physician orders; giving the first dose of a new medication without RN documentation (225.13).'],
        ], [3.45 * inch, 3.45 * inch]),
        P('Ask the MCO nurse or the Medicare home-health RN for written delegation before doing any nursing task. It protects the cousin legally and it is what a professional agency would require.', 'small'),
        H2('8.5 The written care plan (one per spouse)'),
        P('Keep a one-page daily care plan and a daily log for each spouse. It is good care, it is audit protection (the Form 1720 service log must match EVV), and it is the strongest evidence at the next annual reassessment.'),
        checkbox_list([
            'Diagnoses, allergies, physicians, pharmacy, MCO service coordinator name and number',
            'Medication list with times, who sets up, who hands, who checks; RN delegation on file for anything beyond reminders',
            'Transfer and mobility method (gait belt, walker, lift), fall-risk mitigations from the STEADI checklist',
            'Bathing, skin-check and repositioning schedule; toileting and continence schedule; fluids and nutrition targets',
            'Cognition and behavior notes (what triggers agitation, what calms); wandering safeguards',
            'Who covers which hours (cousin, husband, backup on Form 1740), and the respite calendar',
            'Emergency plan: 911 criteria, hospital preference, copies of Medical POA and Directive to Physicians in the binder and on the fridge',
            'A 7-day ADL diary before every assessment, recording typical and worst days',
        ]),
        H2('8.6 Oversight, complaints and protection'),
        table(['Problem', 'Call', 'Notes'], [
            ['MCO slow, low hours, no assessment, service coordinator not responding', 'MCO member services first, then HHSC Managed Care Ombudsman <b>866-566-8989</b> (Mon-Fri 8-5)', 'Online form: heartbep-ext.hhs.state.tx.us. Often resolves hour disputes faster than an appeal.'],
            ['HHSC eligibility (MEPD), caseworker or interest-list problems', 'HHS Office of the Ombudsman <b>877-787-8999</b>', ''],
            ['Denied or reduced hours or items', 'MCO appeal within <b>60 days</b>; ask for continuation of benefits within <b>10 days</b>; State Fair Hearing within <b>120 days</b> of the MCO decision; HCBS eligibility denials (Form H2065-D): fair hearing within 90 days', 'Decision within 90 days. Appeal every low authorization.'],
            ['Abuse, neglect, self-neglect or financial exploitation of an adult at home', 'Adult Protective Services <b>800-252-5400</b> (24/7); txabusehotline.org', 'Reporting is mandatory for everyone in Texas.'],
            ['Complaint about a licensed home-health/attendant agency or a facility', 'HHSC Complaint and Incident Intake <b>800-458-9858</b>', 'Long-Term Care Ombudsman 800-252-2412 is for facility residents only.'],
            ['Medicaid fraud, or you are asked to sign for hours not worked', 'HHSC Office of Inspector General <b>800-436-6184</b>', 'CDS employers and employees are audited on EVV and logs. Never bill time you are merely present.'],
            ['Hospital wants to discharge before home supports are ready', 'Acentra Health (Texas Medicare QIO) <b>888-315-0636</b> before midnight on the discharge day', 'Use the "Important Message from Medicare" fast appeal; no charge while under review.'],
        ], [2.2 * inch, 2.6 * inch, 2.1 * inch]),
    ]
