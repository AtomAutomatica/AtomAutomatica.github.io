#!/usr/bin/env python3
"""
Find 4-star hotel deals in Dallas, TX under $200/night for a specific stay.

Criteria (hard-coded to the requested search; edit the CONFIG block to change):
  - Quality: 4-star hotels
  - Dates:   Check-in Mon 2026-06-08, check-out Fri 2026-06-12 (4 nights)
  - Price:   <= $200 per night
  - Output:  hotel name, exact price per night, and a direct booking URL

USAGE
-----
    pip install playwright
    python -m playwright install chromium
    python scripts/dallas_hotel_deals.py

NOTE ON EXECUTION ENVIRONMENT
-----------------------------
This script targets Booking.com via Playwright. It must be run from a network
that can reach the public internet. It will NOT work from a sandbox whose
egress proxy denies travel sites (e.g. returns HTTP 403 `host_not_allowed`
for booking.com / expedia.com / kayak.com) -- that is a network-policy block,
not a selector problem, so changing target sites will not help there.

Booking.com also serves bot challenges to datacenter IPs; if you get an empty
result or a challenge page, run with HEADLESS=False and solve it once, or run
from a residential connection.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from urllib.parse import urlencode

from playwright.sync_api import sync_playwright

# --------------------------- CONFIG ---------------------------
CITY = "Dallas, Texas"
CHECKIN = "2026-06-08"   # Monday
CHECKOUT = "2026-06-12"  # Friday
NIGHTS = 4
ADULTS = 2
ROOMS = 1
STARS = 4
MAX_PRICE_PER_NIGHT = 200
CURRENCY = "USD"
HEADLESS = True
# -------------------------------------------------------------


@dataclass
class Hotel:
    name: str
    price_per_night: float
    url: str


def build_search_url() -> str:
    params = {
        "ss": CITY,
        "checkin": CHECKIN,
        "checkout": CHECKOUT,
        "group_adults": ADULTS,
        "no_rooms": ROOMS,
        "group_children": 0,
        "selected_currency": CURRENCY,
        # nflt = filters: class=4 (4-star), price upper bound per night
        "nflt": f"class={STARS};price={CURRENCY}-min-{MAX_PRICE_PER_NIGHT}-1",
    }
    return "https://www.booking.com/searchresults.html?" + urlencode(params)


def parse_price(text: str) -> float | None:
    """Extract a numeric price from strings like 'US$412' or '$1,234'."""
    m = re.search(r"[\d,]+", text.replace("\xa0", " "))
    if not m:
        return None
    return float(m.group(0).replace(",", ""))


def scrape() -> list[Hotel]:
    url = build_search_url()
    results: list[Hotel] = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        page = browser.new_page(locale="en-US")
        page.goto(url, wait_until="domcontentloaded", timeout=60_000)

        # Booking.com property cards
        page.wait_for_selector('[data-testid="property-card"]', timeout=30_000)
        cards = page.query_selector_all('[data-testid="property-card"]')

        for card in cards:
            title_el = card.query_selector('[data-testid="title"]')
            price_el = card.query_selector('[data-testid="price-and-discounted-price"]')
            link_el = card.query_selector('a[data-testid="title-link"]')
            if not (title_el and price_el and link_el):
                continue

            name = title_el.inner_text().strip()
            total = parse_price(price_el.inner_text())
            href = link_el.get_attribute("href") or ""
            if total is None or not href:
                continue

            per_night = round(total / NIGHTS, 2)
            if per_night > MAX_PRICE_PER_NIGHT:
                continue

            if href.startswith("/"):
                href = "https://www.booking.com" + href
            results.append(Hotel(name=name, price_per_night=per_night, url=href))

        browser.close()

    results.sort(key=lambda h: h.price_per_night)
    return results


def main() -> None:
    hotels = scrape()
    if not hotels:
        print("No matching hotels found (or the site served a bot challenge).")
        return

    print(f"\n4-star hotels in {CITY} | {CHECKIN} -> {CHECKOUT} "
          f"({NIGHTS} nights) | <= ${MAX_PRICE_PER_NIGHT}/night\n")
    for h in hotels:
        print(f"- {h.name}")
        print(f"    ${h.price_per_night:.2f}/night")
        print(f"    {h.url}")


if __name__ == "__main__":
    main()
