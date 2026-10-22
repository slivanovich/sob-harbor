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
Ferdinand Porsche: Ferdinand Porsche (3 September 1875 – 30 January 1951) was an automotive engineer and founder of the Porsche car company.  He is best known for creating the first gasoline-electric hybrid vehicle (Lohner-Porsche), the Volkswagen Beetle, the Mercedes-Benz SS/SSK, several other important developments and Porsche automobiles.  In addition, Porsche designed the 1923 Benz Tropfenwagen, which was the first racing car with a mid-engine, rear-wheel drive layout.

EAM Nuvolari S1: The EAM Nuvolari S1 is a limited production car announced in 1990 by the Munich-based company Edelsbrunner Automobile München.  It had styling based on that of 1930s sports cars such as the Riley MPH and took its name from racing driver Tazio Nuvolari.

1933 Grand Prix season: The 1933 Grand Prix season was the first year of a two-year hiatus for the European Championship.  Tazio Nuvolari proved to be the most successful driver, winning seven Grands Prix.  Alfa Romeo's cars proved difficult to beat, winning 19 of the season's 36 Grands Prix.

1936 Vanderbilt Cup: The 1936 Vanderbilt Cup (formally known as I George Vanderbilt Cup) was a Grand Prix that was held on 12 October 1936 at Roosevelt Raceway near Westbury, Long Island, New York City, USA.  It was the fourth and last race of the 1936 AAA Championship Car season, not counting the non-championship events.  The race, contested over 75 laps of 6.39 km (3.97 mi), was won by Tazio Nuvolari driving a Alfa Romeo 12C-36 after starting from eighth position.

Nuvola61: Nuvola61 (formerly called Nuvolari) is an Italy-based sports and entertainment television channel part of Gruppo LT Multimedia.  Its primary focus is on motorsports, as inferred by its name taken from Italian driver Tazio Nuvolari.

Castel d'Ario: Castel d'Ario is a "comune" (municipality) in the Province of Mantua in the Italian region Lombardy, located about 150 km east of Milan and about 15 km east of Mantua.  It was the birthplace of car race driver Tazio Nuvolari.

Biodata: In industrial and organizational psychology, biodata is biographical data.  is “...factual kinds of questions about life and work experiences, as well as items involving opinions, values, beliefs, and attitudes that reflect a historical perspective.”  Since the respondent replies to questions about themselves, there are elements of both biography and autobiography.  The basis of biodata’s predictive abilities is the axiom that past behaviour is the best predictor of future behaviour.  Biographical information is not expected to predict all future behaviours but it is useful in personnel selection in that it can give an indication of probable future behaviours based on an individual’s prior learning history.  Biodata instruments (also called Biographical Information Blanks) have an advantage over personality and interest inventories in that they can capture directly the past behaviour of a person, probably the best predictor of his or her future actions.  These measures deal with facts about the person’s life, not introspections and subjective judgements.

Alfa Romeo Nuvola: The Alfa Romeo Nuvola is a concept car with coupé body first shown by Alfa Romeo at the "Mondial de l'Automobile" Paris motor show in 1996.  Nuvola literally means "cloud" in Italian, but also hints to the legendary Italian racing driver Tazio Nuvolari.  The Nuvola has a front-mounted engine and four wheel drive.  The prototype is currently on display at the Alfa Romeo Historical Museum in Arese, Italy.

Mel Kenyon: Mel Kenyon (born April 15, 1933 in Dekalb, IL. ) is a former midget car driver.  He is known as the "King of the Midgets", "Miraculous Mel" and "Champion of Midget Auto Racing."  The Motorsports Hall of Fame of America says "Many consider him to be midget car racing's greatest driver ever."

Tazio Nuvolari: Tazio Giorgio Nuvolari (] ; 16 November 1892 – 11 August 1953) was an Italian racing driver.  First he raced motorcycles and then he concentrated on sports cars and single-seaters.  Resident in Mantua, he was known as 'Il Mantovano Volante' (The Flying Mantuan) and nicknamed 'Nivola'.  His victories—72 major races, 150 in all —included 24 Grands Prix, five Coppa Cianos, two Mille Miglias, two Targa Florios, two RAC Tourist Trophies, a Le Mans 24-hour race, and a European Championship in Grand Prix racing.  Ferdinand Porsche called him "the greatest driver of the past, the present, and the future."

Question: What is the person who called Tazio Nuvolari "the greatest driver of the past, the present, and the future" best known for?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who made the statement about Tazio Nuvolari."
    },
    "quote_about_nuvolari": {
      "type": "string",
      "description": "The specific quote made by the person about Tazio Nuvolari."
    },
    "best_known_for": {
      "type": "array",
      "description": "A list of achievements or creations the person is best known for.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "person_name",
    "quote_about_nuvolari",
    "best_known_for"
  ],
  "additionalProperties": false
}
