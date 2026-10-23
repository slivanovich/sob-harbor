{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOcelot: The ocelot (\"Leopardus pardalis\") is a wild cat found extensively to South America, as well as the islands of Trinidad and Margarita, Central America, and Mexico.  North of Mexico, it is found regularly only in the extreme southern part of Texas, although there are rare sightings in southern Arizona.\n\nJecca Craig: Jessica Craig, known as Jecca Craig, is an environmental conservationist and PhD Student at University College London.  She helped found Panthera, the world’s larges wild cat conservation organisation and Stop Ivory an independent NGO aiming to protect elephant and stop the trade in ivory.  She is currently completing a PhD on the use of remote camera traps and other technology to monitor and manage protected areas.  Jecca is a former girlfriend of Prince William of Wales.  In April 2015, she became engaged to Canadian professor Jonathan Baillie, director of conservation at the Zoological Society of London.\n\nWild Cat (album): Wild Cat is the debut album by the British heavy metal band Tygers of Pan Tang.  It was released in 1980 on MCA Records.  The album was re-issued in 1989 in a double-LP package with \"Spellbound\", and on CD in 1997 with bonus tracks.\n\nMammoth (Interpol song): \"Mammoth\" is the second UK single from Interpol's third album \"Our Love to Admire\".  The single was released on September 3, 2007.  It reached number 44 on the UK Singles Chart.\n\nKellas cat: The Kellas cat is a small black feline found in Scotland.  Once thought to be a mythological wild cat, with its few sightings dismissed as hoaxes, a specimen was killed by being caught in a snare in 1984 by a gamekeeper named Ronnie Douglas and found to be a hybrid between wild and domestic sub-species of \"Felis silvestris\".  It is not a formal breed of cat, but a landrace of felid hybrids.  It is named after the village of Kellas, Moray, where it was first found.  The historian Charles Thomas speculates that the Pictish stone at Golspie may depict a Kellas.  The Golspie stone, now held at the Dunrobin Castle Museum, shows a cat-like creature standing on top of a salmon which may allude to the characteristics ascribed to a Kellas of catching fish while river swimming.\n\nServal: The serval (\"Leptailurus serval\"), also known as the tierboskat, is a wild cat found in Africa.  It is the sole member of the genus \"Leptailurus\" and was first described by German naturalist Johann Christian Daniel von Schreber in 1776.  Eighteen subspecies are recognised.  The serval is a slender, medium-sized cat that stands at the shoulder and weighs .  It is characterised by a small head, large ears, a golden-yellow to buff coat spotted and striped with black, and a short, black-tipped tail.  The serval has the longest legs of any cat relative to its body size.\n\nOur Love to Admire: Our Love to Admire is the third studio album by American rock band Interpol, released on July 10, 2007 on Capitol Records.  Recorded at Electric Lady Studios in Greenwich Village and The Magic Shop Studios in New York City, the album is the group's first to be released on a major label.  On April 25, 2007 the band officially announced the album title as \"Our Love to Admire\" as well as the track listing.  The first single off the new album, \"The Heinrich Maneuver\", was released on May 7, 2007.\n\nThe Heinrich Maneuver: \"The Heinrich Maneuver\" is a song by American rock band Interpol.  It was released as the lead single from their third studio album, \"Our Love to Admire\" (2007), on May 7, 2007.  The cover features a Serval cat.  The song's title is and an allusion to the book White Noise by Don DeLillo.\n\nHistory of Hersheypark: The history of Hersheypark begins with the founding of the town of Hershey in 1903.  The owner of the Hershey Chocolate Company surveyed a nearby area of land, which was to become a leisure park for the employees of his chocolate company.  People began visiting the grounds of the future park in 1904 and 1905, while the park's first pavilion was built in the fall of 1905.  The park was formally opened on May 30, 1906, when the park opened as Hershey Park.  The park slowly added rides until 1923, when the first roller coaster, Wild Cat, was built.  From then on, rides were regularly added, except during World War II.  The park was redeveloped into Hersheypark in 1970, through a multi-phase project.  Since then, the park has added ten roller coasters, expanded to over 110 acres, and features many other attractions including shows with sea lions, well-known acts including Weird Al Yankovic and Duff Goldman from Charm City Cakes in the Hersheypark Amphitheater, and a short-lived laser light show.\n\nSunda clouded leopard: The Sunda clouded leopard (\"Neofelis diardi\"), also known as the Sundaland clouded leopard, is a medium-sized wild cat found in two Indonesian islands of Borneo and Sumatra.  In 2006, it was classified as a separate species, distinct from its continental relative \"Neofelis nebulosa\".\n\nQuestion: The cover of the \"Our Love to Admire\" album by Interpol features a wild cat found in what country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"album_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the album mentioned in the question.\"\n    },\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band that released the album.\"\n    },\n    \"related_artwork_details\": {\n      \"type\": \"object\",\n      \"description\": \"Details about artwork related to the album that features a wild cat, as explicitly stated in the context.\",\n      \"properties\": {\n        \"artwork_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of artwork featuring the cat (e.g., single cover).\"\n        },\n        \"artwork_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the artwork (e.g., the single title).\"\n        },\n        \"featured_cat\": {\n          \"type\": \"object\",\n          \"description\": \"Information about the wild cat featured on the artwork.\",\n          \"properties\": {\n            \"species_name\": {\n              \"type\": \"string\",\n              \"description\": \"The species name of the wild cat.\"\n            },\n            \"habitat_continent\": {\n              \"type\": \"string\",\n              \"description\": \"The continent where the wild cat is found.\"\n            }\n          },\n          \"required\": [\n            \"species_name\",\n            \"habitat_continent\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"artwork_type\",\n        \"artwork_title\",\n        \"featured_cat\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"album_title\",\n    \"band_name\",\n    \"related_artwork_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "album_title": {
        "type": "string",
        "description": "The title of the album mentioned in the question."
      },
      "band_name": {
        "type": "string",
        "description": "The name of the band that released the album."
      },
      "related_artwork_details": {
        "type": "object",
        "description": "Details about artwork related to the album that features a wild cat, as explicitly stated in the context.",
        "properties": {
          "artwork_type": {
            "type": "string",
            "description": "The type of artwork featuring the cat (e.g., single cover)."
          },
          "artwork_title": {
            "type": "string",
            "description": "The title of the artwork (e.g., the single title)."
          },
          "featured_cat": {
            "type": "object",
            "description": "Information about the wild cat featured on the artwork.",
            "properties": {
              "species_name": {
                "type": "string",
                "description": "The species name of the wild cat."
              },
              "habitat_continent": {
                "type": "string",
                "description": "The continent where the wild cat is found."
              }
            },
            "required": [
              "species_name",
              "habitat_continent"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "artwork_type",
          "artwork_title",
          "featured_cat"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "album_title",
      "band_name",
      "related_artwork_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
