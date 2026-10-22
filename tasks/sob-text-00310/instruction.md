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
Edoardo Agnelli Islamic Association: Edoardo Agnelli Islamic Association (Anjoman-e Eslami-ye shahid Edoardo Agnelli) is an Islamic association established in Iran and named after Edoardo Agnelli the Italian convert and the oldest son of Gianni Agnelli.

Edoardo Agnelli (industrialist): Edoardo Agnelli (2 January 1892 – 14 July 1935) was an Italian industrialist and principal family shareholder of the Italian car company Fiat.

Turin-Aeritalia Airport: Turin-Aeritalia Airport (Italian: "Aeroporto di Torino-Aeritalia" , ICAO: LIMA ) also known as Edoardo Agnelli Airport, built in 1916, is the historical airport of Turin in the Piedmont region of northern Italy.  It is located off Corso Marche, some 5 km from the city centre.

Edoardo Agnelli (1831-1871): Edoardo Agnelli (Turin, 18 July 1831 – 7 November 1871) was an Italian entrepreneur and politician.

Giovanni Agnelli: The son of Edoardo Agnelli and Aniceta Frisetti, he was born in 1866 in Villar Perosa, a small town near Pinerolo, Piedmont, still the main home and burial place of the Agnelli family.  His father, mayor of Villar Perosa, died at age 40, when Giovanni was just five.  He studied at the Collegio San Giuseppe in Turin; then embarked on a military career until 1893 when he returned to Villar Perosa, where he followed in his father's footsteps and became mayor in 1895 which he held until his death.  Agnelli heard about the invention of the (then) new horseless carriage and immediately saw an opportunity for using his engineering and entrepreneurial skills.  In 1898, he met Count Emanuele Cacherano of Bricherasio, who was looking for investors for his horseless carriage project; Agnelli sensed the opportunity.

Aniceta Frisetti: Aniceta Frisetti (Turin, 1846 – Turin, 28 October 1920) was an Italian philanthropist.  She became a member of the Agnelli family as she got married with Edoardo Agnelli.

Edoardo Agnelli: Edoardo Agnelli (9 June 1954 – 15 November 2000) was the eldest child and only son of Marella Agnelli (born Donna Marella Caracciolo di Castagneto) and Gianni Agnelli, the industrialist patriarch of Fiat.  His body was found dead under mysterious circumstances under a bridge on the outskirts of Turin.

Umberto Agnelli: Umberto Agnelli (1 November 1934 – 27 May 2004) was an Italian industrialist and politician.  He was the third son of Virginia Agnelli (born Donna Virginia Bourbon del Monte) and of Edoardo Agnelli, and the youngest brother of Gianni Agnelli.

Marella Agnelli: Marella Agnelli, born Donna Marella Caracciolo di Castagneto (born 4 May 1927) is an Italian noblewoman, art collector, socialite, style icon and widow of former Fiat chairman Gianni Agnelli.  She has often appeared in the fashion magazine "Vogue."  She was named to the International Best Dressed List Hall of Fame in 1963.

Virginia Bourbon del Monte: "Donna" Virginia Bourbon del Monte (Rome, 24 May 1899 – Pisa, 30 November 1945) was the wife of Edoardo Agnelli and the mother of Gianni Agnelli.

Question: When was Edoardo Agnelli's mother born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_of_interest": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the Edoardo Agnelli whose mother's birth date is being queried."
        },
        "birth_date": {
          "type": "string",
          "description": "The birth date of this specific Edoardo Agnelli."
        },
        "death_date": {
          "type": "string",
          "description": "The death date of this specific Edoardo Agnelli."
        },
        "relationship_to_gianni_agnelli": {
          "type": "string",
          "description": "The relationship of this Edoardo Agnelli to Gianni Agnelli."
        }
      },
      "required": [
        "name",
        "birth_date",
        "death_date",
        "relationship_to_gianni_agnelli"
      ],
      "additionalProperties": false
    },
    "mother_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of Edoardo Agnelli's mother."
        },
        "birth_date": {
          "type": "string",
          "description": "The birth date of Edoardo Agnelli's mother."
        },
        "other_roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other notable roles or descriptions of the mother."
        }
      },
      "required": [
        "name",
        "birth_date",
        "other_roles"
      ],
      "additionalProperties": false
    },
    "query_resolved": {
      "type": "boolean",
      "description": "Indicates if the query about the mother's birth date was successfully resolved."
    }
  },
  "required": [
    "person_of_interest",
    "mother_details",
    "query_resolved"
  ],
  "additionalProperties": false
}
