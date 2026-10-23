{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIsrael Gelfand: Israel Moiseevich Gelfand, also written Israïl Moyseyovich Gel'fand, or Izrail M. Gelfand (Yiddish: ישראל געלפֿאַנד‎ , Russian: Изра́иль Моисе́евич Гельфа́нд ; 2 September [O.S. 20 August] 1913 – 5 October 2009) was a prominent Soviet mathematician.  He made significant contributions to many branches of mathematics, including group theory, representation theory and functional analysis.  The recipient of many awards, including the Order of Lenin and the Wolf Prize, he was a Fellow of the Royal Society and professor at Moscow State University and, after immigrating to the United States shortly before his 76th birthday, at Rutgers University.\n\nMikhail Kravchuk (footballer): Mikhail Kravchuk (Belarusian: Мiхаiл Краўчук ; Russian: Михаил Кравчук ; born 19 September 1991) is a Belarusian professional football player currently playing for Luch Minsk.\n\nGelfand–Naimark theorem: In mathematics, the Gelfand–Naimark theorem states that an arbitrary C*-algebra \"A\" is isometrically *-isomorphic to a C*-algebra of bounded operators on a Hilbert space.  This result was proven by Israel Gelfand and Mark Naimark in 1943 and was a significant point in the development of the theory of C*-algebras since it established the possibility of considering a C*-algebra as an abstract algebraic entity without reference to particular realizations as an operator algebra.\n\nGelfand–Naimark–Segal construction: In functional analysis, a discipline within mathematics, given a C*-algebra \"A\", the Gelfand–Naimark–Segal construction establishes a correspondence between cyclic *-representations of \"A\" and certain linear functionals on \"A\" (called \"states\").  The correspondence is shown by an explicit construction of the *-representation from the state.  It is named for Israel Gelfand, Mark Naimark, and Irving Segal.\n\nLutsk Gymnasium 21: Lutsk Gymnasium #  21 after Mikhail Kravchuk  is an elementary (grades 1-4), middle (grades 5-9) and high (grades 10-11) school with the specialization in some subjects, determined yearly according to the students' and parents' wishes, recommendations of senior teachers and a stuff phycologist.\n\nVladimir Mazya: Vladimir Gilelevich Maz'ya (Russian: Владимир Гилелевич Мазья ; born December 31, 1937) (the family name is sometimes transliterated as Mazya, Maz'ja or Mazja) is a Russian-born Swedish mathematician, hailed as \"one of the most distinguished analysts of our time\" and as \"an outstanding mathematician of worldwide reputation\", who strongly influenced the development of mathematical analysis and the theory of partial differential equations.  His early achievements include: his work on Sobolev spaces, in particular the discovery of the equivalence between Sobolev and isoperimetric/isocapacitary inequalities (1960), his counterexamples related to Hilbert's 19th and Hilbert's 20th problem (1968), his solution, together with Yuri Burago, of a problem in harmonic potential theory (1967) posed by , his extension of the Wiener regularity test to p –Laplacian and the proof of its sufficiency for the boundary regularity.  Maz'ya solved V. Arnol'd's problem for the oblique derivative boundary value problem (1970) and F. John's problem on the oscillations of a fluid in the presence of an immersed body (1977).  In recent years, he proved a Wiener's type criterion for higher order elliptic equations, together with M. Shubin solved a problem in the spectral theory of the Schrödinger operator formulated by Israel Gelfand in 1953, found necessary and sufficient conditions for the validity of maximum principles for elliptic and parabolic systems of PDEs and introduced the so–called approximate approximations.  He also contributed to the development of the theory of capacities, nonlinear potential theory, the asymptotic and qualitative theory of arbitrary order elliptic equations, the theory of ill-posed problems, the theory of boundary value problems in domains with piecewise smooth boundary.\n\nLiouville–Bratu–Gelfand equation: In mathematics, Liouville–Bratu–Gelfand equation or Lioville's equation is a non-linear eigenvalue Poisson equation, named after the mathematicians Joseph Liouville, G. Bratu and Israel Gelfand.  The equation reads\n\nVictor Lidskii: Victor Borisovich Lidskii (Russian: Виктор Борисович Лидский , 4 May 1924, Odessa – 29 July 2008, Moscow) was a Soviet and Ukrainian mathematician who worked in spectral theory, operator theory, and shell theory.  Lidskii discovered the Lidskii theorem in 1959.  His adviser at Moscow State University was Israel Gelfand.\n\nGelfand–Mazur theorem: In operator theory, the Gelfand–Mazur theorem is a theorem named after Israel Gelfand and Stanisław Mazur which states that a Banach algebra with unit over the complex numbers in which every nonzero element is invertible is isometrically isomorphic to the complex numbers, i. e., the only complex Banach algebra that is a division algebra is the complex numbers C.\n\nMikhail Kravchuk: Mykhailo Pylypovych Kravchuk, also Krawtchouk (Ukrainian: Миха́йло Пили́пович Кравчу́к ) (September 27, 1892 – March 9, 1942), was a Soviet Ukrainian mathematician who, despite his early death, was the author of around 180 articles on mathematics.\n\nQuestion: Who was born first, Mikhail Kravchuk or Israel Gelfand?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"first_individual\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"second_individual\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_born_earliest\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the individual who was born first.\"\n    },\n    \"earliest_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the individual born earliest.\"\n    },\n    \"latest_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the individual born latest.\"\n    }\n  },\n  \"required\": [\n    \"first_individual\",\n    \"second_individual\",\n    \"person_born_earliest\",\n    \"earliest_birth_year\",\n    \"latest_birth_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "first_individual": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "birth_year": {
            "type": "integer"
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "second_individual": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "birth_year": {
            "type": "integer"
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "person_born_earliest": {
        "type": "string",
        "description": "The name of the individual who was born first."
      },
      "earliest_birth_year": {
        "type": "integer",
        "description": "The birth year of the individual born earliest."
      },
      "latest_birth_year": {
        "type": "integer",
        "description": "The birth year of the individual born latest."
      }
    },
    "required": [
      "first_individual",
      "second_individual",
      "person_born_earliest",
      "earliest_birth_year",
      "latest_birth_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
