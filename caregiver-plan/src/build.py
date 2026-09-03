# -*- coding: utf-8 -*-
import sys
from render import *
from reportlab.platypus import PageBreak
import part1, part2, part_cousin, part_money_a, part_money_b, part_timeline, part_care, part_directory
TITLE = 'Texas Family Caregiver Master Plan'
out = sys.argv[1] if len(sys.argv) > 1 else 'Texas_Family_Caregiver_Master_Plan.pdf'
doc = Doc(out, TITLE)
story = []
story += part1.cover()
story += [H1('Contents'), toc(), PageBreak()]
story += part1.how_to_use()
story += part1.one_page()
story += part2.programs()
story += part2.aunt_uncle_steps()
story += part_cousin.cousin_steps()
story += part_cousin.husband_steps()
story += part_money_a.money_a()
story += part_money_b.money_b()
story += part_timeline.timeline()
story += part_care.care()
story += part_timeline.pitfalls()
story += part_directory.directory()
doc.multiBuild(story)
print('built', out)
