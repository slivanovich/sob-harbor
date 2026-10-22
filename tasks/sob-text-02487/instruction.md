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
Richthofen (film): Richthofen (aka Richthofen, The Red Knight of the Air and Richthofen, The Red Ace of Germany) is a 1927 German silent war film directed by Desider Kertesz and Peter Joseph.  The film was subsequently re-mastered with sound and music effects and re-released in the United States in 1929.  The film stars Georg Burghardt, Sybil Moore and Arne Molander.  "Richthofen" was the first film to portray the life of the First World War fighter pilot Manfred von Richthofen.

Manfred von Richthofen (general): Karl Ernst Manfred Freiherr von Richthofen (24 May 1855 – 28 November 1939) was a German "General der Kavallerie" (General of the Cavalry) during World War I and recipient of the order Pour le Mérite, known informally as the Blue Max.  Richthofen was a great uncle of his more famous namesake Manfred von Richthofen, known as the Red Baron, who was his godson and named after him.

Manfred von Richthofen (sports official): Manfred von Richthofen (4 February 1934 – 1 May 2014) was a German hockey player and coach.  He was also an honorary President of German's national Olympic federation.  He was the nephew of World War I German pilot Manfred von Richthofen (the "Red Baron").  His career began during the 1950s.  He retired in 2006.  Richthofen was born in Berlin, Germany.

Frieda Lawrence: Frieda Lawrence (August 11, 1879 – August 11, 1956), born Frieda Freiin von Richthofen, was a German literary figure mainly known for her marriage to the British novelist D. H. Lawrence.  She was a distant relation of Manfred von Richthofen, the "Red Baron".

Bolko von Richthofen: Bolko von Richthofen (September 13, 1899 – March 18, 1983) was a German archaeologist and a distant relative of the family of Manfred von Richthofen, the "Red Baron".  He is sometimes confused with his distant cousin and namesake, Karl Bolko von Richthofen (1903–1971) – the youngest brother of the fighter ace.

Ferdinand von Richthofen: Ferdinand Freiherr von Richthofen (5 May 18336 October 1905), better known in English as Baron von Richthofen, was a German traveller, geographer, and scientist.  He is noted for coining the terms "Seidenstraße" and "Seidenstraßen" = "Silk Road(s)" or "Silk Route(s)" in 1877.  He also standardized the practices of chorography and chorology.  He was an uncle of the World War I flying ace Manfred von Richthofen, best known as the "Red Baron".

Bombing of Frampol: The Bombing of Frampol occurred during the German invasion of Poland in 1939.  On 13 September, the town of Frampol with a population of 4,000 was bombed by the German Luftwaffe as a practice run for future missions.  Over 60% to 90% of the town was completely destroyed — only two streets remained untouched, including some houses on the outskirts.  Frampol was destroyed by the bombers of Luftwaffe's 8th Air Corps, under General Wolfram Freiherr von Richthofen.  According to Polish historians Pawel Puzio and Ryszard Jasinski no units of the Polish army were stationed in Frampol and the town did not have any military facilities.

Wolfram Freiherr von Richthofen: Wolfram Freiherr von Richthofen (10 October 1895 – 12 July 1945) was a German field marshal of the "Luftwaffe" (German Air Force) during the World War II.  Born in 1895 into a family of the Prussian nobility, Richthofen grew up in prosperous surroundings.  At the age of eighteen, after leaving school, he opted to join the German Army rather than choose an academic career, and joined the army's cavalry arm in 1913.

Lothar von Richthofen: Lothar Freiherr von Richthofen (born Lothar Siegfried Freiherr von Richthofen; 27 September 1894 – 4 July 1922) was a German First World War fighter ace credited with 40 victories.  He was a younger brother of top-scoring ace Manfred von Richthofen (the "Red Baron") and a distant cousin of Luftwaffe Field Marshal Wolfram von Richthofen.

Hermann von Richthofen: Hermann Freiherr von Richthofen, GCVO (born 20 November 1933 in Breslau) is a German diplomat.  He is a great nephew of Manfred von Richthofen, the "Red Baron".

Question: Who lived longer, Lothar von Richthofen or  Wolfram Freiherr von Richthofen ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_a_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the first person being compared."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the first person."
        },
        "death_year": {
          "type": "integer",
          "description": "The death year of the first person."
        },
        "lifespan_years": {
          "type": "integer",
          "description": "The approximate lifespan of the first person in full years."
        }
      },
      "required": [
        "name",
        "birth_year",
        "death_year",
        "lifespan_years"
      ],
      "additionalProperties": false
    },
    "person_b_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the second person being compared."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the second person."
        },
        "death_year": {
          "type": "integer",
          "description": "The death year of the second person."
        },
        "lifespan_years": {
          "type": "integer",
          "description": "The approximate lifespan of the second person in full years."
        }
      },
      "required": [
        "name",
        "birth_year",
        "death_year",
        "lifespan_years"
      ],
      "additionalProperties": false
    },
    "comparison_result": {
      "type": "object",
      "properties": {
        "longer_lived_person_name": {
          "type": "string",
          "description": "The name of the person who lived longer."
        },
        "difference_in_years": {
          "type": "integer",
          "description": "The difference in lifespan in full years between the two individuals."
        }
      },
      "required": [
        "longer_lived_person_name",
        "difference_in_years"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_a_details",
    "person_b_details",
    "comparison_result"
  ],
  "additionalProperties": false
}
