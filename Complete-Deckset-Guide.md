# Complete Guide to Creating Presentations with Deckset

Deckset is a powerful presentation tool that uses standard Markdown syntax to transform your thoughts into beautiful presentations. This comprehensive guide covers everything you need to know to create stunning presentations with Deckset.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Basic Slide Structure](#basic-slide-structure)
3. [Text Formatting](#text-formatting)
4. [Headers and Paragraphs](#headers-and-paragraphs)
5. [Lists](#lists)
6. [Links and Code](#links-and-code)
7. [Working with Images](#working-with-images)
8. [Creating Tables](#creating-tables)
9. [Advanced Features](#advanced-features)
10. [Big Text Effects](#big-text-effects)
11. [Multimedia Content](#multimedia-content)
12. [Presentation Controls](#presentation-controls)

---

## Getting Started

Deckset is built on **standard Markdown syntax**, making it easy for anyone familiar with Markdown to create presentations quickly. The key advantage is that you can focus on your content while Deckset handles the beautiful formatting and design.

### Essential Setup

To get started with any Deckset presentation, you can optionally include directives at the very beginning of your markdown file:

```markdown
footer: © Your Name, 2025
slidenumbers: true
```

**Important Notes:**
- These directives must start on the **first line** of your markdown file
- Ensure there are **no empty lines** between the directives
- Both footer and slide numbers are optional

---

## Basic Slide Structure

### Creating New Slides

A new slide is defined by **three dashes** `---` typed on a single line, with an empty line above and below:

```markdown
# First Slide Content

---

# Second Slide Content
```

### Slide Types

Deckset automatically formats different types of slides based on content:
- **Text slides**: Simple paragraphs and headers
- **Quote slides**: Special formatting for quotes
- **Image slides**: Full-screen or combined with text
- **Code slides**: Syntax-highlighted code blocks
- **Table slides**: Formatted data tables

---

## Text Formatting

### Paragraphs

Creating paragraphs is simple - just type your text with no special syntax needed:

```markdown
This is a simple paragraph.

You can include a paragraph break by leaving an empty line between paragraphs.
Otherwise lines will follow on directly like this.
```

### Emphasis

Use various emphasis styles to make your content stand out:

- **Strong text**: Wrap in double asterisks `**like this**` or double underscores `__this__`
- *Emphasized text*: Wrap in single asterisks `*like this*` or single underscores `_this_`
- ***Combined emphasis***: Use both for maximum impact `***like this***`

```markdown
Use **strong**, _emphasis_ or a combination of **_both_** to make your point stand out.
```

---

## Headers and Paragraphs

### Header Sizes

Deckset supports four different heading sizes:

```markdown
# Header Level 1 (largest)
## Header Level 2
### Header Level 3
#### Header Level 4 (smallest)
```

### Usage Tips

- Headers are created by including `#` before the text
- You can change size by adding more `#` symbols
- Each slide typically starts with a header to provide structure

---

## Lists

### Ordered Lists

Create numbered lists by typing a number followed by a period:

```markdown
1. First item
2. Second item  
3. Third item
```

### Unordered Lists

Create bulleted lists using `-`, `*`, or `+`:

```markdown
- Unordered lists
- Type '-' or '*' or '+' before your text
- Your list items will begin with a bullet
```

### Nested Lists

You can create nested lists by indenting each item with **4 spaces**:

```markdown
- You can create nested lists
    1. by indenting
    2. each item with
    3. 4 spaces
- It's that simple
```

---

## Links and Code

### Creating Links

Create clickable links by wrapping link text in square brackets, followed by parentheses containing the URL:

```markdown
[Deckset Website](http://www.deckset.com)
```

**Features:**
- Links will be clickable in exported PDFs
- Works with any external resource or website

### Code Samples

#### Inline Code
Use single backticks for inline code: `code here`

#### Code Blocks
Wrap your code with three backticks and specify the language for automatic syntax highlighting:

```markdown
```javascript
function hello() {
    console.log("Hello, World!");
}
```
```

**Supported Features:**
- Automatic syntax highlighting for many languages
- Dynamic text scaling for optimal readability
- Support for various programming languages

### Monospace Font
Use a single indent (4 spaces) to switch to monospace font for simple code formatting.

---

## Working with Images

Deckset provides **eight powerful ways** to work with images, making it one of its strongest features.

### Basic Image Syntax

The simplest way to add images:

```markdown
![](your-image.jpg)
```

### Image Sources
- **Local images**: Drop onto Deckset window for automatic markdown creation
- **Web images**: Use URLs directly in the syntax
- **Automatic clipboard**: Markdown is automatically copied when dropping images

### Eight Image Modifiers

#### 1. Fill (Default Behavior)
Images fill the whole slide by default - no modifier needed.

#### 2. [fit] - Scale to Fit
```markdown
![fit](image.jpg)
```
- Scales the image to fit the slide while maintaining aspect ratio
- Shows the complete image without cropping

#### 3. [x%] - Exact Scaling
```markdown
![15%](image.jpg)
![50%](image.jpg)
```
- Scale to an exact percentage of the slide

#### 4. [left] - Left Alignment
```markdown
![left](image.jpg)
```
- Positions image on the left side of the slide

#### 5. [right] - Right Alignment  
```markdown
![right](image.jpg)
```
- Positions image on the right side of the slide

#### 6. [inline] - Inline with Text
```markdown
![inline](image.jpg)
```
- Combines text and images on the same slide
- Images are centered and fit available space
- Can be modified with `[inline, left]` or `[inline, right]`
- Perfect for captions: place image first, then text below

#### 7. [filtered] - Apply Filter
```markdown
![filtered](image.jpg)
```
- Applies a filter to make text more readable over images
- Each theme uses a unique filter style

#### 8. [original] - Remove Filter
```markdown
![original](image.jpg)
```
- Overrides automatic filtering on text+image slides
- Shows images in their original form

### Advanced Image Techniques

#### Multiple Images
```markdown
![left](image1.jpg)
![right](image2.jpg)
```
- Combine multiple alignment modifiers
- Deckset divides slide space according to number of images

#### Image Grids
```markdown
![inline, fill](image1.jpg) ![inline, fill](image2.jpg) ![inline, fill](image3.jpg)
![inline, fill](image4.jpg) ![inline, fill](image5.jpg)
```

#### Creative Combinations
```markdown
![15%, original](logo.png)
![25%, filtered](background.jpg)
```

### Text and Image Integration

When text and images are used together:
- Images are automatically filtered for text readability
- Each theme applies its unique filter
- Use `[original]` to override filtering when not needed
- Perfect for magazine-like layouts

---

## Creating Tables

Tables in Deckset use standard Markdown table syntax with additional formatting options.

### Basic Table Structure

```markdown
Header 1 | Header 2 | Header 3
---------|----------|----------
Cell 1   | Cell 2   | Cell 3
Cell 4   | Cell 5   | Cell 6
```

### Essential Elements
- **Cell separation**: Use vertical bar (`|`) to separate cells
- **Header separation**: Use three dashes (`---`) and vertical bars to separate Headers from content
- **Clean formatting**: Alignment is handled automatically

### Cell Alignment

Control text alignment within cells:

```markdown
Header 1 | Header 2  | Header 3
:--------|:---------:|---------:
Left     | Center    | Right
Aligned  | Aligned   | Aligned
```

**Alignment Options:**
- `:---` = Left aligned (default)
- `:---:` = Center aligned  
- `---:` = Right aligned

### Table Examples

#### Simple Data Table
```markdown
First Name | Last Name | Born       | Country
-----------|-----------|------------|--------
Ross       | Anderson  | 1956       | 🇬🇧
Whitfield  | Diffie    | 1944       | 🇺🇸
```

#### Numeric Data with Alignment
```markdown
Item        | Quantity | Price
------------|:--------:|------:
Product A   |    15    | $29.99
Product B   |    8     | $15.50
**Total**   |  **23**  |**$45.49**
```

### Table Formatting Tips
- Use **bold** formatting within cells for emphasis
- Include emojis for visual appeal (flags, symbols)
- Add footnotes for additional information
- Right-align numeric columns for better readability

---

## Advanced Features

### Footers and Slide Numbers

Add persistent elements across all slides:

```markdown
footer: © Your Company Name, 2025
slidenumbers: true
```

**Requirements:**
- Must be on the **first lines** of your markdown file
- **No empty lines** between directives
- Will appear on every slide automatically

### Footnotes

Manage footnotes directly where you need them:

```markdown
This text has a footnote[^1] and another[^custom-note].

[^1]: This is the first footnote reference
[^custom-note]: This is a custom footnote reference
```

**Footnote Features:**
- Use numbers or text references
- References can appear anywhere in the document
- Must be unique within the markdown file
- Separate multiple references with blank lines
- Can be referenced from any slide

### Mathematical Formulas

Display beautiful mathematical formulas using TeX/LaTeX syntax:

```markdown
The Schrödinger equation: $$H\\psi = E\\psi$$

Expanded form:
$$-\\frac{\\hbar^2}{2m} \\frac{d^2 \\psi}{dx^2} + V\\psi = E\\psi$$
```

**Formula Features:**
- Enclose TeX commands in `$$` delimiters
- Uses MathJax for beautiful vector graphics
- Supports complex mathematical notation
- Perfect for academic and scientific presentations

### Speaker Notes

Add private notes for presentation mode:

```markdown
# Slide Content Here

^ This is what speaker notes look like when presenting with an external display or in rehearsal mode.
```

**Speaker Notes Features:**
- Add `^` before your notes
- Notes scale automatically to fit the display
- Visible only in speaker/rehearsal mode
- Write as much as needed

---

## Big Text Effects

Create impactful slides with large, dramatic text using the `[fit]` modifier.

### Basic [fit] Usage

```markdown
# [fit] IMPACT

---

# [fit] Create
# [fit] Amazing  
# [fit] **Presentations**
```

### [fit] Rules and Guidelines

**Essential Requirements:**
1. **Only use with headers**: Start with `#` 
2. **No paragraphs or lists**]