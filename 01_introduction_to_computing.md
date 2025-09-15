footer: MMiDD 2025 - Sofiene Khiari
slidenumbers: true
theme: Plain Jane, 1
autoscale: true

# Introduction to Computing
### Understanding How Computers Work

^ This course is designed for Masters students in Drug Sciences. The goal is to provide fundamental understanding of how computers work, not to turn you into programmers, but to make you more effective researchers who can leverage computational tools safely and effectively. This course assumes no prior knowledge in programming.

---

# Why Are We Here?

- You're studying drug sciences because you want to contribute to developing better treatments. 
- Whether you end up working in computational modeling, cell culture research, or any other area of pharmaceutical research, you'll be using computer tools every day.
- There's real value in understanding what's actually happening when you click those buttons in your research software. Understanding computation doesn't mean you need to become a programmer, but it will make you a better scientist regardless of your specific research area.

---

# Today We'll Explore:

- Why understanding computation matters for your research career
- How computers actually process information
- The basic building blocks that make every software tool work
- How computational thinking can improve your approach to any problem

---

# Section 1 - Why This Matters for Your Career

---

# The Reality of Modern Drug Research

Here's what happens in a typical research lab today:

- **Scenario:** A researcher needs to analyze the effects of 1,000 compounds on cell growth.
- **Current reality:** Upload data → automated analysis → Results in hours
- **This is possible because:** Someone in the group knows how to program, or specialized software was developed for this task.
- **Manual approach (without computational tools):** Measure each sample individually, calculate results by hand → Several weeks of work
- **The critical gap:** However, most researchers know **how** to use the software, but not **what** it's actually doing.

---

# The Hidden Problem

This gap in understanding creates serious issues:
- **Misinterpreted results** when you can't evaluate if the analysis fully makes sense
- **Missed innovations** because you can't adapt tools to new problems  
- **Complete dependence** on others when something goes wrong
- **Limited career growth** in an increasingly computational field

**The opportunity:** Understanding computation transforms you from a tool user into a tool creator, which is slowly but surely becoming a major career differentiator in research. So this isn't about becoming a programmer - it's about understanding enough to be an effective scientist in a computational world.

---

# Common Misconceptions About Programming

- **Misconception 1:** "Programming is only for people doing computational research"
- **Misconception 2:** "It's all about memorizing syntax"
- **Misconception 3:** "I need to become an expert to benefit"
- **Reality:** Basic understanding transforms how you approach any research problem, and with AI, programming is becoming more accessible than ever but still requires critical thinking and problem-solving skills and basic computational literacy.

^ Reality Check:
^ - Misconception 1: Even if you never write a single line of code professionally, understanding how computers work fundamentally makes you better at using any software
^ - Misconception 2: It's about learning to think systematically and break problems down into steps
^ - Misconception 3: Basic understanding can save you hundreds of hours and help you ask better questions when collaborating with computational colleagues

---

# Your Opportunity as Future Research Leaders

**The innovation challenge:**

The most groundbreaking research often requires tools that **don't exist yet**.

When you're working on cutting-edge problems, there may be no software available to do what you need to do.

**Your advantage:** Learn to understand AND create computational solutions for biological problems.

**The game-changer:** Sometimes just a simple script can solve problems that no existing software can handle.

^ This is your opportunity to become research leaders:
^ 
^ The most groundbreaking research happens when you're trying to do something that nobody has done before. By definition, there's no software for that yet. You might be:
^ - Analyzing a new type of data that existing tools can't handle
^ - Combining methods in ways that no one has tried before
^ - Working with experimental approaches that are too new to have established analysis pipelines
^ - Trying to solve problems that are specific to your unique research question
^ 
^ The amazing thing is that often the solution doesn't require becoming a software engineer. A simple script that takes an afternoon to write can sometimes accomplish what would take months of manual work or simply isn't possible with existing tools.
^ 
^ This is where you become not just researchers, but research innovators.

---

# Concrete Impact: Before and After

**Drug Screening Analysis:**
- **Manual:** Analyze 96-well plate data by hand → 1-2 hours
- **Computational:** Upload data → automatic analysis → 10 minutes

**Literature Search:**
- **Manual:** Read through 30 relevant papers → 1-2 weeks  
- **Computational:** Targeted database search → 3-4 hours

**Cell Counting:**
- **Manual:** Count cells in 10 microscopy images → 1-2 hours
- **Computational:** Automated image analysis → 15 minutes

^ Let me show you realistic time savings from computational approaches:
^ 
^ Drug Screening: Instead of manually calculating IC50 values and creating dose-response curves from spreadsheet data, automated analysis can process standard plate reader output and generate publication-ready figures in minutes rather than hours.
^ 
^ Literature Search: Rather than manually scanning through dozens of papers to find relevant studies, targeted database searches and automated citation analysis can identify key papers and trends much more efficiently.
^ 
^ Image Analysis: Instead of manually counting cells or measuring areas in microscopy images, automated tools can process entire image datasets consistently and quickly, freeing researchers to focus on interpreting results.
^ 
^ The key insight: these aren't just faster ways to do the same work - they often enable analysis at scales that wouldn't be practical manually.

---

# Your Unique Advantage as Drug Sciences Students

You have something computer scientists don't: **deep knowledge of biological systems, drug development, and experimental design.**

You have something traditional biologists don't: **computational thinking and problem-solving skills.**

**This combination makes you research innovators who can:**

- **Evaluate** which computational approaches actually make sense for biological problems
- **Communicate** effectively with both wet lab researchers and computational specialists  
- **Identify** when automated analysis might be missing important biological context
- **Create** new tools that bridge the gap between computational power and biological insight
- **Lead** the next generation of drug discovery research

**You're not just learning to use tools - you're learning to create the future of drug research.**

---

# Moving to Implementation

Now that you understand the motivation, let's explore how computers actually process information...

---

# Section 2 - How Computers Actually Work

^ This section covers the universal pattern of computation and how computers process information, using examples relevant to biological research.

---

# The Universal Pattern

Every single computation follows the same basic pattern:

**INPUT → ALGORITHM (Process) → OUTPUT**

This might seem obvious, but it's powerful because computers can repeat this pattern perfectly, thousands of times, without getting tired, distracted, or making calculation errors.

^ This universal pattern is the foundation of all computational work. Understanding this pattern helps you evaluate any software tool and understand what it's actually doing with your data.

---

# The Fundamental Question

How does a machine that only understands 1s and 0s end up analyzing complex molecular structures?

Let's build up from the basics...

---

# Example: Cell Counting

**Manual approach:** Look at image → Identify cells → Mark to avoid double-counting → Count marks

**Computational approach:**
- **INPUT:** Microscopy image + parameters defining cells
- **ALGORITHM:** Convert to numbers → Apply filters → Identify regions → Count
- **OUTPUT:** Cell count + coordinates + measurements

^ Manual approach problems:
^ - Fatigue leads to inconsistency
^ - Different people count differently  
^ - Easy to lose track or double-count
^ - Time-consuming for large datasets
^ - Subjective decisions about what constitutes a "cell"
^ 
^ Computational approach advantages:
^ - Consistency: Same image always produces same result
^ - Speed: Process hundreds of images in time to manually count one
^ - Documentation: Every decision recorded and reviewable
^ - Scalability: Works equally well for 10 or 10,000 images
^ - Reproducibility: Other researchers can use exact same parameters

---

# Binary: The Language of Computers

Everything in a computer is represented as combinations of 1s and 0s

**Why binary?** Because it maps perfectly to electrical states:
- 1 = electricity flowing
- 0 = no electricity

This seems impossibly simple, but from these building blocks, we can represent anything

^ The key insight is that computers can represent any information - text, images, numbers, even complex molecular structures - using just these two states. You don't need to understand the technical details, but knowing that everything reduces to simple on/off states helps you understand that computers follow very logical, step-by-step processes.

---

# From Binary to Information

**Text:** Each character gets a binary code (ASCII/Unicode)
**Images:** Each pixel's color gets binary codes  
**Numbers:** Mathematical binary representation
**Programs:** Instructions encoded as binary

---

# The Processor: The Computer's Brain

The processor (CPU) has billions of tiny switches called **transistors**

Each transistor can be ON (1) or OFF (0)

By combining these switches in clever ways, we can perform calculations

---

# How Processors Think

A processor doesn't "know" what addition means. Instead, it follows precise instructions:

1. Read two numbers from memory
2. Apply electrical patterns that represent "addition"
3. Store the result back to memory

---

# Memory: The Computer's Workspace

**RAM (Random Access Memory):** Fast, temporary storage where the computer keeps data it's currently working with

**Storage (Hard Drive/SSD):** Slower, permanent storage where data is kept when not in use

---

# A Simple Example

When you open Excel and load a spreadsheet:

1. Excel program loads from storage into RAM
2. Your data file loads from storage into RAM  
3. CPU processes your commands using data in RAM
4. Results get stored back to storage when you save

---

# More Research Examples

**Drug screening:**
- **INPUT:** Plate reader data from compound library
- **PROCESS:** Normalize, calculate inhibition, fit curves
- **OUTPUT:** Ranked active compounds with potency

**Protein analysis:**
- **INPUT:** PDB file with atomic coordinates
- **PROCESS:** Calculate distances, angles, binding pockets
- **OUTPUT:** Structural parameters and drug binding sites

^ Gene expression analysis:
^ - INPUT: RNA-seq data from treated vs control cells
^ - PROCESS: Normalize counts, perform statistical tests, pathway analysis  
^ - OUTPUT: List of significantly changed genes and affected pathways
^ 
^ The power of this approach is that it can be applied to any research problem, helping you think systematically about what inputs you need, what processing steps are required, and what outputs you want to generate.

---

# From Theory to Practice

We've seen how computers work fundamentally. Now let's understand the building blocks that make software work...

---

# Section 3 - Building Blocks of Software

^ This section covers the four fundamental building blocks that appear in every computer program: Variables, Loops, Conditionals, and Files. These are the tools that make the "PROCESS" part of our INPUT → PROCESS → OUTPUT pattern work.

---

# What Is Programming?

Programming is giving the computer a series of precise instructions to solve a problem

Think of it like writing a very detailed recipe that a computer can follow

---

# Programming Languages

Humans don't write in binary - we use programming languages that get translated to binary

**High-level languages:** Python, R, MATLAB (closer to human language)
**Low-level languages:** C, Assembly (closer to machine language)

---

# The Four Fundamental Building Blocks

Every computer program uses these four concepts:

1. **Variables** - Storing and retrieving information
2. **Loops** - Repeating actions systematically
3. **Conditionals** - Making decisions based on data
4. **Files** - Saving and sharing results

^ These four concepts are the foundation of all computational thinking. In the next lesson, you'll practice breaking down real research problems using these concepts - but without worrying about programming syntax yet. Understanding these building blocks will help you think systematically about any problem you want to solve with a computer.

---

# Variables: Storing Information

Containers that hold data
- Store experimental measurements
- Keep track of sample names
- Remember calculation results

---

# Functions: Reusable Instructions

Reusable sets of instructions that perform specific tasks
- Calculate molecular weight from formula
- Convert between concentration units
- Apply the same analysis to multiple datasets

^ Variables: Storing Information
^ Think of variables as labeled containers where you store information that you need to use later.
^ 
^ Real-world analogy: Your lab notebook
^ - You write down experimental conditions, measurements, observations
^ - You give each piece of information a label ("Day 3 cell count", "Compound X concentration")
^ - You can look up this information later when analyzing results
^ 
^ In computing:
^ - A variable might store a cell count value like 1247
^ - Another might store a compound name like "Aspirin"  
^ - A list variable might store multiple measurements from an experiment
^ 
^ Why this matters:
^ - Computers can store thousands of pieces of information simultaneously
^ - Information can be updated instantly when new data becomes available
^ - The same information can be used in multiple calculations
^ - Everything is labeled clearly so it doesn't get confused
^ 
^ Research example: When analyzing a dose-response experiment, the computer stores each concentration tested, corresponding response values, experimental metadata (date, cell line, passage number), and this information is then used for curve fitting, statistical analysis, and report generation.

---

# Conditions: Making Decisions

Making decisions based on data:
- "If concentration is above threshold, flag as toxic"
- "If cell viability is below 80%, discard sample"
- "If results are inconsistent, repeat experiment"

---

# Loops: Repeating Actions

Repeating the same process multiple times:
- "For each sample in the experiment, measure absorbance"
- "For each image, count the cells"
- "For each compound, calculate the IC50 value"

^ Loops: Repeating Actions
^ Loops allow computers to repeat the same set of actions multiple times without getting tired or making mistakes.
^ 
^ Real-world analogy: Processing multiple samples
^ - You have 50 cell culture wells to analyze
^ - For each well, you need to: measure cell density, check viability, record results
^ - You repeat these exact same steps for every well
^ 
^ The computational approach:
^ FOR each sample in experiment:
^     Measure cell density
^     Check viability  
^     Record results
^ 
^ Why this is powerful:
^ - No decrease in attention or accuracy after sample #30
^ - Identical procedure applied to every sample
^ - Can process thousands of samples as easily as ten
^ - Guaranteed that every sample gets processed
^ 
^ Conditionals: Making Decisions
^ Conditionals allow computers to make different decisions based on the data they're analyzing.
^ 
^ Real-world analogy: Quality control in cell culture
^ - IF cell viability is below 80% THEN discard the culture
^ - IF cells are above 90% confluent THEN passage the cells
^ - IF contamination is detected THEN autoclave everything and start over
^ - OTHERWISE continue with normal maintenance
^ 
^ In drug screening, the computer might decide:
^ - IF inhibition > 50% THEN classify as "active hit"
^ - IF cytotoxicity > 20% THEN flag as "potentially toxic"
^ - IF variability between replicates > 15% THEN flag for repeat testing

---

# Lists: Organizing Information

Organizing related information together:
- IC50 values from multiple experiments
- Cell count measurements over time
- Names of all compounds in a screening library

---

# Dictionaries: Labeled Information

Storing information with descriptive labels:
- Protein information: name, species, molecular weight
- Experimental conditions: temperature, pH, concentration
- Sample metadata: date, researcher, batch number

---

# Files: Permanent Storage

Saving and sharing results permanently:
- Raw data files from instruments
- Processed analysis results
- Reports and visualizations
- Sharing data with collaborators

^ Files: Permanent Storage and Sharing
^ Files allow computers to save information permanently and share it between different programs and people.
^ 
^ Real-world analogy: Research data management
^ - Experimental data needs to survive computer crashes
^ - Results need to be shared with collaborators
^ - Raw data must be preserved for future analysis
^ - Reports need to be generated from stored data
^ 
^ What happens during a typical experiment:
^ Files created/updated:
^ - Raw data file (measurements from instruments)
^ - Processed data file (normalized, quality-controlled data)
^ - Analysis results file (statistics, curve fits, conclusions)
^ - Metadata file (experimental conditions, protocols used)
^ - Report file (formatted results for publication)
^ 
^ Why this matters:
^ - Permanence: Data survives equipment failures and software updates
^ - Sharing: Collaborators can access the same datasets
^ - Integration: Different analysis programs can work with the same data
^ - Reproducibility: Other researchers can verify your analysis
^ - Archiving: Data can be stored long-term for regulatory compliance

---

# How Software Is Built

Large programs are built by combining these basic concepts:

1. **Variables** store information
2. **Functions** perform operations
3. **Control flow** makes decisions
4. **Data structures** organize information

---

# Putting It All Together

**Drug screening analysis example:**
1. **Variables** store compound names, concentrations, response values
2. **Loops** process every compound in the library
3. **Conditionals** classify each as active, inactive, or cytotoxic
4. **Files** save results and generate reports

^ Real Example: Microscopy Image Analysis
^ Let me walk you through how a researcher would analyze microscopy images to measure cell migration, using our four building blocks:
^ 
^ 1. Variables - Store each cell's position coordinates, the time each image was taken, cell identification numbers, and movement distances
^ 2. Loops - Repeat the analysis for every cell in every image, and for every time point in the experiment
^ 3. Conditionals - Decide if a cell has moved significantly (if movement > threshold), if it's still in the field of view, if it's the same cell between time points
^ 4. Files - Save the original images, the tracking data, the movement measurements, and generate a report with statistics
^ 
^ This is exactly how researchers break down complex analysis tasks into these fundamental building blocks.

---

# Example: Image Analysis Software

**The process:**
1. Load microscopy image from file
2. For each region in the image:
   - Check if the brightness suggests it's a cell
   - If yes, mark it as part of a cell
3. Count all the marked regions
4. Save the count and create a report

^ This example shows how the four building blocks work together without showing any actual code. Students can understand the logical flow and decision-making process that the computer follows.

---

# Building Your Problem-Solving Toolkit

You now understand the building blocks. Let's learn how to use them systematically to solve complex problems...

---

# Section 4 - Computational Thinking

^ Computational thinking is a problem-solving approach that you can apply to any research challenge, not just programming. It means approaching problems like a computer scientist using four key principles.

---

# What Is Computational Thinking?

A problem-solving approach that breaks down complex problems into manageable parts

**Key principles:**
1. **Decomposition** - Break into smaller pieces
2. **Pattern recognition** - Find similarities
3. **Abstraction** - Focus on essentials
4. **Algorithm design** - Create systematic procedures

^ Computational thinking means approaching problems like a computer scientist:
^ 1. Decomposition: Break complex problems into smaller, manageable pieces
^ 2. Pattern recognition: Identify similarities and common elements
^ 3. Abstraction: Focus on the essential details, ignore irrelevant complexity
^ 4. Algorithm design: Create step-by-step solutions that can be repeated

---

# Decomposition

Break a big problem into smaller, solvable pieces

**Example:** "Analyze drug binding affinity"
1. Load molecular structures
2. Calculate binding energy
3. Compare to known drugs
4. Generate report

---

# Pattern Recognition

Look for similarities and trends in data

**Example:** In drug discovery, recognizing that compounds with similar structures often have similar effects

---

# Abstraction

Focus on essential features while ignoring irrelevant details

**Example:** When modeling protein folding, you might ignore individual atoms and work with secondary structures instead

---

# Algorithm Design

Create step-by-step procedures to solve problems

**Example:** Algorithm for finding the best drug candidate:
1. Screen compound library
2. Test top candidates in assays
3. Optimize promising compounds
4. Select best performer

---

# Computational Thinking in Research

This approach helps with **any** research problem, not just computational ones:

- **Experimental design:** Break complex experiments into testable steps
- **Data analysis:** Recognize patterns in results
- **Troubleshooting:** Systematically eliminate variables

---

# Example 1: Planning a Cell-Based Drug Screen

**Traditional approach:** "This is overwhelming, there are so many variables to consider."

**Computational thinking approach:**
1. **Decomposition:** Cell culture prep → Compound prep → Assay development → Data collection → Analysis → Follow-up
2. **Pattern recognition:** Each plate follows same layout, compounds need same QC
3. **Abstraction:** Primary readout is critical, everything else can be standardized
4. **Algorithm design:** SOPs for each step, QC checkpoints, decision trees

^ Example 2: Troubleshooting an Experiment
^ Traditional approach: "Nothing is working, I don't know where to start."
^ 
^ Computational thinking approach:
^ 1. Decomposition: Sample preparation steps, instrument calibration, environmental conditions, reagent quality, data collection methods
^ 2. Pattern recognition: Which steps are new vs. validated? Are failures consistent or random? Do problems correlate with specific batches?
^ 3. Abstraction: What are the most critical control points? Which variables have biggest impact? What can be tested quickly?
^ 4. Algorithm design: Systematic testing plan (change one variable at a time), decision criteria for when to continue vs. restart, documentation system
^ 
^ The Benefits for Your Research:
^ Immediate benefits:
^ - Less overwhelmed by complex experimental designs
^ - More systematic approach to troubleshooting
^ - Better documentation of methods and decisions
^ - Easier to train others and reproduce results
^ - More confident when tackling new challenges
^ 
^ Long-term benefits:
^ - Better at designing efficient experiments
^ - More effective at analyzing complex datasets
^ - Improved collaboration with computational colleagues
^ - Enhanced ability to evaluate and choose software tools
^ - Stronger problem-solving skills for any career path

---

# The Modern Research Landscape

Understanding these fundamentals is especially important in the age of AI tools...

---

# Section 5 - AI Tools and Why Understanding Matters

---

# AI Tools and Why Understanding Matters

You've probably heard about ChatGPT, GitHub Copilot, and other AI tools that can generate code. 

**Key question:** If AI can write programs, why should you learn these fundamentals?

^ This raises an important question: if AI can write programs, why should you learn these fundamentals?

---

# The Real Risks of Using AI Without Understanding

**Risk 1:** Plausible but wrong results - looks professional but produces incorrect conclusions

**Risk 2:** Missing domain-specific requirements - ignores biological research constraints

**Risk 3:** No debugging capability - you're stuck when code breaks

**Risk 4:** Security and reliability issues - vulnerabilities and data corruption

^ AI tools are powerful, but they have serious limitations that can be dangerous if you don't understand what they're producing.
^ 
^ Risk 1: Plausible but Wrong Results
^ - AI often generates code that runs without errors but produces incorrect results
^ - The output looks professional and convincing
^ - Without understanding the logic, you can't verify if it's actually doing what you need
^ - In research, this means potentially publishing incorrect conclusions
^ 
^ Risk 2: Missing Domain-Specific Requirements
^ - AI doesn't understand the specific requirements of biological research
^ - It might create analysis that ignores important statistical considerations
^ - It could miss critical quality control steps
^ - It may not account for biological variability and experimental constraints
^ 
^ Risk 3: No Debugging Capability
^ - When AI-generated code breaks (and it will), you're stuck
^ - You can't modify it for your specific needs
^ - You can't troubleshoot when results don't make sense
^ - You become completely dependent on the AI tool
^ 
^ Risk 4: Security and Reliability Issues
^ - AI-generated code often contains security vulnerabilities
^ - It may not handle edge cases or error conditions properly
^ - For research data, this could mean data corruption or loss

---

# How to Use AI Tools Effectively

**Effective uses:**
- "Help me write code to read this specific file format"
- "Suggest ways to optimize this calculation I've already designed"
- "What are potential problems I should test for in this analysis?"

**Problematic uses:**
- "Write a complete data analysis pipeline for my experiment"
- "Create a statistical analysis program" (without understanding the statistics)

^ The key is to use AI as an assistant, not as a replacement for understanding.
^ 
^ When you understand programming fundamentals:
^ - You can verify that AI suggestions are appropriate for your problem
^ - You can modify AI-generated code to fit your specific requirements
^ - You can debug issues when they arise
^ - You can integrate different tools into custom workflows
^ - You can ask better questions that produce more useful AI responses
^ 
^ Think of it like using statistical software: you need to understand statistics to use SPSS or R effectively. The software doesn't replace your need to understand when to use different tests, how to interpret results, or how to avoid common pitfalls.
^ 
^ Researchers who combine domain expertise with computational understanding will have a significant advantage. You'll be able to evaluate whether computational approaches are appropriate for your research questions, collaborate effectively with computational specialists, use AI tools safely and effectively, adapt to new software and technologies as they emerge, and design better experiments because you understand both the biology and the analysis.

---

# Connecting Theory to Daily Work

Let's see how these concepts apply to the research software you already use...

---

# Section 6 - Practical Applications

---

# Common Research Software

Let's look at what's actually happening when you use familiar tools...

---

# Excel/Spreadsheets

**What you see:** Cells with numbers and formulas
**What's happening:** 
- Each cell is a memory location
- Formulas are mini-programs that calculate values
- Charts are algorithms that convert numbers to visual patterns

---

# ImageJ

**What you see:** Tools to measure and analyze images
**What's happening:**
- Images are arrays of pixel values
- Filters apply mathematical operations to pixel neighborhoods  
- Measurements count pixels meeting certain criteria

---

# Statistical Software (R, GraphPad)

**What you see:** Statistical tests and p-values
**What's happening:**
- Data is stored in structured arrays
- Statistical tests are mathematical algorithms
- P-values are calculated using probability distributions

---

# Molecular Modeling Software

**What you see:** 3D protein structures
**What's happening:**
- Atomic coordinates stored as numbers
- 3D graphics calculated using linear algebra
- Energy calculations use physics equations
- Optimization uses mathematical algorithms

---

# Database Searches

**What you see:** Search results
**What's happening:**
- Text matching algorithms scan millions of records
- Relevance scoring ranks results
- Data retrieval optimized using indexing algorithms

---

# Section 7 - Looking Forward

^ This section covers what we've learned today, the mindset shift you should embrace, and how to continue building these skills.

---

# What We've Covered Today

✅ **Why computational skills matter** for research careers

✅ **How computers process information** using INPUT → PROCESS → OUTPUT

✅ **The four building blocks:** Variables, Loops, Conditionals, Files

✅ **Computational thinking** - systematic problem-solving

✅ **How to work effectively with AI tools** by understanding fundamentals

^ In our time together, you've learned:
^ - Why computational skills matter for research careers, even in predominantly wet-lab fields
^ - How computers process information using the Input → Process → Output pattern
^ - The four building blocks that appear in every program: Variables, Loops, Conditionals, and Files
^ - Computational thinking - a systematic approach to problem-solving you can apply anywhere
^ - How to work effectively with AI tools by understanding what they're actually doing

---

# The Mindset Change

**Before today:** "Software tools are black boxes that somehow produce results"

**Now:** "Every computational tool follows logical, step-by-step processes that I can understand and evaluate"

^ This shift in perspective will help you throughout your research career, whether you're choosing analysis software, troubleshooting data processing issues, or collaborating with computational colleagues.

---

# Emerging Technologies in Research

**Artificial Intelligence:**
- Machine learning for drug discovery
- Pattern recognition in imaging
- Automated literature analysis

**Cloud Computing:**
- Running large simulations without local hardware
- Collaborative data analysis platforms
- Scalable computational resources

---

# Skills That Will Serve You

**Technical Skills:**
- Basic programming (Python/R recommended)
- Data analysis and visualization
- Understanding of databases
- Command line proficiency

**Conceptual Skills:**
- Computational thinking approach
- Problem decomposition
- Algorithm design
- Data interpretation

---

# Getting Started

**Immediate Steps:**
1. **Choose a programming language** (Python is beginner-friendly)
2. **Find online tutorials** (many free resources available)
3. **Practice with your own data** (start with simple analysis tasks)
4. **Join communities** (online forums, local user groups)

---

# What Comes Next

**Next lesson:** Computer-Based Problem Solving
- Break down real research problems into computational steps
- Practice thinking systematically about data analysis
- Discuss different approaches to solving the same problem
- **No programming syntax yet** - just logical thinking

**Then:** Python Programming Basics
- Learn the actual programming language
- Implement the solutions you designed in lesson 2

**Finally:** Solve Real Problems in Code
- Apply everything to solve the problems from lesson 2
- Create working programs for research tasks

^ What Comes Next:
^ Next lesson: Computer-Based Problem Solving
^ We'll practice applying these concepts to real research scenarios. You'll work through examples of breaking down complex problems into computational steps, without getting caught up in programming syntax. You'll think about what data you need, what steps to follow, how to make decisions, and what results to save.
^ 
^ Then: Python Programming Basics
^ You'll learn to implement the solutions you design, creating actual programs that solve research problems.
^ 
^ Finally: Applications in Drug Design
^ You'll apply everything you've learned to molecular modeling, chemical databases, and drug discovery problems.
^ 
^ The Long-Term Perspective:
^ Learning to think computationally is like learning any important skill - it requires practice, but the benefits compound over time.
^ 
^ This semester: You'll create tools that make your coursework and research more efficient
^ During your thesis: You'll be able to tackle data analysis and experimental design challenges that would overwhelm others
^ In your career: You'll be the researcher who can bridge the gap between biological problems and computational solutions
^ Throughout your professional life: You'll approach problems with systematic thinking that makes you more effective in whatever field you choose

---

# Learning Resources

**Free Online Courses:**
- Codecademy (interactive programming lessons)
- Coursera/edX (university-level courses)
- YouTube tutorials for specific tools

**Practice Platforms:**
- Kaggle (data science competitions)
- GitHub (code sharing and collaboration)
- Jupyter notebooks (interactive programming)

---

# Questions to Ask About Any Software Tool

1. What problem is this solving?
2. What kind of input does it need?
3. What algorithms might it be using?
4. How could I verify the results?
5. Could I automate this process?

^ These questions will help you evaluate and use any computational tool more effectively throughout your research career.

---

# Your Next Steps

**This Course:**
- **Next lesson:** Computer-Based Problem Solving (no programming yet!)
- **Then:** Python Programming Basics  
- **Finally:** Applications in Drug Design

**Your Assignment:** Think about repetitive tasks in your research that involve the same steps applied to multiple samples or datasets

^ Next lesson preparation: Identify one research task that involves repetitive steps - we'll practice breaking it down systematically using computational thinking.

# Main Points to Remember

**Understanding computation makes you a better scientist**
Not just a better programmer - a better **scientist**

**Every complex system is built from simple parts**
Binary → Logic → Algorithms → Software → Solutions

**Computational thinking applies everywhere**
Problem-solving approach useful in any research area

**The four building blocks appear in every tool you use**
Variables, Loops, Conditionals, Files - now you can recognize them

^ Today's Key Concepts:
^ 
^ 1. The Universal Computing Pattern: INPUT → ALGORITHM → OUTPUT
^ 2. The Four Building Blocks: Variables, Loops, Conditionals, Files
^ 3. Computational Thinking: Decomposition, Pattern Recognition, Abstraction, Algorithm Design
^ 4. AI Tools Work Best When You Understand the Fundamentals
^ 
^ From this foundation, you can now:
^ - Evaluate any software tool more critically
^ - Approach complex research problems systematically
^ - Collaborate effectively with computational specialists
^ - Use AI tools safely and effectively
^ - Design better experiments with computational awareness

---

# The Bottom Line

**You don't need to become a programmer to benefit from understanding computation**

Understanding how your tools work makes you:
- More effective at using them
- Better at troubleshooting problems  
- Capable of asking better research questions
- Prepared for the future of science

**Every software tool is just someone else's solution to a problem - and now you understand how to evaluate and even create solutions too**

---

# Questions?

**Ready for the next step:** We'll practice breaking down real research problems using computational thinking

^ Final thought: You now have the conceptual foundation to understand any computational tool you encounter in your research career. The goal isn't to make you programmers - it's to make you better scientists who can think systematically about complex problems and use computational tools effectively and safely.

---

# Thank You!

**Contact:** [Your contact information]  
**Course materials:** [Link to course repository]  
**Office hours:** [Your availability]