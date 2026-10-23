{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJack Ely: Jack Brown Ely (September 11, 1943 – April 28, 2015) was an American guitarist and singer, best known for singing the Kingsmen's version of \"Louie Louie\".  Classically trained in piano, he began playing guitar after seeing Elvis Presley on television.  In 1959, he co-founded the Kingsmen and with them recorded \"Louie Louie\" in 1963; Ely's famously incoherent vocals were partly the result of his braces and the rudimentary recording method.  Before the record became a hit Ely was forced out of the group and began playing with his new band, the Courtmen.  Ely died in Terrebonne, Oregon, on April 28, 2015 at age 71.\n\nEyesight to the Blind: \"Eyesight to the Blind\" is a 12-bar blues song written and recorded in 1951 by Sonny Boy Williamson II (Aleck \"Rice\" Miller).  He also recorded the related songs \"Born Blind\", \"Unseeing Eye\", \"Don't Lose Your Eye\", and \"Unseen Eye\" during his career.  The Larks, an American rhythm and blues group, recorded the song, which reached number five on the R&B charts in 1951.  Several musicians subsequently recorded it in a variety of styles.  The Who used Williamson's lyrics for their adaptation for the rock opera \"Tommy\".\n\nLovey Dovey: \"Lovey Dovey\" is a popular American rhythm and blues song originating in the 1950s and written by Eddie Curtis and Ahmet Ertegun, with the latter usually credited using his songwriter's pseudonym \"Nugetre\" - Ertegun spelled backwards.  The song deals with the singer's relationship with his sweetheart and is performed in a light-hearted style.\n\nWhat'd I Say: \"What'd I Say\" (or \"What I Say\") is an American rhythm and blues song by Ray Charles, released in 1959.  As a single divided into two parts, it was one of the first soul songs.  The composition was improvised one evening late in 1958 when Charles, his orchestra, and backup singers had played their entire set list at a show and still had time left; the response from many audiences was so enthusiastic that Charles announced to his producer that he was going to record it.\n\nThe Flies Crawled Up the Window: \"'The Flies Crawled Up the Window\" is a British song originally sung by the actor Jack Hulbert in the 1932 comedy film \"Jack's the Boy\".  The lyrics describe the antics of various flies as they crawl up windows.  In the film it is sung by Hulbert's character, Jack Brown, to his disproving father (Peter Gawthorne) after he has returned drunk from an evening out.\n\nI Don't Mind (James Brown song): \"I Don't Mind\" is a rhythm and blues song written by James Brown and performed by Brown and the Famous Flames.  Its unusual chord progression – in Brown's words, it \"opens with a 13, goes down to a C9, then goes to a G7 and to the A7\" – prompted objections during the recording session from producer Gene Redd, who considered it musically \"wrong\".  Released as a single in 1961, it reached number four in the R&B \"Billboard\" charts and number 47 in the Pop \"Billboard\" charts.  Brown and the Flames also performed it on their 1963 album \"Live at the Apollo\".\n\nSince I Met You Baby (song): \"Since I Met You Baby\" is an American rhythm and blues song written and recorded by pianist Ivory Joe Hunter.  The song, which Hunter recorded in 1956, became an American standard, and saw renewed popularity in 1969 when country music artist Sonny James released his hit version.\n\nI'm a Man (Bo Diddley song): \"I'm a Man\" is a rhythm and blues song written and recorded by Bo Diddley in 1955.  A moderately slow number, it was inspired by an earlier blues song and became a number one U.S. R&B chart hit.  \"I'm a Man\" has been recorded by a variety of artists, including The Yardbirds who had a number 17 pop hit in the U.S. in 1965.\n\nLouie Louie: \"Louie Louie\" is an American rhythm and blues song written by Richard Berry in 1955 and best known for the 1963 hit version by The Kingsmen.  It has become a standard in pop and rock, with hundreds of versions recorded by different artists.  The song was originally written and performed in the style of a Jamaican ballad.  It tells, in simple verse–chorus form, the first-person story of a Jamaican sailor returning to the island to see his lady love.\n\nAll Your Love (I Miss Loving): \"All Your Love (I Miss Loving)\" or \"All Your Love\" is a blues song written and recorded by Chicago blues guitarist Otis Rush in 1958.  Of all of his compositions, it is the best-known with versions by several blues and other artists.  \"All Your Love\" was inspired by an earlier blues song and later influenced other popular songs.\n\nQuestion: In what year was this song written that was an American rhythm and blues song and sung by Jack Brown Ely?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"song_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the song.\"\n    },\n    \"year_written\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the song was written.\"\n    },\n    \"original_writer\": {\n      \"type\": \"string\",\n      \"description\": \"The original writer of the song.\"\n    },\n    \"performer_mentioned\": {\n      \"type\": \"string\",\n      \"description\": \"The performer mentioned in the question.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"song_genre\",\n    \"year_written\",\n    \"original_writer\",\n    \"performer_mentioned\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "song_genre": {
        "type": "string",
        "description": "The genre of the song."
      },
      "year_written": {
        "type": "integer",
        "description": "The year the song was written."
      },
      "original_writer": {
        "type": "string",
        "description": "The original writer of the song."
      },
      "performer_mentioned": {
        "type": "string",
        "description": "The performer mentioned in the question."
      }
    },
    "required": [
      "song_title",
      "song_genre",
      "year_written",
      "original_writer",
      "performer_mentioned"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
