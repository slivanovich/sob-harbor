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
V. Lakshminarayana: V. Lakshminarayana (1911 – 1990) was the Professor of Music from Kerala, India.  He was born in Kerala in 1911 and became professor of music at the age of 29.  His sons L. Vaidyanathan, L. Subramaniam and L. Shankar are also a notable musicians.

Johar Ali Khan: Johar Ali Khan is a Classical Indian violinist.  He is the son and disciple of the Late Ustad Gohar Ali Khan of Rampur, one of the greatest violin genius.  He belongs to the Patiala Gharana of Rampur.  He is the only living classical violinist from Patiala Gharana after his father - late Ustatd Gohar Ali Khan.  His grandfather was Ustad Ali Baksh, the founder of Patiala Gharana, who has produced a number of great musicians like Bade Fateh Ali Khan, Amanat Ali Khan, Asad Amanat Ali Khan, and Hamid Ali Khan.

Subbana (Book): Subbanna is a story written by Masti Venkatesh Iyengar. This is a bildungsroman about an Indian violinist.  This book has got translated to Hindi, Tamil, English and other languages.  Subbanna's father is highly respected scholar in royal court of Mysuru and he hopes his son also follow his footsteps.  However, Subbanna likes music and the story goes through the conflict Subbanna faces thought his life.

R. R. Keshavamurthy: RR Keshavamurthy (1913-2006) was an Indian violinist.  RRK, as he was popularly known specialised in the seven-stringed violin.  RRK was a student of Bidaram Krishnappa, the guru of the violinist Mysore T. Chowdiah.  He was a said to be a legend of seven stringed violin, and the only performing seven stringed violinist to have lived well into the 21st century.  He influenced senior musicians like T. Rukmini, Bhuvaneshawaraih, M.S.Krishnaveni and Anoor Ramakrishna.

L. Subramaniam: Dr. Lakshminarayana Subramaniam (born 23 July 1947) is an acclaimed Indian violinist, composer and conductor, trained in the classical Carnatic music tradition and Western classical music, and renowned for his virtuoso playing techniques and compositions in orchestral fusion.

V. G. Jog: Vishnu Govind Jog, better known as V. G. Jog (22 February 1922 – 31 January 2004), was an Indian violinist.  He was the foremost exponent of the violin in the Hindustani music tradition in the 20th century, and is credited for introducing this instrument into Hindustani music.

V. Balaji: V. Balaji (born 1958) is an Indian violinist who performs Hindustani classical music.  Presently he is a Professor of Music at Banaras Hindu University, eventually became Head of the Instrumental department.

L. Vaidyanathan: Lakshminarayana Vaidyanathan (Tamil: லக்ஷ்மிநாராயண வைத்தியநாதன் ; Kannada: ಎಲ್. ವೈದ್ಯನಾಥನ್ ; April 9, 1942 - May 19, 2007) was an acclaimed musicologist, music director and composer, trained in the classical Carnatic music tradition.  Vaidyanathan was born to V.Lakshminarayana, and Seethalakshmi, both accomplished musicians; he was also the elder brother of accomplished violinist duo L. Shankar and L. Subramaniam.  All three brothers received their musical training from their father.

Manoj George: Manoj George is an Indian violinist and a music composer.  He performed as the conductor, string arranger, violinist and choral arranger for the album "Winds of Samsara", which won the Grammy Award for the Best New Age Album in 2015, making him the first Malayali musician to receive the honor.  He is reported to be the first Indian violinist recognized by the National Academy of Recording Arts and Sciences,The Grammys, USA.

Mysore Manjunath: Mysore Manjunath is a noted Indian violinist.  The son and disciple of violinist Prof. Mahadevappa, Manjunath performed his first concert at the age of 8 in Mysore.  Trained under his father, Manjunath, received special coaching in violin technique and improvisation.  He is one of the Mysore brothers duo.

Question: Which son of V. Lakshminarayana was a notable Indian violinist?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "parent_name": {
      "type": "string",
      "description": "The name of the father."
    },
    "violinist_son": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the son who is a notable Indian violinist."
        },
        "profession": {
          "type": "string",
          "description": "The primary musical profession of the son."
        },
        "other_roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other musical roles or professions of the son."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the son."
        }
      },
      "required": [
        "name",
        "profession"
      ],
      "additionalProperties": false
    },
    "other_notable_sons": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of another notable son."
          },
          "profession": {
            "type": "string",
            "description": "The primary profession of this son."
          },
          "is_violinist": {
            "type": "boolean",
            "description": "Indicates if this son is also a violinist."
          }
        },
        "required": [
          "name",
          "profession",
          "is_violinist"
        ],
        "additionalProperties": false
      },
      "description": "A list of other notable sons of V. Lakshminarayana."
    }
  },
  "required": [
    "parent_name",
    "violinist_son",
    "other_notable_sons"
  ],
  "additionalProperties": false
}
