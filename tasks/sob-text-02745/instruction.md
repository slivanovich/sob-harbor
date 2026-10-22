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
Paulina Ana María Zapata Portillo: Anita Zapata, short for Paulina Ana María Zapata Portillo (1915-2010) daughter of General Emiliano Zapata, was a suffragist who fought for the vote for Mexican women and was the first female federal representative from the state of Morelos.

Emiliano Zapata Municipality, Tlaxcala: Emiliano Zapata Municipality is a municipality in Tlaxcala in south-eastern Mexico.  As of the 2010 census, the municipality had a total population of 4,146 inhabitants.  Its municipal seat, also called Emiliano Zapata, had a population of 2,843 inhabitants.  The town stands at an official elevation of 2,884 meters (9,462 ft.), the highest of any municipal seat in Mexico.

Eulalio Gutiérrez: Eulalio Gutiérrez Ortiz (February 4, 1881 – August 12, 1939) was a general in the Mexican Revolution from state of Coahuila.  He is most notable for his election as provisional president of Mexico during the Aguascalientes Convention and led the country for a few months between November 6, 1914, and January 16, 1915.  The Convention was convened by revolutionaries who had successfully ousted the regime of Victoriano Huerta after more than a year of conflict.  Gutiérrez rather than "First Chief" ("Primer Jefe") Venustiano Carranza was chosen president of Mexico and a new round of violence broke out as revolutionary factions previously united turned against each other.  "The high point of Gutiérrez's career occurred when he moved with the Conventionist army to shoulder the responsibilities of his new office [of president]."  Gutiérrez's government was weak and he could not control the two main generals of the Army of the Convention, Pancho Villa and Emiliano Zapata.  Gutiérrez moved the capital of his government from Mexico City to San Luis Potosí.  He resigned as president and made peace with Carranza.  He went into exile in the United States, but later returned to Mexico.  He died in 1939, outliving many other major figures of the Mexican Revolution.

Emiliano Zapata: Emiliano Zapata Salazar (] ; 8 August 1879 – 10 April 1919) was a leading figure in the Mexican Revolution, the main leader of the peasant revolution in the state of Morelos, and the inspiration of the agrarian movement called "Zapatismo".

Neozapatismo: Neozapatismo or Neozapatism (sometimes mislabeled as Zapatismo) is the Mexican ideology behind movements such as the Zapatista Army of National Liberation.  The official anthem of Neozapatismo and the Zapatista territories is the Himno Zapatista.  The ideology is based on anarchism, Mayan tradition, Marxism, the thoughts of Emiliano Zapata, and the thoughts of Subcomandante Insurgente Galeano.  Neozapatismo is the ideology of the Zapatistas, who govern a small territory in Chiapas and have since the beginning of the Chiapas conflict.  Neozapatismo has no official founder, but its thoughts are mainly attributed to Subcomandante Insurgente Galeano (formerly Subcomandante Marcos) and Emiliano Zapata.  The Neozapatista ideology is believed to be derived largely from libertarian socialism, libertarian Marxism (including autonomism), social anarchism, anarcho-communism, anarcho-collectivism, anarcho-syndicalism, communalism, direct democracy, and radical democracy.

La Revolución de Emiliano Zapata: La Revolución de Emiliano Zapata (meaning ""Emiliano Zapata's Revolution"" in English) is a Mexican rock band that broke sales records in Europe and Mexico with their hit song "Nasty Sex" at the height of the counterculture era of the early 1970s.  Breaking ties with their original concept as the hippie era waned worldwide by the mid-1970s, they continued actively interpreting romantic ballads with considerable success.  In 2009, they returned as a rock act.

Emiliano Zapata Municipality, Veracruz: Emiliano Zapata is a municipality in the Mexican state of Veracruz, located 2 km from Jalapa-Enríquez on Federal Highways 180 and 190.  It named for the hero of the Mexican Revolution, Emiliano Zapata.

Emiliano Zapata, Morelos: Emiliano Zapata is a city in the west-central part of the Mexican state of Morelos.  It stands at .  The city serves as the municipal seat for the surrounding municipality of the same name.  The city is the sixth largest in the state of Morelos, with a 2005 census population of 39,702 inhabitants.  The municipality reported 69,064 inhabitants and has an area of 64.983 km² (25.09 sq mi).  The city was previously known as both San Francisco Zacualpan and San Vicente Zacualpan.  It was renamed in honour of Mexican Revolutionary Emiliano Zapata.

Emiliano Zapata (film): Emiliano Zapata, also known as Zapata, is a 1970 Mexican drama film directed by Felipe Cazals and written, produced, and starring Antonio Aguilar as Emiliano Zapata.  One of the first large-scale, expensive, and unconventional epics ever to be made in Mexico, the film was shot in 70 millimeters and gave Aguilar the opportunity to portray his favorite revolutionary character.  The film features astounding sets, and also many extras.  Aguilar avoided to sing in the film, in order to give the film more realism, although he was displeased at the finished project.

Zapata (lithograph): Zapata (1932) is a lithograph by the Mexican artist Diego Rivera (1886–1957) that depicts the Mexican revolutionary Emiliano Zapata (1879–1919) as he holds the reins of a horse among a group of "campesinos" (peasants).  The lithographic edition was created and printed twelve years after Zapata's assassination.  Zapata is based on Agrarian Leader Zapata (1931), one of eight "portable" frescoes produced explicitly for Rivera's solo exhibition at the Museum of Modern Art (MoMA) in 1931, which was adapted from his previous "Revolt" panel from a fresco titled "The History of Cuernavaca and Morelos" (1929–30) painted in the Palace of Cortés, Cuernavaca.  There were 100 original prints of the lithograph, many of which are in the collections of various art museums.

Question: what does Eulalio Gutiérrez and Emiliano Zapata have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_theme": {
      "type": "string",
      "description": "The main historical event or period that both individuals were part of."
    },
    "individuals": {
      "type": "array",
      "description": "Details about each individual and their role in the common theme.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "role": {
            "type": "string",
            "description": "The specific role or status of the individual within the common theme."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      }
    },
    "relationship_summary": {
      "type": "string",
      "description": "A summary of their direct or indirect relationship during the common theme."
    }
  },
  "required": [
    "common_theme",
    "individuals",
    "relationship_summary"
  ],
  "additionalProperties": false
}
