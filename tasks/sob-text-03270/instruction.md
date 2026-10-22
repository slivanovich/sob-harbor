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
Edwin Catmull: Edwin Earl Catmull (born March 31, 1945) is a computer scientist and current president of Pixar and Walt Disney Animation Studios (including the latter's DisneyToon Studios division).  As a computer scientist, Catmull has contributed to many important developments in computer graphics.

Anil Menon: Anil Menon is a leading Indian writer of speculative fiction, as well as a computer scientist with a Ph.D. from Syracuse University, who has authored research papers and edited books on Evolutionary Algorithms; his research addressed the mathematical foundations of replicator systems, majorization, and reconstruction of probabilistic databases, in collaboration with Professors Kishan Mehrotra, Chilukuri Mohan, and Sanjay Ranka.  After working for several years as a computer scientist, he has directed his creative energies towards fiction.  His short stories and reviews have appeared in the anthology series Exotic Gothic, "Strange Horizons", Interzone", "Lady Churchill's Rosebud Wristlet", "Chiaroscuro", "Sybil's Garage", "Apex Digest" and other magazines.  In 2009, Zubaan Books, India's leading feminist press, published his debut young adult novel "The Beast With Nine Billion Feet".  It was shortlisted for the 2010 Vodafone Crossword Book Award.  In 2009, in conjunction with Vandana Singh and Suchitra Mathur, he helped organize India's first in-residence, three-week speculative fiction workshop at IIT-Kanpur.

Leonid Levin: Leonid Anatolievich Levin ( ; Russian: Леони́д Анато́льевич Ле́вин ; Ukrainian: Леоні́д Анато́лійович Ле́він ; born November 2, 1948) is a Soviet-American computer scientist.

Leftover hash lemma: The leftover hash lemma is a lemma in cryptography first stated by Russell Impagliazzo, Leonid Levin, and Michael Luby.

Leonid Libkin: Leonid Libkin is a computer scientist who works in database theory, logic in computer science, and finite model theory.

Nuria Oliver: Nuria Oliver is a computer scientist.  She is Director of Data Science Research at Vodafone and Chief Data Scientist at DataPop Alliance.  Previously, she was Scientific Director at Telefónica and a researcher at Microsoft Research.  She holds a PhD from the Media Lab at MIT, and is an IEEE Fellow.  She is one of the most cited female computer scientist in Spain, with her research having been cited by more than 11800 publications.  She is well known for her work in computational models of human behavior, human computer-interaction, mobile computing and big data for social good.

Karatsuba algorithm: The Karatsuba algorithm is a fast multiplication algorithm.  It was discovered by Anatoly Karatsuba in 1960 and published in 1962.  It reduces the multiplication of two "n"-digit numbers to at most formula_1 single-digit multiplications in general (and exactly formula_2 when "n" is a power of 2).  It is therefore faster than the classical algorithm, which requires "n" single-digit products.  For example, the Karatsuba algorithm requires 3 = 59,049 single-digit multiplications to multiply two 1024-digit numbers ("n" = 1024 = 2), whereas the classical algorithm requires (2) = 1,048,576.

David H. Bailey: David Harold Bailey (born 1948) is a mathematician and computer scientist.  He received his B.S. in mathematics from Brigham Young University in 1972 and his Ph.D. in mathematics from Stanford University in 1976.  He worked for 14 years as a computer scientist at NASA Ames Research Center, but since 1998 has been at the Lawrence Berkeley National Laboratory.  He is now officially retired, but continues as an active researcher.  He is also a Research Associate at the University of California, Davis, Department of Computer Science.

Annie Easley: Annie J. Easley (April 23, 1933 – June 25, 2011) was an African-American computer scientist, mathematician, and rocket scientist.  She worked for the Lewis Research Center (now Glenn Research Center) of the National Aeronautics and Space Administration (NASA) and its predecessor, the National Advisory Committee for Aeronautics (NACA).  She was a leading member of the team which developed software for the Centaur rocket stage and one of the first African-Americans to work as a computer scientist at NASA.

Anatoly Karatsuba: Anatoly Alexeevitch Karatsuba (Russian: Анато́лий Алексе́евич Карацу́ба ; Grozny, Soviet Union, January 31, 1937 – Moscow, Russia, September 28, 2008) was a Russian mathematician working in the field of analytic number theory, "p"-adic numbers and Dirichlet series.

Question: Who is a computer scientist, Anatoly Karatsuba or Leonid Levin?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "identified_computer_scientist_name": {
      "type": "string",
      "description": "The name of the person identified as a computer scientist from the question."
    },
    "people_compared": {
      "type": "array",
      "description": "Details for each person mentioned in the question for comparison.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the person."
          },
          "is_computer_scientist": {
            "type": "boolean",
            "description": "True if the person is identified as a computer scientist, false otherwise."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions attributed to the person in the context."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the person, if mentioned."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the person, if mentioned."
          }
        },
        "required": [
          "name",
          "is_computer_scientist",
          "professions"
        ],
        "additionalProperties": false
      }
    },
    "total_people_in_question": {
      "type": "integer",
      "description": "The total number of people whose professions were compared in the question."
    }
  },
  "required": [
    "identified_computer_scientist_name",
    "people_compared",
    "total_people_in_question"
  ],
  "additionalProperties": false
}
