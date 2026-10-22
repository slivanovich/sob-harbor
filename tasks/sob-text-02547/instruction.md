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
Polytechnic University of San Luis Potosí: The Polytechnic University of San Luis Potosí (in Spanish: Universidad Politécnica de San Luis Potosí, UPSLP) was created on 27 June 2001 and was the first Polytechnic University of the Subsystem of Polytechnic Universities.

Institute of technology: An institute of technology (also: university of technology, polytechnic university, technikon, and technical university) is a type of university which specializes in engineering, technology, Applied Science, and sometimes natural sciences.  Many Institutes of Technology or Polytechnic Universities are in the global elite of university rankings.  But how the terms are used varies from country to country.

National Polytechnic School (Ecuador): The National Polytechnic University (Spanish: Escuela Politécnica Nacional), also known as EPN, is a public university in Quito, Ecuador.  The campus, called "José Rubén Orellana", is located at the sector center-oriental of Quito.  It occupies an area of 15.2 hectares and has a built area of around 62,000 metres.  Its student body numbers approximately 10,000 of which thirty percent are women.  The main campus encompasses ten teaching and research faculties, in addition to four technical and specialized institutes.  EPN was founded in 1869 with the aim of becoming the first technical and technological center in the country.  Since its beginnings, EPN adopted the polytechnic university model, which stresses laboratory instruction in applied science and engineering.  At the campus, there are some libraries with a content primarily oriented to engineering and scientific topics.

Virginia P. Ruesterholz: Virginia P. Ruesterholz is the president of Verizon Services Operations.  She is also the chairman of the Board of Trustees of Stevens Institute of Technology.  She has a BS from Stevens Institute of Technology and an MS from New York University Tandon School of Engineering.

Stevens Institute of Technology: Stevens Institute of Technology (SIT) is a private, coeducational research university located in Hoboken, New Jersey, United States.  The university also has a satellite location in Washington, D.C..  Incorporated in 1870, it is one of the oldest technological universities in the United States, and was the first college in America solely dedicated to mechanical engineering.  The campus encompasses Castle Point, the highest point in Hoboken, and several other buildings around the city.

Stevens Cooperative School: Stevens Cooperative School is a private school for two-year-olds through 8th grade with campuses in Hoboken and Newport, Jersey City.  Founded in 1949, Stevens is the oldest parent cooperative school in New Jersey, and an excellent model of progressive education in action.  Originally an informal playgroup for children of the faculty at Stevens Institute of Technology, the school has grown into a full progressive nursery, elementary and middle school with over 420 students.  The Stevens community consists of a diverse population of families representing a broad range of towns including Hoboken, Jersey City, Weehawken, North Bergen, Secaucus, Union City, Bayonne, West New York, Cliffside Park and other NJ locations and Manhattan.

Polytechnic University of Bari: The Polytechnic University of Bari (Italian: "Politecnico di Bari" ) is a university located in Bari, Italy.  It was founded in 1990 and is organized in 3 Faculties.

George Bugliarello: George Bugliarello, (1928-February 2011) President Emeritus (having served as president from 1973 to 1994), Institute Professor and former chancellor (1994–2003) of the Polytechnic Institute of NYU (formerly Polytechnic University), was an engineer and educator with a broad background ranging from fluid mechanics to computer languages, the environment, biomedical engineering and science policy.  He held a Doctor of Science degree in engineering from the Massachusetts Institute of Technology, and was awarded honorary degrees from Carnegie-Mellon University, the University of Trieste, the Milwaukee School of Engineering, the Illinois Institute of Technology, Pace University, Trinity College, Rensselaer Polytechnic Institute, and the University of Minnesota.

Tomsk Polytechnic University: Tomsk Polytechnic University (TPU) in Tomsk, Russia, is the oldest technical university in Russia east of the Urals.  The university was founded in 1896 and opened in 1900 as the Tomsk Technological Institute.  In 1925, the school was renamed the Siberian Technological Institute and in 1930, the institute was split into five divisions, three of which remained in Tomsk.  In 1934, the three institutes in Tomsk reunited to form a new institute that would be named the Tomsk Polytechnic Institute.  The university has more than 22,000 current students and has graduated more than 100,000 technical specialists.  s of 2014 the rector was Petr S. Chubik.

Institute of Technology (United States): Polytechnic Institutes are technological universities many dating back to the mid 19th century.  A handful of American universities include the phrases Institute of Technology, Polytechnic Institute, Polytechnic University, University of Technology or similar phrasing in their names; these are generally research-intensive universities with a focus on Science, Technology, Engineering, and Mathematics.

Question: Which unversity was founded first, Stevens Institute of Technology or Polytechnic University of Bari?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "universities_compared": {
      "type": "array",
      "description": "List of universities being compared for their founding dates.",
      "items": {
        "type": "object",
        "properties": {
          "university_name": {
            "type": "string",
            "description": "The name of the university."
          },
          "founding_year": {
            "type": "integer",
            "description": "The year the university was founded."
          }
        },
        "required": [
          "university_name",
          "founding_year"
        ],
        "additionalProperties": false
      }
    },
    "first_founded_university": {
      "type": "object",
      "description": "Details of the university that was founded first.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the university founded first."
        },
        "founding_year": {
          "type": "integer",
          "description": "The founding year of the university founded first."
        }
      },
      "required": [
        "name",
        "founding_year"
      ],
      "additionalProperties": false
    },
    "comparison_summary": {
      "type": "string",
      "description": "A summary statement indicating which university was founded first."
    }
  },
  "required": [
    "universities_compared",
    "first_founded_university",
    "comparison_summary"
  ],
  "additionalProperties": false
}
