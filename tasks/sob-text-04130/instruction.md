{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTerry Teene: Terry Teene (February 1942 – March 9, 2012) [sometimes alternatively spelled as \"Terry Teen\"] was an American musician, vocalist, songwriter, and entertainer, most commonly known for the early 1960s novelty hit \"Curse of the Hearse\".  According to the Rockabilly Hall of Fame, he recorded over 300 distinct songs and played on 100 or more released recordings, performing as a \"major artist\" on 25 of them.  He has recorded under 70 names and appeared in over 500 nightclubs, by his own count.\n\nOh! What a Carry On!: Oh!  What A Carry On!  was a 1971 compilation album of songs performed by actors from the \"Carry On...\" film series, and released on the budget Music For Pleasure label (MFP 1416).  Many were novelty songs with most, such as those by Jim Dale, having previously been released as singles.  None were recorded specifically for this album or had any direct relationship to the \"Carry On\" films.  For example, Kenneth Williams' songs as Rambling Syd Rumpo, which \"Gramophone\" magazine described as the best on the album, were taken from \"Round the Horne\" and Jim Dale's songs had been hits in the 1950s.\n\nMichel Emer: Michel Emer (June 19, 1906 – November 23, 1984), (real name Emer Rosenstein), was a French musician, composer and lyricist.  His songs have been performed by Edith Piaf, Fréhel, Damia, Lys Gauty, Yves Montand, Jean Sablon, André Claveau, Ray Ventura and his Collegians, Luis Mariano, Tino Rossi, and Eartha Kitt.  He also wrote songs for at least one of his wife Jacqueline Maillan's shows.\n\nRay Stevens' Greatest Hits: Ray Stevens' Greatest Hits is a collection of songs that Ray Stevens previously recorded for Barnaby and Monument Records from 1968 to 1971.  This marks the first album appearance of Stevens' novelty hit single \"Bridget the Midget (The Queen of the Blues).\"  This collection contains two more singles from Barnaby while the rest are recordings for Monument (five singles and three album tracks). \" Gitarzan\" is the album version that begins with noises of an audience.  \"Harry the Hairy Ape\" and \"Ahab the Arab\" are not the original recordings but re-recordings that were made for Monument.  \"Mr. Businessman\" is the album version.\n\nBattery Records (dance): Battery Records was a dance sublabel of Jive Records active for a short time in the mid-1990s unrelated to the current hip hop label also part of the Jive/Zomba family.  The label was mostly known for releasing music by the Swedish Eurodance group Rednex in North America, namely its novelty hit \"Cotton Eye Joe.\"\n\nEartha Kitt: Eartha Mae Kitt (January 17, 1927 – December 25, 2008) was an American singer, actress, dancer, activist and comedian, known for her highly distinctive singing style and her 1953 recordings of \"C'est si bon\" and the enduring Christmas novelty smash \"Santa Baby\", which were both US Top 10 hits.  Orson Welles once called her the \"most exciting woman in the world\".\n\nDon Bowman (singer): Don Bowman (August 26, 1937 – June 5, 2013) was an American country music singer, songwriter, comedian and radio host.  He recorded for RCA Victor between 1964 and 1970, charting in the Top 40 with the novelty hit single \"Chit Akins, Make Me a Star\".  Bowman worked at several radio stations, including KRZK in Branson, Missouri.\n\nHappy Holidays, I Miss You: Happy Holidays, I Miss You is the first Christmas compilation released by InVogue Records.  It was released on November 25, 2016, the day after Thanksgiving.  It contains 11 holiday-themed songs performed by various bands/artists signed to the InVogue Records label.  Though it contains mostly original songs, some bands decided to cover songs done by other artists.  The songs \"Yule Shoot Your Eye Out\" is originally performed by the Pop Punk band Fall Out Boy but is performed by the band In Her Own Words and the song \"Last Christmas\" is originally performed by the band Wham!  but is covered by the band Courage My Love.\n\nI Want a Hippopotamus for Christmas: \"I Want a Hippopotamus for Christmas\" is a Christmas novelty song written by John Rox (1902–1957) and performed by Gayla Peevey (10 years old at the time) in 1953.  The song peaked at number 24 on \"Billboard\" magazine's pop chart in December 1953.\n\nI Yust Go Nuts at Christmas: \"I Yust Go Nuts at Christmas\" is a 1949 Christmas novelty song and monologue written and performed by Harry Stewart as fictional Swede \"Yogi Yorgesson\".  Stewart was backed by the Johnny Duffy Trio on the song.\n\nQuestion: Michael Emer has had songs performed by the singer known for which Christmas novelty hit?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"composer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the composer whose songs were performed by the singer.\"\n    },\n    \"singer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the singer who performed songs by the composer and is known for a Christmas novelty hit.\"\n    },\n    \"christmas_novelty_hit\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the Christmas novelty hit song associated with the singer.\"\n    },\n    \"hit_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the Christmas novelty hit was recorded or released.\"\n    }\n  },\n  \"required\": [\n    \"composer_name\",\n    \"singer_name\",\n    \"christmas_novelty_hit\",\n    \"hit_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "composer_name": {
        "type": "string",
        "description": "The name of the composer whose songs were performed by the singer."
      },
      "singer_name": {
        "type": "string",
        "description": "The name of the singer who performed songs by the composer and is known for a Christmas novelty hit."
      },
      "christmas_novelty_hit": {
        "type": "string",
        "description": "The title of the Christmas novelty hit song associated with the singer."
      },
      "hit_year": {
        "type": "integer",
        "description": "The year the Christmas novelty hit was recorded or released."
      }
    },
    "required": [
      "composer_name",
      "singer_name",
      "christmas_novelty_hit",
      "hit_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
