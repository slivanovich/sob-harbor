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
Python Imaging Library: Python Imaging Library (abbreviated as PIL) (in newer versions known as Pillow) is a free library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.  It is available for Windows, Mac OS X and Linux.  The latest version of PIL is 1.1.7, was released in September 2009 and supports Python 1.5.2–2.7, with Python 3 support to be released "later".

RUR-PLE: RUR - Python Learning Environment (RUR-PLE) is an educational tool to help students learn the Python programming language.  Made by André Roberge.  RUR-PLE uses the idea behind Karel the Robot, making the learning of Python programming more interesting.  A student writes a program that controls a 'robot' that moves through a city consisting of a rectangular grid of streets (left-right) and avenues (up-down).

Jim Hugunin: Jim Hugunin is a software programmer who created the Python programming language extension Numeric (ancestor to NumPy), and later created Python implementations for the Java Platform (Jython) and for Microsoft . NET platform (IronPython); he has also co-designed the AspectJ extension for the Java programming language.  He worked for Microsoft from 2004 to 2010, mainly on IronPython and Dynamic Language Runtime.

PyPy: PyPy is an alternate implementation of the Python programming language written in Python.  Specifically, its interpreter is written in RPython (a subset of Python).  In contrast, the standard reference implementation of Python is written in C (known as CPython).  The implementation of the interpreter in high level Python, over a low-level implementation in C, enables quick experimentation of new language features.  This is shown to have benefits in areas of execution speed, memory usage, sandboxing etc., in certain use cases.  The self-hosting nature of PyPy is reflected in the project's logo, which depicts a snake swallowing its own tail in an ouroboros.

Python Software Foundation: The Python Software Foundation (PSF) is a nonprofit organization devoted to the Python programming language, launched on March 6, 2001.  The mission of the foundation is to foster development of the Python community and is responsible for various processes within the Python community, including developing the core Python distribution, managing intellectual rights, developer conferences including PyCon, and raising funds.

Core Python Programming: Core Python Programming is a textbook on the Python programming language, written by Wesley J. Chun.  The first edition of the book was released on December 14, 2000.  The second edition was released several years later on September 18, 2006.  "Core Python Programming" is targeted mainly at higher education students and IT professionals.

Taiwan Python Conference: Taiwan Python Conference also known as Annual Taiwan Python Conference abbreviated PyCon TW has been held by Python communities in Taiwan since 2012 at Academia Sinica's human and social study research institute, aimed to discuss the improvement and versatile application of Python programming language and promote the use of it.

Anaconda (Python distribution): Anaconda is a freemium open source distribution of the Python and R programming languages for large-scale data processing, predictive analytics, and scientific computing, that aims to simplify package management and deployment.  Package versions are managed by the package management system "conda".

Guido van Rossum: Guido van Rossum (] , born 31 January 1956) is a Dutch programmer who is best known as the author of the Python programming language.  In the Python community, van Rossum is known as a "Benevolent Dictator For Life" (BDFL), meaning that he continues to oversee the Python development process, making decisions where necessary.  He was employed by Google from 2005 until December 7th 2012, where he spent half his time developing the Python language.  In January 2013, van Rossum started working for Dropbox.

Astropy: Astropy is a collection of software packages written in the Python programming language and designed for use in .  The software is a single, free, core package for astronomical utilities due to the increasingly widespread usage of Python by astronomers, and to foster interoperability between various extant Python astronomy packages.  Astropy is included in several large Python distributions; it is part of package managers for Linux and macOS, the Anaconda Python Distribution, Enthought Canopy and Ureka.

Question: Which other snake's name is the brand for a distribution of the Python programming language that includes Astropy?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "distribution_name": {
      "type": "string",
      "description": "The name of the Python programming language distribution."
    },
    "distribution_details": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "description": "The general type of the software, e.g., 'Python distribution'."
        },
        "is_open_source": {
          "type": "boolean",
          "description": "Indicates if the distribution is open source."
        },
        "supported_languages": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of programming languages supported by the distribution."
        },
        "includes_astropy": {
          "type": "boolean",
          "description": "Indicates if the Astropy package is included in this distribution."
        }
      },
      "required": [
        "type",
        "is_open_source",
        "supported_languages",
        "includes_astropy"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The final answer to the question, which is the name of the distribution."
    }
  },
  "required": [
    "distribution_name",
    "distribution_details",
    "final_answer"
  ],
  "additionalProperties": false
}
