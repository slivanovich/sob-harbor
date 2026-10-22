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
Henry M. Morris: Henry Madison Morris (October 6, 1918 – February 25, 2006) was an American young Earth creationist, Christian apologist, and engineer.  He was one of the founders of the Creation Research Society and the Institute for Creation Research.  He is considered by many to be "the father of modern creation science."  He is widely known for coauthoring "The Genesis Flood" with John C. Whitcomb in 1961.

Museum of Creation and Earth History: The Museum of Creation and Earth History is a young earth creationist promotional facility opened by the Institute for Creation Research at its original headquarters in Santee, California in 1992, replacing an earlier museum located in the Institute's basement.  It cost $50,000, and took 2 years to complete.

Hendren v. Campbell: Hendren et al. v. Campbell et al. was a 1977 ruling by an Indiana state superior court that the young-earth creationist textbook could not be used in Indiana public schools.  Jon Hendren, a ninth-grade student in the West Clark Community Schools, sued when the district picked "Biology: A Search For Order In Complexity", published by the Creation Research Society and promoted through the Institute for Creation Research, as the sole biology textbook.

John Baumgardner: John R. Baumgardner is an American young earth creationist and geophysicist.

Kurt Wise: Kurt Patrick Wise (born 1959) is an American young earth creationist who serves as the Director of Creation Research Center at Truett McConnell University.  He has a PhD in paleontology from Harvard University.  He is known for his writings in support of creationism as well as his work for the Creation Museum.

Duane Gish: Duane Tolbert Gish (February 17, 1921 – March 5, 2013) was an American biochemist and a prominent member of the creationist movement.  A Young Earth creationist, Gish was a former vice-president of the Institute for Creation Research (ICR) and the author of numerous publications about creation science.  Gish was called "creationism's T. H. Huxley" for the way he "relished the confrontations" of formal debates with prominent evolutionary biologists, usually held on university campuses.  A creationist publication noted in his obituary that "it was perhaps his personal presentation that carried the day.  In short, the audiences liked him."

RATE project: The RATE project (Radioisotopes and the Age of The Earth) was a research project conducted by the Creation Research Society and the Institute for Creation Research between 1997 and 2005 to assess the validity of radiometric dating and other dating techniques in the light of the doctrine of a recent creation.  It was funded by $250,000 from the Institute for Creation Research and over $1 million in donations.  The RATE team was chaired by Larry Vardiman (meteorology) and included Steven A. Austin (soft rock geology), John Baumgardner (geophysics), Steven W. Boyd (Hebrew), Eugene F. Chaffin (physics), Donald B. DeYoung (physics), Russell Humphreys (physics) and Andrew Snelling (hard rock geology).

Frank Lewis Marsh: Frank Lewis Marsh (18 October 1899, Aledo, Illinois – 14 July 1992) was an American Seventh-day Adventist biologist, educator and young Earth creationist author.  In 1963 he was one of the ten founding members of the Creation Research Society.

John D. Morris: John David Morris (born 1946) is an American young earth creationist.  He is the son of "the father of creation science", Henry M. Morris, and after his father's death became the president of the Institute for Creation Research (ICR).  Morris is a creationist author and speaks at a variety of churches.  Many of his presentations discuss the fossil record and its relation to evolution.

Institute for Creation Research: The Institute for Creation Research (ICR) is a Creationist apologetics institute in Dallas, Texas that specializes in media promotion of pseudoscientific creation science and interpretation of the Genesis creation narrative as a historical event.  The ICR adopts the Bible as an inerrant and literal documentary of scientific and historical fact as well as religious and moral truths, and espouses a Young Earth creationist worldview.  It rejects evolutionary biology, which it views as a corrupting moral and social influence and threat to religious belief.  The ICR was formed by Henry M. Morris in 1972 following an organizational split with the Creation Science Research Center (CSRC).

Question: What  American young earth creationist and geophysicist was on  a research project conducted by the Creation Research Society and the Institute for Creation Research between 1997 and 2005?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the individual."
    },
    "person_profession": {
      "type": "string",
      "description": "The profession of the individual."
    },
    "person_affiliation": {
      "type": "string",
      "description": "The specific affiliation or belief system of the individual."
    },
    "research_project": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the research project."
        },
        "conducting_organizations": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of organizations that conducted the research project."
        },
        "start_year": {
          "type": "integer",
          "description": "The start year of the research project."
        },
        "end_year": {
          "type": "integer",
          "description": "The end year of the research project."
        }
      },
      "required": [
        "name",
        "conducting_organizations",
        "start_year",
        "end_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "person_profession",
    "person_affiliation",
    "research_project"
  ],
  "additionalProperties": false
}
