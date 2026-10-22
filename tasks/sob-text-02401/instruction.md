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
Evgeny Bareev: Evgeny Ilgizovich Bareev (Russian: Евгений Ильгизович Бареев ; born 21 November 1966 in Yemanzhelinsk) is a Russian (until 2015) and Canadian (since 2015) chess grandmaster and coach.  In October 2003, he was ranked fourth in the FIDE World Rankings, with an Elo rating of 2739.

Russian Spaniel: The Russian Spaniel is a type of spaniel first standardised in 1951 in the Soviet Union after World War II by cross breeding English Cocker Spaniels, English Springer Spaniels and other spaniel breeds.  Physically it is similar to a Cocker Spaniel, but has a shorter, tighter coat and a longer body.  Developed and used as hunting dogs, this breed does not suffer from any major health complaints other than those normally associated with spaniels.  Popular in its native Russia, the breed was only introduced overseas in the 1990s, and is not yet recognised by any major kennel clubs.

Elo (dog): The Elo is an emerging breed of dog, with development beginning in 1987 in Germany.  The breed name is trademarked and development has been closely supervised by the Elo Breeding and Research Association.  The Elo is notable in that it is primarily selected and bred according to behavioral characteristics and social behavior, with the goal of creating the best family pet.

Diamondprox: Danil Reshetnikov (born December 24, 1992) known as Diamondprox, is a Russian "League of Legends" player was most recently the jungler for Team Apex of the North American League of Legends Championship Series (NA LCS).  He has also played for Team Empire, Moscow Five, Gambit Gaming, and Unicorns of Love.  Diamondprox hails from Saint Petersburg, Russia.  Diamond is one of the world's most known junglers, known for his play on such champions as Lee Sin in Season 2, and innovating the popular Season 3 jungle play of Nasus and Xin Zhao.  Danil became known in the high elo ladders of League of Legends end of Season 1 and pre-Season 2.

Boris Gulko: Boris Franzevich Gulko (Russian: Борис Францевич Гулько ; ] ; born February 9, 1947) is a Soviet-American International Grandmaster in chess.  His peak Elo rating was 2644 in 2000.

Urii Eliseev: Urii Mikhailovich Eliseev (Russian: Юрий Михайлович Елисеев ; August 29, 1996 – November 26, 2016) was a Russian chess player.  He won the Under-16 section of World Youth Chess Championship in 2012 and was awarded the Grandmaster title by FIDE in 2013 at the age of 17.  He won the Moscow Chess Championship in 2015 and the Moscow Open in 2016.  He was ranked 212th in the world and 42nd in Russia, with an Elo rating of 2614.

Question: What are both a Russian Spaniel and an Elo?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the entities mentioned in the question."
    },
    "common_classification": {
      "type": "string",
      "description": "The shared classification or category for both entities."
    },
    "classification_details": {
      "type": "string",
      "description": "Additional details about the common classification from the context."
    }
  },
  "required": [
    "entity_names",
    "common_classification",
    "classification_details"
  ],
  "additionalProperties": false
}
