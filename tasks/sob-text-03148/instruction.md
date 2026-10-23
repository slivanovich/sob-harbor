{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGood Timing: Good Timing is the third full-length album released by B1A4 under WM Entertainment.  The album was released on November 28, 2016 by WM Entertainment and distributed by LOEN Entertainment.  The first single, \"A Lie (거짓말이야)\", was produced by Jinyoung along with 9 other songs on the album.  CNU also composed 3 songs.\n\nIgnition (B1A4 album): Ignition is the first full-length album released by B1A4 under WM Entertainment.  The album was released on March 14, 2012 by WM Entertainment and their distributing label Pony Canyon Korea.  The album spawned 2 singles namely \"This Time Is Over\" and \"Baby I'm Sorry\" which is the title track written and composed by the group's leader Jinyoung.  A special edition of the album was released on May 24, 2012.\n\nOh My Girl (EP): Oh My Girl is the debut extended play (EP) by South Korean girl group Oh My Girl.  It was released by WM Entertainment on April 20, 2015 and distributed by LOEN Entertainment.  The album was produced by Lee Won-min, CEO of WM Entertainment, with music produced by 72 and Moon Jeong-gyu.  The album contains four songs, including the single \"Cupid\", which was released in conjunction with the album.\n\nWho Am I (B1A4 album): Who Am I is the second full-length album released by B1A4 under WM Entertainment.  The album was released on January 13, 2014 by WM Entertainment and their distributing label Pony Canyon Korea.  The title song of the album, \"Lonely (없구나), was produced by leader Jinyoung along with 7 other tracks in the album.  CNU also took part in the composition with 2 self-produced songs.\n\nOh My Girl discography: The discography of the South Korean girl group Oh My Girl consists of five extended plays, one repackage album, and seven singles. Oh My Girl was formed by the Korean entertainment company WM Entertainment in 2015.  The group's debut mini album, \"Oh My Girl\", was released on April 20, 2015.  On October 8, 2015, their second extended play entitled Closer was released.  The group's third mini album, Pink Ocean was released on March 28, 2016 along with its lead single \"Liar Liar\".  After almost 2 months, they released a repackage album of Pink Ocean, titled Windy Day with two additional tracks and a Chinese version of \"Liar Liar\".  On August 1, 2016 they released Listen to My Word, a special summer album entitled containing four remake songs, including Papaya's \"Listen to My Word (A-ing)\" featuring Skull and Haha.  The album topped the Korean Music chart which became their most selling album release.\n\nGirl's Day Everyday 3: Girl's Day Everyday #3 (also stylized as Girl's Day Everyday III) is the fourth mini-album released by South Korean girl group, Girl's Day.  It was released by Dream Tea Entertainment and distribuited by Loen Entertainment on January 3, 2014.  It consists of five songs, including the title track \"Something\", used to promote the EP on several South Korean music programs, including \"Music Bank\" and \"Inkigayo\".  A music video for the title track was also released on January 3.\n\nSolo Day: Solo Day is the fifth mini-album released by B1A4 under WM Entertainment.  The album was released on July 14, 2014 by WM Entertainment and their distributing label Pony Canyon Korea.  The title song of the album, \"Solo Day, was produced by leader Jinyoung along with 5 other tracks in the album.  CNU also produced 1 song in the album.\n\nLet's Fly: Let's Fly is the first mini-album released by B1A4 under WM Entertainment on April 21, 2011.  The songs were mainly composed by Lee Sang-ho but Im Sanghyuk (Beast’s main songwriter) and Jeon Dawoon (K.Will’s main songwriter) have participated in the album along with all the members especially Jinyoung who was directly involved with the songwriting.  All rap lyrics were written by Baro.\n\nSweet Girl (EP): Sweet Girl is the sixth mini-album released by B1A4 under WM Entertainment.  The album was released on August 10, 2015 by WM Entertainment and distributed by LOEN Entertainment.  The title song of the album, \"Sweet Girl\", along with the other songs, was produced by leader Jinyoung.  CNU also produced one song in the album called \"Love is Magic\".  B1A4 won a trophy with \"Sweet Girl\" on the August 19 episode of MBC Every1 Show Champion and earned the title of the tenth most watched music video in America for August by Billboard.\n\nJung Jin-young (singer): Jung Jin-young (Hangul: 정진영 ; born November 18, 1991), professionally known as Jinyoung, is a South Korean singer, songwriter, record producer, and actor.  He is the leader and vocalist of the South Korean boy group B1A4 under WM Entertainment, and has also gained recognition with the television series \"Love in the Moonlight\" (2016).\n\nQuestion: Sweet Girl is the sixth mini-album released by which organization, under WM Entertainment, the  title song of the album, \"Sweet Girl\", along with the other songs, was produced by leader   professionally known as Jinyoung, is a South Korean singer, songwriter, record producer, and actor, given name is Jung Jin-young?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"album_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the album.\"\n    },\n    \"releasing_organization\": {\n      \"type\": \"string\",\n      \"description\": \"The group or artist that released the album.\"\n    },\n    \"record_label\": {\n      \"type\": \"string\",\n      \"description\": \"The entertainment company under which the album was released.\"\n    },\n    \"producer_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"professional_name\": {\n          \"type\": \"string\",\n          \"description\": \"The professional name of the producer.\"\n        },\n        \"given_name\": {\n          \"type\": \"string\",\n          \"description\": \"The given name of the producer.\"\n        },\n        \"role_in_group\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the producer within the releasing organization.\"\n        },\n        \"produced_songs_count\": {\n          \"type\": \"string\",\n          \"description\": \"Description of songs produced by this person on the album.\"\n        }\n      },\n      \"required\": [\n        \"professional_name\",\n        \"given_name\",\n        \"role_in_group\",\n        \"produced_songs_count\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"album_name\",\n    \"releasing_organization\",\n    \"record_label\",\n    \"producer_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "album_name": {
        "type": "string",
        "description": "The name of the album."
      },
      "releasing_organization": {
        "type": "string",
        "description": "The group or artist that released the album."
      },
      "record_label": {
        "type": "string",
        "description": "The entertainment company under which the album was released."
      },
      "producer_details": {
        "type": "object",
        "properties": {
          "professional_name": {
            "type": "string",
            "description": "The professional name of the producer."
          },
          "given_name": {
            "type": "string",
            "description": "The given name of the producer."
          },
          "role_in_group": {
            "type": "string",
            "description": "The role of the producer within the releasing organization."
          },
          "produced_songs_count": {
            "type": "string",
            "description": "Description of songs produced by this person on the album."
          }
        },
        "required": [
          "professional_name",
          "given_name",
          "role_in_group",
          "produced_songs_count"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "album_name",
      "releasing_organization",
      "record_label",
      "producer_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
