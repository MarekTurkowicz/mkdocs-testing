# Markdown Tutorial
- [Markdown Tutorial - site version](https://blog.webdevsimplified.com/2023-06/markdown-crash-course/#interactive-markdown-editor)
- [Markdown Tutorial - Youtube version](https://www.youtube.com/watch?v=_PPWWRV6gbA&ab_channel=WebDevSimplified)

## Headings (#)
**Created by putting one to six `#` symbols in front of your heading text.**

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

## Paragraphs
**If you just type text, it will automatically be converted into a paragraph.**

```markdown
This is a paragraph.
```

## Text Styling (* _ ** __)
**Use one `*` or `_` to italicize text and two `*` or `_` to bold text.**

```markdown
*This is italicized text*  
_This is also italicized text_  

**This is bold text**  
__This is also bold text__
```

**To make text both bold and italicized, wrap it in three `*` or `_`.**

```markdown
***This is both***  
___This is also both___


## Inline Code (`)
**Wrap your code in a single backtick (`) to format it as inline code.**


This is `inline code tutorial` within a paragraph.


## Code Blocks (```)
**For multi-line code blocks, wrap your code with three backticks. Optionally, specify the language for syntax highlighting.**


```py
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
```



## Lists (- * 1. 2.)
**To create an unordered list, add `-`, `*`, or `+` before each item. For an ordered list, use numbers followed by a `.` character.**

```markdown
- This is an unordered list
- Of items

1. This is an ordered list
2. The numbers do not matter
3. This says 3
   * This is a nested list
   * Of items
      1. This is a nested
      2. List of items
```

## Tables
**To create a table, use `|` to separate columns and `|` at the start and end of each row. The second row must contain three or more `-` for each column, with `:` optionally added to control text alignment.**

| Col 1 | Col 2 |
| ----- | ------ |
| This  | is      |
| an    | example |
| table | with    |
| two   | columns |



| Right  | Center | Left |
| ------ | :-----: | :--- |
| R      | C       | L    |

| Head One | Head Two |
| -------- | -------- |
| Does Not Need | To Be |
| Aligned        | Properly |


