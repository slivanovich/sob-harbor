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
Andrew Bryan (Baptist): Andrew Bryan (1737–1812) founded First Bryan Baptist Church, affectionately called the Mother Church of Black Baptists, and First African Baptist Church of Savannah in Savannah, Georgia, the first black Baptist churches to be established in America.  Bryan was the former slave of Jonathan Bryan.

First Descents: First Descents is a charitable non-profit organization that gives a free outdoor adventure experience trip to young adults who are fighting cancer.  Brad Ludden, a professional kayaker, founded First Descents in 2001 at age 20.

Krefeld Pinguine: The Krefeld Pinguine (Krefeld Penguins) are an ice hockey team in the Deutsche Eishockey Liga.  Their home ice is in Krefeld, North Rhine-Westphalia, Germany at the König Palast.  Founded first in 1936 by Willi Münstermann, the pro team became a limited liability company in 1994 and joined the top tier Deutsche Eishockey Liga.  In their history they have won the German championship in 1952 and 2003.

Michelle Sun: Michelle Sun (born late 1980s) is a Hong Kong engineer, entrepreneur and teacher.  In 2013, she founded First Code Academy which teaches Hong Kong children from the age of six how to code and create mobile applications.  Teaching is given either in their school classrooms or in the firm's own offices.

Spin (magazine): Spin is an American music magazine founded in 1985 by publisher Bob Guccione, Jr. The magazine stopped running in print in 2012 and currently runs as a webzine.

Syracuse Triad: The Syracuse Triad is the name given to the three women's sororities founded at Syracuse University.  Alpha Phi was founded first in 1872 by 10 of the original 20 women admitted into Syracuse University.  Gamma Phi Beta came along two years later in 1874 and with it came the term "sorority," which was coined at the time of its founding.  (Prior to that, women's Greek-letter organizations used the term "women's fraternity," since no more appropriate term existed.)  Alpha Gamma Delta completed the triad in 1904.

Stewart Spiers: Stewart Spiers was a small but innovative firm of plane-makers in Scotland, founded first of all in Ayr in Ayrshire and continuing under the registered name of Stewart Speirs Ltd ["sic"] in Paisley, Renfrewshire, from c. 1933 until its demise in the mid to late 1930s.  Like the Glasgow firm of Alexander Mathieson & Sons, Spiers benefited hugely from the thriving industries on the Firth of Clyde in the latter half of the nineteenth century.

Penco: Penco (Mapudungun: "Peumo water") is a Chilean city and commune in Concepción Province, Bío Bío Region on the Bay of Concepción.  Founded as the city of Concepción del Nuevo Extremo ('beginning of the new extreme') on February 12, 1550 by Pedro de Valdivia, it is the third oldest city in Chili, after capital Santiago founded first in 1541 and La Serena second in 1544.

Tanta University: It was founded first in 1962 as a branch from the University of Alexandria with the faculty of Medicine only and then it became an independent university named University of the Middle Delta in 1972.  It had at that time Medicine, Science, Agriculture and Education faculties.  Then, its name was changed into Tanta University in 1973.

InStyle: InStyle is a monthly women’s fashion magazine published in the US by Time Inc. "InStyle" was founded in 1994.

Question: Was InStyle or Spin founded first?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "first_founded_entity": {
      "type": "string",
      "description": "The name of the entity that was founded first."
    },
    "first_founded_year": {
      "type": "integer",
      "description": "The year the first entity was founded."
    },
    "second_entity": {
      "type": "string",
      "description": "The name of the other entity in the comparison."
    },
    "second_entity_year": {
      "type": "integer",
      "description": "The year the second entity was founded."
    },
    "is_first_entity_older": {
      "type": "boolean",
      "description": "True if the first_founded_entity was indeed founded earlier than the second_entity."
    },
    "comparison_summary": {
      "type": "string",
      "description": "A summary statement comparing the founding dates of the two entities."
    }
  },
  "required": [
    "first_founded_entity",
    "first_founded_year",
    "second_entity",
    "second_entity_year",
    "is_first_entity_older",
    "comparison_summary"
  ],
  "additionalProperties": false
}
