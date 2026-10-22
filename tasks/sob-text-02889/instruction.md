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
Acapulco, cuerpo y alma: Acapulco, cuerpo y alma (English: "Acapulco, Body and Soul"), is a Mexican telenovela produced by José Alberto Castro in 1995 for Televisa.  It is a remake of the Mexican telenovela produced by Televisa in 1985, "Tú o nadie".

Sin tu mirada: Sin tu mirada is an upcoming Mexican telenovela created for Televisa by Ignacio Sada Madero, based on the 1997 Mexican drama, titled "Esmeralda".  The series is stars Claudia Martín and Osvaldo de León.  Production began on September 15, 2017 and is scheduled to premiere on November 2017.

Si Dios me quita la vida: Si Dios me quita la vida (English title: "If God takes away my life") is a Mexican telenovela produced by Pedro Damián and Juan Osorio for Televisa in 1995.  This is a remake of the 1961 telenovela "La leona" starred by Amparo Rivelles and Ernesto Alonso.

El Perdedor (Enrique Iglesias song): "El Perdedor" (English: "The Loser") is the second Spanish single from Enrique Iglesias' album "Sex and Love".  It serves as the opening theme of Mexican telenovela "Lo que la vida me robó".  This is the fifth time that Enrique's song is chosen as an opening theme of a telenovela after "Cosas del Amor", "Nunca Te Olvidaré", "Cuando Me Enamoro" and "Marisol" (Por Amarte).  The song was released in the United States and Mexico on 30 October 2013 and was later released to other Latin countries.  The song was composed by Iglesias and Descemer Bueno.

Lo mejor que me pasó en la vida: Lo mejor que me pasó en la vida (English: "The best thing that happened to me in life"), is the first studio album by singer-songwriter Alex Sirvent.  Launched on December 12, 2013 by Alman Music.  Some of the songs on this album are part of the soundtrack of the telenovela "Lo que la vida me robó".

Osvaldo de León: Osvaldo de León (born May 6, 1984 in Brownsville, Texas, United States) is an American actor and model.  He debuted on television in 2007 in the Mexican telenovela "Palabra de Mujer", playing Ariel Castellanos.  Osvaldo has participated in several plays and Mexican movies, and since its inception with Televisa has participated in several soap operas such as "Juro que te amo", "Niña de mi Corazón", "Una familia con suerte", "Lo que la vida me robó", "La Malquerida" and "Sueño de amor" and "La candidata"

Lo que no fue: Lo que no fue, is a 1969 Mexican telenovela produced by Televisa and originally transmitted by Telesistema Mexicano.

A que no me dejas: A que no me dejas, formerly known as "A que no me dejas, corazón" (English title: "I Dare You to Leave"), is a Mexican telenovela produced by Carlos Moreno for Televisa.  It is a remake of the Mexican telenovela "Amor en silencio", produced in 1988.

Rosa salvaje: Rosa salvaje (English title: "Wild Rose") (] ; is a Mexican telenovela produced by Valentín Pimstein for Televisa.  The telenovela premiered on Canal de las Estrellas on July 6, 1987 and ran for 199 episodes until April 8, 1988.  This telenovela was a huge success in Mexico, Latin America, Bulgaria, Croatia, Serbia, Bosnia and Herzegovina, Russia, Estonia, China the United States, Indonesia and provided the template for numerous other Latin American soap operas in terms of story, plot twists and characters for years to come.

Lo que la vida me robó: Lo que la vida me robó (English title: "What Life Took From Me"), is a Mexican telenovela produced by Angelli Nesma Medina for Televisa, broadcast by Canal de las Estrellas now known as Las Estrellas.  The series originally aired from October 28, 2013 to July 27, 2014.  It is an adaptation of the telenovela of 1983 "Bodas de odio" produced by Ernesto Alonso, which also inspired "Amor real", produced by Carla Estrada in 2003.

Question: Osvaldo de León, is an American actor and model, since its inception with Televisa has participated in several soap operas such as Lo que la vida me robó, a Mexican telenovela produced by who for Televisa?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "actor_nationality": {
      "type": "string",
      "description": "The nationality of the actor."
    },
    "telenovela_title": {
      "type": "string",
      "description": "The title of the telenovela the actor participated in."
    },
    "telenovela_producer": {
      "type": "string",
      "description": "The producer of the specified telenovela."
    },
    "production_company": {
      "type": "string",
      "description": "The company that produced the telenovela."
    }
  },
  "required": [
    "actor_name",
    "actor_nationality",
    "telenovela_title",
    "telenovela_producer",
    "production_company"
  ],
  "additionalProperties": false
}
