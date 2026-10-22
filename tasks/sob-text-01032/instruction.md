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
Passenger name record: In the airline and travel industries, a passenger name record (PNR) is a record in the database of a computer reservation system (CRS) that consists of the personal information for a passenger and also contains the itinerary for the passenger, or a group of passengers travelling together.  The concept of a PNR was first introduced by airlines that needed to exchange reservation information in case passengers required flights of multiple airlines to reach their destination (“interlining”).  For this purpose, IATA and ATA defined standards for interline messaging of PNR and other data through the "ATA/IATA Reservations Interline Message Procedures - Passenger" (AIRIMP).  There is no general industry standard for the layout and content of a PNR.  In practice, each CRS or hosting system has its own proprietary standards, although common industry needs, including the need to map PNR data easily to AIRIMP messages, has resulted in many general similarities in data content and format between all of the major systems.

Krishnan–Panju: R. Krishnan (1909–1997) and S. Panju (1915–1984), collectively referred to as Krishnan–Panju, were Indian filmmakers.  The duo directed more than 50 films in South Indian languages and in Hindi.

Gunnar Olsson (actor): Gunnar Olsson (10 July 1904 – 16 September 1983) was a Swedish film actor and director.  He was born in Oxelösund, Sweden.

Gunnar Olsson (canoeist): Gunnar Olsson (born April 26, 1960) is a Swedish sprint canoer who competed from the mid-1980s to the early 1990s.  Competing in two Summer Olympics, he won a silver medal in the K-2 1000 m event at Barcelona in 1992.

Hanna in Society: Hanna in Society (Swedish: Hanna i societén) is a 1940 Swedish comedy film directed by Gunnar Olsson and starring Rut Holm, Carl Barcklind and Elsa Carlsson.

Gunnar Olsson (footballer): Olof Gunnar Olsson (19 July 1908 – 27 September 1974) was a Swedish football forward who played for Sweden in the 1934 FIFA World Cup.  He also played for GAIS.

The Happy Tailor: The Happy Tailor (Swedish:Den glade skräddaren) is a 1945 Swedish comedy film directed by Gunnar Olsson and starring Edvard Persson, Mim Persson and Marianne Gyllenhammar.

Poompaavai: Poompaavai is a 1944 Indian Tamil-language film directed by the duo Krishnan–Panju in their directorial debut.  Produced under the banner of Leo Films, it features K. R. Ramaswamy, U. R. Jeevarathinam, K. Sarangkapani, K. R. Chellam, T. R. Ramachandran, A. R. Sakunthala, S. V. Sahasranamam, D. Balasubramaniam, N. S. Krishnan, T. A. Madhuram, M. R. Durairaj and ‘Kottapuli’ K. P. Jayaraman.

Ratha Kanneer: Ratha Kanneer (English: "Blood Tears" ) is a 1954 Indian Tamil-language drama film directed by R. Krishnan and S. Panju.  The screenplay was written by Tiruvarur K. Thangaraj, and the film features M. R. Radha in the lead role.  The film was produced by Perumal Mudaliar of National Pictures.  The story revolves around Mohanasundaram, a returned-from-abroad, westernised, rich man who shows arrogance and contempt towards anything part of Indian culture and anyone below his social standards.

Anders Olsson (writer): Anders Olsson (born 19 June 1949) is a Swedish writer, professor of literature at Stockholm University, literary critic and member of the Swedish Academy.  Olsson has written some 15 books on poetry and the history of literature; together with his friend and ally Horace Engdahl he was a key introducer of the work of Jacques Derrida and other post-structuralist thinkers into Swedish literary research and criticism.  His doctoral dissertation on Swedish poet and essayist Gunnar Ekelöf was published in 1983 and met with mostly favourable reviews.

Question: Krishnan–Panju and Gunnar Olsson, have a common industry occupation, it is what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_1_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "roles"
      ],
      "additionalProperties": false
    },
    "entity_2_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "roles"
      ],
      "additionalProperties": false
    },
    "common_industry_occupation": {
      "type": "string"
    }
  },
  "required": [
    "entity_1_details",
    "entity_2_details",
    "common_industry_occupation"
  ],
  "additionalProperties": false
}
