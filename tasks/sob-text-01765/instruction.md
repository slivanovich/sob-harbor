{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDo You Do You Dig Destruction: \"Do You Do You Dig Destruction\" is the first single released by the Norwegian band Turbonegro from their 2007 album Retox.  The single was released in 2007, only available as a mobile download in Norway.  This was the first time a Norwegian band has chosen to initially release a single exclusively for mobile phones.  \"Protect the environment, buy your music digitally,\" urges Turbonegro.  The song was available from Djuice and Telenor in partnership with Universal Music and could be downloaded for free until the end of April.\n\nAres (musician): Ronny Hovland, better known as Ares, (born 3 June 1973 in Bergen) is a Norwegian metal vocalist, guitarist and bassist, and the founder of the Norwegian death metal band Aeternus.\n\nHeXaeon: HeXaeon is the sixth studio album by Norwegian death metal band Aeternus.\n\nAeternus: Aeternus is a Blackened Death metal band from Bergen, Norway.  It was formed in 1993 as an idea of Ronny Hovland, calling himself Ares, and Erik Heggernes, a.k.a. Vrolok.  Later in 1996 Nicola Trier, a.k.a. Morrigan, joined the duo as a bass player, forming the core trio that created the important first two albums of the band.  Morrigan also created the logo picture of ravens and axes that still exists as one of the band's trademarks.\n\nEn gang til (song): \"En gang til\" is a single from Norwegian DJ and electronic music duo Broiler and Norwegian band Sirkus Eliassen.  It was released in Norway on 20 June 2013 for digital download.  The song peaked at number 8 on the Norwegian Singles Chart.  The song is included on Broiler's debut studio album \"The Beginning\" (2013).\n\nStage Dolls: Stage Dolls is a Norwegian hard rock band based in Trondheim, Norway.  In 1982, Erlend Antonsen and Terje Storli played at local clubs in and around Trondheim.  In need of a guitarist they called on Torstein Flakne, who by then had finished playing in The Kids (a popular teeny-band in Norway 1980-82).  Throughout the summer and fall of 1982 the newly formed band started rehearsing and playing shows in the region.  The trio took the name Stage Dolls in January 1983.  The first album, titled \"Soldier's Gun\", was released in the early winter of 1985 after a successful nationwide tour in Norway supporting the Norwegian band TNT.\n\nDeath metal: Death metal is an extreme subgenre of heavy metal music.  It typically employs heavily distorted and low-tuned guitars, played with techniques such as palm muting and tremolo picking, deep growling vocals, aggressive, powerful drumming featuring double kick or blast beat techniques, minor keys or atonality, abrupt tempo, key, and time signature changes and chromatic chord progressions.  The lyrical themes of death metal may invoke slasher film-stylized violence, religion (sometimes Satanism), occultism, Lovecraftian horror, nature, mysticism, mythology, philosophy, science fiction, and politics, and they may describe extreme acts, including mutilation, dissection, torture, rape, cannibalism, and necrophilia.\n\nChillador: A chillador is a very small guitar-shaped fretted stringed instrument, usually with 10, 12, or 14 metal strings, in paired or tripled courses.It is played in Peru and in some border areas in Bolivia, usually has 5 courses like its cousin, the charango.  The sort of music played on chillador it is very much like the music played on charango.  The main difference between charango and chillador is that the charango soundbox is made of an armadillo shell while the chillador is just a little guitar.\n\nBackground music: Background music refers to various styles of music or soundscapes primarily intended to be passively listened to.  It is not meant to be the main focus of an audience, but rather to supplement that which is meant to be focused upon.  Music that is played at a low volume and is not the main focus of an audience is also referred to as background music.  Traditional examples of background music include music played at various social gatherings and music played in certain retail venues.  It is also common to employ background music in various electronic media including film, television, video games, and Internet videos such as video blogs.\n\nOla Nordmann (song): \"Ola Nordmann\" is a Norwegian language song by the Norwegian band Plumbo.  The music was written by band member Lars Erik Blokkhus and the lyrics is by another band member Glenn Hauger.  It is about the traditional Norwegian character Ola Nordmann.  The song was a follow up to Plumbo's successful single \"Møkkamann\" that topped VG lista, the official Norwegian Singles Chart.\n\nQuestion: What is the music played by the Norwegian band Aeternus a subgenre of?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band.\"\n    },\n    \"country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the band is from.\"\n    },\n    \"primary_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The specific genre of music played by the band.\"\n    },\n    \"parent_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The broader genre that the band's primary genre is a subgenre of.\"\n    }\n  },\n  \"required\": [\n    \"band_name\",\n    \"country_of_origin\",\n    \"primary_genre\",\n    \"parent_genre\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "band_name": {
        "type": "string",
        "description": "The name of the band."
      },
      "country_of_origin": {
        "type": "string",
        "description": "The country where the band is from."
      },
      "primary_genre": {
        "type": "string",
        "description": "The specific genre of music played by the band."
      },
      "parent_genre": {
        "type": "string",
        "description": "The broader genre that the band's primary genre is a subgenre of."
      }
    },
    "required": [
      "band_name",
      "country_of_origin",
      "primary_genre",
      "parent_genre"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
