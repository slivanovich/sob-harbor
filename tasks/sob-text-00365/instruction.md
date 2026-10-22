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
Curtain Call (1998 film): Curtain Call is a 1998 romantic comedy directed by Peter Yates, photographed by Sven Nykvist and edited by Hughes Winborne.  It stars James Spader, Polly Walker, Michael Caine and Maggie Smith.  The film was later re-released under the title It All Came True (not to be confused with the completely unrelated 1940 Humphrey Bogart film of the same name).  It was to be Peter Yates' last film made for cinema, although in most markets it went directly to TV or home video.

What I Saw: Reports from Berlin, 1920-1933: What I Saw: Reports from Berlin, 1920-1933 is a book of reportage by the Austrian writer Joseph Roth from the era of the Weimar Republic.  The selection of pieces from Roth's large journalistic output was made by Michael Bienert and published in German in 1996.  The English translation with the present title was made by Michael Hofmann and appeared in 2003.

The Wandering Jews: The Wandering Jews is a short non-fiction book (1926–27) by Joseph Roth about the plight of the Jews in the mid-1920s who, with other refugees and displaced persons in the aftermath of the First World War, the Russian Revolution and the redrawing of national frontiers following the Treaty of Versailles, had fled to the West from the Baltic States, Poland and Russia.  "They sought shelter in cities and towns where most of them had never been and , unfortunately, where they were made despicably unwelcome."  Poverty stricken villagers, they were set apart by their origins, their piety and their dress.  In the last five months of 1926 he visited the Soviet Union where he wrote the final section, "The Condition of the Jews in Soviet Russia".  Walter Jens called it the best book on its subject in German.  An English translation by Michael Hofmann was published in 2001.

The Emperor's Tomb: The Emperor's Tomb (German: Die Kapuzinergruft ) is a 1938 novel by the Austrian writer Joseph Roth.  The Overlook Press published an English translation by John Hoare in 1984.  The novel was adapted into the 1971 film "Trotta" directed by Johannes Schaaf.  New Directions Publishing Corporation published a new translation by Michael Hofmann in 2013.

Bangladesh Film Directors Association: Bangladesh Film Directors Association is the pan-national trade body of film directors in Bangladesh.  The Bangladesh Film Directors Association’s General Secretary is Badiul Alam Khokon.  Mushfiqur Rahman Gulzar is the president of Bangladesh Film Directors Association.

Paul Bogart: Paul Bogart (November 21, 1919 – April 15, 2012) was an American television and film director and producer.

Nick Dennis: Nick Dennis (April 26, 1904 – November 14, 1980) was a Greek American film actor born in Thessaly, Greece.  The supporting actor, who began in films in 1947, was known for playing ethnic types (usually Greek) in films such as "Kiss Me Deadly" and the Humphrey Bogart film "Sirocco".  Dennis, who spoke Greek fluently, appeared in a number of television programs in the 1960s and 1970s including playing the parts of Orderly Nick Kanavaras on the medical drama "Ben Casey" and Uncle Constantine on the detective show "Kojak".

Michael Hofmann (director): Michael Hofmann (born 1961) is a German film director.

Eden (2006 film): Eden is a 2006 German film directed by Michael Hofmann in which a successful chef falls for a married woman.

Michael Hofmann (sumi-e): Michael Hofmann is an artist and teacher.  He has been an active sumi-e painter since moving from the United States to Japan in 1972.  For 33 years Hofmann worked closely with (1904-2005), the prominent sumi-e painter, Abbot of Kokusei-ji Temple, Awajishima and Director of Japan's National Association of Nanga Painters.  Hofmann has taught sumi-e ink painting at universities, museums and cultural institutions in both Japan and the United States.  He has illustrated numerous books and his work has been exhibited extensively in galleries and museums.

Question: Are both Michael Hofmann and Paul Bogart film directors?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question that was asked."
    },
    "answer": {
      "type": "boolean",
      "description": "True if both individuals are film directors, false otherwise."
    },
    "individuals_checked": {
      "type": "array",
      "description": "Details for each individual mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "is_film_director": {
            "type": "boolean",
            "description": "True if the individual is identified as a film director in the context."
          },
          "other_professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Other professions or roles attributed to the individual in the context."
          }
        },
        "required": [
          "name",
          "is_film_director"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "question_asked",
    "answer",
    "individuals_checked"
  ],
  "additionalProperties": false
}
