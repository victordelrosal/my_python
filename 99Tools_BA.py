import random

tools = [
"4As communication model",
"Acceptance criteria definition",
"Activity diagrams",
"Activity sampling",
"Ansoff's Box",
"Ansoff's matrix",
"ARCI charts",
"Background reading",
"Background research",
"Balanced Business Scorecard",
"BCG matrix",
"Benefit-cost analysis (BCA)",
"Benefits categorisation",
"Benefits classification",
"Benefits management",
"Benefits realisation",
"Boston Box",
"Boston Consulting Group matrix",
"Business Activity Model (BAM)",
"Business activity modelling",
"Business case presentation",
"Business case report creation",
"Business event analysis",
"Business process Engineering (BPE)",
"Business process Improvement patterns",
"Business process modelling",
"Business process triggers",
"Business rules analysis",
"Business use case descriptions",
"Business use case diagrams",
"Business use case modelling",
"Capability modelling",
"CATWOE",
"Cause-and-effect diagrams",
"Class modelling",
"Concept maps",
"Conceptual model",
"Conscious competence model",
"Constraints analysis",
"Context diagram",
"Contextual inquiry",
"Cost-benefit analysis (CBA)",
"Critical success factors",
"CRUD matrix",
"Cultural analysis",
"Cynefin",
"Decision tables",
"Decision trees",
"Document analysis",
"Entity relationship diagrams (ERDs)",
"Entity relationship modelling",
"Ethnographic studies",
"Ethnography",
"Facilitated workshops",
"Feasibility analysis",
"Fishbone diagrams",
"Flowcharting",
"Force-field analysis",
"Four-view model",
"Gap analysis",
"Hothousing",
"Impact analysis",
"Influence/interest grid",
"Number Chapter Page Name",
"Power/impact grid",
"Power/interest grid",
"Principled negotiation",
"Process maps",
"Process redesign patterns",
"Product backlog",
"Protocol analysis",
"Prototyping",
"Questionnaires",
"RACI charts",
"RASCI charts",
"Record sampling",
"Repertory grid",
"Report analysis",
"Requirements documentation",
"Requirements management",
"Requirements organisation",
"Requirements traceability matrix",
"Requirements validation",
"Resource analysis",
"Resource Audit",
"Rich pictures",
"Risk analysis",
"Risk identification",
"Risk management",
"Root definition",
"Sampling",
"SARAH model",
"Scenarios",
"Semantic networks",
"Sensemaking",
"Shadowing",
"Social network analysis",
"Sociometry",
"Special-purpose records",
"Stakeholder management planning",
"Stakeholder map",
"Stakeholder nomination",
"Stakeholder wheel",
"State machine diagrams (SMDS)",
"State transition diagrams",
"Statecharts",
"STEEPLE analysis",
"Storyboarding",
"STROBE",
"Structured observation",
"Surveys",
"Swimlane diagrams",
"SWOT analysis",
"System event analysis",
"Task Analysis",
"Task modelling",
"Thomas-Kilmann conflict mode instrument",
"Thomas-Kilmann conflict model",
"Thomas-Kilmann instrument (TKI)",
"Timeboxing",
"Timesheets",
"TOWS analysis",
"UML Activity Diagrams",
"Use case descriptions",
"Use case diagrams",
"User analysis",
"User persona",
"User stories",
"Value chain analysis",
"Value proposition analysis",
"Value streams",
"Value streams analysis",
"Value streams mapping",
"VMOST analysis",
"VOCATE",
"Webs",
"Wireframes",
"Work measurement",
"Workshops"
    ]

#Designed for less than 20 teams

groups = int(input('Number of groups: '))
n = len(tools)
tools_per_group = int(round(n/groups,0))


for i in range(1,(groups+1)):
    print(f'\n_______________Group {i}_________________')
    for j in range(tools_per_group):
        if len(tools) == 0:
            break
        pick = random.choice(tools)
        print(j+1, pick)
        tools.remove(pick)

print()