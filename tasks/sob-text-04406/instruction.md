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
João Grande: João Oliveira dos Santos (born 15 January 1933) better known as Mestre João Grande, is a Grão-Mestre (Grand Master) of the Afro-Brazilian martial art of capoeira angola who has contributed to the spread of this art throughout the world.  He was a student of the "father of Angola", Mestre Pastinha, and has an academy in New York City.

Capoeira: Capoeira (] ) is an Afro-Brazilian martial art that combines elements of dance, acrobatics and music.  It was developed in Brazil mainly by Angolans, at the beginning of the 16th century.  It is known for its quick and complex maneuvers, predominantly using power, speed, and leverage across a wide variety of kicks, spins and other techniques.

Antonio Neves Braga: Mestre Braga (born Antonio Neves Braga; June, 13 1957; Rio de Janeiro, Brazil) is a "Mestre" (a master practitioner) of the Afro-Brazilian martial art Capoeira Angola.  He is the founder of the capoeira Angola group, Africa Bantu, and one of the founders of the Grupo de Capoeira Angola Pelourinho (GCAP).

Pé de Chumbo: Pé de Chumbo is a master of Capoeira Angola, an Afro-Brazilian martial art, and a student of João Pequeno's.  This mestre is one of the few capoeira angola mestres who carry on the Centro Esportivo de Capoeira Angola (CECA) school created by Mestre Pastinha.  He has academies in Brazil and in Europe - including several academies in Sweden, Portugal, Mexico City, Germany and the United States.  Mestre Pé de Chumbo (literally Master Foot of Lead) was one of the first capoeira angola masters to take the Bahian art form to São Paulo and is known in capoeira circles for his low ground movements, dedication to his master and focus on the traditional aspects of the capoeira game.

Berimbau: The berimbau (] ) is a single-string percussion instrument, a musical bow, from Brazil.  Originally from Africa where it receives different names, the berimbau was eventually incorporated into the practice of the Afro-Brazilian martial art "capoeira", the berimbau (the soul of capoeira) leads the capoeiristas movement in the "roda"—the faster the berimbau is playing the faster the capoeirista moves in the game.  The instrument is known for being the subject matter of a popular song by Brazilian guitarist Baden Powell, with lyrics by Vinicius de Moraes.  The instrument is also a part of Candomblé-de-caboclo tradition.

Grupo Capoeira Brasil: Grupo Capoeira Brasil is an organization that practices, teaches, and demonstrates the Afro-Brazilian martial art of Capoeira.  Grupo Capoeira Brasil practices a style of Capoeira known as "Capoeira Regional Contemporânea".  This style is derived from movements and sequences developed and systematized by Mestre Bimba's "Luta Regional Baiana", the adapted techniques of Grupo Senzala, as well as influences from the founding Mestres of Grupo Capoeira Brasil, each of whom brought personal contributions specific to their ideology, stylistic methodology and personality.

Headspin: A headspin is an athletic move in which a person balances on their head while rotating along the vertical axis of their body, usually without any other form of support.  The move is commonly employed in the Afro-Brazilian martial art Capoeira and in breakdancing.  Though b-boy Kid Freeze is sometimes credited with having invented the headspin, the first known footage of the move is seen in the 1933 film, "Wild Boys of the Road".  One of the film's protagonists Edward 'Eddie' Smith, played by Frankie Darro, performs a Headspin at the 67 minute mark.  There is also an older video featuring a headspin "A Street Arab" Thomas A. Edison, INC April 21, 1898 in which a preadolescent boy, dressed like a street urchin, performs acrobatic stunts for the camera.  The dancer, Olav Thorshaug, performed Norwegian hallingdans shows in the United States of America around 1910-1920, incorporating the headspin in his dance.

Only the Strong (film): Only the Strong is a 1993 martial arts film directed by Sheldon Lettich, starring Mark Dacascos.  It is considered to be the only Hollywood film that showcases capoeira, an Afro-Brazilian martial art, from beginning to end.

Choreomusicology: Choreomusicology is a portmanteau word joining the words choreology and musicology.  As a discipline, choreomusicology emerged at the end of the twentieth century as a field of study concerned with the relationship between music and dance.  More precisely, choreomusicology grew out of Euro-American performance traditions that considered musical composition and dance choreography as separate specialties.  Not all performance genres separate music and dance into separate theoretical categories.  The directionality of the relationship between sound and movement is not always fixed.  Choreomusicologists hold that studying the variable relationships between sound and movement in diverse performance arts can provide insight into perceptual sensibilities, cultural processes, and interpersonal dynamics.  Famous artists whose works exhibit rich choreomusical relationships include: John Cage and Merce Cunningham, Igor Stravinsky and George Balanchine, and Louis Horst and Martha Graham.  Interesting choreomusical relationships also exist in West Sumatran Tari Piring, West Javanese Pencak Silat, and Afro-Brazilian Capoeira to name but a few examples.

Manuel dos Reis Machado: Manuel dos Reis Machado, commonly called Mestre Bimba (] ; November 23, 1899 – February 5, 1974), was a "mestre" (a master practitioner) of the Afro-Brazilian martial art of capoeira.

Question: Choreomusicology is a portmanteau word joining the words choreology and musicology, interesting choreomusical relationships also exist in which Afro-Brazilian martial art that combines elements of dance, acrobatics and music?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "discipline_name": {
      "type": "string",
      "description": "The name of the discipline being discussed."
    },
    "discipline_type": {
      "type": "string",
      "description": "The type of word the discipline name is (e.g., portmanteau)."
    },
    "combined_words": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The words that form the portmanteau."
    },
    "martial_art_name": {
      "type": "string",
      "description": "The name of the Afro-Brazilian martial art."
    },
    "martial_art_origin": {
      "type": "string",
      "description": "The origin of the martial art."
    },
    "martial_art_elements": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Key elements combined in the martial art."
    },
    "has_interesting_choreomusical_relationships": {
      "type": "boolean",
      "description": "Indicates if the martial art exhibits interesting choreomusical relationships."
    }
  },
  "required": [
    "discipline_name",
    "discipline_type",
    "combined_words",
    "martial_art_name",
    "martial_art_origin",
    "martial_art_elements",
    "has_interesting_choreomusical_relationships"
  ],
  "additionalProperties": false
}
