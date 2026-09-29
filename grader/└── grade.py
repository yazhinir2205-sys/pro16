import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

HTML_FILE = ROOT / "index.html"
CSS_FILE = ROOT / "styles" / "c09x_rollovers.css"

score = 0
results = []


def check(name, marks, condition):
    global score

    if condition:
        score += marks
        results.append(f"PASS: {name} (+{marks})")
    else:
        results.append(f"FAIL: {name} (+0)")


def read_file(path):
    if not path.exists():
        return ""

    return path.read_text(
        encoding="utf-8",
        errors="ignore"
    )


html = read_file(HTML_FILE)
css = read_file(CSS_FILE)

html_lower = html.lower()
css_lower = css.lower()


# ---------------------------------------------------------
# HTML STRUCTURE - 5 marks
# ---------------------------------------------------------

check(
    "HTML5 doctype",
    1,
    "<!doctype html>" in html_lower
)

check(
    "HTML language attribute",
    1,
    re.search(r"<html[^>]+lang\s*=\s*[\"']en[\"']", html_lower)
    is not None
)

check(
    "Header element",
    1,
    "<header" in html_lower and "</header>" in html_lower
)

check(
    "Main element",
    1,
    "<main" in html_lower and "</main>" in html_lower
)

check(
    "Footer element",
    1,
    "<footer" in html_lower and "</footer>" in html_lower
)


# ---------------------------------------------------------
# HEADER AND LOGO - 5 marks
# ---------------------------------------------------------

check(
    "Town Hall logo",
    2,
    "town_hall_logo.gif" in html_lower
)

check(
    "Town Hall heading",
    1,
    "san joaquin valley town hall" in html_lower
)

check(
    "75th Year text",
    1,
    "75" in html_lower and "year" in html_lower
)

check(
    "Logo has alt text",
    1,
    re.search(
        r'<img[^>]*town_hall_logo\.gif[^>]*alt\s*=\s*[\'"][^\'"]+[\'"]',
        html_lower
    ) is not None
)


# ---------------------------------------------------------
# MAIN / SECTION - 5 marks
# ---------------------------------------------------------

check(
    "Section element",
    2,
    "<section" in html_lower and "</section>" in html_lower
)

check(
    "Rollover heading",
    1,
    "an image rollover using background images" in html_lower
)

check(
    "Rollover element with id=image1",
    2,
    re.search(
        r'id\s*=\s*[\'"]image1[\'"]',
        html_lower
    ) is not None
)


# ---------------------------------------------------------
# GUEST SPEAKERS - 5 marks
# ---------------------------------------------------------

check(
    "Jeffrey Toobin",
    1,
    "jeffrey toobin" in html_lower
)

check(
    "Andrew Ross Sorkin",
    1,
    "andrew ross sorkin" in html_lower
)

check(
    "Amy Chua",
    1,
    "amy chua" in html_lower
)

check(
    "Scott Sampson",
    1,
    "scott sampson" in html_lower
)

check(
    "Aside element",
    1,
    "<aside" in html_lower and "</aside>" in html_lower
)


# ---------------------------------------------------------
# FOOTER - 3 marks
# ---------------------------------------------------------

check(
    "Footer copyright",
    1,
    "2016" in html_lower
)

check(
    "Fresno address",
    1,
    "fresno" in html_lower
)

check(
    "Footer paragraph",
    1,
    re.search(
        r"<footer[\s\S]*?<p[\s\S]*?</p>[\s\S]*?</footer>",
        html_lower
    ) is not None
)


# ---------------------------------------------------------
# GENERAL CSS - 7 marks
# ---------------------------------------------------------

check(
    "CSS universal reset",
    1,
    re.search(
        r"\*\s*\{[\s\S]*?margin\s*:\s*0[\s\S]*?padding\s*:\s*0",
        css_lower
    ) is not None
)

check(
    "Body width 850px",
    1,
    re.search(
        r"body[\s\S]*?width\s*:\s*850px",
        css_lower
    ) is not None
)

check(
    "Body centered",
    1,
    re.search(
        r"body[\s\S]*?margin\s*:\s*0\s+auto",
        css_lower
    ) is not None
)

check(
    "Body border",
    1,
    "#931420" in css_lower and "3px" in css_lower
)

check(
    "Header border",
    1,
    re.search(
        r"header[\s\S]*?border-bottom\s*:\s*3px",
        css_lower
    ) is not None
)

check(
    "Logo float",
    1,
    re.search(
        r"header\s+img[\s\S]*?float\s*:\s*left",
        css_lower
    ) is not None
)

check(
    "Footer clear",
    1,
    re.search(
        r"footer[\s\S]*?clear\s*:\s*both",
        css_lower
    ) is not None
)


# ---------------------------------------------------------
# ROLLOVER - 20 marks
# ---------------------------------------------------------

image1_match = re.search(
    r"#image1\s*\{([\s\S]*?)\}",
    css_lower
)

hover_match = re.search(
    r"#image1:hover\s*\{([\s\S]*?)\}",
    css_lower
)

image1_css = image1_match.group(1) if image1_match else ""
hover_css = hover_match.group(1) if hover_match else ""


# Default image - 8 marks

check(
    "Rollover default image",
    8,
    "sampson_dinosaur.jpg" in image1_css
)


# Hover image - 8 marks

check(
    "Rollover hover image",
    8,
    "sorkin_desk260.jpg" in hover_css
)


# Dimensions/repeat - 2 marks

check(
    "Rollover width 260px",
    1,
    re.search(r"width\s*:\s*260px", image1_css) is not None
)

check(
    "Rollover height 260px",
    1,
    re.search(r"height\s*:\s*260px", image1_css) is not None
)


# ---------------------------------------------------------
# NO JAVASCRIPT ROLLOVER - 2 marks
# ---------------------------------------------------------

check(
    "No JavaScript rollover",
    2,
    "onmouseover" not in html_lower
    and "onmouseout" not in html_lower
    and "javascript:" not in html_lower
)


# ---------------------------------------------------------
# SCORE
# ---------------------------------------------------------

print("=" * 60)
print("C09X IMAGE ROLLOVER - AUTOGRADER")
print("=" * 60)

for result in results:
    print(result)

print("-" * 60)
print(f"TOTAL: {score}/50")
print("-" * 60)


# GitHub Classroom / Actions can use exit code
# 0 = tests completed
# 1 = grading failure
sys.exit(0)
