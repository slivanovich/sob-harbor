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
Kirsty Flavell: Kirsty Elizabeth Flavell (née Bond; born 20 November 1967) is a former international cricketer who played six women's test matches and 38 one day internationals for New Zealand.  She was the first woman to score a double century in a women's Test match in 1996 (204).  She is now one of the selectors for the New Zealand Woman's Cricket Team (The White Ferns).

New Zealand Woman's Weekly: The New Zealand Woman's Weekly is a weekly New Zealand women's magazine published by Bauer Media.  s of 2011 , it has a circulation of 82,040, third by paid sales after "TV Guide" and "New Zealand Woman's Day".

Kathleen Nunneley: Kathleen Mary 'Kate' Nunneley (16 September 1872 – 28 September 1956) was a New Zealand tennis player and librarian.  She was the best woman tennis player in New Zealand in the late 1800s and early 1900s, and possibly still the best New Zealand woman player ever.

Wendy Campbell-Purdie: Wendy Campbell Purdie was a New Zealand woman who worked with a British timber firm in Corsica.  She was born and mostly brought up in New Zealand.  When travel became easier after the second world war she set off on the young New Zealander's traditional grand tour.  In Hampshire, England, she called upon Richard St. Barbe Baker, a tree expert, and learned about his idea that green wall agriculture could tame the desert.

Jean Wishart: Jean Boughton Wishart {'1': ", '2': ", '3': ", '4': "} (8 October 1920 – 16 November 2016) was a New Zealand journalist who was the editor of the "New Zealand Woman's Weekly" from 1952 until 1985.

Rachael Ngeungeu Te Irirangi Zister: Rachael Ngeungeu Te Irirangi Zister {'1': ", '2': ", '3': ", '4': "} (née Beamish, 10 October 1893 – 22 May 1997) was a New Zealand woman of mana, secretary, community leader.  Of Māori descent, she identified with the Ngāti Tai and Ngāti Paoa iwi.  She was born in Waiariki, Waikato, New Zealand in 1893.  In the 1989 New Year Honours, Zister was made a Commander of the Order of the British Empire, for services to the Māori people.  She was awarded the New Zealand 1990 Commemoration Medal in 1990 and the New Zealand Suffrage Centennial Medal in 1993.

Alexis Pritchard: Alexis Pritchard (born 24 September 1983) is a South-African born New Zealand boxer.  On 5 August 2012 she became the first New Zealand woman to win an Olympic bout when she beat Tunisia's Rim Jouini in the Round of 16.

Toni Hodgkinson: Toni Louise Hodgkinson (born 12 December 1971) is a former New Zealand middle distance runner, originally from Takaka.  She currently holds the New Zealand woman's record in the 800 m.

Philippa Baker (rower): Philippa June Baker, {'1': ", '2': ", '3': 'MBE', '4': "} (born 12 June 1963), now known by her married name Philippa Baker-Hogan, is a former New Zealand rower and politician.  She was the first New Zealand woman to win a gold medal at World Rowing Championships and won gold at world championships on two more occasions.  She has twice represented New Zealand at the Olympics.  She has received numerous awards for her rowing success and in 2012, she and fellow double sculler Brenda Lawson were inducted into the New Zealand Sports Hall of Fame.  A trained radiographer, she manages her husband's medical practice.  She has been a Whanganui District Health Board and Wanganui District Council member since 2004 and 2006, respectively, and was a mayoral candidate in 2010.  She is a member of the New Zealand Labour Party.

Olivia (magazine): Olivia is a monthly Finnish women's magazine published in Finland.

Question: New Zealand Woman's Weekly and Olivia are both what kind of publications?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "publication_type": {
      "type": "string",
      "description": "The common type of publication for the listed items."
    },
    "number_of_publications_identified": {
      "type": "integer",
      "description": "The total number of publications identified in the answer."
    },
    "publications": {
      "type": "array",
      "description": "Details about each identified publication.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the publication."
          },
          "country_of_origin": {
            "type": "string",
            "description": "The country where the publication is based or published."
          },
          "frequency": {
            "type": "string",
            "description": "How often the publication is released (e.g., weekly, monthly)."
          }
        },
        "required": [
          "name",
          "country_of_origin",
          "frequency"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "publication_type",
    "number_of_publications_identified",
    "publications"
  ],
  "additionalProperties": false
}
