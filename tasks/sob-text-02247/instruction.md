{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHood Billionaire: Hood Billionaire is the seventh studio album by American hip hop recording artist Rick Ross.  The album was released through Maybach Music Group, Def Jam Recordings and Slip-n-Slide Records on November 24, 2014.  The album features guest appearances from Jay-Z, K. Michelle, French Montana, Project Pat, Yo Gotti, Boosie Badazz, Big K.R.I.T., Whole Slab, R. Kelly, and Snoop Dogg.  The album was supported by the singles \"Elvis Presley Blvd.\", \"Keep Doin' That (Rich Bitch)\" and \"Nickel Rock\".\n\nBoosie Badazz discography: The discography of Boosie Badazz, an American rapper.\n\nSharp On All 4 Corners: Corner 1: Sharp On All 4 Corners: Corner 1 is the twenty first studio album by American rapper E-40.  The album was released on December 9, 2014, by Heavy on the Grind Entertainment.  The album features guest appearances from Boosie Badazz, T-Pain, Kid Ink, B.o.B, Turf Talk, Cousin Fik, Ezale, Vell, Adrian Marcel, Willie Joe, Nef the Pharaoh, Too Short, B-Legit and Otis & Shug.  The album was supported by the singles \"Red Cup\" and \"Choices (Yup)\".\n\nBoosie Badazz: Torrence Hatch (born November 14, 1982), known professionally as Boosie Badazz (formerly known as Lil Boosie), is an American rapper from Baton Rouge, Louisiana.  Hatch was bestowed the nickname Boosie by his family, and he was raised in Southside Baton Rouge.  As Boosie, he has released numerous regular studio albums while also contributing to a number of mixtapes and compilations.\n\nTouch Down 2 Cause Hell: Touch Down 2 Cause Hell is the sixth studio album by American rapper Boosie Badazz.  The album was released on May 26, 2015, by Trill Entertainment, Bad Azz and Atlantic Records.\n\nLil B.I.G. Pac: Lil B.I.G. Pac is the fourth mixtape by American rapper Kodak Black.  It was released on June 11, 2016, by Dollaz N Dealz Entertainment and Sniper Gang.  The mixtape features guest appearances from rappers Gucci Mane, Boosie Badazz and PnB Rock.\n\nSeen It All: The Autobiography: Seen It All: The Autobiography is the fifth studio album by American rapper Jeezy.  The album was released on September 2, 2014, through CTE World and Def Jam Recordings.  The production was handled by several Southern hip hop producers, namely Drumma Boy, Mike Will Made It and Childish Major, among others.  It features guest appearances from Jay-Z, Future, Rick Ross, The Game, Lil Boosie, August Alsina and Akon.\n\nI Changed a Lot: I Changed a Lot is the eighth studio album by DJ Khaled.  It was released on October 23, 2015, by We the Best Music Group and RED Distribution.  Recording sessions took place during 2014 to 2015, with its production by Khaled, along with The Beat Bully, Lee on the Beats, Danja, Bkorn and The Mekanics, as well as guest appearances from Future, Rick Ross, Boosie Badazz, Jeezy, Chris Brown, August Alsina, Fetty Wap, Yo Gotti, Trick Daddy, French Montana, Meek Mill, Beanie Sigel, Jadakiss, Lil Wayne, Big Sean.  Trey Songz, Jeremih, Ace Hood, Vado, Jay-Z, Mavado, John Legend, Usher and Fabolous.\n\nCardiak: Carl McCormick (born June 26, 1989), professionally known as Cardiak, is an American record producer from Willingboro Township, New Jersey.  He began producing music in 2008.  Cardiak is widely known for his work with closely associated artists such as Ace Hood, J. Cole, Drake, Joe Budden, G-Unit/lloyd Banks, Freeway, DJ Khaled, Rick Ross, Meek Mill, Trina, Red Cafe, Boosie Badazz, Wale, Fabolous, D-Block, Dr. Dre, among others.\n\nThe Kanan Tape: The Kanan Tape is the eleventh mixtape by American rapper 50 Cent.  Released on December 9, 2015 via his community website \"ThisIs50\" and on Datpiff as a free download.  The mixtape features guest appearances from American rappers Boosie Badazz, Young Buck and Post Malone, featuring production from Sonny Digital, London on da Track and The Alchemist, among others.\n\nQuestion: what does Seen It All: The Autobiography and Boosie Badazz have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"common_ground_description\": {\n      \"type\": \"string\",\n      \"description\": \"A summary of what Boosie Badazz and the album 'Seen It All: The Autobiography' have in common.\"\n    },\n    \"boosie_badazz_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"artist_name\": {\n          \"type\": \"string\",\n          \"description\": \"The professional name of the artist Boosie Badazz.\"\n        },\n        \"artist_nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of Boosie Badazz.\"\n        },\n        \"artist_genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of music Boosie Badazz performs.\"\n        }\n      },\n      \"required\": [\n        \"artist_name\",\n        \"artist_nationality\",\n        \"artist_genre\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"album_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"album_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the album.\"\n        },\n        \"primary_artist_name\": {\n          \"type\": \"string\",\n          \"description\": \"The primary artist of the album.\"\n        },\n        \"primary_artist_nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the album's primary artist.\"\n        },\n        \"primary_artist_genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of music the album's primary artist performs.\"\n        },\n        \"is_boosie_badazz_featured\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if Boosie Badazz is a featured artist on the album.\"\n        },\n        \"featured_as_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name under which Boosie Badazz was featured on the album.\"\n        }\n      },\n      \"required\": [\n        \"album_title\",\n        \"primary_artist_name\",\n        \"primary_artist_nationality\",\n        \"primary_artist_genre\",\n        \"is_boosie_badazz_featured\",\n        \"featured_as_name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"common_ground_description\",\n    \"boosie_badazz_details\",\n    \"album_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "common_ground_description": {
        "type": "string",
        "description": "A summary of what Boosie Badazz and the album 'Seen It All: The Autobiography' have in common."
      },
      "boosie_badazz_details": {
        "type": "object",
        "properties": {
          "artist_name": {
            "type": "string",
            "description": "The professional name of the artist Boosie Badazz."
          },
          "artist_nationality": {
            "type": "string",
            "description": "The nationality of Boosie Badazz."
          },
          "artist_genre": {
            "type": "string",
            "description": "The genre of music Boosie Badazz performs."
          }
        },
        "required": [
          "artist_name",
          "artist_nationality",
          "artist_genre"
        ],
        "additionalProperties": false
      },
      "album_details": {
        "type": "object",
        "properties": {
          "album_title": {
            "type": "string",
            "description": "The title of the album."
          },
          "primary_artist_name": {
            "type": "string",
            "description": "The primary artist of the album."
          },
          "primary_artist_nationality": {
            "type": "string",
            "description": "The nationality of the album's primary artist."
          },
          "primary_artist_genre": {
            "type": "string",
            "description": "The genre of music the album's primary artist performs."
          },
          "is_boosie_badazz_featured": {
            "type": "boolean",
            "description": "Indicates if Boosie Badazz is a featured artist on the album."
          },
          "featured_as_name": {
            "type": "string",
            "description": "The name under which Boosie Badazz was featured on the album."
          }
        },
        "required": [
          "album_title",
          "primary_artist_name",
          "primary_artist_nationality",
          "primary_artist_genre",
          "is_boosie_badazz_featured",
          "featured_as_name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "common_ground_description",
      "boosie_badazz_details",
      "album_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
