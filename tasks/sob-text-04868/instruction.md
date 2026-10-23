{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe &quot;Pretty Little Lightning Paw&quot; E.P.: The \"Pretty Little Lightning Paw\" E.P. is an EP by Thee Silver Mt. Zion Memorial Orchestra & Tra-La-La Band under the name Thee Silver Mountain Reveries.  It was released May 2004 on Constellation Records.  The name the band assumed for this EP was temporary; they have since reverted to using Thee Silver Mt. Zion Memorial Orchestra.\n\nKollaps Tradixionales: Kollaps Tradixionales is the sixth full-length album by the experimental rock group Thee Silver Mt. Zion under the name Thee Silver Mt. Zion Memorial Orchestra.  It was released in February 2010 on Constellation Records.  The songs \"I Built Myself a Metal Bird\", \"I Fed My Metal Bird the Wings of Other Metal Birds\" and \"There Is a Light\" were played on earlier tours.\n\nBorn into Trouble as the Sparks Fly Upward: Born into Trouble as the Sparks Fly Upward is the second album by the Canadian band The Silver Mt. Zion Memorial Orchestra & Tra-La-La Band.  It was released by Constellation Records in October 2001.\n\nThee Silver Mt. Zion Memorial Orchestra: Thee Silver Mt. Zion Memorial Orchestra (previously A Silver Mt. Zion, The Silver Mt. Zion Memorial Orchestra & Tra-La-La Band, The Silver Mt. Zion Memorial Orchestra and Tra-La-La Band with Choir and Thee Silver Mountain Reveries) is a Canadian band which formed in 1999, originating from Montreal, Quebec.  They use a number of different variations of the name on different releases, but the group use the shorthand SMZ and their name is most often simplified to Silver Mt. Zion.  Since their inception, the group has undergone almost yearly personnel changes.  The band currently has five members following the resignation of three in late 2008.\n\nPlays &quot;High Gospel&quot;: Plays \"High Gospel\" (2011) is the debut album from Canadian musician Efrim Menuck, best known for his work as a founding member of Godspeed You!  Black Emperor and Thee Silver Mt. Zion.  The album alternates instrumental and vocal tracks, an aspect of his work which began with the Silver Mt. Zion album Horses in the Sky.  It was self produced and recorded at the Hotel2Tango and various other locations in Canada in 2010.\n\nNorth Star Deserter: North Star Deserter is a 2007 album by Vic Chesnutt.  The backing musicians on the album are Guy Picciotto (guitarist and vocalist for the groups Rites of Spring and Fugazi) and Canadian Post-rock band, A Silver Mt. Zion.  It was released on Constellation Records on August 27, 2007 (Europe), September 11, 2007 (rest of world)\n\nPost-rock: Post-rock is a form of experimental rock characterized by the influence and use of instruments commonly associated with rock music, but using rhythms and \"guitars as facilitators of timbre and textures\" not traditionally found in rock.  Post-rock bands are often instrumental.  Although firmly rooted in the indie or underground scene of the 1980s and early 1990s, post-rock's style often bears little resemblance musically to that of contemporary indie rock.\n\nHoward Bilerman: Howard Bilerman (born September 25, 1970) is a Canadian recording engineer, producer, and Grammy nominated musician.  He is a former member of the band Arcade Fire, having recorded & drummed on their debut album, \"Funeral\", as well as records by Thee Silver Mt. Zion Memorial Orchestra & Tra-La-La Band, Vic Chesnutt, Basia Bulat, Peter Peter, Rich Aucoin and Angela Desveaux.  He runs the hotel2tango recording studio in Montreal along with Efrim Menuck and Thierry Amar of Godspeed You!  Black Emperor and A Silver Mt. Zion, and Radwan Moumneh.  Before that, he ran a studio in Old Montreal called Mom & Pop Sounds.  Bilerman has been a frequent faculty member at the Banff Centre in Alberta.  He resides in Montreal.\n\nRebecca Foon: Rebecca Foon, also credited as Beckie Foon, is a Canadian cellist, vocalist, and composer from Montreal, Quebec.  Foon currently records under the alias Saltland and is a member and co-founder of the Juno Award-winning modern chamber ensemble Esmerine.  She has also been a member of several groups associated with the post rock, experimental and chamber music scene of Montreal, including Set Fire to Flames, A Silver Mt. Zion, and the instrumental string/piano/accordion-based trio Fifths of Seven.  Esmerine's Turkish folk influenced album \"Dalmak,\" released in 2013, was awarded the Juno Award for Instrumental Album of the Year in 2014.  In 2013 she released her first Saltland album, which \"Exclaim.ca\" called \"a captivating combination of genres from dream pop to chamber music to ambient and shoegaze.\"\n\nHorses in the Sky: Horses in the Sky (2005) is the fourth album by the Canadian post-rock band Silver Mt. Zion, this time under the alias Thee Silver Mt. Zion Memorial Orchestra & Tra-La-La Band.  This is the first Silver Mt. Zion release to feature lyrics on every track (an aspect of the band distinguishing it from parent group Godspeed You!  Black Emperor).\n\nQuestion: What musical genre, consisting of instruments commonly associated with rock and untraditional rhythm, does the Canadian band A Silver Mt. Zion play?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band in question.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The primary musical genre played by the band.\"\n    },\n    \"genre_characteristics\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the genre's characteristics as found in the context.\"\n    },\n    \"band_origin_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country of origin for the band.\"\n    },\n    \"associated_members\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Names of individuals mentioned in the context as members or closely associated with the band.\"\n    }\n  },\n  \"required\": [\n    \"band_name\",\n    \"genre\",\n    \"genre_characteristics\",\n    \"band_origin_country\",\n    \"associated_members\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "band_name": {
        "type": "string",
        "description": "The name of the band in question."
      },
      "genre": {
        "type": "string",
        "description": "The primary musical genre played by the band."
      },
      "genre_characteristics": {
        "type": "string",
        "description": "A description of the genre's characteristics as found in the context."
      },
      "band_origin_country": {
        "type": "string",
        "description": "The country of origin for the band."
      },
      "associated_members": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Names of individuals mentioned in the context as members or closely associated with the band."
      }
    },
    "required": [
      "band_name",
      "genre",
      "genre_characteristics",
      "band_origin_country",
      "associated_members"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
