{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRosie Flores: Rosie Flores (born September 10, 1950 in San Antonio, Texas) is a rockabilly and country music artist.  Her music blends rockabilly, honky tonk, jazz, and Western swing along with traditional influences from her Tex-Mex heritage.  She currently resides in Austin, Texas, where August 31 was declared Rosie Flores Day by the Austin City Council in 2006.\n\nHarry Mathes: Harry A. Mathes (1882–1969) was an American painter in the New York art scene from the early 20th century until his death in 1969.  He was a graduate of the Chicago Art Institute.  He had additional training in Paris, London, Munich and Italy between the wars (and with Hans Hofmann).  He settled in New York City living most of his life in Greenwich Village and he was a frequent exhibitor at the Lynn Kottler and Pietrantonio galleries and at juried shows.  His stylistic repertoire encompassed post-impressionism, cubism and abstract expressionism.  Mathes had a lifetime membership in the New York Art Students' League, where he studied over several decades.  Pre-1950s colleagues include Sigmund Menkes, Yasuo Kuniyoshi, Nahum Tschacbasov, and others.  Midwestern artist Joe Jones credits Mathes for \"training\" him during a brief residence in St. Louis as one of the \"Blue Lantern\" waterfront group in the early 1920s.  Mathes was reviewed in the New York Times and the Herald Tribune, and is listed in Who Was Who in American Art.  The recipient of numerous awards and prizes, he was photographed by Paul Juley in the 1950s and 60s and exhibited at the National Museum of American Art as part of the Peter Juley and Son Collection documenting American artists, which currently resides in the archive of the Museum of American Art, the Smithsonian Institution.\n\nOnly Girl (In the World): \"Only Girl (In the World)\" is a song by Barbadian singer Rihanna from her fifth album, \"Loud\" (2010).  The album's lead single, it was released on September 10.  Crystal Johnson wrote the song in collaboration with producers Stargate and Sandy Vee.  Rihanna contacted Stargate before \"Loud\"'s production and asked them to create lively, uptempo music.  \"Only Girl (In the World)\" was the first song composed for the album, and the singer decided to include it on the track list before she recorded her vocals.  Backed by strong bass and synthesizer, it is a eurodance song that incorporates elements of hi-NRG, rave and R&B in its composition.  In its lyrics, Rihanna demands physical attention from her lover.\n\nSoul Khan: Noah Weston, better known as Soul Khan (born April 18, 1985) is an American songwriter, rapper, and retired battle rapper.  Born in West Hollywood and raised in Woodland Hills, California, he currently resides in Brooklyn, New York City.  After a short career in battle rap that started in late 2008, in which he appeared in American circuits such as Grindtime and Smack/URL, as well as outside the United States, notably in Canada (KOTD) and United Kingdom (Don't Flop), he retired from the scene to focus his attention on his musical career in early 2010.  He is a member of the Brown Bag AllStars, a collective of emcees and producers from the Brooklyn area.\n\nGeorge Cartwright (musician): George Cartwright (born December 10, 1950, in Midnight, Mississippi) is an American musician, best known as the founder of the band Curlew in 1979 in New York City.  Besides playing soprano, alto, and tenor saxophones, he has composed music for Curlew, his own solo recordings and other music ensembles such as Zeitgeist.  He attended the Creative Music Studio in Woodstock, New York, and currently resides in Minnesota.\n\nSandy Vee: Sandy Julien Wilhelm (born 22 April 1975) better known by his stage name Sandy Vee, is a French music producer and songwriter.  He gained much commercial and critical recognition for co-producing Rihanna’s \"Only Girl (In the World)\", Katy Perry's “Firework”, and 8 songs on the David Guetta album One Love.  He originally played bass in a variety of jazz, rock, and punk bands before gaining exposure to the underground DJ scene in France.  He currently resides in New York City.\n\nMatty Goldberg: He went to Onteora Central School in New York.  He was diagnosed at the age of 20 with a brain tumor, after which he had to learn how to walk again (he has lost complete control of one-half of his body as a result of the brain tumor).  He went to State University of New York at Purchase and dropped out.  In 2002 he started doing comedy in New York City.  He had his TV debut in 2006 on BET's \"106 and Park.\"  He also did an ad campaign in 2009 for Converse with Dwyane Wade as billionaire Charles Charles MaGalls.  He currently resides in Los Angeles.\n\nFoley Stewart: Foley Stewart is an American singer-songwriter, born and raised in the Lower East Side of New York City; he currently resides and regularly plays shows in New York City.\n\nAnn Chernow: Ann Chernow, née Levy (born February 1, 1936 in New York City) is an American artist who is known for her portrait-style illustrations that evoke the images of female cinematic figures of the 1930s and 1940s.  Born and raised in New York City, Chernow studied music and art from a young age and acquired an affinity for the arts.  Chernow was exposed to several movies that left a lasting impression and prompted her to make the likenesses of leading ladies.  Bette Davis, Joan Crawford, Norma Shearer and Katharine Hepburn were the subjects of some of her works in the late 1990s.  In most of her works, however, Chernow avoids specificity, choosing instead to portray universal situations through figures who are inspired by film but reinterpreted to transcend stereotypes.  Chernow has worked extensively in the mediums of lithography, silkscreen, etching, and colored pencil.  She currently resides in Westport, Connecticut, and serves her community through the arts.\n\nJohn Adikes Bond: John Adikes Bond is an author, attorney, poker player, political activist and real estate developer born in Jamaica, New York January 14, 1955.  He grew up in Massapequa and Port Washington, New York before moving to South Florida in 1972.  He currently resides between Dania Beach, Florida and Andros Island, the Bahamas.  He is the eldest of five children; his brother James Alexander Bond is a theatre director in New York City.\n\nQuestion: What song, co-produced by a man who currently resides in New York City, released on September 10 and in the song Rihanna demands physical attention from her lover?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"artist\": {\n      \"type\": \"string\",\n      \"description\": \"The main artist of the song.\"\n    },\n    \"release_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"month\": {\n          \"type\": \"string\",\n          \"description\": \"The month the song was released.\"\n        },\n        \"day\": {\n          \"type\": \"integer\",\n          \"description\": \"The day of the month the song was released.\"\n        }\n      },\n      \"required\": [\n        \"month\",\n        \"day\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"producer_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the co-producer.\"\n        },\n        \"current_residence_city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the co-producer currently resides.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"current_residence_city\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"lyrical_content_summary\": {\n      \"type\": \"string\",\n      \"description\": \"A summary of the song's lyrical theme.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"artist\",\n    \"release_details\",\n    \"producer_details\",\n    \"lyrical_content_summary\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "artist": {
        "type": "string",
        "description": "The main artist of the song."
      },
      "release_details": {
        "type": "object",
        "properties": {
          "month": {
            "type": "string",
            "description": "The month the song was released."
          },
          "day": {
            "type": "integer",
            "description": "The day of the month the song was released."
          }
        },
        "required": [
          "month",
          "day"
        ],
        "additionalProperties": false
      },
      "producer_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the co-producer."
          },
          "current_residence_city": {
            "type": "string",
            "description": "The city where the co-producer currently resides."
          }
        },
        "required": [
          "name",
          "current_residence_city"
        ],
        "additionalProperties": false
      },
      "lyrical_content_summary": {
        "type": "string",
        "description": "A summary of the song's lyrical theme."
      }
    },
    "required": [
      "song_title",
      "artist",
      "release_details",
      "producer_details",
      "lyrical_content_summary"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
