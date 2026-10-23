{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nStill Got Time: \"Still Got Time\" is a song by English singer Zayn featuring Canadian singer and rapper PartyNextDoor.  Zayn announced the song through social media.  and it is taken from his upcoming second studio album.  \"Still Got Time\" debuted on American radio on 24 March 2017.\n\nYou've Got Time: \"You've Got Time\" is the main title theme song for the Netflix Original Series \"Orange Is the New Black\", written, composed and performed by Regina Spektor.  The song was nominated in the Best Song Written for Visual Media category at the 56th Annual Grammy Awards.\n\nI Ain't Got Time to Tarry: \"I Ain't Got Time to Tarry\", also known as \"The Land of Freedom\", is an American song written by blackface minstrel composer Dan Emmett.  It premiered in a minstrel show performance by Bryant's Minstrels in late November 1858.  The song was published in New York City in 1859.\n\nFor a Minute (M.O song): \"For a Minute\" is a song by English recording trio M.O.  It was co-written by Jess Glynne and produced by Bless Beats and Loadstar.  The song was released by Operator Records as a digital download on 13 April 2014 in the United Kingdom, marking the trio's debut single after buzz tracks \"On Ya\", \"Hot\", \"Wait Your Turn\", \"Come Let Me Show You\", and \"Ain't Got Time\".\n\nZayn Malik: Zain Javadd \"Zayn\" Malik ( Urdu: ‎ ; born 12 January 1993), who records mononymously as Zayn, is a British singer and songwriter.  Born and raised in Bradford, Malik aspired to pursue a career in music from a young age, and auditioned as a solo artist for the British music competition \"The X Factor\" in 2010.  After being eliminated as a solo performer, Malik was brought back into the competition, along with four other contestants, to form the boy band that would become known as One Direction.  Malik split from the group in March 2015 and signed a solo recording contract with RCA Records.  Adopting a more R&B music style with his debut studio album \"Mind of Mine\" (2016) and its lead single, \"Pillowtalk\", Malik became the first British male artist to debut at number one in both the UK and US with a debut single and debut album.  Malik is the recipient of several accolades, including an American Music Award and a Billboard Music Award.\n\nStill Got Tonight: \"Still Got Tonight\" is a song recorded by American actor and singer Matthew Morrison for his eponymous debut studio album.  It was written and produced by Andrew Frampton and Steve Kipner and co-written by Kris Allen.  \"Still Got Tonight\" was released April 26, 2011 as the second single from \"Matthew Morrison\".\n\nThe Glass Bottle: The Glass Bottle was an American pop band fronted by Gary Criss, whose song about bitterness and heartbreak, \"I Ain't Got Time Anymore\", was recorded in 1970 and reached #36 on the \"Billboard\" Hot 100 chart in September 1971.  The band was co-produced by Dickie Goodman.  Goodman had an advertising deal with a PR firm that was trying to save the glass industry from losing soda pop clients to plastic bottles, so Goodman and partner Bill Ramal formed a group, called them \"The Glass Bottle\" and produced their album.  The group produced two hits, \"I Ain't Got Time Anymore\" and \"The Girl Who Loved Me When\", before breaking up and drifting into obscurity.\n\nI'm Going Home to Dixie: \"I'm Going Home to Dixie\" is an American walkaround, a type of dance song.  It was written by Dan Emmett in 1861 as a sequel to the immensely popular walkaround \"Dixie\".  The sheet music was first published that same year by Firth, Pond & Company in an arrangement by C. S. Grafully.  Despite the publisher's claim that \"I'm Going Home to Dixie\" had been \"Sung with tumultuous applause by the popular Bryant's Minstrels\", the song lacked the charm of its predecessor, and it quickly faded into obscurity.  The song's lyrics follow the minstrel show scenario of the freed slave longing to return to his master in the South; it was the last time Emmett would use the term \"Dixie\" in a song.  Its tune simply repeated Emmett's earlier walkaround \"I Ain't Got Time to Tarry\" from 1858.\n\nStill Got It: \"Still Got It\" is a song by American rapper Tyga featuring fellow Young Money-member, Drake.  The original song was first leaked on June 21, 2010 with only Drake on it.  The song was then re-released on October 4, 2011 as the second single from the rapper's debut studio album, \"\".  The song was produced by Noah \"40\" Shebib and Supa Dups, appearing as a bonus track on the deluxe edition of the album.  \"Still Got It\" marks the rapper's third consecutive release to impact the \"Billboard\" Hot 100, debuting at number eighty-nine for the chart week dated October 24, 2011; also peaking at number seventy on the R&B/hip-hop chart.\n\nStill Got the Blues (For You): \"Still Got the Blues (For You)\" is a song by Northern Irish guitarist Gary Moore.  It was originally released as the title track of the album \"Still Got the Blues\".  The song was released as a single and reached #31 on the UK Singles Chart in May 1990.  It is the only single of Moore's solo career to chart on the \"Billboard\" Hot 100, where it reached #97 on 16 February 1991.  Moore played his Les Paul Standard Guitar throughout the song.  He also filmed a basic music video for the song.\n\nQuestion: \"Still Got Time\", is a song by which British singer and songwriter, and rapper PartyNextDoor?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"primary_artist\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the primary artist.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the primary artist.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the primary artist (e.g., singer, songwriter).\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"featured_artist\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the featured artist.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the featured artist.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the featured artist (e.g., singer, rapper).\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"album_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"album_status\": {\n          \"type\": \"string\",\n          \"description\": \"The status of the album the song is taken from (e.g., upcoming).\"\n        }\n      },\n      \"required\": [\n        \"album_status\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"radio_debut_date\": {\n      \"type\": \"string\",\n      \"description\": \"The date the song debuted on American radio.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"primary_artist\",\n    \"featured_artist\",\n    \"album_info\",\n    \"radio_debut_date\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "primary_artist": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the primary artist."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the primary artist."
          },
          "role": {
            "type": "string",
            "description": "The role of the primary artist (e.g., singer, songwriter)."
          }
        },
        "required": [
          "name",
          "nationality",
          "role"
        ],
        "additionalProperties": false
      },
      "featured_artist": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the featured artist."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the featured artist."
          },
          "role": {
            "type": "string",
            "description": "The role of the featured artist (e.g., singer, rapper)."
          }
        },
        "required": [
          "name",
          "nationality",
          "role"
        ],
        "additionalProperties": false
      },
      "album_info": {
        "type": "object",
        "properties": {
          "album_status": {
            "type": "string",
            "description": "The status of the album the song is taken from (e.g., upcoming)."
          }
        },
        "required": [
          "album_status"
        ],
        "additionalProperties": false
      },
      "radio_debut_date": {
        "type": "string",
        "description": "The date the song debuted on American radio."
      }
    },
    "required": [
      "song_title",
      "primary_artist",
      "featured_artist",
      "album_info",
      "radio_debut_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
