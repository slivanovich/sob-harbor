{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nI. Howard Marshall: Ian Howard Marshall (12 January 1934 – 12 December 2015) was a Scottish New Testament scholar.  He was Professor Emeritus of New Testament Exegesis at the University of Aberdeen, Scotland.  He was formerly the chair of the Tyndale Fellowship for Biblical and Theological Research; he was also president of the British New Testament Society and chair of the Fellowship of European Evangelical Theologians.  Marshall identified as an Evangelical Methodist.  He was the author of numerous publications, including 2005 Gold Medallion Book Award winner \"New Testament Theology\".  He died of pancreatic cancer in 2015.\n\nMary of Bethany: Mary of Bethany (Judeo-Aramaic מרים, \"Maryām\", rendered Μαρία, Maria, in the Koine Greek of the New Testament; form of Hebrew מִרְיָם, Miryām, or Miriam, \"wished for child\", \"bitter\" or \"rebellious\") is a biblical figure described in the Gospels of John and Luke in the Christian New Testament.  Together with her siblings Lazarus and Martha, she is described by John as living in the village of Bethany near Jerusalem; in Luke only the two sisters, living in an unnamed village, are mentioned.  Most Christian commentators have been ready to assume that the two sets of sisters named as Mary and Martha are the same, though this is not conclusively stated in the Gospels, and the proliferation of New Testament \"Marys\" is notorious.\n\nList of Christian holy sites in the Holy Land: The list Christian holy sites in the Holy Land outlines sites within cities located in the Holy Land that are regarded as having a special significance to Christians, usually by association with Jesus or other persons mentioned in the New Testament.\n\nConcordant Version: The Concordant Version is an English translation of the Bible compiled by the Concordant Publishing Concern (CPC), which was founded by Adolph Ernst Knoch in 1909.  The principal works of the CPC are the Concordant Literal New Testament with Keyword Concordance (\"CLNT\") and the Concordant Version of the Old Testament (\"CVOT\").  A. E. Knoch designed the Concordant Version in such a way as to put the English reader who lacks a formal knowledge of Koine Greek in possession of all the vital facts of the most ancient codices: Codex Vaticanus, Codex Sinaiticus, and Codex Alexandrinus.  The CPC's efforts yielded a restored Greek text, titled The Concordant Greek Text, containing all of the important variant readings found in the codices mentioned above.  This was done with the intent of conforming, as far as possible, to the original autograph manuscripts.  An utterly consistent hyper-literal sub-linear based upon a standard English equivalent for each Greek element is to be found beneath each Greek word.  The Concordant Greek Text forms the basis of the Concordant Literal New Testament, which is more idiomatic in its English than the hyper-literal sublinear.  The Concordant Literal New Testament and the Concordant Greek Text are linked together and correlated for the English reader by means of an English concordance—the Keyword Concordance—and a complementary list of the Greek elements.\n\nIllés Relief: Illés Relief is a scale model of the holy city of Jerusalem.  The model is made from molten and beaten zinc and is hand-painted.  It was hand-crafted between 1864 and 1873 by Stephen Illés (] ), a Hungarian Catholic who lived in the city making a living from book binding.  The scale model reflects the city under the later stages of Ottoman rule.  The model is considered the first scientific relief model of the city.\n\nPalestine Park: Palestine Park is a scale model of the Holy Land, including cities, hills, rivers, and seas, in approximately correct geographical relation on the grounds of Chautauqua Institution in Chautauqua, New York.  Palestine Park is laid out along the southwestern side of Chautauqua Lake, which takes the place of the Mediterranean Sea.  This creates a rotated version of the actual land, which is on the east coast of the Mediterranean.  A large mound of stones represents Mount Hermon, with an artificial stream representing the Jordan River as it flows south from the Sea of Galilee to the Dead Sea.  Small hills represent biblical landmarks such as Mount Tabor and the Mount of Olives, with markers representing sites of biblical significance including Jacob's Well, Jericho, Bethsaida and a scale model of Jerusalem in the time of Jesus complete with a small replica of the ancient Jewish Temple.\n\nMaquette: A maquette (French word for scale model, sometimes referred to by the Italian names plastico or \"modello\") is a small scale model or rough draft of an unfinished sculpture.  An equivalent term is bozzetto, from the Italian word that means \"sketch\".\n\nCustody of the Holy Land: The Custody of the Holy Land (Latin: Custodia Terræ Sanctæ) is a custodian priory of the Franciscan order in Jerusalem, founded as \"Province of the Holy Land\" in 1217 by Saint Francis of Assisi, who also founded the Franciscan Order.  Its mission is to guard \"the grace of the Holy Places\" of the Holy Land and the rest of the Middle East, \"sanctified by the presence of Jesus\", as well as pilgrims visiting them, on behalf of the Catholic Church.  The \"Custodial Curia\" was led by \"Custos\" Fr.  Pierbattista Pizzaballa since 2004, with the approval of the Holy See; since 2016, the chief custodian is Francesco Patton.  Its headquarters are located in the Monastery of Saint Saviour, a 16th-century Franciscan monastery near the New Gate in the Old City of Jerusalem.\n\nBiblical archaeology: Biblical archaeology involves the recovery and scientific investigation of the material remains of past cultures that can illuminate the periods and descriptions in the Bible, be they from the Old Testament (Tanakh) or from the New Testament, as well as the history and cosmogony of the Judeo-Christian religions.  The principal location of interest is what is known in the relevant religions as the Holy Land, which from a western perspective is also called the Middle East.  In contrast, the archaeology of the ancient Middle East simply deals with the Ancient Near East, or Middle East, without giving any especial consideration to whether its discoveries have any relationship with the Bible.\n\nBethsaida: Bethsaida (from Hebrew/Aramaic בית צידה \"beth-tsaida\", lit. \" house of hunting\" or \"fishing\", from the Hebrew root צדה or צוד) is a place mentioned in the New Testament.\n\nQuestion: What is a scale model of the Holy Land including cities, hills, rivers, and seas feature Bethsaida, which means \"house of hunting\", as mentioned in the New Testament?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"scale_model_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the scale model.\"\n    },\n    \"model_description\": {\n      \"type\": \"string\",\n      \"description\": \"A general description of what the model represents, including its scope.\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"institution_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the institution where the model is located.\"\n        },\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the model is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the model is located.\"\n        }\n      },\n      \"required\": [\n        \"institution_name\",\n        \"city\",\n        \"state\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"included_geographical_features\": {\n      \"type\": \"array\",\n      \"description\": \"A list of major geographical features represented in the model.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"included_biblical_sites\": {\n      \"type\": \"array\",\n      \"description\": \"A list of biblical sites represented in the model.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"site_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the biblical site.\"\n          },\n          \"is_scale_model_replica\": {\n            \"type\": \"boolean\",\n            \"description\": \"Indicates if the site is represented by a scale model replica within the larger model, or just a marker.\"\n          },\n          \"attributes\": {\n            \"type\": \"object\",\n            \"description\": \"Specific attributes or details about the biblical site.\",\n            \"properties\": {\n              \"meaning\": {\n                \"type\": \"string\",\n                \"description\": \"The meaning of the site's name.\"\n              },\n              \"mentioned_in_text\": {\n                \"type\": \"string\",\n                \"description\": \"The biblical text where the site is mentioned.\"\n              },\n              \"time_period\": {\n                \"type\": \"string\",\n                \"description\": \"The historical period represented for the site.\"\n              }\n            },\n            \"additionalProperties\": false\n          }\n        },\n        \"required\": [\n          \"site_name\",\n          \"is_scale_model_replica\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"scale_model_name\",\n    \"model_description\",\n    \"location\",\n    \"included_geographical_features\",\n    \"included_biblical_sites\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "scale_model_name": {
        "type": "string",
        "description": "The name of the scale model."
      },
      "model_description": {
        "type": "string",
        "description": "A general description of what the model represents, including its scope."
      },
      "location": {
        "type": "object",
        "properties": {
          "institution_name": {
            "type": "string",
            "description": "The name of the institution where the model is located."
          },
          "city": {
            "type": "string",
            "description": "The city where the model is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the model is located."
          }
        },
        "required": [
          "institution_name",
          "city",
          "state"
        ],
        "additionalProperties": false
      },
      "included_geographical_features": {
        "type": "array",
        "description": "A list of major geographical features represented in the model.",
        "items": {
          "type": "string"
        }
      },
      "included_biblical_sites": {
        "type": "array",
        "description": "A list of biblical sites represented in the model.",
        "items": {
          "type": "object",
          "properties": {
            "site_name": {
              "type": "string",
              "description": "The name of the biblical site."
            },
            "is_scale_model_replica": {
              "type": "boolean",
              "description": "Indicates if the site is represented by a scale model replica within the larger model, or just a marker."
            },
            "attributes": {
              "type": "object",
              "description": "Specific attributes or details about the biblical site.",
              "properties": {
                "meaning": {
                  "type": "string",
                  "description": "The meaning of the site's name."
                },
                "mentioned_in_text": {
                  "type": "string",
                  "description": "The biblical text where the site is mentioned."
                },
                "time_period": {
                  "type": "string",
                  "description": "The historical period represented for the site."
                }
              },
              "additionalProperties": false
            }
          },
          "required": [
            "site_name",
            "is_scale_model_replica"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "scale_model_name",
      "model_description",
      "location",
      "included_geographical_features",
      "included_biblical_sites"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
