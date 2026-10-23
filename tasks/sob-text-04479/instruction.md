{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIf You're Gone: \"If You're Gone\" is a song by the rock band Matchbox Twenty.  It was released in October 2000 as the second single off \"Mad Season\".  The song, written by Matchbox Twenty frontman Rob Thomas, became a hit on adult contemporary radio, spending two weeks at number 1 on the \"Billboard\" Hot Adult Contemporary Tracks chart.  It also reached number 5 on the US \"Billboard\" Hot 100 chart, the band's second best-ranking song at this moment, preceded by the single \"Bent\" from the same album.  Rob Thomas never dreamed of the song going out on an album, let alone being a huge success.  The horn-driven outro of \"If You're Gone\" borrows heavily (note for note) from \"When the Rainbow Comes\" by World Party from their 1990 release \"Goodbye Jumbo\".\n\nBig High: Big High is an American rock band formed in Seattle, Washington in 2008 by vocalist Mesa and guitarist Ari Joshua, most noted as the guitarist for Arisawkadoria.  On bass there is William \"Sandy\" Dickerson, and on drums there is Barrett Martin.  The band recorded one untitled demo at London bridge studio before original drummer Steven Barci left the band to tour with Manx guitarist Davy Knowles and The Back Door Slam.  Barrett Martin of Screaming Trees and Mad Season fame joined the band in late 2009 and quickly began recording a self-titled debut album at Seattle's legendary Avast Studios in Ballard Washington.  The debut album was released internationally on June 15, 2010 through Burnside Distribution in Portland, Oregon.\n\nMad Season (album): Mad Season, also known as Mad Season by Matchbox Twenty, is the second studio album from American rock band Matchbox Twenty, released in May 2000.  The album was a significant departure from the bands's debut album, \"Yourself or Someone Like You\", as it moved from a straight rock sound to poppier sounds and experimental rock.  While not as successful as its predecessor, the album entered and peaked at #3 on the \"Billboard\" 200 with first week sales of 365,000 and was certified 4× Platinum in the United States in October 2001.\n\nMad Season (band): Mad Season was an American rock supergroup formed in Seattle, Washington in 1994 by members of three popular Seattle-based bands: Alice in Chains, Pearl Jam and Screaming Trees.  Mad Season released only one album, \"Above\", and is best known for the single \"River of Deceit\".  The band went on a semi-permanent hiatus in 1996 due to the band members' conflicting schedules and vocalist Layne Staley's problems with substance abuse.  Attempts were made in the late 1990s to revive the group without Staley; however, the band dissolved following the death of bassist John Baker Saunders in 1999.  Staley died three years later of a drug overdose.\n\nAbove (Mad Season album): Above is the only studio album by the American rock band Mad Season, released on March 14, 1995, through Columbia Records.  The album has been certified gold by the RIAA in the United States.  Layne Staley also did the album artwork on the cover.\n\nMad Season (song): \"Mad Season\" is the title-track and third single off Matchbox Twenty's second album, \"Mad Season\".  It was released on April 16, 2001.  The song peaked at #48 on the \"Billboard\" Hot 100 and #76 on the UK Singles Chart.\n\nBarrett Martin: Barrett Martin (born April 14, 1967) is an American drummer, composer, producer, award-winning writer, and Zen artist.  He was the drummer for the Seattle, Washington groups Skin Yard and Screaming Trees, as well as the supergroups Mad Season and Tuatara.  A multi-instrumentalist and producer, he does recording session work in Seattle and Los Angeles and has played on, or produced, over 100 albums to date.  In 2014, he was awarded the ASCAP Deems Taylor award for excellence in writing for his liner notes in the Mad Season Deluxe Reissue.  He is primarily known for his powerful tribal drumming style, which includes the use of the tom toms as a rhythmic component that replaces the traditional hihat and ride cymbal.  He credits the jazz drummers Art Blakey, Max Roach, and Elvin Jones for inspiring this approach to his drumming style, as well as the rock drummers John Bonham, Keith Moon, and Neil Peart.  He has also stated that the heavyweight boxer Muhammad Ali inspired his drumming at a young age, saying, \"Ali was so incredibly fast on his feet, and his hands were both light and heavy at the same time.  Float like a butterfly, sting like bee, that's the way a great drummer should play – light and heavy, the way Ali boxed.\"\n\nThe Cribs: The Cribs are an English indie rock band originally from Wakefield, West Yorkshire.  The band consists of twins Gary and Ryan Jarman and their younger brother Ross Jarman.  They were subsequently joined by ex-The Smiths and Modest Mouse guitarist Johnny Marr who was made a formal member of the group in 2008.  Marr would remain as part of the band until 2011; his departure was officially announced on 11 April through the band's website.  The band, who first became active on the concert circuit in 2002, were initially tied to other like-minded UK bands of that time, most notably The Libertines, by a British music press that were looking for a 'British rearguard' to the wave of popular US alternative rock bands of the time.  They had outgrown this tag by the time of the commercial success of their third LP.  In 2008, \"Q\" magazine described the band as \"The biggest cult band in the UK\".\n\nLong Gone Day: \"Long Gone Day\" is a song by the American rock band Mad Season, released in 1995 as the third single from the band's sole studio album, \"Above\" (1995).\n\nMike McCready: Michael David \"Mike\" McCready (born April 5, 1966) is an American musician who serves as the lead guitarist for the American grunge band Pearl Jam.  Along with Jeff Ament, Stone Gossard and Eddie Vedder, he is one of the founding members of Pearl Jam.  McCready was also a member of the side project bands Flight to Mars, Temple of the Dog, Mad Season and The Rockfords.  He is also the proprietor of Hockey Talkter Records.\n\nQuestion: Are The Cribs and Mad Season from the same country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"band_1_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first band in question.\"\n    },\n    \"band_1_country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the first band originated.\"\n    },\n    \"band_2_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second band in question.\"\n    },\n    \"band_2_country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the second band originated.\"\n    },\n    \"are_from_same_country\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if both bands are from the same country, false otherwise.\"\n    },\n    \"reasoning\": {\n      \"type\": \"string\",\n      \"description\": \"Explanation for why the bands are or are not from the same country.\"\n    }\n  },\n  \"required\": [\n    \"band_1_name\",\n    \"band_1_country_of_origin\",\n    \"band_2_name\",\n    \"band_2_country_of_origin\",\n    \"are_from_same_country\",\n    \"reasoning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "band_1_name": {
        "type": "string",
        "description": "The name of the first band in question."
      },
      "band_1_country_of_origin": {
        "type": "string",
        "description": "The country where the first band originated."
      },
      "band_2_name": {
        "type": "string",
        "description": "The name of the second band in question."
      },
      "band_2_country_of_origin": {
        "type": "string",
        "description": "The country where the second band originated."
      },
      "are_from_same_country": {
        "type": "boolean",
        "description": "True if both bands are from the same country, false otherwise."
      },
      "reasoning": {
        "type": "string",
        "description": "Explanation for why the bands are or are not from the same country."
      }
    },
    "required": [
      "band_1_name",
      "band_1_country_of_origin",
      "band_2_name",
      "band_2_country_of_origin",
      "are_from_same_country",
      "reasoning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
