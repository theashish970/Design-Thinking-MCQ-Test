import streamlit as st
import random

st.set_page_config(page_title="Design Thinking MCQ Exam", layout="wide")
st.title("📝 Design Thinking – Full MCQ Exam")

# ---------------- QUESTION BANK (ALL QUESTIONS) ---------------- #
QUESTION_BANK = [

# -------- WEEK 1 --------
("What is the first Noble Truth according to Lord Buddha?",
 ["Accept suffering","Origin of suffering","Cessation of suffering","Path leading to cessation"],
 "Accept suffering"),

("How does empathy in Design Thinking relate to Buddha’s teachings?",
 ["Finding cause of suffering","Understanding others’ feelings","Cessation of suffering","Eightfold path"],
 "Understanding others’ feelings"),

("What tool visualizes the steps a customer goes through?",
 ["SWOT","Customer Journey Mapping","Brainstorming","Business Model Canvas"],
 "Customer Journey Mapping"),

("What best describes a Customer Persona?",
 ["Fictional typical user","Customer problem report","Complaints list","Business summary"],
 "Fictional typical user"),

("Which tool captures and organizes thoughts during design thinking?",
 ["Notebook","WhatsApp","Sticky Notes","Teacups"],
 "Sticky Notes"),

("Why is it important to use real observations?",
 ["Customers forget","More accurate data","Takes time","More fun"],
 "More accurate data"),

("What should be documented before Analyze stage?",
 ["Solutions","Steps and emotions","Marketing","Specifications"],
 "Steps and emotions"),

("Final step to ensure Customer Journey Map completeness?",
 ["Survey","Second persona","Peer feedback","Mentor review"],
 "Second persona"),

("IDEO team problem with senior citizen medication?",
 ["Forget medicine","Cannot open bottle","Wrong medicine","Less supply"],
 "Cannot open bottle"),

# -------- WEEK 2 --------
("Multi-Why Analysis is effective for?",
 ["Statistical problems","Simple problems","Known root cause","Unknown root cause"],
 "Unknown root cause"),

("Best way to resolve conflicts in Design Thinking?",
 ["Avoid conflicts","Satisfy all parties","Accept conflicts","Focus on customer"],
 "Satisfy all parties"),

("Who coined the 5 Why method?",
 ["Apple","Toyota","Google","Microsoft"],
 "Toyota"),

("Samudaya in Design Thinking refers to?",
 ["Analyze","Define","Introspect","Anatomy"],
 "Analyze"),

("Graphical representation in Analyze phase?",
 ["Histogram","Pie Chart","Element-Name-Value","Line Graph"],
 "Element-Name-Value"),

("Why is conflict essential in storytelling?",
 ["Longer stories","Better characters","Adds excitement","Faster resolution"],
 "Adds excitement"),

("Porthos tailor conflict?",
 ["Fashion vs time","Measured without touch","High price","Visual measurement"],
 "Measured without touch"),

("Hershey’s chocolate conflict?",
 ["Chocolate melts","Cheap packaging","Costly materials","Too heavy"],
 "Chocolate melts"),

("Conflict analysis helps by?",
 ["Optimal solution","Visual conflict","Creative thinking","Solving root cause"],
 "Solving root cause"),

("Impact of solving understaffing?",
 ["Improved satisfaction","Higher prices","More ads","Expansion"],
 "Improved satisfaction"),

# -------- WEEK 3 --------
("Outcome of Altshuller’s TRIZ work?",
 ["Education revolution","Industry problem solving","Warfare","Patent filing"],
 "Industry problem solving"),

("Altshuller’s method differed because?",
 ["Intuition","Experience","Systematic formula","Heavy training"],
 "Systematic formula"),

("Design Thinking phases classification?",
 ["Analytical/Systematic","Initiate/Crash","Convergent/Divergent","R&D"],
 "Convergent/Divergent"),

("Zen master advice?",
 ["Keep pouring","Empty the mind","Focus on cup","None"],
 "Empty the mind"),

("Blind men & elephant story teaches?",
 ["Trial error","Experts only","Multiple solutions","Whole picture"],
 "Whole picture"),

("Best TRIZ principle for checkout improvement?",
 ["Segmentation","Prior Action","Termination","Reverse roles"],
 "Prior Action"),

("Solve phase is?",
 ["Cheap solution","Divergent phase","Expert ideas","No ideas"],
 "Divergent phase"),

("TRIZ is used to?",
 ["Test solutions","Trigger ideas","Grant patent","License tech"],
 "Trigger ideas"),

("NOT part of Solve phase?",
 ["Brainstorming","User interviews","TRIZ","Collaboration"],
 "User interviews"),

("Solve phase reduces bias by?",
 ["Experts only","Diverse team","Avoid feedback","Skip prototype"],
 "Diverse team"),

# -------- WEEK 4 --------
("Purpose of prototyping?",
 ["Test & refine","Deploy products","Future tech","Revenue"],
 "Test & refine"),

("Why do we test assumptions?",
 ["We don’t know users fully","Budget issues","Skill issues","No answers"],
 "We don’t know users fully"),

("Needed before testing ideas?",
 ["Notes","Products","Competitors","Features & assumptions"],
 "Features & assumptions"),

("Test phase contributes by?",
 ["Revenue","Lateral thinking","Validating ideas","Generating ideas"],
 "Validating ideas"),

("Iteration in Test phase means?",
 ["Not required","Repeat full process","Small adjustments","Only if failed"],
 "Small adjustments"),

("Understanding audience preferences stage?",
 ["HMW","5WHY","CJM","WH questions"],
 "CJM"),

("Customers’ needs written down stage?",
 ["Empathize","Analyze","Solve","Test"],
 "Analyze"),

("Thinking of many solutions stage?",
 ["Silent brainstorming","Prototyping","Frame problems","Persona"],
 "Silent brainstorming"),
]

# ---------------- SESSION STATE ---------------- #
if "quiz" not in st.session_state:
    st.session_state.quiz = []
    st.session_state.answers = {}
    st.session_state.submitted = False

# ---------------- GENERATE RANDOM QUIZ ---------------- #
def generate_quiz():
    quiz = random.sample(QUESTION_BANK, len(QUESTION_BANK))
    shuffled_quiz = []
    for q, options, correct in quiz:
        shuffled_options = random.sample(options, len(options))
        shuffled_quiz.append((q, shuffled_options, correct))
    return shuffled_quiz

if not st.session_state.quiz:
    st.session_state.quiz = generate_quiz()

# ---------------- QUIZ UI ---------------- #
for i, (question, options, correct) in enumerate(st.session_state.quiz):
    st.subheader(f"Q{i+1}. {question}")

    selected = st.radio(
        "Choose one option:",
        options,
        key=f"q_{i}",
        index=None,
        disabled=st.session_state.submitted
    )

    if selected:
        st.session_state.answers[i] = selected

    if st.session_state.submitted:
        if st.session_state.answers.get(i) == correct:
            st.success("✅ Correct")
        else:
            st.error(f"❌ Wrong | Correct Answer: {correct}")

    st.divider()

# ---------------- SUBMIT ---------------- #
if not st.session_state.submitted:
    if st.button("📊 Submit Exam"):
        st.session_state.submitted = True
        st.rerun()

# ---------------- RESULT ---------------- #
if st.session_state.submitted:
    correct_count = sum(
        1 for i, (_, _, correct) in enumerate(st.session_state.quiz)
        if st.session_state.answers.get(i) == correct
    )

    total = len(st.session_state.quiz)
    wrong_count = total - correct_count

    st.header("📈 Result")
    st.write(f"✅ Correct Answers: **{correct_count}**")
    st.write(f"❌ Incorrect Answers: **{wrong_count}**")
    st.write(f"🎯 Score: **{correct_count}/{total}**")

    if correct_count >= total * 0.5:
        st.success("🎉 PASSED")
    else:
        st.error("❌ FAILED")

    # ---------------- RESET ---------------- #
    if st.button("🔄 Take Exam Again"):
        st.session_state.quiz = []
        st.session_state.answers = {}
        st.session_state.submitted = False
        st.rerun()
