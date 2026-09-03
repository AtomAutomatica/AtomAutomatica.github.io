# Texas Family Caregiver Master Plan

`Texas_Family_Caregiver_Master_Plan.pdf` is a step-by-step plan for an elderly married couple in Texas and the niece (and her husband) who will move in and become their paid Medicaid attendants.

It covers the Texas programs that pay relatives (Community Attendant Services, STAR+PLUS HCBS, Community First Choice, the Consumer Directed Services option), 2026 dollar limits and hourly rates, itemized steps for each person, a 120-day timeline, an income model, tax treatment, VA stacking, a care-quality plan, pitfalls, and a verified phone and form directory.

Research date: September 3, 2026. Sources are Texas HHSC handbooks and rate schedules, the Texas Administrative Code, CMS, IRS, VA, SSA and OPM publications. Not legal, tax or medical advice.

## Rebuilding the PDF

```
pip install reportlab
cd src && python3 build.py ../Texas_Family_Caregiver_Master_Plan.pdf
```

Fonts: DejaVu Sans and Liberation Sans (paths in `src/render.py`).
