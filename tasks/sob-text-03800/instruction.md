{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNaughty Dread: \"Naughty Dread\" is a hip-hop song by Kardinal Offishall.  It is his debut single, released in 1996 on Knee Deep Records, before being featured on the \"Rap Essentials Volume One\" compilation album.  The song contains a sample of \"Natty Dread\" by Bob Marley & The Wailers.  It earned him a Juno Award nomination for Best Rap Recording in 1997.\n\nNatty Dread: Natty Dread is a 1974 album by Bob Marley and the Wailers.  It was the first album released as Bob Marley and the Wailers instead of just the Wailers, the first recorded without Peter Tosh and Bunny Wailer, and the first recorded with the I Threes, a female vocal trio consisting of Marcia Griffiths, Judy Mowatt, and Marley's wife, Rita Marley.\n\nNo Woman, No Cry: \"No Woman, No Cry\" is a reggae song by Bob Marley and the Wailers.  The song first became known in 1974 through the studio album \"Natty Dread\".  The live version from the 1975 album \"Live! \" was released as a single and is the best known version — it was included on the greatest hits compilation \"Legend\" and was recorded at the Lyceum Theatre in London on July 19, 1975 as part of his \"Natty Dread Tour\".\n\nBob Marley Museum: The Bob Marley Museum is a museum in Kingston, Jamaica, dedicated to the reggae musician Bob Marley.  The museum is located at 56 Hope Road, Kingston 6, and is Bob Marley's former place of residence.  It was home to the Tuff Gong reggae record label which was founded by The Wailers in 1970.  In 1976, it was the site of a failed assassination attempt on Bob Marley.  The Chicago-based band 56 Hope Road takes its name in homage to the address.\n\nVincent Ford: Vincent Ford (c. 1940 – 28 December 2008), known as \"Tata\" or \"Tartar\", was a Jamaican songwriter best known for receiving writing credit for \"No Woman, No Cry\", the reggae song made famous by Bob Marley & The Wailers, as well as three other Bob Marley songs.  However, controversy persisted as to whether the compositions had actually been written by Marley himself, and had been credited to Ford to allow Marley to avoid contractual obligations, resulting in a legal battle that ended with the Marley estate being granted control of the songs.\n\nRebel Music (Bob Marley &amp; The Wailers album): Rebel Music is a compilation album by Bob Marley & The Wailers released by Island Records in 1986.  It consists of tracks drawn from such albums as Natty Dread, Rastaman Vibration, and Survival, as well as an exclusive remix of Rebel Music (3 O' Clock Road Block) and the first album appearance of 1977 B Side \"Roots\".  The album includes the hit singles \"So Much Trouble in the World\", \"War / No More Trouble\", and \"Get Up, Stand Up.\"  Some of the vinyl pressings include a looping sound at the end groove of side A.  The remastered edition of the CD features Wake Up And Live (Parts 1&2) as a bonus track.  Both parts had previously appeared on either side of a rare single in 1979, here they are mixed together to form one track.\n\nList of Bob Marley and the Wailers band members: Bob Marley and the Wailers were a Jamaican reggae band created by Bob Marley.  The band formed when self-taught musician Hubert Winston McIntosh (Peter Tosh) met Neville Livingston (Bunny Wailer), and Robert Nesta Marley (Bob Marley) in 1963 and taught them how to play guitar, keyboards, and percussion.  By late 1963 Junior Braithwaite, Beverley Kelso, and Cherry Smith had joined the Wailers.  After Peter Tosh and Bunny Wailer left the band in 1974, Bob Marley began touring with new band members.  His new backing band included brothers Carlton Barrett and Aston \"Family Man\" Barrett on drums and bass respectively, Junior Marvin and Al Anderson on lead guitar, Tyrone Downie and Earl \"Wya\" Lindo on keyboards, and Alvin \"Seeco\" Patterson on percussion.  The \"I Threes\", consisting of Judy Mowatt, Marcia Griffiths, and Marley's wife, Rita, provided backing vocals.\n\nBob Marley and the Wailers: Bob Marley and the Wailers were a Jamaican reggae band led by Bob Marley which developed from the earlier ska vocal group, the Wailers, created by Marley with Peter Tosh and Bunny Wailer in 1963.  By late 1963 singers Junior Braithwaite, Beverley Kelso, and Cherry Smith had joined the Wailers.  By the early 1970s, Marley and Bunny Wailer had learned to play some instruments and brothers Aston \"Family Man\" Barrett (bass) and Carlton Barrett (drums), had joined the band.  After Bunny Wailer and Peter Tosh left the band in 1974, Marley began touring with new band members.  His new backing band included the Barrett brothers, Junior Marvin and Al Anderson on lead guitar, Tyrone Downie and Earl \"Wya\" Lindo on keyboards, and Alvin \"Seeco\" Patterson on percussion.  The \"I Threes\", consisting of Judy Mowatt, Marcia Griffiths, and Marley's wife, Rita, provided backing vocals.\n\nNatty Dread Tour: The Natty Dread Tour was a concert tour organised to support the album \"Natty Dread\" by Bob Marley and the Wailers.\n\nOne Love/People Get Ready: \"One Love/People Get Ready\" is a reggae/rhythm and blues song by Bob Marley & The Wailers from their 1977 album \"Exodus\".  It was first recorded in a ska style by Marley's original group, The Wailers in 1965 and was released as a single.  This version was later included on their first singles compilation \"The Wailing Wailers\" in 1966.  It was rerecorded as part of the 1970 medley All In One, which contained reggae reworkings of their early ska songs.  This was released as a single and is also included on the compilation \"African Herbsman\" under the name \"All in One\".  The version on \"Exodus\" was not released as a single until 9 April 1984, promoting the forthcoming greatest hits album \"Legend\".  However, the single became one of his biggest hits and has been included on many of Marley and the Wailers subsequent compilation albums.\n\nQuestion: Who best known for receiving writing credit for a reggae song by Bob Marley and the Wailers that became known in 1974 through the studio album \"Natty Dread\" was also know by what name?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the person.\"\n    },\n    \"song_credited\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the song for which the person received writing credit.\"\n    },\n    \"album_known_through\": {\n      \"type\": \"string\",\n      \"description\": \"The studio album through which the song became known.\"\n    },\n    \"alternative_names\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other names or nicknames the person was known by.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"song_credited\",\n    \"album_known_through\",\n    \"alternative_names\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The full name of the person."
      },
      "song_credited": {
        "type": "string",
        "description": "The name of the song for which the person received writing credit."
      },
      "album_known_through": {
        "type": "string",
        "description": "The studio album through which the song became known."
      },
      "alternative_names": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other names or nicknames the person was known by."
      }
    },
    "required": [
      "person_name",
      "song_credited",
      "album_known_through",
      "alternative_names"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
