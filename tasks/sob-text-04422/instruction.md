{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAdam Bravin: Adam Michael Bravin, also known as DJ Adam 12, is a musician and producer who is half of the darkwave duo She Wants Revenge.  He has also played in Crazy Town from 1995 to 1996, prior to DJ AM.  After She Wants Revenge, Bravin started working on his own solo project, Love Ecstasy Terror.  He has also been the personal DJ for President Barack Obama.\n\nShe Wants Revenge: She Wants Revenge is an American rock band, based in San Fernando Valley, California and formed in 2004.  The group's debut album \"She Wants Revenge\" was released in early 2006, with three singles to follow (\"These Things,\" a video featuring Shirley Manson from Garbage, \"Out of Control,\" and \"Tear You Apart\" for which the video was directed by Joaquin Phoenix).  The band has sold more than 300,000 records in the US.  The band's second album, \"This Is Forever\", was released in 2007.  The group's third album, entitled \"Valleyheart\", was released in 2011.\n\nIRIS Distribution: IRIS Distribution (Independent Recording Industry Services) - now The Orchard - is a digital music distribution and marketing firm based in San Francisco, CA and New York City.  Co-founded by Matt Laszuk (CEO), Bryn Boughton (CMO) and Eric Ferraro (General Counsel) in 2003, IRIS distributes digital music, ringtones, and video to over 450 digital retailers in over 85 countries.  It also promotes label catalogs through various outlets, including social networking sites, newsletters, and label profiles.  The company offers its technical, marketing, and legal services to a wide range of independent artists and labels from all genres.  Artists distributed by IRIS include She Wants Revenge, Le Tigre, Lou Reed, Mogwai, and many more.\n\nRevenge play: The revenge tragedy, or revenge play, is a dramatic genre in which the protagonist seeks revenge for an imagined or actual injury.  The term, revenge tragedy, was first introduced in 1900 by A.H. Thorndike to label a class of plays written in the late Elizabethan and early Jacobean eras (circa 1580s to 1620s).\n\nMichael Patterson (producer): Michael Patterson (b. Memphis, Tennessee) is an American record producer and mixer.  He has worked on the critically and commercially acclaimed albums \"Midnite Vultures\" (1999) by Beck (where he was nominated for a Grammy award), \"Life After Death\" (1997) by Notorious B.I.G, the debut album by Black Rebel Motorcycle Club, \"B.R.M.C.\" (2001), and dark pop duo She Wants Revenge's first two albums, \"She Wants Revenge\" and \"This Is Forever\".\n\nRevenge tragedy: Revenge tragedy (less commonly referred to as revenge drama, revenge play, or tragedy of blood) defines a genre of plays made popular in early modern England.  Ashley H. Thorndike formally established this genre in his seminal 1902 article \"The Relations of Hamlet to Contemporary Revenge Plays,\" which characterizes revenge tragedy \"as a tragedy whose leading motive is revenge and whose main action deals with the progress of this revenge, leading to the death of the murderers and often the death of the avenger himself.\"  Thomas Kyd's \"The Spanish Tragedy\" (c.1580s) is often considered the inaugural revenge tragedy on the early modern stage.  However, more recent research extends early modern revenge tragedy to the 1560s with poet and classicist Jasper Heywood's translations of Seneca at Oxford University, including \"Troas\" (1559), \"Thyestes\" (1560), and \"Hercules Furens\" (1561).  Additionally, Thomases Norton and Sackville's play \"Gorbuduc\" (1561) is considered an early revenge tragedy (almost twenty years prior to \"The Spanish Tragedy\").  Other well-known revenge tragedies include William Shakespeare's \"Hamlet\" (c.1599-1602) and \"Titus Andronicus\" (c.1588-1593) and Thomas Middleton's \"The Revenger's Tragedy\" (c.1606).\n\nFreeze the Atlantic: Freeze the Atlantic are an English alternative rock band based in Farnborough, Hampshire.  The band were formed in late 2008 by Guy Davis, Jon Pearce and Andy Gilmour following the hiatus of both Reuben and Hundred Reasons.  The group's name is taken from a song by English alternative rock band Cable from their 1997 album, \"When Animals Attack\".\n\nThe Spanish Tragedy: The Spanish Tragedy, or Hieronimo is Mad Again is an Elizabethan tragedy written by Thomas Kyd between 1582 and 1592.  Highly popular and influential in its time, \"The Spanish Tragedy\" established a new genre in English theatre, the revenge play or revenge tragedy.  Its plot contains several violent murders and includes as one of its characters a personification of Revenge.  \"The Spanish Tragedy\" was often referred to (or parodied) in works written by other Elizabethan playwrights, including William Shakespeare, Ben Jonson, and Christopher Marlowe.\n\nThis Is Forever: This Is Forever is the second full-length studio album by She Wants Revenge.  It was released on October 9, 2007.  The cover art replicates that of their debut, \"She Wants Revenge\", but with a black-themed twist: the model is wearing black underwear and a funeral veil, while the back cover reveals she's holding a black rose behind her back instead of a kitchen knife.\n\nShe Wants Revenge (album): She Wants Revenge is the debut studio album by American rock band She Wants Revenge.  Mixed by Michael Patterson, it was released on January 31, 2006 by Perfect Kiss, a subsidiary of Geffen Records.\n\nQuestion: Although they come from different countries, what genre of music do the bands Freeze the Atlantic and She Wants Revenge play?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"bands_involved\": {\n      \"type\": \"array\",\n      \"description\": \"Details of the bands mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"band_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the band.\"\n          },\n          \"country_of_origin\": {\n            \"type\": \"string\",\n            \"description\": \"The country where the band is based or from.\"\n          },\n          \"specific_genre\": {\n            \"type\": \"string\",\n            \"description\": \"The specific music genre of the band as stated in the context.\"\n          }\n        },\n        \"required\": [\n          \"band_name\",\n          \"country_of_origin\",\n          \"specific_genre\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"common_music_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The common overarching music genre shared by both bands.\"\n    },\n    \"genre_comparison_notes\": {\n      \"type\": \"string\",\n      \"description\": \"Notes on how the specific genres relate to the common genre to derive the answer.\"\n    }\n  },\n  \"required\": [\n    \"bands_involved\",\n    \"common_music_genre\",\n    \"genre_comparison_notes\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "bands_involved": {
        "type": "array",
        "description": "Details of the bands mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "band_name": {
              "type": "string",
              "description": "The name of the band."
            },
            "country_of_origin": {
              "type": "string",
              "description": "The country where the band is based or from."
            },
            "specific_genre": {
              "type": "string",
              "description": "The specific music genre of the band as stated in the context."
            }
          },
          "required": [
            "band_name",
            "country_of_origin",
            "specific_genre"
          ],
          "additionalProperties": false
        }
      },
      "common_music_genre": {
        "type": "string",
        "description": "The common overarching music genre shared by both bands."
      },
      "genre_comparison_notes": {
        "type": "string",
        "description": "Notes on how the specific genres relate to the common genre to derive the answer."
      }
    },
    "required": [
      "bands_involved",
      "common_music_genre",
      "genre_comparison_notes"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
