{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBeograd, uživo '97 – 1: Beograd, uživo '97 – 1 (trans. \" Belgrade, Live '97 - 1\") is the first disc of the fourth live album by Serbian and former Yugoslav rock band Riblja Čorba, released in 1997.  \"Beograd, uživo '97 - 1\" was followed by \"Beograd, uživo '97 - 2\", as the band, instead of releasing a double live album, opted for two separate releases.  Album was recorded on Riblja Čorba concert held on June 1, 1997 on Belgrade's Tašmajdan Stadium.\n\nBeograd, uživo '97 – 2: Beograd, uživo '97 – 2 (trans. \" Belgrade, Live '97 – 2\") is the second disc of the fourth live album by Serbian and former Yugoslav rock band Riblja Čorba, released in 1997.  \"Beograd, uživo '97 - 2\" was preceded by \"Beograd, uživo '97 - 1\", as the band, instead of releasing a double live album, opted for two separate releases.  Album was recorded on Riblja Čorba concert held on June 1, 1997 on Belgrade's Tašmajdan Stadium.\n\nYoung American Primitive: Young American Primitive (real name Greg Scanavino) is a prominent American producer/remixer, and one of the more popular acts to originate from the Bay Area's early 90s house scene.  Released several 12\"s and one full length CD on the San Francisco based label ZoëMagik, and made several compilation appearances, culminating with the sample heavy \"These Waves\" being included on Sasha and Digweed's Northern Exposure mix album.  Apparently impressed by his remixing skills on Geffen Records release The Stone Roses' single \"Begging You\", Scanavino was signed by Geffen in '96 and finished his second full length album in late '97.  The track \"Beyond\" was slated for single release in November '97 (complete with music video created by San Francisco based multimedia studio Mind's Eye Media), and the album, titled \"African Cosmopolitan\", was slated for a January '98 release, however, neither saw the light of day, and YAP was apparently dropped from the label.  The ZoëMagik-released album was not re-released on Geffen due to unresolved sample clearance issues.\n\nGreco-Turkish War (1897): The Greco-Turkish War of 1897, also called the Thirty Days' War and known in Greece as the Black '97 (Greek: Μαύρο '97 , \"Mauro '97\") or the Unfortunate War (Ατυχής πόλεμος, \"Atychis polemos\"), was a war fought between the Kingdom of Greece and the Ottoman Empire.  Its immediate cause was the question over the status of the Ottoman province of Crete, whose Greek majority long desired union with Greece.  Despite the Ottoman victory at the field, an autonomous Cretan State under Ottoman suzerainty was established the following year (as a result of the intervention of the Great Powers after the war), with Prince George of Greece and Denmark as its first High Commissioner.\n\nAC'97: AC'97 (Audio Codec '97; also MC'97 for Modem Codec '97) is an audio codec standard developed by Intel Architecture Labs in 1997.  The standard was used in motherboards, modems, and sound cards.\n\nNFL '97: NFL '97 is a follow-up video game to Sega's classic Joe Montana series on the Sega Mega Drive/Genesis.  \"NFL '97\" featured some sound effects directly from that series.  \"NFL 97\" was released exclusively for the Sega Saturn.\n\n'97 Bonnie &amp; Clyde: \"'97 Bonnie & Clyde\" is a song by American rapper Eminem.  The song appears on the \"Slim Shady EP\" (as \"Just the Two of Us\") & \"The Slim Shady LP\".  Eminem recorded a prequel for The Marshall Mathers LP, \"Kim\".  The song is covered by Tori Amos on her 2001 album of gender-swapped covers, \"Strange Little Girls\".\n\nKim (song): \"Kim\" is a song by American rapper Eminem which appears on his 2000 album \"The Marshall Mathers LP\".  The song reflects intense anger and hatred toward Eminem's then-wife Kim Mathers and features Eminem imitating her voice, and ends with Eminem killing Kim and later burying her.  \"Kim\" was the first song the rapper recorded for the album, shortly after finishing work on \"The Slim Shady LP\" in late 1998.  Eminem wrote this song, along with \"'97 Bonnie & Clyde\" (where Eminem and his daughter go to the lake to dispose of Kim's dead body), at a time when he and Kim were having marital problems and Kim was preventing him from seeing his daughter Hailie.  While the song has been cited as an example of misogyny in hip hop culture, it is often highlighted as one of Eminem's most memorable songs.\n\nEminem: Marshall Bruce Mathers III (born October 17, 1972), known professionally as Eminem (often stylized as EMINƎM), is an American rapper, record producer, and actor.\n\nK-1 Grand Prix '97 Final: K-1 Grand Prix '97 Final was a kickboxing event promoted by the K-1 organization.  It was the fifth K-1 World Grand Prix final involving eight of the world's best heavyweight fighters (+95 kg/209 lbs), with all bouts fought under K-1 Rules.  The eight finalists had all qualified via elimination fights at the K-1 Grand Prix '97 1st Round.  Also on the card was a four-man tournament for featherweight kickboxers (57 kg/126 lbs) based in Japan and a local 'Super Fight', with all bouts fought under K-1 Rules.  In total there were fourteen fighters at the event, representing seven countries.\n\nQuestion: When was the rapper who made '97 Bonnie & Clyde\" born?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"rapper_name\": {\n      \"type\": \"string\",\n      \"description\": \"The professional name of the rapper.\"\n    },\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song mentioned in the question.\"\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The full birth date of the rapper.\"\n    },\n    \"birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the rapper.\"\n    },\n    \"birth_month\": {\n      \"type\": \"string\",\n      \"description\": \"The birth month of the rapper.\"\n    },\n    \"birth_day\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth day of the month for the rapper.\"\n    }\n  },\n  \"required\": [\n    \"rapper_name\",\n    \"song_title\",\n    \"birth_date\",\n    \"birth_year\",\n    \"birth_month\",\n    \"birth_day\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "rapper_name": {
        "type": "string",
        "description": "The professional name of the rapper."
      },
      "song_title": {
        "type": "string",
        "description": "The title of the song mentioned in the question."
      },
      "birth_date": {
        "type": "string",
        "description": "The full birth date of the rapper."
      },
      "birth_year": {
        "type": "integer",
        "description": "The birth year of the rapper."
      },
      "birth_month": {
        "type": "string",
        "description": "The birth month of the rapper."
      },
      "birth_day": {
        "type": "integer",
        "description": "The birth day of the month for the rapper."
      }
    },
    "required": [
      "rapper_name",
      "song_title",
      "birth_date",
      "birth_year",
      "birth_month",
      "birth_day"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
