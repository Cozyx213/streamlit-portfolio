"""Autobiography and portfolio of Jake C. Bajenting, CSIT 349 (Applied AI), section F1.

Run with:  streamlit run app.py
"""

import re
from datetime import date
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Jake Bajenting | Portfolio",
    page_icon="👋",
    layout="wide",
)

HERE = Path(__file__).parent


# ---------------------------------------------------------------------------
# Content. Everything about me lives here; the page code below only reads it.
# ---------------------------------------------------------------------------

ME = {
    "name": "Jake C. Bajenting",
    "program": "BS Computer Science",
    "year": "3rd year",
    "school": "Cebu Institute of Technology – University",
    "course": "CSIT 349 · Applied AI",
    "section": "F1",
    "hometown": "Argao, Cebu",
    "github": "https://github.com/Cozyx213",
    "linkedin": "https://www.linkedin.com/in/jake-bajenting-902947274/",
    "email": "bajentingjackie@gmail.com",
}

BIO = (
    "I'm Jake, a third-year Computer Science student at CIT-U from Argao, Cebu. "
    "I like turning messy problems into clean, useful software: mostly web apps, "
    "and lately AI assistants and data projects. Outside class, I play CTFs."
)

BACKGROUND = (
    "I'm from Argao, a heritage town in southern Cebu, and a lot of my projects "
    "started there. In senior high I took the STEM strand at Argao National High "
    "School, which is where I started building things for real people: a Flask web "
    "app for my Practical Research 1 class, then ANHSLINK, a student portal for my "
    "school with news, an e-library, and an online forum."
)

EDUCATION = (
    "Since 2024 I've been taking BS Computer Science at Cebu Institute of "
    "Technology – University. College pushed me past web apps: a JavaFX ticketing "
    "system for my CSIT 228 capstone, C# and .NET for Blazor sites and Windows Forms "
    "agents, and this semester, machine learning with pandas and scikit-learn in "
    "Applied AI."
)

LONGER_STORY = [
    "**How I like to work.** My favorite part of any project is taking an "
    "interesting idea and getting it to a working prototype. I'm open to "
    "collaborating on meaningful software, to volunteer work where tech helps people "
    "move faster, and to learning from other builders while sharing what I know.",
    "**Where I am now.** Summer 2026 brought my first internship, working on an AI "
    "assistant. This semester I'm learning to check a model's numbers instead of "
    "trusting them. The "
    "clustering and classification projects in the Projects tab are where that "
    "started.",
]

INTERESTS = [
    ("🌐", "Useful web apps", "Projects that solve real problems and are pleasant to maintain."),
    ("🛡️", "CTFs and security", "Forensics and steganography challenges in capture-the-flag competitions."),
    ("🧩", "Browser extensions", "Small add-ons that fix daily annoyances, like restyling my school's student portal."),
    ("🤖", "AI assistants", "Chatbots that answer from real documents, and agents that call real tools."),
]

MILESTONES = [
    ("Aug 2023", "First websites", "Built a school website and a Flask web app for STEM students in senior high."),
    ("Sep 2023", "FLATAPS", "Chemistry flashcards with a leaderboard, made for Practical Research 1."),
    ("Jan 2024", "ANHSLINK", "Started a student portal for Argao National High School as its only developer."),
    ("2024", "College", "Started BS Computer Science at CIT-U."),
    ("Apr 2026", "TIX.org capstone", "Top committer on a five-person JavaFX ticketing system for CSIT 228."),
    ("Jun 2026", "First internship", "AI / data science intern, prototyping an AI shipping assistant."),
    ("Oct 2026", "Applied AI", "Clustering and classification projects, and this Streamlit site."),
]

SKILLS_TEXT = (
    "Python is home base. I've used it for Flask and Django sites, data work in "
    "pandas and scikit-learn, and LLM prototypes at my internship. For the web I "
    "reach for Django or Flask with Tailwind CSS. School added Java (JavaFX) and C# "
    "(.NET Blazor), and outside class I use Bash for CTF challenges."
)

# Rating is my own 1–5 self-assessment.
SKILLS = pd.DataFrame(
    [
        ("Python", "Language", 4, "Flask and Django sites, data work, LLM prototypes"),
        ("JavaScript", "Language", 3, "Front-end logic, browser extensions"),
        ("Java", "Language", 3, "TIX.org capstone, GUI coursework"),
        ("C# / .NET", "Language", 3, "Blazor sites, Windows Forms agents"),
        ("SQL", "Language", 3, "SQLite, MySQL, and PostgreSQL"),
        ("Bash", "Language", 3, "CTF challenges and shell automation"),
        ("Django", "Framework", 4, "ANHSLINK, a Django + Supabase class project"),
        ("Flask", "Framework", 4, "FLATAPS and my first school web apps"),
        ("Tailwind CSS", "Framework", 4, "Styling for most of my sites"),
        ("React", "Framework", 3, "Dashboards and my Next.js portfolio"),
        ("Blazor", "Framework", 3, "Argawanon"),
        ("JavaFX", "Framework", 3, "TIX.org"),
        ("pandas", "AI & data", 3, "Applied AI notebooks"),
        ("scikit-learn", "AI & data", 3, "K-means, PCA, random forests"),
        ("LLM apps", "AI & data", 3, "RAG and agents (LangGraph, MCP) at my internship"),
        ("Git & GitHub", "Tools & security", 4, "24 public repos and team projects"),
        ("Docker", "Tools & security", 2, "FLATAPS and internship prototypes"),
        ("CTF forensics", "Tools & security", 3, "Steganography, file carving, XOR"),
    ],
    columns=["Skill", "Category", "Rating", "Where I used it"],
)

# Each project's tools are names from SKILLS, so the two stay linked.
PROJECTS = [
    {
        "title": "AI shipping assistant",
        "icon": "🤖",
        "when": "Jun – Aug 2026",
        "kind": "Internship",
        "role": "AI / data science intern",
        "summary": "Prototypes for a company's AI assistant that answers shipping questions over chat.",
        "tools": ["Python", "LLM apps", "Docker"],
        "outcome": [
            "Built retrieval-augmented generation (RAG) experiments that answer from "
            "the company's own documents.",
            "Tried three agent designs: a plain tool-calling loop, LangGraph, and MCP "
            "(Model Context Protocol).",
            "Containerized a prototype back end with Docker.",
        ],
        "stats": [("Agent prototypes", "3"), ("Length", "3 months")],
        "note": "Internship code stays with the company.",
    },
    {
        "title": "TIX.org",
        "icon": "🎫",
        "when": "Apr – May 2026",
        "kind": "CSIT 228 capstone · team of 5",
        "role": "Developer, and the team's top committer",
        "summary": (
            "A ticketing system where organizations create, assign, and track tasks, "
            "and members can volunteer for open tickets."
        ),
        "tools": ["Java", "JavaFX", "SQL", "Git & GitHub"],
        "outcome": [
            "Role-based dashboards for executives, editors, and members.",
            "Observer-pattern notifications on ticket and comment events, stored per "
            "user as read or unread.",
            "Java 21 with JavaFX (FXML), JDBC, MySQL, and Maven.",
        ],
        "stats": [
            ("My commits", "101", "Out of 259 in total, the most on the team"),
            ("Team size", "5"),
            ("User roles", "3"),
        ],
        "links": [("GitHub", "https://github.com/Cozyx213/CSIT228-Capstone", ":material/code:")],
    },
    {
        "title": "Argawanon",
        "icon": "🏛️",
        "when": "Oct 2026",
        "kind": "School project · solo",
        "role": "Solo developer",
        "summary": "A tourism website about my hometown, Argao, Cebu: its heritage, local food, and nature.",
        "tools": ["C# / .NET", "Blazor", "Tailwind CSS"],
        "outcome": [
            "Home, Explore, and Place Details pages for 9 places, with search by name "
            "or location and a category filter.",
            "A validated review form. Each visitor's reviews live in their own scoped "
            "in-memory store.",
            "Built with .NET 8 Blazor (Interactive Server) and Tailwind CSS.",
        ],
        "stats": [("Places", "9"), ("Pages", "3"), ("Commits", "14")],
        "links": [("GitHub", "https://github.com/Cozyx213/argawanon", ":material/code:")],
    },
    {
        "title": "Pokémon stat profiles",
        "icon": "⚡",
        "when": "Oct 2026",
        "kind": "CSIT 349 activity · solo",
        "role": "Solo: cleaning, feature engineering, modeling",
        "summary": (
            "Grouping fully evolved Pokémon by the shape of their stats, then "
            "predicting which Pokémon are Legendary."
        ),
        "tools": ["Python", "pandas", "scikit-learn"],
        "outcome": [
            "Removed 11 extreme-HP outliers (Chansey, Blissey, Wailord, and others) and "
            "turned raw stats into ratios plus offense and defense biases, so groups "
            "reflect a stat shape, not raw power.",
            "K-means (k = 5) found five archetypes: walls, physical tanks, special "
            "sweepers, bulky special attackers, and physical sweepers.",
            "A class-balanced random forest flagged Legendaries with 96.7% accuracy on "
            "151 test Pokémon and caught all 12 of them (recall 1.00, precision 0.71).",
        ],
        "stats": [("Accuracy", "96.7%"), ("Legendaries caught", "12 / 12"), ("Dataset", "800")],
        "chart": "pokemon",
        "note": "Notebook from class; available on request.",
        "learned": (
            "Legendaries are rare, so plain accuracy hides misses. Lowering the decision "
            "threshold to 0.35 caught sub-legendaries like Terrakion and Regice, at the "
            "cost of a few false alarms."
        ),
    },
    {
        "title": "Iris clustering",
        "icon": "🌸",
        "when": "Sep 2026",
        "kind": "CSIT 349 activity · solo",
        "role": "Solo",
        "summary": (
            "Clustering the classic Iris flowers without labels, then checking how well "
            "the clusters match the real species."
        ),
        "tools": ["Python", "pandas", "scikit-learn"],
        "outcome": [
            "Standardized the 4 features and chose k = 3 from the elbow: inertia falls "
            "from 222 to 140, then only by smaller steps.",
            "83.3% cluster purity and an adjusted Rand index of 0.62. Setosa clustered "
            "perfectly; all 25 mistakes were versicolor vs. virginica.",
        ],
        "stats": [("Purity", "83.3%"), ("ARI", "0.62"), ("Chosen k", "3")],
        "chart": "iris",
        "note": "Notebook from class; available on request.",
        "learned": (
            "The elbow and the silhouette score disagreed (k = 3 vs. k = 2), so choosing "
            "k was a judgment call. I went with 3 because it matches the three real "
            "species."
        ),
    },
    {
        "title": "ANHSLINK",
        "icon": "🏫",
        "when": "2024 – 2025",
        "kind": "Personal project · solo",
        "role": "Solo developer",
        "summary": (
            "A web portal for students of Argao National High School, with news and "
            "updates, an e-library, and an online forum."
        ),
        "tools": ["Python", "Django", "Tailwind CSS"],
        "outcome": [
            "Django back end styled with Tailwind CSS, built and maintained alone over "
            "128 commits.",
            "Hosted on PythonAnywhere; I later started a React front end on Netlify.",
        ],
        "stats": [("Commits", "128"), ("Features", "3")],
        "links": [
            ("GitHub", "https://github.com/Cozyx213/ANHSLINK2", ":material/code:"),
            ("React front end", "https://anhslink.netlify.app/", ":material/open_in_new:"),
        ],
    },
    {
        "title": "FLATAPS",
        "icon": "🧪",
        "when": "2023",
        "kind": "Senior high · Practical Research 1",
        "role": "Lead developer",
        "summary": (
            "Chemistry flashcards for STEM students: elements, ions, polyatomic ions, "
            "and acids, with scoring and a leaderboard."
        ),
        "tools": ["Python", "Flask", "SQL", "JavaScript", "Tailwind CSS", "Docker"],
        "outcome": [
            "Flask and SQLite back end, JavaScript flashcards, and Tailwind CSS styling.",
            "Scores, times, and dates go to a sortable leaderboard.",
            "Deployed on PythonAnywhere, with a recorded video demo.",
        ],
        "stats": [("My commits", "52", "Out of 61 in total"), ("Card categories", "4")],
        "links": [
            ("Video demo", "https://youtu.be/pLfWu_dDv3A", ":material/play_circle:"),
            ("GitHub", "https://github.com/Cozyx213/FLATAPS", ":material/code:"),
        ],
    },
]

# Cluster averages from my Pokémon notebook (fully evolved, HP outliers removed).
POKEMON_GROUPS = pd.DataFrame(
    {
        "Walls": [57.3, 74.8, 130.4, 57.8, 130.5, 43.4],
        "Physical tanks": [76.3, 105.9, 125.8, 64.3, 66.5, 62.0],
        "Special sweepers": [71.7, 72.2, 62.2, 99.2, 105.4, 93.0],
        "Bulky special attackers": [82.8, 77.1, 85.3, 99.5, 87.7, 73.3],
        "Physical sweepers": [82.5, 110.4, 73.9, 74.4, 72.0, 86.6],
    },
    index=pd.Index(["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"], name="Stat"),
)

# Elbow and silhouette results from my Iris notebook.
IRIS = pd.DataFrame(
    {
        "k": [2, 3, 4, 5, 6],
        "Inertia": [222, 140, 114, 91, 82],
        "Silhouette": [0.58, 0.46, 0.39, 0.35, 0.32],
    }
)

REPLIES = {
    "Just saying hi": "Hi back, {name}! Thanks for stopping by.",
    "A project or collaboration": "Thanks, {name}! Turning ideas into working prototypes is my favorite kind of work.",
    "An internship or job": "Thanks for thinking of me, {name}!",
    "Feedback on this site": "Thanks for the feedback, {name}. It goes into the next version.",
}

RATING_REPLIES = [
    "Thanks for being honest. Tell me what to fix in the form.",
    "Thanks. There's room to improve, and I'm on it.",
    "Thanks! Glad it was worth a look.",
    "Thank you, glad you liked it!",
    "Five stars, thank you! That made my day.",
]

COMPONENTS = [
    ("st.title, st.header, st.subheader, st.markdown, st.write, st.caption", "Lecture set", "Hero, section headings, story text"),
    ("st.dataframe", "Lecture set", "Skills table, messages sent this session"),
    ("st.bar_chart, st.altair_chart", "Lecture set", "Skills chart, Pokémon groups, Iris elbow"),
    ("st.button", "Lecture set", "Projects: Previous / Next"),
    ("st.slider", "Lecture set", "Skills: minimum rating · Iris: try a different k"),
    ("st.selectbox", "Lecture set", "Projects: pick a project · Contact: topic"),
    ("st.checkbox", "Lecture set", "Story: longer version · Skills: only skills used here"),
    ("st.text_input, st.text_area", "Lecture set", "Contact form"),
    ("st.radio", "Lecture set", "Skills: chart or table"),
    ("st.multiselect", "Lecture set", "Projects: filter by tool"),
    ("st.sidebar, st.columns", "Lecture set", "Profile sidebar · side-by-side layout throughout"),
    ("st.image", "Extra", "Profile photo"),
    ("st.tabs", "Extra", "Story, Skills, Projects, Contact"),
    ("st.metric", "Extra", "Hero numbers, project stats, Iris explorer"),
    ("st.form", "Extra", "Contact form"),
    ("st.session_state", "Extra", "Project navigation, sent messages, rating replies"),
    ("st.download_button", "Extra", "Résumé (.md) and skills (.csv)"),
    ("Custom theme", "Extra", ".streamlit/config.toml: accent colors and fonts"),
    ("st.expander", "Extra", "What I learned, this table"),
    ("st.feedback, st.toast, st.balloons", "Extra", "Contact: star rating and replies"),
    ("st.badge, st.link_button, st.pills, st.container", "Extra", "Tags, links, Pokémon group picker, bordered cards"),
]

STANDIN_PHOTO = """<svg xmlns="http://www.w3.org/2000/svg" width="480" height="480" viewBox="0 0 480 480">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#0d9488"/><stop offset="1" stop-color="#4f46e5"/></linearGradient></defs>
<rect width="480" height="480" rx="40" fill="url(#bg)"/>
<circle cx="240" cy="200" r="80" fill="#fff" fill-opacity="0.92"/>
<path d="M88 440c0-92 68-148 152-148s152 56 152 148z" fill="#fff" fill-opacity="0.92"/>
<text x="240" y="70" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="26"
 font-weight="700" letter-spacing="4" fill="#fff">PHOTO STAND-IN</text>
</svg>"""

EMAIL_RE = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def profile_photo():
    """My photo from assets/profile.*, or a labeled stand-in until one is added."""
    for ext in ("jpg", "jpeg", "png", "webp"):
        path = HERE / "assets" / f"profile.{ext}"
        if path.exists():
            return str(path), ME["name"]
    return STANDIN_PHOTO, "Photo stand-in"


def tool_badges(tools):
    return " ".join(f":gray-badge[{tool}]" for tool in tools)


def skills_table():
    table = SKILLS.copy()
    table["Projects"] = [sum(skill in p["tools"] for p in PROJECTS) for skill in table["Skill"]]
    return table[["Skill", "Category", "Rating", "Projects", "Where I used it"]]


def skills_chart(data):
    return (
        alt.Chart(data)
        .mark_bar(cornerRadiusEnd=4)
        .encode(
            x=alt.X(
                "Rating:Q",
                title="Self-rating (1–5)",
                scale=alt.Scale(domain=[0, 5]),
                axis=alt.Axis(tickCount=5, format="d"),
            ),
            y=alt.Y("Skill:N", sort="-x", title=None, axis=alt.Axis(labelOverlap=False)),
            color=alt.Color("Category:N", legend=alt.Legend(orient="top", title=None)),
            tooltip=["Skill", "Category", "Rating", "Projects", "Where I used it"],
        )
        .properties(height=max(160, 32 * len(data)))
    )


def resume_markdown():
    lines = [
        f"# {ME['name']}",
        f"{ME['program']}, {ME['year']} · {ME['school']}",
        f"GitHub: {ME['github']} · LinkedIn: {ME['linkedin']} · Email: {ME['email']}",
        "",
        "## Summary",
        BIO,
        "",
        "## Skills",
    ]
    for category, group in SKILLS.groupby("Category", sort=False):
        lines.append(f"- **{category}:** {', '.join(group['Skill'])}")
    lines += ["", "## Projects"]
    for p in PROJECTS:
        lines += [f"### {p['title']} ({p['when']})", f"*{p['role']}* · {', '.join(p['tools'])}", "", p["summary"]]
        lines += [f"- {item}" for item in p["outcome"]]
        lines.append("")
    lines.append("## Milestones")
    lines += [f"- **{when}:** {title}. {detail}" for when, title, detail in MILESTONES]
    return "\n".join(lines) + "\n"


def step_project(titles, offset):
    current = titles.index(st.session_state.project_pick)
    st.session_state.project_pick = titles[(current + offset) % len(titles)]


def send_message():
    ss = st.session_state
    name, email, message = ss.c_name.strip(), ss.c_email.strip(), ss.c_message.strip()
    if not name or not message:
        ss.c_flash = ("error", "Please add your name and a message before sending.")
        return
    if email and not EMAIL_RE.fullmatch(email):
        ss.c_flash = ("error", "That email address doesn't look right. Fix it, or leave it blank.")
        return
    ss.inbox.append({"Name": name, "Email": email or "—", "About": ss.c_reason, "Message": message})
    ss.c_flash = ("success", REPLIES[ss.c_reason].format(name=name) + " Your message is saved below.")
    ss.celebrate = True
    ss.c_message = ""


def rated():
    stars = st.session_state.site_rating
    if stars is not None:
        st.session_state.toast = RATING_REPLIES[stars]


def pokemon_chart():
    groups = st.pills(
        "Groups to compare",
        list(POKEMON_GROUPS.columns),
        selection_mode="multi",
        default=list(POKEMON_GROUPS.columns),
        key="poke_groups",
    )
    if not groups:
        st.info("Pick at least one group to compare.")
        return
    data = POKEMON_GROUPS[groups].reset_index().melt(id_vars="Stat", var_name="Group", value_name="Average")
    st.bar_chart(data, x="Stat", y="Average", color="Group", stack=False, sort=False, height=320)
    st.caption("Average base stats per K-means group. Walls tower on both defenses; sweepers trade bulk for Speed.")


def iris_explorer():
    controls, charts = st.columns([1, 2], gap="large")
    k = controls.slider("Try a different k", 2, 6, 3, key="iris_k")
    by_k = IRIS.set_index("k")
    row = by_k.loc[k]
    prev = by_k.loc[k - 1] if k > 2 else None
    a, b = controls.columns(2)
    a.metric(
        "Inertia",
        f"{row['Inertia']:.0f}",
        delta=None if prev is None else f"{row['Inertia'] - prev['Inertia']:.0f}",
        delta_color="inverse",
        help="Lower is tighter clusters. The change is versus k − 1.",
        border=True,
    )
    b.metric(
        "Silhouette",
        f"{row['Silhouette']:.2f}",
        delta=None if prev is None else f"{row['Silhouette'] - prev['Silhouette']:.2f}",
        help="Higher is better-separated clusters. The change is versus k − 1.",
        border=True,
    )
    controls.caption("k = 3 is where the elbow bends. Silhouette prefers k = 2 because setosa sits far from the other two.")
    marker = alt.Chart(pd.DataFrame({"k": [k]})).mark_rule(strokeDash=[4, 4], color="#94a3b8").encode(x="k:O")
    for col, metric in zip(charts.columns(2), ("Inertia", "Silhouette")):
        line = (
            alt.Chart(IRIS)
            .mark_line(point=True)
            .encode(
                x=alt.X("k:O", title="k", axis=alt.Axis(labelAngle=0)),
                y=alt.Y(f"{metric}:Q", title=metric, scale=alt.Scale(zero=False), axis=alt.Axis(tickCount=4)),
                tooltip=["k", metric],
            )
        )
        col.altair_chart((line + marker).properties(height=240))


# ---------------------------------------------------------------------------
# Page
# ---------------------------------------------------------------------------

st.session_state.setdefault("inbox", [])
if toast := st.session_state.pop("toast", None):
    st.toast(toast, icon="⭐")

with st.sidebar:
    st.markdown(f"### {ME['name']}")
    st.caption(f"{ME['program']} · {ME['year']}  \n{ME['school']}")
    with st.container(horizontal=True, gap="xsmall"):
        st.badge(ME["course"], color="blue")
        st.badge(f"Section {ME['section']}", icon=":material/class:", color="primary")
    st.divider()
    st.markdown("**Find me**")
    st.link_button("GitHub", ME["github"], icon=":material/code:", width="stretch")
    st.link_button("LinkedIn", ME["linkedin"], icon=":material/work:", width="stretch")
    st.link_button("Email", f"mailto:{ME['email']}", icon=":material/mail:", width="stretch")
    st.divider()
    st.download_button(
        "Download my résumé",
        resume_markdown(),
        file_name="Jake_Bajenting_resume.md",
        mime="text/markdown",
        icon=":material/download:",
        type="primary",
        width="stretch",
    )
    st.caption("Built with Streamlit for CSIT 349 · Applied AI.")

# Hero
photo, photo_caption = profile_photo()
left, right = st.columns([1, 2.6], gap="large", vertical_alignment="center")
with left:
    st.image(photo, caption=photo_caption, width="stretch")
with right:
    st.title(ME["name"])
    with st.container(horizontal=True, gap="xsmall"):
        st.badge(f"{ME['program']} · {ME['year']}", icon=":material/school:", color="primary")
        st.badge(f"{ME['course']} · Section {ME['section']}", icon=":material/class:", color="blue")
        st.badge(ME["hometown"], icon=":material/location_on:", color="gray")
    st.write(BIO)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Projects", len(PROJECTS), help="Projects on this page", border=True)
    m2.metric("Public repos", 24, help="On my GitHub", border=True)
    m3.metric("Coding since", "2023", border=True)
    m4.metric("Top accuracy", "96.7%", help="My Pokémon Legendary classifier", border=True)

story_tab, skills_tab, projects_tab, contact_tab = st.tabs(["📖 Story", "🛠️ Skills", "🚀 Projects", "✉️ Contact"])

with story_tab:
    st.header("My story")
    left, right = st.columns([3, 2], gap="large")
    with left:
        st.subheader("Background")
        st.write(BACKGROUND)
        st.subheader("Education")
        st.write(EDUCATION)
        if st.checkbox("Read the longer version"):
            for paragraph in LONGER_STORY:
                st.markdown(paragraph)
        st.subheader("What I'm into")
        interest_cols = st.columns(2)
        for i, (icon, title, text) in enumerate(INTERESTS):
            with interest_cols[i % 2].container(border=True):
                st.markdown(f"**{icon} {title}**")
                st.write(text)
    with right:
        st.subheader("Milestones")
        with st.container(border=True):
            for when, title, detail in MILESTONES:
                st.markdown(f":primary[**{when}**] · **{title}**  \n{detail}")

with skills_tab:
    st.header("Skills")
    left, right = st.columns([2, 3], gap="large")
    with left:
        st.write(SKILLS_TEXT)
        st.caption("Ratings are my own 1–5 self-assessment. *Projects* counts the projects on this page that use each skill.")
        view = st.radio("Show as", ["Chart", "Table"], horizontal=True)
        min_rating = st.slider("Minimum self-rating", 1, 5, 1)
        only_used = st.checkbox("Only skills used in the projects on this page")
    shown = skills_table()
    shown = shown[shown["Rating"] >= min_rating]
    if only_used:
        shown = shown[shown["Projects"] > 0]
    with right:
        if shown.empty:
            st.info("No skills match those filters. Try a lower minimum rating.")
        elif view == "Chart":
            st.altair_chart(skills_chart(shown))
        else:
            st.dataframe(
                shown,
                hide_index=True,
                column_config={
                    "Rating": st.column_config.ProgressColumn("Self-rating", min_value=0, max_value=5, format="%d / 5"),
                    "Projects": st.column_config.NumberColumn("Projects", help="Projects on this page that use it"),
                },
            )
        st.download_button(
            "Download skills as CSV",
            shown.to_csv(index=False),
            file_name="jake_bajenting_skills.csv",
            mime="text/csv",
            icon=":material/table:",
        )

with projects_tab:
    st.header("Projects")
    st.write(
        f"{len(PROJECTS)} things I've built, from my first Flask app in senior high to this "
        "semester's machine learning. Filter by tool, or pick one below for the details."
    )
    all_tools = sorted({tool for p in PROJECTS for tool in p["tools"]}, key=str.lower)
    picked = st.multiselect("Filter by tool", all_tools, placeholder="All tools")
    matches = [p for p in PROJECTS if not picked or set(picked) & set(p["tools"])]
    st.caption(f"Showing {len(matches)} of {len(PROJECTS)} projects.")

    cards = st.columns(3)
    for i, p in enumerate(matches):
        with cards[i % 3].container(border=True):
            st.markdown(f"**{p['icon']} {p['title']}**")
            st.caption(f"{p['when']} · {p['kind']}")
            st.write(p["summary"])
            st.markdown(tool_badges(p["tools"]))

    st.subheader("Take a closer look")
    titles = [p["title"] for p in matches]
    if st.session_state.get("project_pick") not in titles:
        st.session_state.project_pick = titles[0]
    pick_col, prev_col, next_col = st.columns([6, 1, 1], vertical_alignment="bottom")
    pick_col.selectbox("Project", titles, key="project_pick")
    prev_col.button("Previous", icon=":material/arrow_back:", on_click=step_project, args=(titles, -1), width="stretch")
    next_col.button("Next", icon=":material/arrow_forward:", on_click=step_project, args=(titles, 1), width="stretch")

    p = next(p for p in matches if p["title"] == st.session_state.project_pick)
    with st.container(border=True):
        st.markdown(f"### {p['icon']} {p['title']}")
        st.caption(f"{p['when']} · {p['kind']}")
        for col, (label, value, *help_text) in zip(st.columns(4), p["stats"]):
            col.metric(label, value, help=help_text[0] if help_text else None, border=True)
        st.write(p["summary"])
        st.markdown(f"**My role:** {p['role']}")
        st.markdown(f"**Tools:** {tool_badges(p['tools'])}")
        st.markdown("**Outcome**")
        st.markdown("\n".join(f"- {item}" for item in p["outcome"]))
        if "learned" in p:
            with st.expander("What I learned"):
                st.write(p["learned"])
        if links := p.get("links"):
            with st.container(horizontal=True):
                for label, url, icon in links:
                    st.link_button(label, url, icon=icon)
        if note := p.get("note"):
            st.caption(note)
        if chart := p.get("chart"):
            st.markdown("**Explore the results**")
            if chart == "pokemon":
                pokemon_chart()
            else:
                iris_explorer()

with contact_tab:
    st.header("Get in touch")
    left, right = st.columns([3, 2], gap="large")
    with left:
        with st.form("contact", enter_to_submit=False):
            name_col, email_col = st.columns(2)
            name_col.text_input("Your name *", key="c_name", placeholder="Juan dela Cruz")
            email_col.text_input("Your email", key="c_email", placeholder="you@example.com")
            st.selectbox("What's this about?", list(REPLIES), key="c_reason")
            st.text_area("Message *", key="c_message", max_chars=1000, height=140)
            st.form_submit_button("Send message", type="primary", icon=":material/send:", on_click=send_message)
        if flash := st.session_state.pop("c_flash", None):
            kind, text = flash
            (st.success if kind == "success" else st.error)(text)
        if st.session_state.pop("celebrate", False):
            st.balloons()
        st.caption(
            "This form is a class demo: messages stay in your browser session and aren't "
            "emailed. For a real reply, use the Email button in the sidebar."
        )
    with right:
        with st.container(border=True):
            st.markdown("**Rate this page**")
            st.feedback("stars", key="site_rating", on_change=rated)
            if (stars := st.session_state.site_rating) is not None:
                st.caption(f"You gave it {stars + 1} / 5. {RATING_REPLIES[stars]}")
        with st.container(border=True):
            st.metric("Messages sent this session", len(st.session_state.inbox))
            if st.session_state.inbox:
                st.dataframe(pd.DataFrame(st.session_state.inbox), hide_index=True)

st.divider()
st.caption(f"© {date.today().year} {ME['name']} · {ME['course']} · Section {ME['section']} · Built with Streamlit")
with st.expander("How this page uses Streamlit"):
    st.dataframe(
        pd.DataFrame(COMPONENTS, columns=["Component", "Type", "Where it's used"]),
        hide_index=True,
    )
