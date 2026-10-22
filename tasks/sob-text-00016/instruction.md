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
Violeta Rivas: Ana María Francisca Adinolfi (known by her stage name, Violeta Rivas; born 4 October 1937) is an Argentine singer and actress, known for participating in the music program "El Club del Clan", along with Palito Ortega, Raúl Lavié, Johnny Tedesco and Chico Novarro.

Cristina Lemercier: Cristina Lemercier (née, Noemi Cristina Perone; José C. Paz, April 3, 1951 - San Miguel, December 27, 1996) was an Argentine actress and television presenter.  Her mother, a Peronist, took Lemercier to an acting audition when she was a teenager.  She had two sisters, Gloria and Maria Rosa Perone.  In 1968, she married the singer Freddy Tadeo (Ricardo Ortega), brother of Palito Ortega.  They had three children, Pablo, Paula, and Julia.  She died from a gunshot wound to the head.

Palito Ortega: Ramón Bautista Ortega (born March 8, 1942) is an Argentine singer and actor, better known as Palito Ortega.  (] ) Ortega It's icon of Popular Argentine Music.  Considered one of the main Argentine representatives of the musical style called New wave that marked the Hispanic-American music between the years '60 and '70.  Ortega reached international fame, particularly in Latin America and Spain, during the 1960s, when the rock en español style of rock and roll music was popularized among teenagers in the region.

Aquellos años locos: Aquellos años locos (also known as "Those Crazy Years" in USA) is a 1971 Argentine musical comedy film directed and written by Enrique Carreras with Norberto Aroldi.  The film premiered on 30 July 1971 in Buenos Aires and stars Palito Ortega and Mercedes Carreras.  The movie was filmed in Mar del Plata, Buenos Aires.

Verónica Diorio: Verónica Diorio is a fictional character in the 2012 Argentine telenovela "Graduados".  She is played by Julieta Ortega, both as an adult and, in flashbacks, as a teenager.

La familia hippie: La familia hippie ('The Hippie Family') is a 1971 Argentine musical comedy film by Enrique Carreras.  It stars Ángel Magaña and Palito Ortega.  Not being a movie about 'hippies' as such, the title refers to the portrayal of a family in which mother and daughter are pregnant simultaneously.  The movie is a remake of the 1955 production "La Cigüeña dijo sí", both films are based on a play by Carlos Llopis.

El Tío Disparate: El Tío Disparate (English language:The Silly Uncle) is a 1978 Argentine comedy musical film directed by Palito Ortega and written Juan Carlos Mesa.  It stars Palito Ortega and Carlos Balá.

La felicidad: "La felicidad" is a song by Argentine singer Palito Ortega.

Julieta Ortega: Julieta Ortega is an Argentine actress, with a leading role in the 2012 successful telenovela "Graduados".  She is the daughter of Palito Ortega and Evangelina Salazar, and sister of Emanuel Ortega, Luis Ortega, Sebastián Ortega and Rosario Ortega.

Son o se hacen: Son o se hacen is a 1997 Argentine comedy television series.  It stars Julieta Ortega, Rodrigo De la Serna, Carolina Fal, Walter Quiroz, and Iván González.  It was one of the first Argentine television series to explore the topic of sexual diversity.

Question: Julieta Ortega is the daughter of Palito Ortega, considered one of the main Argentine representatives of the musical style called what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person whose musical style is being identified."
    },
    "relationship_to_julieta_ortega": {
      "type": "string",
      "description": "The relationship of the person to Julieta Ortega."
    },
    "musical_style": {
      "type": "string",
      "description": "The musical style associated with the person."
    },
    "era_of_popularity": {
      "type": "string",
      "description": "The period when the musical style was popular."
    }
  },
  "required": [
    "person_name",
    "relationship_to_julieta_ortega",
    "musical_style",
    "era_of_popularity"
  ],
  "additionalProperties": false
}
