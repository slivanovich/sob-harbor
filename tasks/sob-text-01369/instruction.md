{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Quiet Family: The Quiet Family () is a 1998 South Korean comedy horror film.  It was director Kim Jee-woon's feature film debut.  The story centers on a family who owns a hunting lodge in a remote area, whose customers always happen to end up dying.  Among the film's main cast are pre-stardom Choi Min-sik and Song Kang-ho.\n\nSchloß Wolfsgarten: Schloss Wolfsgarten is a former hunting seat of the ruling family of Hesse-Darmstadt, located in the German state of Hessen, approximately 15 kilometers south of Frankfurt am Main.  The hunting lodge was established between 1722 and 1724 by Landgrave Ernst Ludwig of Hesse-Darmstadt.  Ernst Ludwig's purpose in establishing Wolfsgarten was to pursue his passion for hunting with dogs which he introduced into Hesse in 1709.  The original building corresponded to the usual pattern for hunting seats of that era with a rectangular yard around which was grouped housing for gentlemen, the stables for the houses, and kennels for the dogs.  After Ernst Ludwig's successors abandoned hunting with dogs in 1768, Wolfsgarten was abandoned until the 1830s when the grand ducal family began to restore and expand the property.  From 1879, Wolfsgarten became a favorite country retreat for Grand Dukes Ludwig IV and his son Ernst Ludwig.\n\nThe Happiness of the Katakuris: The Happiness of the Katakuris (カタクリ家の幸福 , Katakuri-ke no Kōfuku ) is a 2001 Japanese musical comedy horror film directed by Takashi Miike, with screenplay by Kikumi Yamagishi.  It is loosely based on the South Korean film \"The Quiet Family\".  The film is a surreal horror-comedy in the farce tradition, which includes claymation sequences, musical and dance numbers, a karaoke-style sing-along scene, and dream sequences.\n\nThe Bunch and Judy: The Bunch and Judy is a musical comedy in two acts with book by Anne Caldwell and R. H. Burnside, lyrics by Anne Caldwell, and music by Jerome Kern.  The story centered on a Broadway starlet, who marries a Scottish nobleman, only to grow disenchanted and return to show business and the man she loves.\n\nElliðaey: Elliðaey is the most northeastern of the Vestmannaeyjar (Westman Islands), an archipelago consisting of 15 to 18 islands (and assorted smaller rocks) located south of Iceland.  Contrary to a recent urban legend, it does not belong to the Icelandic singer Björk (who owns a home on a second Icelandic island named Elliðaey), but rather belongs to the Elliðaey Hunting Association.  The island is 110 acres, making it the third-largest island in the archipelago.  The island is not home to much wildlife except for an abundance of puffins.  The only building is a hunting lodge built by the Elliðaey Hunting Association.  The permanent population of the island is zero.\n\nE. M. Backus Lodge: E. M. Backus Lodge, also known as Camp Toxaway and Canaan Land, is a historic hunting lodge and national historic district located near Lake Toxaway, Jackson County and Transylvania County, North Carolina.  The lodge was built about 1908, and is a 1 1/2-story, double-pile house of chestnut logs.  The lodge contains eight rooms on two floors, each grouped around a central hall.  Also on the property are the contributing log stable (1908, 1922), caretaker's cottage (1908, 1922), guest cottage (c. 1922), barn (c. 1922), and Davis Cottage (c. 1922).  The camp became an exclusive girls' camp, Camp Toxaway, in 1922, and a religious and educational retreat in 1955 known as Canaan Land.\n\nComedy horror: Comedy horror is a literary and film genre that combines elements of comedy and horror fiction.  Comedy horror has been described as able to be categorized under three types: \"black comedy, parody and spoof.\"  The genre almost inevitably crosses over with the black comedy genre.  Comedy horror will often use satire on horror clichés as its main source of humour or take a story in a different perspective, such as \"The Cabin in the Woods\" and \"Drag Me to Hell\".\n\nSchloss Holzheim (hunting seat): Schloss Holzheim is a former hunting seat of the ruling family of Hesse-Kassel, located in the village of in the German state of Hesse, approximately 80 km south of Kassel.  The hunting lodge was built between 1732 and 1735 under Frederick I, King of Sweden and also Landgrave of Hesse-Kassel, in baroque style on the medieval foundation walls (from 1183) of the former manor house of the local noble families Von Holzheim and Von Romrod.  Frederick's father, Landgrave Charles I, Landgrave of Hesse-Kassel had often come here for hunting.  Frederick's brother and governor, Prince William (from 1751 William VIII, Landgrave of Hesse-Kassel), liked to be here as well because of the rich game population of the forest areas around the princely estate.\n\nHen Gwrt Moated Site: Hen Gwrt, (English:Old Court), Llantilio Crossenny, Monmouthshire is the site of a thirteenth century manor house and a sixteenth century hunting lodge.  Originally constructed for the Bishops of Llandaff, it subsequently came into the possession of the Herberts of Raglan Castle.  The bishops constructed a substantial manor house on the site in the thirteenth century, which was moated in the fourteenth.  The building was then adapted by the Herberts to create a lodge within their extensive hunting grounds.  The lodge continued in use until the slighting of Raglan Castle in the English Civil War.\n\nButterfly Lodge: Butterfly Lodge is a five and half room log cabin, originally constructed as a hunting lodge in 1913 for the author, James Willard Schultz.  Originally a rectangular building measuring 18 feet by 24 feet, it has been expanded over the years and now covers 40 feet, 10 inches by 32 feet, 6 inches, the shorter side being the front of the cabin.  It was added to the National Register of Historic Places on June 17, 1992.\n\nQuestion: What musical comedy horror film was originally based on a story centered on a family who owns a hunting lodge?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the musical comedy horror film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the film was produced.\"\n    },\n    \"genres\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of genres the film belongs to.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"original_film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the original film it was based on.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the original film.\"\n        },\n        \"country_of_origin\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the original film was produced.\"\n        },\n        \"plot_summary_key_element\": {\n          \"type\": \"string\",\n          \"description\": \"A key element of the original film's plot, specifically mentioning the family and hunting lodge.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"country_of_origin\",\n        \"plot_summary_key_element\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"country_of_origin\",\n    \"genres\",\n    \"director\",\n    \"original_film_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the musical comedy horror film."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "country_of_origin": {
        "type": "string",
        "description": "The country where the film was produced."
      },
      "genres": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of genres the film belongs to."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "original_film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the original film it was based on."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the original film."
          },
          "country_of_origin": {
            "type": "string",
            "description": "The country where the original film was produced."
          },
          "plot_summary_key_element": {
            "type": "string",
            "description": "A key element of the original film's plot, specifically mentioning the family and hunting lodge."
          }
        },
        "required": [
          "title",
          "release_year",
          "country_of_origin",
          "plot_summary_key_element"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "release_year",
      "country_of_origin",
      "genres",
      "director",
      "original_film_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
