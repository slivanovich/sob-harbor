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
Cornell University Department of History: The Cornell University Department of History is an academic department in the College of Arts and Sciences at Cornell University that focuses on the study of history.  Founded in 1868, it is one of Cornell's original departments.  Its first faculty included university president Andrew Dickson White and English historian Goldwin Smith.  In 1881, the department named Moses Coit Tyler the first professor of American history in the United States.  Three of Cornell's twelve presidents have been members of the department: Andrew Dickson White, Charles Kendall Adams, and Hunter R. Rawlings III.  The longest teaching member of the faculty was Frederick Marcham who, upon completing his graduate work at Cornell in 1924, continued lecturing until a month before his death in 1992 – a total of 68 years.

Cornell University Glee Club: The Cornell University Glee Club (CUGC) is the oldest student organization at Cornell University, having been organized shortly after the first students arrived on campus in 1868.  The CUGC is a sixty-member chorus for male voices, with repertoire including classical, folk, 20th-century music, and traditional Cornell songs.  The Glee Club also performs major works with the Cornell University Chorus such as Beethoven's Missa Solemnis, Handel's Messiah, and Bach's Mass in B Minor.

Hilary Blumberg: Hilary Patricia Blumberg is a medical doctor and the inaugural John and Hope Furth Professor of Psychiatry at the Yale School of Medicine.  She is also a professor of Radiology and Biomedical Imaging, and works in the Child Study Center at Yale where she has been a faculty member since 1998.  She attended Harvard University as an undergraduate, and completed medical school at Cornell University Medical College (1990).  She completed her medical internship and psychiatry residency at Cornell University Medical College/New York Hospital, and her neuroimaging fellowship training at Cornell University, Weill Medical College.  She has received numerous awards for her work such as the 2006 National Alliance for Research in Schizophrenia and Depression (NARSAD) and the Gerald L. Klerman Award for Clinical Research.  Blumberg has authored a number of scientific articles that focus on bipolar disorder, neuroimaging, and effects of specific genetic variations, developmental trajectories and structure-function relationships.

List of presidents of Cornell University: The President of Cornell University is the chief administrator of Cornell University, an Ivy League institution located in Ithaca, New York and New York City.  Included in the list below are all Presidents of Cornell University, from the first President Andrew Dickson White and through the current President, Martha E. Pollack.  There have been 14 Presidents of Cornell University, not including three interregnum presidencies during university presidential transitions.

List of Cornell University alumni: This list of Cornell University alumni includes notable graduates, non-graduate former students, and current students of Cornell University, an Ivy League university located in Ithaca, New York.  Cornell counted 245,027 living alumni as of August 2008.  Its alumni constitute 25 recipients of National Medal of Science and National Medal of Technology and Innovation combined, 32 MacArthur Fellows, 34 Marshall Scholars and 31 Rhodes Scholars, and Cornell is the only university with three female winners of unshared Nobel Prizes among its graduates (Pearl S. Buck, Barbara McClintock, and Toni Morrison).  Many alumni maintain university ties through Homecoming's reunion weekend, through "Cornell Magazine", and through the Cornell Club of New York.  In 2005, Cornell ranked #3 nationwide for gifts and bequests from alumni.  Alumni are known as "Cornellians".

Irving Literary Society (Cornell University): The Irving Literary Society (also known as the Irving Literary Association or simply The Irving) was a literary society at Cornell University active from 1868 to 1887.  The U.S. Bureau of Education described it as a "purely literary society" following the "traditions of the old literary societies of Eastern universities."  During the period when the Cornell literary societies flourished, the Irving and its peers produced literature at a rate higher than the campus average for the next generation, leading commentators at the turn of the 20th century to question whether academic standards had fallen since the university's founding.  Named after the American writer Washington Irving, the Irving Literary Society was founded on October 20, 1868, shortly after Cornell opened.  Past members who went on to prominent careers included Judge Morris Lyon Buchwalter, Senator Joseph Benson Foraker, and the journalists John Andrew Rea and Francis Whiting Halsey.  The Irving's last public meeting was held on May 23, 1887.  After that it ceased to exist as a Cornell University student society.  However, the New York Alpha Chapter of the Phi Kappa Psi undergraduate fraternity at Cornell claims to have "served as steward of the Irving Literary Society

Cornell University: Cornell University ( ) is a private and statutory Ivy League research university located in Ithaca, New York.  Founded in 1865 by Ezra Cornell and Andrew Dickson White, the university was intended to teach and make contributions in all fields of knowledge—from the classics to the sciences, and from the theoretical to the applied.  These ideals, unconventional for the time, are captured in Cornell's motto, a popular 1865 Ezra Cornell quotation: "I would found an institution where any person can find instruction in any study."

Weill Cornell Graduate School of Medical Sciences: The Weill Cornell Graduate School of Medical Sciences (WCGS) (formerly known as the Cornell University Graduate School of Medical Sciences) is a graduate college of Cornell University that was founded in 1952 as an academic partnership between two major medical institutions in New York City: the Weill Cornell Medical College and the Sloan-Kettering Institute.  Cornell is involved in the Tri-Institutional MD-PhD Program with Rockefeller University and the Sloan-Kettering Institute; each of these three institutions is part of a large biomedical center extending along York Avenue between 65th and 72nd Streets on the Upper East Side of Manhattan.

University of Cincinnati: The University of Cincinnati (commonly referred to as UC or Cincinnati) is a comprehensive public research university in Cincinnati, in the U.S. state of Ohio, and a part of the University System of Ohio.

The Hangovers (Cornell University): The Hangovers are a men's collegiate a cappella ensemble based at Cornell University.  Founded in 1968, they are the oldest active "a cappella" group on campus and are the official "a cappella" subset of the Cornell University Glee Club, itself the oldest student organization of any kind at Cornell University.  The Hangovers' repertoire consists mainly of popular songs arranged for the ensemble by its members and alumni, but the group also performs traditional Cornell songs, as well as selections from the Glee Club repertoire on occasion.

Question: Cornell University and University of Cincinnati, are which type of universities?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "universities_compared": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the university."
          },
          "type": {
            "type": "string",
            "description": "The specific type of the university as described in the context."
          },
          "location": {
            "type": "string",
            "description": "The primary location of the university."
          }
        },
        "required": [
          "name",
          "type",
          "location"
        ],
        "additionalProperties": false
      },
      "description": "Details for each university mentioned in the question."
    },
    "common_university_type": {
      "type": "string",
      "description": "The common type of university shared by all universities in the question."
    },
    "number_of_universities": {
      "type": "integer",
      "description": "The total number of universities being compared."
    }
  },
  "required": [
    "universities_compared",
    "common_university_type",
    "number_of_universities"
  ],
  "additionalProperties": false
}
