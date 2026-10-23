{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBorn in '58: \"Born in '58\" is the last single from Bruce Dickinson's debut solo album, \"Tattooed Millionaire\", released on March 25 1991.  The song is about Bruce Dickinson's early life, growing up with his Grandparents in Worksop (Dickinson was born in 1958).\n\nThe Best of Bruce Dickinson: The Best of Bruce Dickinson is a compilation album released in 2001 by Bruce Dickinson.  Two versions were released; a single disc version and a bonus disc version.  On the front cover, the album title is imposed upon the seal of the demon Astaroth.\n\nThe Book of Souls World Tour: The Book of Souls World Tour was a concert tour by Iron Maiden, held in support of their sixteenth studio album, \"The Book of Souls\".  The first leg of the tour saw the band play shows in 36 countries across six continents, which included their debut performances in El Salvador, Lithuania and China.  With 117 shows, it was the longest tour with Bruce Dickinson on vocals since the \"Somewhere on Tour\" in 1986-87.  The group, their crew and equipment were transported on a customised Boeing 747-400, nicknamed \"Ed Force One\", which was piloted by vocalist Bruce Dickinson.\n\nMan of Sorrows (Bruce Dickinson song): Man of Sorrows is the second single from Bruce Dickinson's fourth solo album, \"Accident of Birth\", released on 3 June 1997.  The song was originally written for a film called Chemical Wedding, which existed only as a script at the time (it was eventually filmed and released in May 2008).  The original version of the song is included on the Best Of Bruce Dickinson album and was recorded in 1990, engineered by André Jacquemin (who is better known for his sound-engineer work for Monty Python) and with Janick Gers on guitar.\n\nList of songs recorded by Iron Maiden: Iron Maiden are an English heavy metal band formed by bassist Steve Harris in 1975.  The band's first album, 1980's \"Iron Maiden\", was written primarily by Harris, with vocalist Paul Di'Anno co-writing two tracks and guitarist Dave Murray contributing \"Charlotte the Harlot\".  The 1981 follow-up, \"Killers\", was written almost entirely by the bassist, with frontman Di'Anno contributing only to the title track, \"Killers\" (the North American bonus track \"Twilight Zone\" was credited to Harris and Murray).  Bruce Dickinson replaced Di'Anno after the release of \"Killers\", although he did not contribute any songwriting to \"The Number of the Beast\", released in 1982, which featured three songs co-written by guitarist Adrian Smith.  \"The Number of the Beast\" also spawned Iron Maiden's first UK Singles Chart top ten in the form of \"Run to the Hills\", which charted at number seven on its release.  It was not until 1983's \"Piece of Mind\" that the songwriting process became a more varied and collaborative approach, with just four of its nine tracks being credited solely to Harris, two to Dickinson and Smith, one to Harris and Murray, one to Dickinson alone, and one to Harris, Dickinson, and Smith.  The Dickinson and Smith-penned \"Flight of Icarus\" was the first Iron Maiden single to chart in the United States, reaching number eight on the \"Billboard\" Mainstream Rock chart.\n\nBruce Dickinson: Paul Bruce Dickinson (born 7 August 1958), known professionally as Bruce Dickinson, is an English singer, songwriter, musician, airline pilot, entrepreneur, author and broadcaster.  He is the lead singer of the heavy metal band Iron Maiden and is renowned for his wide-ranging operatic vocal style and energetic stage presence.\n\nBob Geldof: Robert Frederick Zenon \"Bob\" Geldof, KBE (born 5 October 1951), is an Irish singer-songwriter, author, political activist and occasional actor.  He rose to prominence as the lead singer of the Irish rock band The Boomtown Rats in the late 1970s and early 1980s, alongside the punk rock movement.  The band had Number One hits with his compositions \"Rat Trap\" and \"I Don't Like Mondays\".  He co-wrote \"Do They Know It's Christmas? \", one of the best-selling singles of all time, and starred in Pink Floyd's 1982 film \"Pink Floyd – The Wall\" as \"Pink.\"\n\nThe Vegetarians of Love: The Vegetarians of Love is the second solo studio album by Bob Geldof, released in July 1990.  'The Vegetarians of Love' was also the name of the band of musicians with whom Geldof recorded the album.  It includes Pete Briquette from Geldof's previous band, The Boomtown Rats, who also co-wrote one track.  Another notable co-writer was David A. Stewart of The Eurythmics.  The album was produced by Rupert Hine, who also played on it.\n\nBand Aid 30: Band Aid 30 is the 2014 incarnation of the charity supergroup Band Aid.  The group was announced on 10 November 2014 by Bob Geldof and Midge Ure, with Geldof stating that he took the step after the United Nations had contacted him, saying help was urgently needed to prevent the 2014 Ebola crisis in Western Africa spreading throughout the world.  As in previous incarnations, the group covered the track \"Do They Know It's Christmas? \", written in 1984 by Geldof and Ure, this time to raise money towards the Ebola crisis in Western Africa.  The track has re-tweaked lyrics to reflect the current Ebola virus epidemic in West Africa with all proceeds going towards battling what Geldof described as a \"particularly pernicious illness because it renders humans untouchable and that is sickening\".\n\nThe Wicker Man (song): \"The Wicker Man\" is a song by Iron Maiden, released as the first single and opening track from their album \"Brave New World\" in April 2000.  It is also the first single by the band since the returns of vocalist Bruce Dickinson and guitarist Adrian Smith in 1999.  It was co-written by Smith, Dickinson and Steve Harris.  It was co-produced by Kevin Shirley and Harris.  The title is inspired by the British cult film of the same name.  The song should not be confused with \"Wicker Man\" from Dickinson's solo career, the lyrics of which are more closely themed around the film.  The latter song can be found on the 2 disc edition of \"The Best of Bruce Dickinson\".\n\nQuestion: Are either Bruce Dickinson or Bob Geldof American?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_asked\": {\n      \"type\": \"string\",\n      \"description\": \"The original question posed by the user.\"\n    },\n    \"persons_checked\": {\n      \"type\": \"array\",\n      \"description\": \"List of individuals whose nationality was checked.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the person.\"\n          },\n          \"nationality\": {\n            \"type\": \"string\",\n            \"description\": \"The nationality of the person as stated in the context.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"nationality\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"are_any_american\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if any of the checked persons are American, false otherwise.\"\n    }\n  },\n  \"required\": [\n    \"question_asked\",\n    \"persons_checked\",\n    \"are_any_american\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_asked": {
        "type": "string",
        "description": "The original question posed by the user."
      },
      "persons_checked": {
        "type": "array",
        "description": "List of individuals whose nationality was checked.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the person."
            },
            "nationality": {
              "type": "string",
              "description": "The nationality of the person as stated in the context."
            }
          },
          "required": [
            "name",
            "nationality"
          ],
          "additionalProperties": false
        }
      },
      "are_any_american": {
        "type": "boolean",
        "description": "True if any of the checked persons are American, false otherwise."
      }
    },
    "required": [
      "question_asked",
      "persons_checked",
      "are_any_american"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
