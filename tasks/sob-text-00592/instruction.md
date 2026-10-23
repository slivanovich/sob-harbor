{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Unforgiving Tour: The Unforgiving World Tour was a concert tour by Dutch symphonic metal band Within Temptation in support of their fifth studio album, \"The Unforgiving\", released by Roadrunner Records on 25 March 2011.  To date, it was their seventh major tour and their second to see them playing worldwide.\n\nThe Q-Music Sessions: The Q-music Sessions is a special Within Temptation cover album in which consists of eleven covers made by the band for the Belgian radio station \"Q-music\" in celebration of their fifteenth anniversary.  Due to the positive reactions from fans and the radio audience, the band decided to release a special album containing eleven of the fifteen covers made.\n\nFaster (Within Temptation song): \"Faster\" is the first single from Dutch symphonic metal/rock band Within Temptation's album \"The Unforgiving\".  It had its worldwide radio première on 96.3 Rock Radio on 21 January 2011.\n\nThe Unforgiving: The Unforgiving is the fifth studio album by Dutch symphonic metal band Within Temptation, released by Roadrunner Records on March 25, 2011.  It was a concept album as one part of a transmedia storytelling project.The first single, \"Faster\", was released on January 21.  The first related short film \"Mother Maiden'\", was released on January 31.  The second short film, \"Sinéad\" was released on March 21, and the second single with the same name on July 15.  The first issue of the comic books, \"Penance, Part One\", was released on March 18, 2011, and digitally released by Diamond Digital at the New York Comic Con on October 22.  The second issue, \"Penance, Part Two\" was released on May 13.  The third issue, \"Penance, Part Three,\" was released on August 31 and the fourth issue, \"Penance, Part Four\", on November 2.  As of November 2012, the album reportedly sold 313,790 copies exclusively on the iTunes merchandise website.\n\nWhat Have You Done: \"What Have You Done\" is the first single from Dutch symphonic metal/rock band Within Temptation's fourth studio album \"The Heart of Everything\" (2007).  The song features guest vocals from Life of Agony's lead singer Mina Caputo (then known as Keith Caputo) and it was released as the album's first single in early 2007 (see 2007 in music).  It became their first charting single in Canada and in the United States.  A new edit/version of the song was released in the U.S. through iTunes on 26 June 2007.\n\nOur Farewell: \"Our Farewell\" is the first single of the Netherlands symphonic metal/rock band Within Temptation from their second studio album \"Mother Earth\".  Although the song was released as a single, it never entered the charts, just like their previous single, \"Restless\".  There was also no promotional video made for the single.\n\nShot in the Dark (Within Temptation song): \"Shot in the Dark\" is a single from Within Temptation's fifth studio album \"The Unforgiving\".  The song had a promo radio release, but the physical single release although, which was confirmed on 30 September, never came about.  It was released on iTunes on 12 September 2011.  The music video, alongside the short film \"Triplets\", is the last part of the combined \"The Unforgiving\" short movies, following \"Mother Maiden\"/\"Faster\" and \"Sinéad\".\n\nSanctuary (tour): Sanctuary Tour is a concert tour, predominantly acoustic, by Dutch symphonic rock band Within Temptation in support of their fifth studio album, \"The Unforgiving\", released by Roadrunner Records on 25 March 2011.  This is their eight tour and the third passing over theaters.\n\nSinéad (Within Temptation song): \"Sinéad\" is the second single from Within Temptation's fifth studio album, \"The Unforgiving\", released on 15 July 2011.  Its release was announced alongside the unveiling of its artwork on 15 April 2011.  On 19 May 2011, the band announced that the single would contain special dance remixes, confirming on 10 June that there will be four different versions by Benno De Goeij, Scooter, VNV Nation and Groove Coverage.  \"Empty Eyes\" was the b-side on the 5-track maxi CD.\n\nHydra (Within Temptation album): Hydra is the sixth studio album by Dutch symphonic metal band Within Temptation.  It was released on January 31, 2014 in Europe and on February 4, 2014 in North America.  The album contains guest appearances by singer Howard Jones (ex-Killswitch Engage), rapper Xzibit, metal vocalist Tarja Turunen (ex-Nightwish) and alternative rock singer Dave Pirner (Soul Asylum).  The first single, \"Paradise (What About Us?) \", was released on September 27, 2013, and featured Turunen as guest vocalist.  The second single, \"Dangerous\", was released on December 20, in which Jones provided the male vocals.\n\nQuestion: What radio station premiered Within Temptation's first single \"Faster\" from their fifth studio album on January 21,2011?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the single.\"\n    },\n    \"album_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the album the single is from.\"\n    },\n    \"album_studio_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The studio album number.\"\n    },\n    \"premiere_date\": {\n      \"type\": \"string\",\n      \"format\": \"date\",\n      \"description\": \"The date of the worldwide radio premiere.\"\n    },\n    \"radio_station_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the radio station that premiered the single.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"album_title\",\n    \"album_studio_number\",\n    \"premiere_date\",\n    \"radio_station_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the single."
      },
      "album_title": {
        "type": "string",
        "description": "The title of the album the single is from."
      },
      "album_studio_number": {
        "type": "integer",
        "description": "The studio album number."
      },
      "premiere_date": {
        "type": "string",
        "format": "date",
        "description": "The date of the worldwide radio premiere."
      },
      "radio_station_name": {
        "type": "string",
        "description": "The name of the radio station that premiered the single."
      }
    },
    "required": [
      "song_title",
      "album_title",
      "album_studio_number",
      "premiere_date",
      "radio_station_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
