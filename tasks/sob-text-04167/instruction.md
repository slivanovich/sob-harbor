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
Muhammad Ali vs. Jimmy Ellis: Muhammad Ali and Jimmy Ellis fought each other in a boxing match at the Astrodome in Houston on July 26, 1971.  Ali won the bout through a technical knockout when the referee stopped the fight in the twelfth round.  This was Ali's first boxing match after Fight of the Century.

Cassius Clay vs. Donnie Fleeman: Cassius Clay (soon Muhammad Ali) fought an eight-round boxing match with Texan Donnie Fleeman in Miami on February 21, 1961.  Prior to this fight, Fleeman had a record of 51 fights with 45 wins including 20 knockouts.  Clay won the bout through a technical knockout after the referee stopped the fight in the seventh round.  This was the first time Clay had gone over six rounds in a boxing match.  It was also the first time Fleeman had ever been knocked down in a boxing match.  Fleeman retired from boxing after this fight.

Astrodome: The NRG Astrodome, also known as the Houston Astrodome or simply The Astrodome, is the world's first multi-purpose, domed sports stadium, located in Houston, Texas.  Construction on the stadium began in 1962, and it officially opened in 1965.  It served as home to the Houston Astros of Major League Baseball (MLB) from its opening in 1965 until 1999, and the home to the Houston Oilers of the National Football League (NFL) from 1968 until 1996, and also the part-time home of the Houston Rockets of the National Basketball Association (NBA) from 1971 until 1975.  Additionally, the Astrodome was the primary venue of the Houston Livestock Show and Rodeo from 1966 until 2002.  When opened, it was named the Harris County Domed Stadium and was nicknamed the "Eighth Wonder of the World".

Cassius Clay vs. Sonny Banks: Cassius Clay (soon Muhammad Ali) fought Sonny Banks in a ten-round boxing match at Madison Square Garden in New York City on February 10, 1962.  Clay won the fight through a technical knockout when the referee stopped the fight in the fourth round.  The event is remembered for being the first professional boxing match in which Ali was officially knocked down in the ring by his boxing opponent.

Fearless (Eighth Wonder album): Fearless is the 1988 debut album by British pop group Eighth Wonder.  It is the group's only UK album release, is entirely uptempo, and contains six UK-issued singles (the earliest, "Stay With Me", dating back to 1985) including their highest-selling and best-remembered track, the Pet Shop Boys-produced and written "I'm Not Scared" (a #7 hit), and "Cross My Heart" (#13).  "Fearless" peaked at #47 on the UK Albums Chart.  Eighth Wonder split up in 1989, with lead singer Patsy Kensit going on to devote herself to her acting career.

Muhammad Ali vs. Zora Folley: Muhammad Ali and Zora Folley fought each other in a boxing match at Madison Square Garden in New York City on March 22, 1967. Ali won the bout by knocking out Folley in the seventh round.This would be Ali's last boxing match before his suspension from boxing.

Drama in Bahama: Drama in Bahama was a ten-round boxing match that took place between Muhammad Ali and Trevor Berbick in Nassau, Bahamas on December 11, 1981.  Ali was 39 years old at this time, and Berbick was 27 years old.  The fight went the distance with Berbick winning through a unanimous decision on points.  This was Ali's last boxing match.

Muhammad Ali vs. Buster Mathis: Muhammad Ali and Buster Mathis fought each other in a twelve-round boxing match at the Astrodome in Houston on November 17, 1971. Ali dominated the fight throughout and won easily on points.  Ali knocked Mathis down twice in eleventh round and twice again in the final round but refused to move in for a knockout out of compassion for Mathis.  Ali had joked before the fight that "I'm going to do to Buster what the Indians did to Custer".  One of the fight posters promoting the match said "Be there when the Mountain comes to Muhammad".

Muhammad Ali vs. Cleveland Williams: Muhammad Ali and Cleveland Williams fought each other in a boxing match at the Astrodome in Houston on November 14, 1966.  Ali won the bout through a technical knockout in the third round.  Many experts regard Ali's performance in this fight to be the finest of his boxing career.  It was in this fight that Ali unveiled for the first time the dance step he called "the Ali shuffle".

Cassius Clay vs. Jim Robinson: Cassius Clay (soon Muhammad Ali) fought Jim Robinson in a boxing match at Miami Beach Convention Center on February 7, 1961.  Clay won the fight through a technical knockout when the referee stopped the fight in the first round.  Robinson was a last minute replacement for another fighter who was supposed to fight Clay on the night of the fight; this was Robinson's second professional boxing match.

Question: what "eighth wonder of the world location hosted a boxing match between Ali amd Mathis?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "venue_name": {
      "type": "string",
      "description": "The official name of the venue where the boxing match took place."
    },
    "venue_city": {
      "type": "string",
      "description": "The city where the venue is located."
    },
    "venue_nickname": {
      "type": "string",
      "description": "The nickname given to the venue, specifically 'Eighth Wonder of the World'."
    },
    "fighters": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the boxers who fought in the match."
    },
    "fight_date": {
      "type": "string",
      "format": "date",
      "description": "The date when the boxing match occurred in YYYY-MM-DD format."
    }
  },
  "required": [
    "venue_name",
    "venue_city",
    "venue_nickname",
    "fighters",
    "fight_date"
  ],
  "additionalProperties": false
}
