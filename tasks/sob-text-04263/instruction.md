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
Mulata de tal: Mulata de tal (English: "A Kind of Mulatto" ) is a novel by Nobel Prize-winning novelist Miguel Ángel Asturias.  Asturias published this novel while he and his wife were living in Genoa in 1963.

Men of Maize: Men of Maize (Spanish: "Hombres de maíz" ) is a 1949 novel by Guatemalan Nobel Prize in Literature winner Miguel Ángel Asturias.  The novel is usually considered to be Asturias's masterpiece, yet remains one of the least understood novels produced by Asturias.  The title "Hombres de maíz" refers to the Maya Indians' belief that their flesh was made of corn.  Its title originates in the Popol Vuh, one of the sacred books of the Maya.  The English translation is part of the UNESCO Collection of Representative Works.

El Señor Presidente: "El Señor Presidente" (Mister President) is a 1946 novel written in Spanish by Nobel Prize-winning Guatemalan writer and diplomat Miguel Ángel Asturias (1899–1974).  A landmark text in Latin American literature, "El Señor Presidente" explores the nature of political dictatorship and its effects on society.  Asturias makes early use of a literary technique now known as magic realism.  One of the most notable works of the dictator novel genre, "El Señor Presidente" developed from an earlier Asturias short story, written to protest social injustice in the aftermath of a devastating earthquake in the author's home town.

Rafael Arévalo Martínez: Rafael Arévalo Martínez (25 July 1884, Guatemala City –12 June 1975, Guatemala City) was a Guatemalan writer.  He was a novelist, short-story writer, poet, diplomat, and director of Guatemala’s national library for more than 20 years.  Though Arévalo Martínez’s fame has waned, he is still considered important because of his short stories, and one in particular: "The man who resembled a horse" and the biography of president Manuel Estrada Cabrera, "¡Ecce Pericles!" .  Arévalo Martínez was director of the Guatemalan National Library from 1926 until 1946, when he became for a year Guatemala’s representative before the Pan American Union in Washington, D.C. He was the political and literary counterpart of his more famous countryman, Nobel Prize winner Miguel Ángel Asturias; while Arévalo Martínez was an unapologetic admirer of the United States, Asturias was a bitter critic of the New Orleans-based United Fruit Company (now part of United Brands Company), which he felt had plundered his country.

Augusto Monterroso: Augusto Monterroso Bonilla (December 21, 1921 - February 7, 2003) was a Honduran writer who adopted Guatemalan nationality, known for the ironical and humorous style of his short stories.  He is considered an important figure in the Latin American "Boom" generation, and received several awards, including the Prince of Asturias Award in Literature (2000), Miguel Ángel Asturias National Prize in Literature (1997), and Juan Rulfo Award (1996).

Poet-diplomat: Poet-diplomats are poets who have also served their countries as diplomats.  The best known poet-diplomats are perhaps Geoffrey Chaucer and Thomas Wyatt; the category also includes recipients of the Nobel Prize in Literature: Ivo Andrić, Gabriela Mistral, Saint-John Perse, Miguel Ángel Asturias, Pablo Neruda, George Seferis, Czesław Miłosz and Octavio Paz.  Contemporary poet-diplomats include Abhay K, Indran Amirthanayagam, Kofi Awoonor, Philip McDonagh and Yiorgos Chouliaras.

Miguel Ángel Asturias: Miguel Ángel Asturias Rosales (October 19, 1899 – June 9, 1974) was a Nobel Prize-winning Guatemalan poet-diplomat, novelist, playwright and journalist.  Asturias helped establish Latin American literature's contribution to mainstream Western culture, and at the same time drew attention to the importance of indigenous cultures, especially those of his native Guatemala.

James Dickey: James Lafayette Dickey (February 2, 1923 – January 19, 1997) was an American poet and novelist.  He was appointed the eighteenth United States Poet Laureate in 1966.  He also received the Order of the South award.  Dickey was also a novelist, known for "Deliverance" (1970) which was adapted into an acclaimed film of the same name.

Humberto Ak'ab'al: Humberto Ak'ab'al also Ak'abal or Akabal (born 1952 Momostenango, Totonicapán department) is a K'iche' Maya poet from Guatemala.  His poetry has been published in French, English, Estonian, Scots, German, Arabic and Italian translations, as well as in the original K'iche' and Spanish.  His book "Guardián de la caída de agua" (or "Guardian of the Waterfall" in English) was named book of the year by Association of Guatemalan Journalists and received their Golden Quetzal award in 1993.  In 1995 he received an honorary degree from the Department of Humanities of the Universidad de San Carlos de Guatemala.  In 2004 he declined to receive the Guatemala National Prize in Literature because it is named for Miguel Ángel Asturias, whom Ak'ab'al accused of encouraging racism.  He said Asturias' 1923 essay "The Social Problem of the Indian", "Offends the indigenous peoples of Guatemala, of which I am part."

Editorial Losada: Editorial Losada is a traditional Argentine publishing house founded in 1938.  The house has published important writers such as Nobel Prize winners Pablo Neruda and Miguel Ángel Asturias.

Question: Between James Dickey and Miguel Ángel Asturias, which was a nobel prize winner?  

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "nobel_prize_winner": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the individual who won the Nobel Prize."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the Nobel Prize winner."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions held by the Nobel Prize winner."
        },
        "won_nobel_prize": {
          "type": "boolean",
          "description": "Indicates if the person won a Nobel Prize (should be true for this object)."
        }
      },
      "required": [
        "name",
        "nationality",
        "professions",
        "won_nobel_prize"
      ],
      "additionalProperties": false
    },
    "other_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the other individual mentioned in the question."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the other person."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions held by the other person."
        },
        "won_nobel_prize": {
          "type": "boolean",
          "description": "Indicates if the person won a Nobel Prize (should be false for this object)."
        }
      },
      "required": [
        "name",
        "nationality",
        "professions",
        "won_nobel_prize"
      ],
      "additionalProperties": false
    },
    "comparison_result": {
      "type": "string",
      "description": "A direct answer to the question stating which person was the Nobel Prize winner."
    }
  },
  "required": [
    "nobel_prize_winner",
    "other_person",
    "comparison_result"
  ],
  "additionalProperties": false
}
