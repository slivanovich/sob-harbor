{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nX-Sinner: X-Sinner is an American hard rock band formed in 1988 by guitarist Greg Bishop.  The band is known for having a very similar sound to that of AC/DC, Kix and Def Leppard and has continued performing and releasing albums today.  Originating in the White Metal scene, the band has expanded their fan base into mainstream metal over the years with great success.  They were named the favorite new band of 1989 by the readers of \"HM Magazine\", and their debut album \"Get It\" was one of the most talked about albums within the white metal scene at the time.  Their first two albums were produced by John Elefante formerly of the band Kansas and released on Pakaderm Records, as well as on the mainstream A&M Records label of Hollywood.  They have released five full-length albums including the latest album \"A World Covered In Blood\" now on Image Records.  Experiencing a resurgence of interest with the release of \"World Covered In Blood\" in 2009/10, the band has gone on to perform in Europe recently as well as concerts in the U.S. and Canada.  The band has opened for many mainstream metal artists like Warrant and Paul Dianno as well as headlining and performing at rock festivals and performing concerts of their own.  The band has united with members of Rex's new side project GX for their live performances recently and have added that material to their live set list.  X-Sinner's album, \"Going Out With a Bang\", will be released track by track starting in 2014.\n\nRatt: Ratt is an American heavy metal band that had significant commercial success in the 1980s, with their albums having been certified as gold, platinum, and multi-platinum by the RIAA.  The group is perhaps best known for hit singles such as \"Round and Round\" and \"Lay It Down\", tracks that ranked on Billboard's top 40 at No. 12 and No. 40, respectively, as well as other songs such as \"Wanted Man\", \"You're in Love\" and \"Dance\".  Along with groups such as friendly rivals Mötley Crüe, Ratt has been recognized as instrumental in the formation of the early 1980s Los Angeles glam metal scene, also known as \"hair metal\" or \"pop metal\".\n\nHalfcocked: Halfcocked (also known as Half Cocked, Halfc*cked or Half-Cocked) was an American hard rock band.  Influenced by 1970s hard rock and punk rock, along with 1980s glam metal, they started out in Boston in 1997 and signed with independent label Curve of the Earth Records.  In 1999 the band placed third in the finals of the WBCN Rock & Roll Rumble, being the first \"wild card\" act to play in the finals.  They signed with DreamWorks imprint Megatronic Records (headed by Powerman 5000 frontman Spider One) and moved to Los Angeles in 2000.  After numerous delays, they released one final album—\"The Last Star\"—before splitting up.\n\nL.A. Guns: L.A. Guns are an American hard rock band from Los Angeles, California, formed in 1983.  As of 2017, the lineup consists of Phil Lewis (lead vocals, rhythm guitar), Tracii Guns (guitar), Michael Grant (guitar), Johnny Martin (bass, backing vocals) and Shane Fitzgibbon (drums).  The first incarnation of the group was formed by Tracii Guns in 1983 and merged with fellow Los Angeles group Hollywood Rose to form Guns N' Roses in 1984.  In 1985, the group was reformed by Guns and singer Paul Black adding Mick Cripps and Nickey Alexander.  Black would soon be replaced by former Girl singer Phil Lewis while former Faster Pussycat bassist Kelly Nickels was added to the group.  Later, Alexander would be replaced by former W.A.S.P. drummer Steve Riley with this being known as the \"classic lineup\" of L.A. Guns.  They achieved moderate chart success in the late 1980s and early 1990s.  However, the group went through numerous lineup changes (with Riley being the most consistent member) and failed to regain mainstream attention.\n\nTrixter: Trixter are an American hard rock band from Paramus, New Jersey.  The band achieved major success in the early 1990s but disbanded for several years as glam metal lost mainstream popularity.  The most recent lineup reunited in 2008 to tour and record new material.\n\nAccept (band): Accept is a German heavy metal band from the town of Solingen, originally assembled by former vocalist Udo Dirkschneider, guitarist Wolf Hoffmann and bassist Peter Baltes.  Their beginnings can be traced back to the late 1960s.  The band played an important role in the development of speed and thrash metal, being part of the German heavy metal scene, which emerged in the early to mid-1980s.  Accept achieved commercial success with their fifth studio album \"Balls to the Wall\" (1983), which is the band's only album to be certified gold in the United States and Canada, and spawned their well-known hit \"Balls to the Wall\".\n\nLive &amp; Learn (Vixen album): Live & Learn is the fourth studio album by American hard rock band Vixen.  This is the last album for founding member Jan Kuehnemund and the only one for the other members.\n\nWinger (band): Winger are an American rock band that has combined elements of glam metal and progressive metal.  Formed in New York City, Winger gained popularity during the late 1980s and early 1990s.  The band's two platinum albums, \"Winger\" and \"In the Heart of the Young\", along with charting singles \"Seventeen\", \"Headed for a Heartbreak\" and \"Miles Away\", put the band on the top of the charts by the early 1990s.  In 1990, the band was nominated for an American Music Award for \"Best New Heavy Metal Band\".  As the music scene changed in the early to mid-1990s due to the popularity of grunge, the band faded after their third release \"Pull\".\n\nVixen (band): Vixen are an American rock band.  They achieved commercial success during the late 1980s and early 1990s as part of the Los Angeles, California glam metal scene.\n\nThe Zeros (American glam punk band): The Zeros, originally known as The Double “O” Zeros, were a glam metal and glam punk band from Los Angeles, California.  Characterized by their matching purple hair, the band was a prominent figure on the Hollywood club scene of the late 1980s – early 1990s.  In 1991 the band’s record label Restless Records had the nightclubs Whisky a Go Go and Coconut Teaszer painted purple to commemorate the release of their album \"4-3-2-1 The Zeros\".\n\nQuestion: Live & Learn is the fourth studio album by which American hard rock band, that achieved commercial success during the late 1980s and early 1990s as part of the Los Angeles, California glam metal scene?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band.\"\n    },\n    \"album_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the album.\"\n    },\n    \"album_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of album (e.g., studio album).\"\n    },\n    \"album_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The sequential number of the album in the band's discography.\"\n    },\n    \"band_origin\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"country\": {\n          \"type\": \"string\"\n        },\n        \"city_state\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"country\",\n        \"city_state\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"genres\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Musical genres associated with the band.\"\n    },\n    \"commercial_success_period\": {\n      \"type\": \"string\",\n      \"description\": \"The period during which the band achieved commercial success.\"\n    },\n    \"associated_scenes\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Music scenes the band was part of.\"\n    }\n  },\n  \"required\": [\n    \"band_name\",\n    \"album_name\",\n    \"album_type\",\n    \"album_number\",\n    \"band_origin\",\n    \"genres\",\n    \"commercial_success_period\",\n    \"associated_scenes\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "band_name": {
        "type": "string",
        "description": "The name of the band."
      },
      "album_name": {
        "type": "string",
        "description": "The name of the album."
      },
      "album_type": {
        "type": "string",
        "description": "The type of album (e.g., studio album)."
      },
      "album_number": {
        "type": "integer",
        "description": "The sequential number of the album in the band's discography."
      },
      "band_origin": {
        "type": "object",
        "properties": {
          "country": {
            "type": "string"
          },
          "city_state": {
            "type": "string"
          }
        },
        "required": [
          "country",
          "city_state"
        ],
        "additionalProperties": false
      },
      "genres": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Musical genres associated with the band."
      },
      "commercial_success_period": {
        "type": "string",
        "description": "The period during which the band achieved commercial success."
      },
      "associated_scenes": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Music scenes the band was part of."
      }
    },
    "required": [
      "band_name",
      "album_name",
      "album_type",
      "album_number",
      "band_origin",
      "genres",
      "commercial_success_period",
      "associated_scenes"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
