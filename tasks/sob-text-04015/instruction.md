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
Mel Andrews: Mel Andrews (14 October 1980) is a British adventurer and athlete, specializing as a Musher in Dogsled Racing.  On 5 February 2013, she became the first British woman to finish Europe’s biggest sled dog race, Femundløpet.  A month later Andrews broke the record for fastest GB rookie to finish the World’s longest 8-dog race Finnmarksløpet.

Kelvin Kent (mountaineer): Kelvin Kent is a British adventurer, hiker, mountaineer, businessman and lecturer.  He served in the British army for many years, seeing combat in Borneo and working with the Gurkhas of Nepal, before moving to the United States in 1976.  Previously he had been a member of two mountaineering expeditions organized by Chris Bonington, to the south face of Annapurna in 1970 and the south-west face of Mount Everest in 1972.  The Annapurna expedition, on which Kent served as base camp commander, successfully put Dougal Haston and Don Whillans on the summit, but Kent's friend Ian Clough was killed by a falling ice-pillar on the descent.  In 1999 Kent established a plaque in Clough's memory at the site.

John Kirkham (adventurer): John Charles Kirkham (c.1835 – June 1876) was a British adventurer, hotelier and ship's steward who fought with William Walker in Nicaragua and Charles George Gordon in China during the Taiping Rebellion before landing in Ethiopia at the beginning of the British campaign against Emperor Tewodros II in 1868.  At the conclusion of the latter campaign, Kirkham stayed in the country and became the main Western advisor to Emperor Yohannes IV.  He was instrumental in training Ethiopian troops to Western military standards, raising and drilling what became known as the Emperor's Disciplined Force.

Bear Grylls: Edward Michael "Bear" Grylls (born 7 June 1974) is a British adventurer, writer and television presenter from Northern Ireland.  He is widely known for his television series "Man vs. Wild" (2006–2011), originally titled "Born Survivor: Bear Grylls" in the United Kingdom.  Grylls is also involved in a number of wilderness survival television series in the UK and US.  In July 2009, Grylls was appointed the youngest-ever Chief Scout in the UK at age 35.

James Ketchell: James Ketchell (born 11 January 1982), commonly known as 'Captain Ketch', is a British adventurer and Scouting Ambassador.  He recently completed what the media dubbed the 'Ultimate Global Triathlon'.  Having made numerous television appearances.  discussing his achievements and recently completing his first book, Ketchell is also currently pursuing a career as a writer, television presenter and documentary journalist.

Robert Vargas (artist): Robert Vargas is a contemporary artist known for his mixed-media portraits, murals and live events.  He was born and raised in the Los Angeles neighborhood of Boyle Heights.  Vargas is a leading creative force in the revitalization of Downtown LA’s art scene.  His paintings and drawings infuse classic genres of portraiture and nudes with an avant-garde explosivity that not only captures the visage and likeness of his subjects, but seems to excavate the intimate aspects of their character.  Vargas selects his subjects intuitively at his highly attended live-painting sessions, creating powerful and sublime representations of the human connection through his portraiture.  His visual vocabulary pulls from life experience, a viscerally sensual approach to line and texture, and an almost mannerist choreography of abstraction and representation that combine to unforgettable effect in his portraits.  His best-known works include a City of L.A. commissioned mural "Cant Stop" of legendary Suicidal Tendencies frontman, "Mike Muir, and his "Warrior Odyssey" mural of skateboard Icon and Z-boy legend, Tony Alva for the Kinney Hotel in Venice.  In 2013, Vargas was a key figure in helping Los Angeles lift its street art ban while creating his masterpiece, "Our Lady Of DTLA" a four story mural on Spring street in the heart of downtown L.A.  In May 2011, Vargas was named one of LA Weekly's People of the Year and was featured on a limited-edition cover of the issue.  His public mural work both in Los Angeles and throughout the world he sees as a means to reach a wider audience and promote accessible art and community through the creative process.  Continuing to shape the way the city’s history is written, in the Summer of 2017 he will begin work on his biggest project yet: a fourteen-story mural in L.A. that will rank as the largest mural in the world by a single artist.

David Mayer de Rothschild: David Mayer de Rothschild (born 25 August 1978) is a British adventurer, ecologist, and environmentalist and head of Sculpt the Future Foundation, a charity that supports innovations and creativity in social and environmental impact efforts.  He is a member of the Rothschild family, the youngest of three children of Victoria Lou Schott (born 1949) and Sir Evelyn de Rothschild (b. 1931) of the Rothschild banking family of England.  His middle name "Mayer" is taken from the name of the founder of the Rothschild family banking empire, Mayer Amschel Rothschild.

Debra Searle: Debra Louise Searle MVO MBE (born 8 July 1975), née Newbury, later Veal, is a British adventurer, television presenter, author and motivational speaker.  In 2002, Searle rowed across the Atlantic alone after her then husband and rowing partner, Andrew Veal, was rescued from their plywood rowing boat.

Johnny Jonas: John Harold Jonas (born 27 February 1948) is a British painter.  Over his career he has portrayed the culture on the French Riviera, depicted British sporting and cultural life, and maintains a current focus on portraiture.  His commissions include Queen Elizabeth The Queen Mother, Elizabeth II, David Cameron, Aga Khan IV, Sir Stirling Moss and Bear Grylls.

Rhodes (TV series): Rhodes is an eight part British television drama series about the life of Cecil Rhodes, a 19th century British adventurer, empire-builder and politician.  It starred Martin Shaw as the controversial figure, and was written by Antony Thomas.  "Rhodes" received its British television debut on 15 September 1996, and concluded on 3 November.  It was produced by Scott Meek and Charles Salmon, and directed by David Drury.

Question: When was the British adventurer who has his portraiture commissioned by Johnny Jonas born? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "adventurer_name": {
      "type": "string",
      "description": "The full name of the British adventurer."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the adventurer."
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the adventurer in 'Day Month Year' format."
    },
    "commissioning_artist": {
      "type": "string",
      "description": "The name of the artist who commissioned the portrait."
    },
    "adventurer_known_for": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Key activities or achievements the adventurer is known for."
    }
  },
  "required": [
    "adventurer_name",
    "nationality",
    "birth_date",
    "commissioning_artist",
    "adventurer_known_for"
  ],
  "additionalProperties": false
}
