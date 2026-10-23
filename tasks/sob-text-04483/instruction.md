{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDino Borgioli: Dino Borgioli (February 15, 1891September 12, 1960) was an Italian lyric tenor.  Praised by critics for his musicianship, he was particularly associated with roles in operas composed by Mozart, Rossini, and Donizetti.\n\nElaine Malbin: Elaine Malbin (born May 24, 1932 in New York City) is an American soprano who had a prolific international career singing in operas, musicals, and concerts from 1949 through 1967.  She appeared in a number of Broadway productions in the 1940s and 1950s and notably portrayed Marsinah in the original 1953 West End production of \"Kismet\".  She was a regular at the New York City Opera during the 1950s and 1960s and appeared with most of America's leading opera companies during this time as well, including the Houston Grand Opera and the San Francisco Opera.  She also appeared in concert with several notable orchestras including the New York Philharmonic and the Philadelphia Orchestra.  On the International stage she appeared at a number of opera houses and major music festivals in the United Kingdom, Italy, and France.  She is perhaps best remembered for appearing in several opera roles live for television with the NBC Opera Theatre and for recording music with Mario Lanza for the 1951 film \"The Great Caruso\".\n\nLaura Harling: Laura Harling (born 21 March 1986) is a British actress, theatre producer and artist, who has played roles with the Royal Shakespeare Company and at the Royal Opera House.  She began as a child actor on stage, in films and on television.  After post-graduate training at the Drama Studio London, Harling has focused on stage and opera roles and producing.  In 2010 she co-founded First Draft Theatre, for which she is also Artistic Director.\n\nWolfgang Amadeus Mozart: Wolfgang Amadeus Mozart ( ; ; ] ; 27 January 1756 – 5 December 1791), baptised as Johannes Chrysostomus Wolfgangus Theophilus Mozart, was a prolific and influential composer of the Classical era.\n\nLucienne Bréval: Lucienne Bréval (4 November 1869 in Zürich – 15 August 1935 in Neuilly-sur-Seine) was a Swiss dramatic soprano who had a major international opera career from 1892-1918.  Although she appeared throughout Europe and in the United States, Bréval spent most of her career performing with the Opéra National de Paris where she became a greatly admired interpreter of French grand opera roles and Wagner heroines.  She also specialized in the works of Gluck and Rameau, becoming particularly associated with the title roles in Gluck’s \"Armide\" and Rameau's \"Hippolyte et Aricie\".  A favorite of the composers of her day, such as Massenet and Dukas, Bréval sang in numerous world premières during her career.\n\nDoña Croll: Doña Croll (born 29 August 1953) is a Jamaican-born British actress.  She is best known for her British soap opera roles as Pearl McHugh in Channel 5's \"Family Affairs\" and more recently as Vera Corrigan in the BBC soap opera \"Doctors\", and as Emerald Fox in the popular BBC soap opera, \"EastEnders\".\n\nLauren Flanigan: Lauren Flanigan (born May 18, 1959) is an American operatic soprano who has had an active international career since the 1980s.  She enjoyed a particularly fruitful partnership with the New York City Opera, appearing with the company almost every year since 1990.  She has sung more than 100 different opera roles on stage during her career, often appearing in contemporary works or more rarely staged operas. \" Opera News\" stated that, \"Flanigan has enjoyed one of the most distinctive careers of any artist of her generation, one marked by a high volume of contemporary works.  Modern composers love her because of her innate musicality, dramatic power and lightning-fast skills and instincts.\"\n\nJames Billings: James Billings (born 1932, Springfield, Missouri) is an American operatic baritone, librettist, and opera director.  He began his career in the late 1950s in Boston and later became a member of the New York City Opera where he performed regularly from the early 1970s through the 1990s.  A specialist in the comprimario repertoire, he has portrayed more than 175 opera roles on stage during his long career.  Billings has also written librettos for numerous operas for children and since the mid-1990s has directed several opera productions.\n\nMary Lou Fallis: Mary Lou Fallis {'1': \", '2': \", '3': \", '4': \"} (born April 22, 1948) is a Canadian opera singer.  She performs both serious opera roles and comedic shows as the character Primadonna, a satirical take on popular stereotypes of opera divas.\n\nLeonard Treash: Leonard Treash (January 1, 1909 in Pennsylvania - January 31, 1996 in Rochester, New York) was an American bass, opera director, and educator.  As a performer he sang leading opera roles throughout the United States under such conductors as Fritz Reiner, Leopold Stokowski, Artur Rodzinski, and Erich Leinsdorf.  He was particularly active as a performer with opera companies in Philadelphia, and is especially remembered as the long time director of the opera program at the Eastman School of Music, a post he held for nearly 30 years.  He also served as General Director of Chautauqua Opera for 10 seasons and was the first President of the National Opera Association from 1955-1956.\n\nQuestion: Dino Borgioli was associated with opera roles by which composer born January 27, 1756?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"composer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the composer.\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"description\": \"The birth date of the composer in YYYY-MM-DD format.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_date\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"performer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the performer.\"\n        },\n        \"association_type\": {\n          \"type\": \"string\",\n          \"description\": \"Describes the performer's association with the composer's roles.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"association_type\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"opera_roles_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the type of opera roles the performer was associated with.\"\n    }\n  },\n  \"required\": [\n    \"composer\",\n    \"performer\",\n    \"opera_roles_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "composer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the composer."
          },
          "birth_date": {
            "type": "string",
            "description": "The birth date of the composer in YYYY-MM-DD format."
          }
        },
        "required": [
          "name",
          "birth_date"
        ],
        "additionalProperties": false
      },
      "performer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the performer."
          },
          "association_type": {
            "type": "string",
            "description": "Describes the performer's association with the composer's roles."
          }
        },
        "required": [
          "name",
          "association_type"
        ],
        "additionalProperties": false
      },
      "opera_roles_description": {
        "type": "string",
        "description": "A description of the type of opera roles the performer was associated with."
      }
    },
    "required": [
      "composer",
      "performer",
      "opera_roles_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
