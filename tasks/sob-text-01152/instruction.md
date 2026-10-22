Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Leafpad: Leafpad is an open source text editor for Linux, BSD, and Maemo.  Created with the focus of being a lightweight text editor with minimal dependencies, it is designed to be simple and easy-to-compile.  Leafpad is the default text editor for LXDE Desktop environment, including Lubuntu, and also Xubuntu.

Rich Text Format Directory: Rich Text Format Directory, also known as RTFD (due to its extension ". rtfd"), or Rich Text Format with Attachments, is a primary document format of TextEdit, an application native to NeXTSTEP and OS X which has also been ported to other versions of Unix.  The file format is based on the Rich Text Format, but can also include "attachments" such as images and animations.

Yahoo!: Yahoo! is a web services provider, wholly owned by Verizon Communications through Oath Inc. and headquartered in Sunnyvale, California.  The original Yahoo! company was founded by Jerry Yang and David Filo in January 1994 and was incorporated on March 2, 1995.  Yahoo was one of the pioneers of the early Internet era in the 1990s.  Marissa Mayer, a former Google executive, served as CEO and President of Yahoo until June 2017.

Full-screen writing program: In computing, a full-screen writing program or distraction-free editor is a text editor that occupies the full display with the purpose of isolating the writer from the operating system (OS) and other applications.  In this way one should be able to focus on the writing alone, with no distractions from the OS and a cluttered interface.  Often distraction-free editors feature a dark background and a text field, with lighter colored text.  However, most distraction-free editors include customisable user interfaces.  Some editors support rich text editing.

TECO (text editor): TECO ( ; originally an acronym for [paper] "Tape editor and corrector", but later "Text editor and corrector", then "Text editor character oriented") is a text editor originally developed at the Massachusetts Institute of Technology (MIT) in the 1960s, after which it was modified by many other people.  TECO was a direct ancestor of Emacs, which was originally implemented in TECO macros.

Froala Editor: Froala Editor ( ) is a web-based WYSIWYG rich text editor (RTE).  It is a platform-independent, web-based JavaScript/HTML WYSIWYG text editor made by Froala.  Froala Editor is available under 4 licenses: Single Website License, Developer License, Business License and OEM License.

YUI Rich Text Editor: YUI Rich Text Editor is a project developed by Yahoo! as a part of the YUI Library for an online rich-text editor that replaces a standard HTML textarea.  It allows for drag and drop inclusion and sizing of images, text coloring, realignment, fonts, italic and bold text.  The YUI rich text editor uses a plug in architecture and it is skinnable along with the rest of the YUI.

Markdown: Markdown is a lightweight markup language with plain text formatting syntax.  It is designed so that it can be converted to HTML and many other formats using a tool by the same name.  Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.  As the initial description of Markdown contained ambiguities and unanswered questions, many implementations and extensions of Markdown appeared over the years to answer these issues.

GNU Emacs: GNU Emacs is the most popular and most ported Emacs text editor.  It was created by GNU Project founder Richard Stallman.  In common with other varieties of Emacs, GNU Emacs is extensible using a Turing complete programming language.  GNU Emacs has been called "the most powerful text editor available today."  With proper support from the underlying system, GNU Emacs is able to display files in multiple character sets, and has been able to simultaneously display most human languages since at least 1999.  Throughout its history, GNU Emacs has been a central component of the GNU project, and a flagship of the free software movement.  GNU Emacs is sometimes abbreviated as GNUMACS, especially to differentiate it from other EMACS variants.  The tag line for GNU Emacs is "the extensible self-documenting text editor".

CygnusEd: CygnusEd is a text editor for the Amiga OS and MorphOS.  It was first developed in 1986-1987 by Bruce Dawson, Colin Fox and Steve LaRocque who were working for CygnusSoft Software.  It was the first Amiga text editor with an undo/redo feature and one of the first Amiga programs that had an AREXX scripting port by which it was possible to integrate the editor with AREXX enabled C compilers and build a semi-integrated development environment.  Many Amiga programmers grew up with CygnusEd and a considerable part of the Amiga software library was created with CygnusEd.  It is still one of very few text editors that support jerkyless soft scrolling.

Question: Who owns the company that developed the YUI Rich Text Editor?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "product_developed": {
      "type": "string",
      "description": "The name of the product that was developed."
    },
    "developer_company": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the company that developed the product."
        },
        "owner_company_name": {
          "type": "string",
          "description": "The name of the company that owns the developer company."
        },
        "ownership_structure": {
          "type": "string",
          "description": "Description of how the developer company is owned by the owner company."
        }
      },
      "required": [
        "name",
        "owner_company_name",
        "ownership_structure"
      ],
      "additionalProperties": false
    },
    "final_owner_name": {
      "type": "string",
      "description": "The name of the ultimate owner company."
    }
  },
  "required": [
    "product_developed",
    "developer_company",
    "final_owner_name"
  ],
  "additionalProperties": false
}
