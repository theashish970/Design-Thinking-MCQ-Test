const questions = [

/* ---------- WEEK 1 ---------- */
{
question: "What is the first Noble Truth according to Lord Buddha?",
options: [
"Accept suffering",
"Origin of suffering",
"Cessation of suffering",
"Path leading to cessation of suffering"
],
correct: 0
},
{
question: "How does empathy in Design Thinking relate to Buddha’s teachings?",
options: [
"Finding cause of suffering",
"Understanding others’ feelings",
"Cessation of suffering",
"Eightfold path"
],
correct: 1
},
{
question: "What tool visualizes the steps a customer goes through?",
options: [
"SWOT",
"Customer Journey Mapping",
"Brainstorming",
"Business Model Canvas"
],
correct: 1
},
{
question: "What best describes a Customer Persona?",
options: [
"Fictional typical user",
"Customer problem report",
"Complaints list",
"Business summary"
],
correct: 0
},
{
question: "Which tool captures and organizes thoughts in design thinking?",
options: [
"Notebook",
"WhatsApp",
"Sticky Notes",
"Teacups"
],
correct: 2
},
{
question: "Why use real observations instead of only asking customers?",
options: [
"Customers forget",
"More accurate data",
"Takes time",
"More fun"
],
correct: 1
},
{
question: "What should be documented before Analyze stage?",
options: [
"Solutions",
"Steps and emotions",
"Marketing",
"Specifications"
],
correct: 1
},
{
question: "Final step to ensure Customer Journey Map completeness?",
options: [
"Survey",
"Second persona",
"Peer feedback",
"Mentor review"
],
correct: 1
},
{
question: "IDEO team problem with senior citizen medication?",
options: [
"Forget medicine",
"Open bottle",
"Wrong medicine",
"Insufficient supply"
],
correct: 1
},

/* ---------- WEEK 2 ---------- */
{
question: "Multi-Why Analysis is effective for?",
options: [
"Statistical problems",
"Simple problems",
"Known root cause",
"Unknown root cause"
],
correct: 3
},
{
question: "Best way to resolve conflicts in Design Thinking?",
options: [
"Avoid conflicts",
"Satisfy all parties",
"Accept conflicts",
"Focus on customer"
],
correct: 1
},
{
question: "Who coined the 5 Why method?",
options: [
"Apple",
"Toyota",
"Google",
"Microsoft"
],
correct: 1
},
{
question: "Samudaya in Design Thinking refers to?",
options: [
"Analyze",
"Define",
"Introspect",
"Anatomy"
],
correct: 0
},
{
question: "Graphical representation in Analyze phase?",
options: [
"Histogram",
"Pie chart",
"Element-Name-Value",
"Line graph"
],
correct: 2
},
{
question: "Why is conflict essential in storytelling?",
options: [
"Longer stories",
"Better characters",
"Adds engagement",
"Faster resolution"
],
correct: 2
},
{
question: "Porthos tailor conflict?",
options: [
"Fashion vs time",
"No touch measurement",
"High price",
"Visual measurement"
],
correct: 1
},
{
question: "Hershey’s conflict?",
options: [
"Chocolate melts",
"Cheap packaging",
"Costly materials",
"Too heavy"
],
correct: 0
},
{
question: "Conflict analysis helps by?",
options: [
"Optimal solution",
"Visual conflict",
"Creative need",
"Root cause solution"
],
correct: 3
},
{
question: "Impact of solving understaffing?",
options: [
"Better satisfaction",
"Higher prices",
"More ads",
"Expansion"
],
correct: 0
},

/* ---------- WEEK 3 ---------- */
{
question: "Outcome of Altshuller’s TRIZ work?",
options: [
"Education revolution",
"Industry problem solving",
"Warfare",
"Patent filing"
],
correct: 1
},
{
question: "Altshuller’s method differed because?",
options: [
"Intuition",
"Experience",
"Systematic formula",
"Training heavy"
],
correct: 2
},
{
question: "Design Thinking phases classification?",
options: [
"Analytical/Systematic",
"Initiate/Crash",
"Convergent/Divergent",
"R&D"
],
correct: 2
},
{
question: "Zen master advice?",
options: [
"Keep pouring",
"Empty the mind",
"Focus on cup",
"None"
],
correct: 1
},
{
question: "Blind men & elephant story teaches?",
options: [
"Trial error",
"Experts only",
"Multiple solutions",
"Whole picture"
],
correct: 3
},
{
question: "Best TRIZ principle for checkout?",
options: [
"Segmentation",
"Prior action",
"Termination",
"Reverse roles"
],
correct: 1
},
{
question: "Solve phase is?",
options: [
"Cheap solution",
"Divergent phase",
"Expert ideas",
"No ideas"
],
correct: 1
},
{
question: "TRIZ used to?",
options: [
"Test solutions",
"Trigger ideas",
"Grant patent",
"License tech"
],
correct: 1
},
{
question: "NOT part of Solve phase?",
options: [
"Brainstorming",
"User interviews",
"TRIZ",
"Collaboration"
],
correct: 1
},
{
question: "Solve phase reduces bias by?",
options: [
"Experts only",
"Diverse team",
"Avoid feedback",
"Skip prototype"
],
correct: 1
},

/* ---------- WEEK 4 ---------- */
{
question: "Purpose of prototyping?",
options: [
"Test & refine",
"Deploy products",
"Future tech",
"Revenue"
],
correct: 0
},
{
question: "Why test assumptions?",
options: [
"Unknown users",
"Budget issue",
"Skill lack",
"No answers"
],
correct: 0
},
{
question: "Needed before testing ideas?",
options: [
"Notes",
"Products",
"Competitors",
"Features & assumptions"
],
correct: 3
},
{
question: "Test phase contributes by?",
options: [
"Revenue",
"Lateral thinking",
"Validate ideas",
"Generate ideas"
],
correct: 2
},
{
question: "Iteration means?",
options: [
"Not needed",
"Repeat full process",
"Small adjustments",
"Only on failure"
],
correct: 2
},
{
question: "Understanding audience preferences stage?",
options: [
"HMW",
"5WHY",
"CJM",
"WH questions"
],
correct: 2
},
{
question: "Customers’ needs written down stage?",
options: [
"Empathize",
"Analyze",
"Solve",
"Test"
],
correct: 1
},
{
question: "Thinking of many solutions stage?",
options: [
"Silent brainstorming",
"Prototyping",
"Frame problems",
"Persona"
],
correct: 0
}
];

/* ---------- LOGIC ---------- */

let correctCount = 0;
let wrongCount = 0;

const quiz = document.getElementById("quiz");

questions.forEach((q, qIndex) => {
    const box = document.createElement("div");
    box.className = "question-box";

    const ques = document.createElement("div");
    ques.className = "question";
    ques.innerText = `Q${qIndex + 1}. ${q.question}`;
    box.appendChild(ques);

    q.options.forEach((opt, optIndex) => {
        const optDiv = document.createElement("div");
        optDiv.className = "option";
        optDiv.innerText = opt;

        optDiv.onclick = () => {
            const allOptions = box.querySelectorAll(".option");
            allOptions.forEach(o => o.classList.add("disabled"));

            if (optIndex === q.correct) {
                optDiv.classList.add("correct");
                correctCount++;
            } else {
                optDiv.classList.add("wrong");
                allOptions[q.correct].classList.add("correct");
                wrongCount++;
            }
        };

        box.appendChild(optDiv);
    });

    quiz.appendChild(box);
});

document.getElementById("submitBtn").onclick = () => {
    document.getElementById("result").innerHTML =
        `✅ Correct Answers: ${correctCount}<br>❌ Incorrect Answers: ${wrongCount}`;
};
