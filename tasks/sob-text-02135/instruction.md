{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nActual Size: Actual Size is the sixth album by the American rock band Mr. Big, originally released in August 2001.  It was their second and final studio album to feature guitarist Richie Kotzen.  \"Actual Size\" would be Mr. Big's final studio album for 10 years, until \"What If...\" in 2011.\n\nPat Torpey: Pat Torpey is an American hard rock drummer and singer, known as the drummer and backing vocalist of the hard rock band Mr. Big.  He has also played for John Parr, Belinda Carlisle, Robert Plant, Montrose, Richie Kotzen and The Knack.  Pat has recorded with Impellitteri and Ted Nugent.  He is noted by Neil Peart for composing unique rhythms such as that of \"Take Cover\", a rock song from Mr. Big.\n\nDeep Cuts (Mr. Big album): Deep Cuts: The Best of the Ballads is a compilation album by hard rock band Mr. Big, focusing on Mr. Big's most popular ballads.  It was released in 2000.  The two opening tracks \"Where Are They Now\" and \"I'll Leave It Up to You\" are previously unreleased.  \"You Don't Have to Be Strong\" is a non-album track originally only available as a B-side to \"Superfantastic.\"  Tracks 3, 4 & 5 \"Had Enough\", \"Promise Her the Moon\" and \"Just Take My Heart\" are songs re-recorded for this album.  Tracks 6-15 are the original recordings.\n\nBig Bigger Biggest: Greatest Hits: Big, Bigger, Biggest!  The Best of Mr. Big is a compilation CD and DVD by the hard rock band Mr. Big.  CD released in 1996 and DVD released in 2009, it contains the following songs:\n\nCadbury Mr. Big: Mr. Big is the largest sized candy bar produced by Cadbury in Canada, hence the name.  The standard bar is made of a layered vanilla wafer coated in caramel, peanuts and rice crisps covered in a brown simulated chocolate-like coating.  Because of Canada's higher chocolate standards compared to other areas of the world, it is not considered a \"chocolate bar\" and is labeled instead as a \"candy bar\".  The bar is the length of two \"standard\"-sized bars – around 20 centimeters (8 inches) long.  Additional varieties include Mr. Chew Big, Mr. Big Fudge, and Mr. Big with Maple.\n\nMr. Big (film): Mr. Big is a 2007 documentary directed and produced by Tiffany Burns and edited by Alec MacNeill Richardson.  The documentary examines the \"Mr. Big\" undercover methods used by the Royal Canadian Mounted Police (RCMP).  In these operations, RCMP officers pose as gang criminals and develop a relationship with the target in the hope of eventually determining what, if any, knowledge the target has of the crime being investigated.  \"Mr. Big\" operations have been credited with securing difficult convictions in a large number of cases, but concerns have been raised that they involve a risk of false confessions and wrongful convictions.\n\nJust a Closer Walk with Thee: \"Just a Closer Walk with Thee\" is a traditional gospel song that has been covered by many artists.  Performed as either an instrumental or vocal, \"A Closer Walk\" is perhaps the most frequently played number in the hymn and dirge section of traditional New Orleans jazz funerals.  The title and lyrics of the song allude to the Biblical passage from 2 Corinthians 5:7 which states, \"We walk by faith, not by sight\" and James 4:8, \"Come near to God and he will come near to you.\"\n\nMr. Big (Mr. Big album): Mr. Big is the self-titled debut album by the American hard rock supergroup Mr. Big.  Produced by Kevin Elson and Val Garay, the album proved a partial commercial success, reaching the 46th slot on the Billboard 200 chart.  Lead-off single \"Addicted to that Rush\", featuring the band's aggressive guitar and bass playing, also brought the group some mainstream attention, reaching the No. 39 slot on the Billboard Mainstream Rock chart.  300,000 copies were sold, according to a \"Musician\" magazine interview with Mr. Big in 1990.\n\nA Closer Walk: A Closer Walk is Robert Bilheimer's documentary film about the global AIDS epidemic.  Narrated by Glenn Close and Will Smith, \"A Closer Walk\" features cinematography by Richard D. Young, interviews with the Dalai Lama, Bono, and Kofi Annan, and musical contributions by Annie Lennox, The Neville Brothers, Dido, Eric Clapton, Moby, Geoffrey Oryema, and Sade.\n\n...The Stories We Could Tell: ...The Stories We Could Tell is the eighth studio album by hard rock band Mr. Big, the second since their 2010 reunion album \"What If...\".  It was recorded with producer Pat Regan (Kiss, Deep Purple, Warrant, Keel), and features 13 new studio recordings, including \"Gotta Love the Ride\", \"The Man Who Has Everything\", \"Just Let Your Heart Reside\", and \"I Forget to Breathe\".  The European edition also includes a live version of \"Addicted to the Rush\", while the Japanese release features a live version of \"30 Days in the Hole\" from \"Mr. Big\".  The LP was issued by Frontiers Music with performances from original members Paul Gilbert, Eric Martin, Billy Sheehan, and Pat Torpey.\n\nQuestion: What do A Closer Walk and Mr. Big have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"common_attribute\": {\n      \"type\": \"string\",\n      \"description\": \"The attribute that both entities share.\"\n    },\n    \"attribute_value\": {\n      \"type\": \"string\",\n      \"description\": \"The specific value of the shared attribute.\"\n    },\n    \"films_compared\": {\n      \"type\": \"array\",\n      \"description\": \"Details about the films that share the common attribute.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"title\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the film.\"\n          },\n          \"release_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The year the film was released.\"\n          },\n          \"director\": {\n            \"type\": \"string\",\n            \"description\": \"The director of the film.\"\n          },\n          \"subject\": {\n            \"type\": \"string\",\n            \"description\": \"The main subject or topic of the film.\"\n          }\n        },\n        \"required\": [\n          \"title\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"common_attribute\",\n    \"attribute_value\",\n    \"films_compared\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "common_attribute": {
        "type": "string",
        "description": "The attribute that both entities share."
      },
      "attribute_value": {
        "type": "string",
        "description": "The specific value of the shared attribute."
      },
      "films_compared": {
        "type": "array",
        "description": "Details about the films that share the common attribute.",
        "items": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string",
              "description": "The title of the film."
            },
            "release_year": {
              "type": "integer",
              "description": "The year the film was released."
            },
            "director": {
              "type": "string",
              "description": "The director of the film."
            },
            "subject": {
              "type": "string",
              "description": "The main subject or topic of the film."
            }
          },
          "required": [
            "title"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "common_attribute",
      "attribute_value",
      "films_compared"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
