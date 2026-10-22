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
Santolo Cirillo: Santolo Cirillo (active first half of 18th century, died 1742) was an Italian painter, engraver, and stucco artist, active in Naples.  He was born in Grumo Nevano, a town near Naples.  He contributed frescoes and paintings for Santa Caterina a Formiello, the Cathedral of San Gennaro, the Basilica of Santa Restituta, and Santa Donna Regina Nuova in Naples.  He also painted for the Basilica di San Tamaro in his home town of Grumo Nevano.

Music video director: A music video director is the head of music video production.  The director conceives of videos' artistic and dramatic aspects while instructing the musical act, technical crew, actors, models, and dancers.  They may or may not be in collaboration with the musical act.

Jacopo Bertucci: Jacopo Bertucci (active first half 16th century) was an Italian painter of the Renaissance period.  He is also known as Jacopone da Faenza.  He was born in Faenza, and worked under Raphael in Rome.  One of his pupils was Taddeo Zuccari.  He was active c. 1530 and painted in the manner of Raphael.  He painted for the church of San Vitale at Ravenna.  He died at the age of 20.

Master of San Verecondo: The Master of San Verecondo (active first half of 15th century) was an anonymous painter active in the towns of Fabriano and Gualdo Tadino in the Marche.

Pietro Paolo Baldinacci: Pietro Paolo Baldinacci (active first half of 16th century) was an Italian painter of the Renaissance, active in Gubbio.

APB (band): APB was a Scottish post-punk band, formed in 1979, that blended funk rock, punk rock and new wave music.  The group had only modest success during its brief run, yet their influence can be heard in the sound of such current bands as Franz Ferdinand, The Rapture, and Red Hot Chili Peppers.

Girolamo Lancerotti: Girolamo Lancerotti (active first half of the 1600s) was an Italian painter, active mainly in the Veneto.  He was born at Verona,and is best known for an altarpiece of St Jerome in Santa Maria Consolatrice and frescoes in the chapel of St Sebastian de'Gesuiti in Venice.  He painted in the style of Paolo Veronese.

Supply Belcher: Supply Belcher (29 March 1751 – 9 June 1836) was an American composer, singer, and compiler of tune books.  He was one of the members of the so-called First New England School, a group of mostly self-taught composers who created sacred vocal music for local choirs.  He was active first in Lexington, Massachusetts, then eventually moved to Farmington, Maine.  Like most of his colleagues, Belcher could not make music his main occupation, and worked as tax assessor, schoolmaster, town clerk, and so on; nevertheless he was considerably well known for his musical activities, and even dubbed 'the Handell [sic] of Maine' by a local newspaper.  Most of his works survive in "The Harmony of Maine", a collection Belcher published himself in Boston in 1794.

Bernardino del Signoraccio: Bernardino del Signoraccio or Signoracci (active first three decades of 16th century) was an Italian painter of the Renaissance period, active in Tuscany.

Hozier (musician): Andrew Hozier-Byrne (born 17 March 1990), known professionally by the mononym Hozier, is an Irish musician, singer and songwriter from County Wicklow.  He released his debut EP, featuring the hit single "Take Me to Church", in 2013 and his second EP, "From Eden", in 2014.  His debut studio album, "Hozier", was released in Ireland in September 2014 and globally in October 2014.

Question: Which musical act was active first, APB or Hozier?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musical_acts": {
      "type": "array",
      "description": "Details of the musical acts being compared.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the musical act."
          },
          "active_start_year": {
            "type": "integer",
            "description": "The year the musical act became active or was formed."
          }
        },
        "required": [
          "name",
          "active_start_year"
        ],
        "additionalProperties": false
      }
    },
    "first_active_act_name": {
      "type": "string",
      "description": "The name of the musical act that was active first."
    },
    "first_active_year": {
      "type": "integer",
      "description": "The year the first active musical act started."
    },
    "comparison_successful": {
      "type": "boolean",
      "description": "Indicates if a successful comparison was made between the active dates."
    }
  },
  "required": [
    "musical_acts",
    "first_active_act_name",
    "first_active_year",
    "comparison_successful"
  ],
  "additionalProperties": false
}
