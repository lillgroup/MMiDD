footer: MMiDD 2025 - Sofiene Khiari
slidenumbers: true
theme: Plain Jane, 1
autoscale: true

# Introduction to Computing
### Understanding How Computers Work

^ - **Welcome** to the Molecular Modelling in Drug Design lecture and to this **first part** which is about **programming with Python**.
- The goal is to provide fundamental understanding of **how computers and programming work** and **how you can use them to solve problems**, not to turn you into programmers, but to make you **more effective researchers who can leverage computational tools** safely and effectively.
- This course **assumes no prior knowledge in programming** because of the different backgrounds.
- A bit about **my background**: My name is Sofiene Khiari, I'm a **first year PhD student in the computational pharmacy group in the Pharmazentrum**. I actually did the **master in drug sciences** and **finished my master's last December (come to me if you have questions)**. I'm a **pharmacist by training** but have been **programming my whole life basically**. I have formal training in computer science and I've also **worked for several years as a freelance web developper**.

---

# Today We'll Explore

1. **Why computational skills matter** for your research career
2. **How computers actually work** - from binary to complex analysis
3. **Software building blocks** - the fundamental concepts
4. **Computational thinking** - systematic problem-solving approach
5. **AI tools and why understanding matters** - using AI safely and effectively

^ Today's journey takes us from the big picture of why this matters for your career, down to the fundamental building blocks of how computers work, and back up to practical applications and modern AI tools.

^ The goal is to give you a solid foundation that will make you more effective at using any computational tool, whether you ever write code yourself or not.

---

# Section 1: Why This Matters for Your Career

^ I want take some time to **motivate you about why this is important**, so to **follow this lecture** but also take **another more detailed lecture** if you're interested.

---

# Why Are We Here?

- You're studying drug sciences because you want to contribute to developing **better treatments**. 
- Whether you end up working in computational modeling, in-vitro research, or any other area of pharmaceutical research, **you'll be using computer tools** every day. Programming isn't only for in-silico researchers.
- Even if you don't end up programming yourself, there's **real value** in understanding the **basics** of what's actually happening when you click those buttons in your research software or what the script that a colleague provided  actually does.

^ And **I'll tell you later why**

---

# Modern Drug Research

- **Scenario:** A researcher needs to analyze the effects of 1000 compounds on cell growth.
- **Current reality:** Upload data → automated analysis → Results in hours.
- **This is possible because:** Either someone in the group knows how to program, or specialized software was developed for this task.
- **Manual approach (without computational tools):** Measure each sample individually, calculate results by hand → Maybe several weeks of work.
- **The critical gap:** However, a lot of researchers know **how** to use the software, but not **what** it's actually doing.

---

# The Hidden Problem

This gap in understanding creates issues:

- **Misinterpreted results** when you can't evaluate if the analysis fully makes sense (less likely but can happen)
- ⚠️ **Missed innovations** because you can't adapt tools to new problems  
- ⚠️ **Complete dependence** on others when something goes wrong
- **Limited career growth** in an increasingly computational field

**The opportunity:** Understanding computation transforms you **from a tool user into a tool creator**, which is slowly but surely becoming a major career differentiator in research. So this isn't about becoming a programmer - it's about **understanding enough to be an effective scientist** in a computational world.

---

# Common Misconceptions About Programming

- **Misconception 1:** "Programming is only for people doing computational research"
- **Misconception 2:** "It's all about memorizing syntax"
- **Misconception 3:** "I need to become an expert to benefit"
- **Reality:** Basic understanding **transforms how you approach any research problem**, and with AI, programming is becoming **more accessible than ever** but **still requires critical thinking and problem-solving skills** and **basic computational literacy**, will tell you later why.

^ Reality Check:
^ - Misconception 1: Even if you never write a single line of code professionally, understanding how computers and software work fundamentally makes you better at using any software or script
^ - Misconception 2: It's about learning to think systematically and break problems down into steps and how to search online for solutions
^ - Misconception 3: Basic understanding can save you hours of work and **VERY VERY VERY IMPORTANT: help you ask better questions when collaborating with computational colleagues, more effective communication**

---

# Your Opportunity as Future Research Leaders

- **The innovation challenge:** The most groundbreaking research often requires tools that **don't exist yet**. When you're working on cutting-edge problems, there may be no software available to do what you need to do.
- **You would have an advantage if:** Learn to understand and create computational solutions for biological problems.
- **The reality:** Sometimes just a simple script can solve problems that no existing software can handle. Even if you don't write the code yourself and you have a computational colleague (who may not have your specific pharmaceutical expertise), being able to **think like a computer scientist and communicate your scientific needs clearly and simply** (so that they just have to implement what you explain) would save you hours and hours of back and forth.

^ The most groundbreaking research happens when you're trying to do something that nobody has done before. By definition, there's no software for that yet. You might be:
- **Analyzing a new type of data** that existing tools can't handle
- **Combining methods** in ways that no one has tried before
- Working with experimental approaches that are **too new to have established analysis pipelines**
- Trying to solve **problems that are specific to your unique research question**

^ The amazing thing is that often the solution doesn't require becoming a software engineer. A simple script that **takes an afternoon to write** can sometimes accomplish what **would take weeks to months of manual work or simply isn't possible with existing tools**.

^ Those are the reasons why this is very important.

---

# Section 2: How Computers Actually Work

^ Now that you understand the motivation, let's explore how computers actually work...

---

# The Universal Pattern

Every single computation follows the same basic pattern:

**INPUT → ALGORITHM (Process) → OUTPUT**

This might seem obvious, but it's **powerful** because computers can **repeat this pattern perfectly**, millions of times, **without getting tired, distracted, or making calculation errors**.

^ This universal pattern is the **foundation** of all computational work, very helpful to understand it properly.

---

# The Fundamental Question

How does a machine that only understands 1s and 0s ends up analyzing complex molecular structures?

Let's build up from the basics...

---

# Example: Cell Counting

**Manual approach:** Look at image → Identify what you think looks like cells → Mark them to avoid double-counting → Count marks

**Computational approach:**
- **INPUT:** Microscopy image (rows and columns of pixels with color values) + parameters defining cells
- **ALGORITHM:** Convert to numbers → Apply filters (matrix operations) → Identify regions → Count
- **OUTPUT:** Cell count + with computers: coordinates, different types of visualizations and plots

^ Manual approach **problems** because it relies on humans:
- Fatigue leads to inconsistency
- Different people count differently
- Easy to lose track or double-count
- Time-consuming for large datasets
- Relatively subjective decisions about what constitutes a "cell"

^ Filters: Mathematical operations applied to the matrix of pixel values to enhance features of interest (e.g., edges, brightness), making it easier for the computer to identify structures that match the defined parameters of a cell.

^ **When you automate**, you can also **enrich the analysis** that you get with **additional outputs like plots** (wouldn't do it manually because too time consuming and your PI may think it's a waste of time if done manually but it could be very useful if done automatically, e.g. coordinates can be useful for further analysis in the future).

^ Computational approach **advantages**:
- Consistency: Same image always produces same result
- Speed and Scalability: Process hundreds of images in time to manually count one, works equally well for 10 or 10000 images
- Documentation: Every decision recorded and reviewable
- Reproducibility: Other researchers can use exact same parameters that you used to define cells

---

# How Computers Work: From 1s and 0s to Complex Analysis

**Everything is binary:** 1s and 0s (electricity on/off)

**Hardware:** Processor (billions of transistors) + Memory (RAM + Storage)

**The Process:** Read binary → Apply patterns through transistor combinations → Store binary → **Repeat perfectly, millions of times**

**Your microscopy image** = read matrix of numbers → algorithm finds patterns → cell count stored and displayed

^ Binary **maps to electrical states** - this is why computers are so reliable. Text, images, numbers, programs all become binary patterns that **transistors** can manipulate.

^ **VERY IMPORTANT: The processor doesn't "understand" anything** - it just follows precise electrical patterns through transistor combinations. But it does this millions/billions of times per second without fatigue or errors.
Memory: RAM is fast temporary workspace, storage is permanent archive. The processor constantly moves data between these.

^ Key insight to keep in mind: **Computers aren't smart**, they're just **incredibly fast and consistent at simple operations**. This transforms tedious manual work into automated analysis that's reproducible and scalable.

---

# PB&J Exact Instructions Challenge

![inline](https://www.youtube.com/watch?v=FN2RM-CHkuI)

^ Very funny but important video that illustrates how computers need **very precise instructions** to do anything. **Humans can fill in gaps with common sense, but computers cannot**.

^ It's very helpful to learn how to identify the **exact steps** needed to solve a problem, **makes you better at problem solving even outside of the programming context**.

---

# More Research Examples

**DRUG SCREENING:**
- **Input:** Plate reader data from compound library
- **Process:** Normalize, calculate inhibition for each compound
- **Output:** Ranking of active compounds with values of potency

**PROTEIN POCKET ANALYSIS:**
- **Input:** PDB file (list of elements/residues and coordinates)
- **Process:** Calculate distances, angles, predict binding pockets based on geometry and physicochemical properties
- **Output:** Prediction of binding pockets

^ The power of this approach is that it can be applied to **any research problem**, helping you **think systematically** about what **inputs you need**, what **processing steps are required**, and what **outputs you want to generate**. VERY IMPORTANT: It teaches you to **simplify complex problems so much**, because it has to be translated into code which is very rigid and unforgiving (think of the PB&J Exact Instructions Challenge), that the **solving of the problem becomes trivial** in a lot of cases.

^ ALSO VERY IMPORTANT **especially for those of you who don't have professional experience yet**: Understanding these concepts intellectually is **just the first step**. In **real research situations**, when you’re **juggling multiple experiments**, facing **tight deadlines**, or dealing with **unexpected results**, **stress** and **workload** can make you **skip crucial analytical steps** or **forget to properly assess your approach**. The key is to **practice these thinking patterns** until they become **automatic habits rather than conscious efforts**.

^ !!!! Just like learning to drive, **proper problem solving skills need to be practiced enough that you naturally apply these systematic approaches even under pressure**. This is why it’s **essential not just to learn these concepts**, but to **actively practice them in low-stakes situations** before you’re in demanding professional environments where clear, methodical thinking becomes critical for research success.

^ This is what's most important about learning programming, not the syntax, but learning how to break down problems into such a level of fundamental steps.

---

# Section 3: Building Blocks of Software

^ We've seen how computers work fundamentally. Now let's understand the building blocks that make software work...

---

# What Is Programming?

Programming is giving the computer a **series of precise instructions** to solve a problem as we said, think of it like **writing a very detailed recipe** that a computer can follow.

---

# Programming Languages

Humans don't write in binary - we use programming languages that translate the instructions to binary

**High-level languages:** Python, R, MATLAB (believe it or not, closer to human language)
**Low-level languages:** C, Assembly (closer to machine language)

---

# The Fundamental Building Blocks

Every computer program uses these basic concepts:

1. **Variables** - Storing and retrieving information
2. **Data Structures** - Organizing information
3. **Functions** - Reusable blocks of code
4. **Loops** - Repeating actions systematically
5. **Conditionals** - Making decisions based on data
6. **Files** - Storing the code & saving and sharing results

^ May be trivial for some, but helpful to understand these concepts and why they matter. We'll see how they are translated to code the week after next week, but **for now we'll just understand what they are and why they matter**.

---

# Variables: Storing Information

Containers that hold data:

- Store **experimental measurements** (e.g. cell count)
- Keep **track of sample** (e.g. drug) names
- Remember **calculation results**

^ Why do they exist and why were they needed: It's because computers need to **store and retrieve information** to perform any meaningful task. Variables are the way we **label and organize this information** so that it can be used later in the program.

^ They can store **thousands of pieces of information simultaneously**, and they can be **updated instantly when new data becomes available**. Everything is **labeled clearly so it doesn't get confused**.

^ Sometimes you need to store data in a more complex way, which is where data structures come in.

---

# Data Structures: Complex variables for organizing information

Ways to group related information:

- **Lists:** Ordered collections (e.g. list of IC50 values)
- **Dictionaries:** Key-value pairs (e.g. protein name, species, molecular weight)

^ Why do they exist and why were they needed: It's because programs often need to handle **large amounts of related information**. Data structures allow us to **organize this information efficiently** so that it can be accessed and manipulated easily. For example, if you have a list of IC50 values from multiple experiments, you can store them in a list data structure, which allows you to **loop through each value** and perform calculations on them. If you have more complex information about a protein (like its name, species, and molecular weight), you can use a dictionary to **label each piece of information clearly**, making it easy to retrieve specific details when needed.

^ These are the way to handle data, and so we need to write instructions to do something with this data, which is where lines of instructions come in. Sometimes, you need to group related instructions together, which is where functions come in.

---

# Functions: Reusable Instructions

Reusable sets of instructions that perform specific tasks, for example with different inputs:

- Calculate molecular weight from formula
- Convert between concentration units
- Apply the same analysis to multiple datasets

^ Why do they exist and why were they needed: It's because programs often need to perform the same task multiple times. Functions allow us to **define a set of instructions once** and then **reuse them whenever needed** without rewriting the same code. This makes programs **more organized, easier to read, and less error-prone**. If you need to change how a task is done, you only have to update it in one place.

^ Functions can include special kinds of instructions like loops and conditionals

---

# Loops: Repeating Actions

Repeating the same identical process multiple times:

- "For each sample in the experiment, measure absorbance"
- "For each image, count the cells"
- "For each compound, calculate the IC50 value"

^ Why do they exist and why were they needed: It's because many tasks in research involve **repeating the same process** for multiple items, such as samples, images, or compounds. Loops allow us to **automate this repetition**, ensuring that the same steps are applied consistently to each item.

---

# Conditionals: Making Decisions

Making decisions based on data:

- "If concentration is above threshold, flag as toxic"
- "If cell viability is below 80%, discard sample"
- "If results are inconsistent, repeat experiment"

^ Why do they exist and why were they needed: It's because research often involves **making decisions based on data**. Conditionals allow us to **set rules** that determine how the program behaves in different situations. This is crucial for handling variability in experimental data and ensuring that the analysis adapts appropriately to different scenarios.

^ Once processing is done, we need to store the results permanently, which is where files come in.

---

# Files: Permanent Storage

Saving and sharing results permanently:

- Raw data files from instruments
- Processed analysis results
- Reports and visualizations
- Sharing data with collaborators

^ Why do they exist and why were they needed: It's because research data and results need to be **stored permanently** for future reference, sharing, and reproducibility. Files allow us to **save information outside of the program's temporary memory**, ensuring that it can be accessed later, even after the program has finished running. This is essential for maintaining a record of experiments and analyses.

---

# Putting It All Together - Cell Counting

- **Variables:** Store image data, cell parameters, results
- **Data Structures:** List of cell coordinates (coordinates themselves being a list of x, y and z values), dictionary of cell properties
- **Functions:** `load_image`, `apply_filter`, `count_cells`. If you need to change how filtering works for example, you only update one function (programming also teaches you how to think in a modular and compartmentalized way, which is very useful for problem solving in general)
- **Loops:** "For each pixel" → "For each detected region"
- **Conditionals:** "If region matches cell parameters, then it's a cell"
- **Files:** Save original image, processed results, analysis report

^ This shows **how abstract programming concepts directly enable the INPUT → ALGORITHM → OUTPUT pattern we discussed**. Each building block serves a specific purpose in transforming raw microscopy data into quantified results.

---

# Section 4: Computational Thinking

^ Now that we understand the building blocks, let's see how to use them systematically to solve complex problems...

---

# Computational Thinking

A systematic problem-solving approach that breaks complex challenges into manageable parts

**The four key principles:**

1. **Decomposition** - Break into smaller pieces
2. **Pattern Recognition** - Find similarities and trends
3. **Abstraction** - Focus on what matters most
4. **Algorithm Design** - Create repeatable procedures

^ This approach **mimics how computer scientists tackle problems**, but it's **equally powerful for experimental design, data analysis, and research troubleshooting**. The beauty is that it **makes overwhelming problems feel manageable**.

---

# Decomposition: Break It Down

**The Problem:** "Why isn't my cell culture growing?"

**Decomposed into testable pieces:**

- Media composition and pH
- Incubator temperature and CO₂ levels
- Contamination check
- Cell line authenticity
- Passage number and age

^ BEFORE TALKING ABOUT THE EXAMPLE: Instead of panicking about "everything is wrong," decomposition lets you **test each component systematically**. Each piece becomes a **manageable question you can answer definitively**.

^ Real example: A student's cells weren't growing. Instead of changing everything at once, we decomposed: checked media (fine), incubator (fine), contamination (negative), then discovered the CO₂ tank was empty. One systematic check solved it.

^ This prevents the **common mistake of changing multiple variables simultaneously**, which makes it impossible to identify the actual cause of problems.

^ In the context of writing code, decomposition means breaking a complex task into smaller functions or modules that can be developed and tested independently.

---

# Pattern Recognition: Find the Trends

**The Situation:** Your drug screening results seem inconsistent

**Patterns to look for:**

- Do compounds with similar structures show similar effects?
- Are certain experimental days always different?
- Do specific plate positions consistently behave oddly?

^ BEFORE TALKING ABOUT THE EXAMPLE: Pattern recognition **helps you see signal through noise**. Instead of treating each data point as isolated, you look for **underlying trends** that reveal **systematic issues** or biological insights.

^ Real example: A researcher noticed that compounds in the edge wells of 96-well plates consistently showed different results. Pattern recognition revealed edge effects from evaporation - a systematic error, not biological variation.

^ Note: Edge wells experience higher evaporation rates than inner wells because they have more surface area exposed to air circulation and lack the insulating effect of being completely surrounded by neighboring wells, leading to increased concentration of medium components and altered pH.

^ This principle also works for **positive discoveries**: **noticing that all active compounds share a specific chemical motif** can guide future drug design.

^ In the context of writing code, pattern recognition means identifying common tasks or operations that can be abstracted into functions or classes, reducing redundancy and improving code maintainability.

---

# Abstraction: Focus on What Matters

- **The Challenge:** Modeling how a drug reaches its target in the body
- **Essential features:** Drug concentration, binding affinity, target location
- **Ignore for now:** Individual blood cell interactions, minor metabolites

^ BEFORE TALKING ABOUT THE EXAMPLE: Abstraction **prevents getting lost in irrelevant complexity**. You can't model everything at once, so you **focus on the variables that most impact your research question**.

^ Example: When studying enzyme kinetics, you **abstract to Vmax and Km values rather than tracking every molecular collision**. This simplification **reveals the essential behavior without overwhelming detail**.

^ In the context of writing code, abstraction means creating interfaces or APIs that hide complex implementation details, allowing users to interact with the code at a higher level without needing to understand all the underlying complexity.

---

# Algorithm Design: Create Repeatable Procedures

**The Goal:** Optimize cell transfection efficiency

**Your Algorithm:**

1. Test DNA concentrations: 0.5, 1.0, 2.0 μg
2. For each concentration, test reagent ratios: 2:1, 3:1, 4:1
3. Measure efficiency 24h and 48h post-transfection
4. Select best combination and validate with biological replicates

^ Algorithm design creates **systematic procedures that anyone can follow and reproduce**. This is the **foundation of reproducible science - clear, step-by-step protocols**.

^ Notice how this **algorithm incorporates all previous principles**: decomposed variables (concentration vs. ratio vs. time), pattern recognition (systematic testing), and abstraction (focusing on key parameters).

^ Good algorithms are like good recipes - **specific enough that different people get consistent results, but flexible enough to adapt to different situations**.

^ In the context of writing code, **algorithm design means outlining the logical steps needed to solve a problem before translating them into code**, ensuring clarity and efficiency in the implementation.

^ Cell transfection is the process of deliberately introducing foreign nucleic acids (DNA, RNA, or proteins) into eukaryotic cells to alter their properties or study gene function.

---

# Computational Thinking in Action: Software Example

**Research Challenge:** "Predict which small molecules will bind to my protein target"

**Decomposition:** Structure preparation → Ligand library → Docking parameters → Docking & Scoring → Analysis
**Pattern Recognition:** Do high-scoring compounds share structural features? Binding modes?
**Abstraction:** Focus on binding affinity predictions, ignore solvent dynamics details
**Algorithm Design:** Systematic pipeline from structure to ranked compound list

^ Molecular docking is a computational method that predicts how small molecules (ligands) orient and bind within protein active sites, helping identify potential drug candidates.

^ Decomposition breaks this complex prediction into **manageable steps**: preparing the protein structure (removing water, adding hydrogens), curating the compound library, setting search parameters, running docking calculations, and analyzing results.

^ Pattern recognition helps **identify which chemical scaffolds consistently score well**, what binding orientations are favored, and whether certain protein regions are consistently targeted by active compounds.

^ **Abstraction focuses on the essential question** - "will this molecule bind?" - while ignoring computationally expensive details like full molecular dynamics simulations or explicit solvent effects that don't significantly impact initial screening.

^ Algorithm design creates a **reproducible pipeline**: input protein structure → preprocess → dock compound library → score interactions → rank by binding affinity → select top candidates for experimental validation. This systematic approach ensures consistent, unbiased screening.

^ This computational thinking approach **transforms the overwhelming question** "which of these million compounds might work?" into a **systematic, step-by-step process that can reliably identify promising drug candidates**.

---

# Computational Thinking in Action: Lab Example

**Real Research Scenario:** "My Western blot results are inconsistent"

- **Decomposition:** Protein extraction → SDS-PAGE → Transfer → Antibodies → Detection
- **Pattern Recognition:** Are certain samples always problematic? Specific days? Antibody batches?
- **Abstraction:** Focus on the steps most likely to cause variability (usually antibodies or transfer)
- **Algorithm Design:** Create systematic troubleshooting protocol testing one variable at a time

^ This shows computational thinking applied to a common lab problem. **Instead of random troubleshooting, you approach it systematically**.

^ The power is that this approach **works for any research challenge**: designing experiments, analyzing data, troubleshooting equipment, or even writing papers and grants.

^ By thinking computationally, you **transform overwhelming research problems into manageable, systematic processes** - just like computers break down complex tasks into simple operations.

^ Again as I said, the point **is not just knowing that you can solve problems like this**, it's about **practicing it enough in this lecture and beyond** that it **becomes second nature, especially under pressure**.

^ So this is something we're going to be **keeping in mind and practicing over the next weeks** and I hope it's a **way of thinking that you'll take with you throughout your research career**.

---

# Section 5: AI Tools and Why Understanding Matters

^ Now that we understood these fundamental, let's see why understanding them is especially important in the age of AI tools...

---

# AI Tools and Why Understanding Matters

**The big question:** If AI can write code, why learn programming fundamentals?

**The answer:** Understanding lets you use AI safely and effectively, rather than blindly trusting it

^ Understanding these fundamentals is especially important in the age of AI tools. You've **probably heard about ChatGPT, GitHub Copilot, and other AI tools that can generate code**.

^ This raises a critical question for researchers: if AI can write programs, why should you learn these fundamentals? The answer is that understanding fundamentals transforms AI from a dangerous black box into a powerful assistant.

---

# The Hidden Dangers of AI Code

- **Plausible but Wrong:** Code runs smoothly but produces incorrect results (for example calculations seem correct but are actually wrong because the wrong formula was used, you may end up publishing incorrect conclusions)
- **Missing Biology:** Ignores experimental constraints and statistical requirements
- **Debugging Nightmare:** You're stuck when (not if) things break
- **Security Risks:** Vulnerabilities and potential data corruption

^ OBVIOUS LIMITATION: AI tools can produce buggy code, but you can generally see that by just running it, so this is not what I'm focusing on here.

^ AI tools are powerful, but they have serious limitations that can be dangerous if you don't understand what they're producing.

^ Plausible but Wrong: **AI often generates code that runs without errors** but **can sometimes produce incorrect results**. The output looks professional and convincing, but without understanding the logic, you can't verify if it's actually doing what you need. In research, this means potentially publishing incorrect conclusions.

^ Math formulas **can be subtly wrong**, or **span across multiple lines in ways that are hard to spot** unless you wrote it yourself and understand the logic behind it.

^ Missing Biology: **AI doesn't necessarily understand the specific requirements of biological research**. It might create analysis that ignores important statistical considerations, miss critical quality control steps, or not account for biological variability and experimental constraints. **You can do this properly if you understand and know how to use the AI tools**.

^ Debugging Nightmare: **Good scripts are built iteratively through writing good code, checking that it works properly, refining it, and then writing more**. When AI generates code, it **can lack this iterative refinement** which means that **when it breaks it's way more difficult to fix it** because you're way less aware of where the problem could be. You gain time in the code writing phase, but **if you don't use AI properly, you end up with bad quality code**.

^ Security Risks: AI-generated code can contain security vulnerabilities and may not handle edge cases properly.

---

# Smart AI Usage: Be the Director, Not the Audience

**Effective AI prompts:**
- "Help me read this `.czi` microscopy file format"
- "Optimize this cell counting loop I designed"
- "What edge cases should I test in my IC50 calculation?"

**Dangerous AI prompts:**
- "Write a complete proteomics analysis pipeline"
- "Create statistical analysis for my drug screen data"

→ Will give you way more **details about how to use AI properly** since I know you will use it anyway.

^ The key is using AI **as an assistant, not as a replacement** for understanding. Think of AI like a **very knowledgeable but unreliable intern** - great for specific tasks when supervised, dangerous when given complete autonomy.

^ Effective prompts give AI specific, **bounded tasks where you can verify the output**. You understand what you're asking for and can evaluate whether the response is appropriate.

^ Dangerous prompts ask AI to make **decisions that require domain expertise you don't have**. Without understanding the fundamentals, you can't evaluate whether the AI's approach is scientifically sound.

^ When you understand programming fundamentals, you can verify AI suggestions, modify code for your specific requirements, debug issues when they arise, and ask better questions that produce more useful responses.

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
- Need a [Student GitHub account](https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student) starting here

**Finally:** Solve Real Problems in Code
- Apply everything to solve the problems from lesson 2
- Create working programs for research tasks

---

# Assignment

**Think of something you'd love to automate** - from your studies, work, or personal life / hobbies.

**Create a PDF explaining:**
- **What** would you want to automate?
- **INPUT:** What information/materials do you start with?
- **ALGORITHM:** What are the step-by-step processes? (Think PB&J video - be specific!)
- **OUTPUT:** What would you want as the final result?

**Examples:** Lab protocol, data analysis, meal planning, workout routine, literature review process, whatever!

**Deadline:** Next Wednesday, 24th of September, 11:59pm

**Goal:** Practice thinking systematically about breaking down problems into computational steps.

^ This isn't graded - I just want to see that you've spent a few minutes thinking through the INPUT → ALGORITHM → OUTPUT pattern **for something that matters to you**.

^ **Be as specific as possible with your algorithm steps. Remember the PB&J video - computers need very precise instructions.** This exercise helps you practice the systematic thinking that makes computational approaches so powerful.

---

# Thank You for your attention! Questions?
