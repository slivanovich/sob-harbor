{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBlackhouse Records: Blackhouse Records is a Coeur d'Alene, Idaho-based independent record label founded by Moral Crux and Scatterbox drummer Scott Rozell and Tony Shields.  The label was originally \"just a logo and a P.O. box\" created in 2001 for the purpose of selling Scatterbox records, but has evolved into a moderate-sized independent record label.  Throughout the 2000s most of the bands on Blackhouse were punk and pop punk groups, while there are many Metal and Rap artists signed to the label as well.  A sister-label also exists, Totally Fucked, that have signed noise and grindcore bands.\n\nEOne Music discography: The E1 Discography has produced more Billboard hits than any other independent record label.  Entertainment One Music was known as Koch Records from its founding in 1987, until 2009, when it was re-branded.  In its early years, the record label signed many country, classical and rock acts, including artists Ringo Starr, Joan Baez, Chris Brubeck and Bob James.  In the early 2000s, the label began to sign more hip hop acts and made deals with hip hop labels, releasing records by 2Pac, Tha Dogg Pound, Kurupt, Daz Dillinger and Gangsta Advisory.  E1 Music has had over 100 albums chart on the Billboard Independent chart and is the largest independently owned record label in the United States.\n\nFlying Tart: Flying Tart was an independent record label based in Nashville, Tennessee.  It was started by Alex Parker, formerly of R.E.X. Records, and operated from 1990 until 1996 when it was purchased by Light Records.\n\nEpitaph Records: Epitaph Records is a Hollywood-based independent record label owned by Bad Religion guitarist Brett Gurewitz.  The label was originally \"just a logo and a P.O. box\" created in the 1980s for the purpose of selling Bad Religion records, but has evolved into a large independent record label.  Gurewitz took the name from a King Crimson song of the same name.  Throughout the 1980s and 1990s most of the bands on Epitaph were punk and pop punk groups, while there are many post-hardcore and bands signed to the label as well.  A large portion of the record label, known as Hellcat Records, is owned by Tim Armstrong, frontman of the punk rock band Rancid.  Several sister-labels also exist, such as ANTI-, Burning Heart Records, Fat Possum Records, Hellcat Records and Heart & Skull Records that have signed other types of bands.  The label has recently been added to the Forza Horizon franchise as a radio station.\n\nHer Royal Majesty's Records: Her Royal Majesty's Records (HRMR) is a Canadian independent record label founded in Vancouver in 1995 by Bif Naked and Peter Karroll and managed by Peter Karroll.  Originally HRM Records was created to be a home for Bif Naked's music after Plum Records folded up shop after the release of Bif Naked's self-titled release.  Peter Karroll licensed Bif's songs to many major labels and did co-venture music projects including mixing and recording tracks for Films and Television.  Peter Karroll co-wrote, produced and mixed many successful tracks including Platinum and Gold selling albums and singles with Bif Naked.  In 2005 Peter Karroll merged the music label with Bodog to create Bodog Music and Bodog Entertainment.  Her Royal Majesty's Records was the backbone of the Bodog entertainment juggernaut and combined with the Artist Management company TKO Entertainment Corp the Bodog Entertainment entity produced over 150 Network Television shows in the USA and licensed in many countries.  As well live events on In Demand and music television programing on the Fuse Network all contributed to the overall success of Bodog Entertainment.  In 2008 the entertainment companies were unmerged and Peter Karroll moved forward more albums with Bif Naked and DMX the American rap / hip hop superstar.  During the Bodog Era Peter signed and released the Legendary Hip Hop group the WuTang Clan.  Thousands of Live events were produced with the Artists from HRMR / Bodog with them touring extensively on major festivals and tours such as Warped Tour, Family Values, Rock Am Ring, Rock Am Park, Hultsfred Festival Bif Naked's largest attendance in the headline position was 2011 in Cloverdale BC where she performed in front of 110,000 estimated audience.\n\nSherie Rene Scott: Sherie Rene Scott (born February 8, 1967) is an American actress, singer, writer and producer.  She is a co-founder of Grammy Award-winning Sh-K-Boom Records and Ghost light Records.  She has also been seen in multiple Off-Broadway and Broadway musicals/plays, and appears on numerous solo and original cast recordings.\n\nDawkins &amp; Dawkins: Dawkins & Dawkins is an American gospel music and Christian R&B duo from Davenport, Iowa, who are currently signed to Light Records, a division of Entertainment One Music.  The group consist of two brothers, Anson Dawkins and Eric Dawkins.  The first album, \"Dawkins & Dawkins\", was released in 1993 by A&M Records.  This was the only record released with the label.  Their second album, \"Necessary Measures\", released in 1994 by CGI Records.  The third album, \"Focus\", was released by Harmony Records in 1998.  This album was their breakthrough release on the \"Billboard\" charts, by placing on the Gospel Albums chart.  They released, \"From Now On\", in 2011 with Light Records a division of Entertainment One Music.  The album placed on the Gospel Albums chart along with the Independent Albums chart.\n\nSh-K-Boom Records: Sh-K-Boom Records is an independent record label and producer of recorded and live entertainment, which was founded in 2000 by husband and wife Kurt Deutsch and Sherie Rene Scott with the mission of bridging the gap between pop music and theater.  In 2004 Sh-K-Boom created their second imprint, Ghostlight Records, dedicated to the preservation of traditional musical theater, spurred by the popular release of their first-ever show cast recording, Jason Robert Brown's \"The Last Five Years\".  Together the two labels have over 150 albums in their catalogues.  The company has also produced over 50 live concerts as part of their Sh-K-Boom Room Concert Series, and are currently developing new and innovative projects for the stage and screen.\n\nFaultline Records: Faultline Entertainment Group also known as Faultline Records is an Australian independent record label based in Melbourne.  It was founded in 1998 by metal music producer, dw Norton, and began as a development label.  As of 2007 it has taken on partners Richard De Silva and Gary Buckley to become a full-time independent record label within Australian and Overseas.  Faultline Entertainment Group has opened an office in Florida and in the near future will be opening offices in the UK and Japan.  Distribution for Faultline releases within Australia are handled by both Shock Records and MGM Distribution.\n\nPattie Howard: Pattie Howard (born Francine Patience Howard, April 12, Cleveland, Ohio, United States) is an American Gospel and R&B Singer-Songwriter, Producer, Composer and Vocal Arranger.  She is a music industry veteran who has released two albums with major record labels, RCA Records and Light Records.  Howard, who owns her own full service entertainment company, PH Balanced Music, is also known for singing background for many major artists including Whitney Houston, Gladys Knight, Brandy, Mary J Blige, Fantasia, Queen LaTifah, Madonna, Andrae Crouch, Michael Jackson, Curtis Siger, Lisa Stanfield, BeBe and CeCe Winans, Reba Rambo,and Diana Ross.  She has dozens of gold and platinum albums to her credits encompassing artists from almost every genre.  Howard landed one of her most profound gigs traveling the world with Whitney Houstonfrom 1992-2001, at the height of her career, The Bodyguard Era.  During the early 2000s, Howard returned to songwriting, music production, mixing, and mastering and is currently singing (solo & background), composing, arranging and producing various artists/bands.  In 2016 Pattie released 2 singles through her record label PH Balanced Music.  \"Jesus Is His Name\" introduces Pattie's daughter Shekinah Nicole Howard in a contemporary gospel duet produced by Wow Jones and co produced by Pattie Howard.  The second single titled \"Feel Me, Heal Me\" was also Produced by Wow Jones, written and arranged by Pattie Howard.\n\nQuestion: Sh-K-Boom Records is an independent record label and producer of recorded and live entertainment, which was founded in 2000 by husband and wife Kurt Deutsch and which American actress, singer, writer and producer, and co-founder of Ghost light Records?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"record_label_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the record label in question.\"\n    },\n    \"co_founder_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the co-founder.\"\n        },\n        \"roles\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Professional roles of the co-founder.\"\n        },\n        \"other_founded_labels\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Other record labels co-founded by this person.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"roles\",\n        \"other_founded_labels\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"founding_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the record label was founded.\"\n    }\n  },\n  \"required\": [\n    \"record_label_name\",\n    \"co_founder_details\",\n    \"founding_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "record_label_name": {
        "type": "string",
        "description": "The name of the record label in question."
      },
      "co_founder_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the co-founder."
          },
          "roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Professional roles of the co-founder."
          },
          "other_founded_labels": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Other record labels co-founded by this person."
          }
        },
        "required": [
          "name",
          "roles",
          "other_founded_labels"
        ],
        "additionalProperties": false
      },
      "founding_year": {
        "type": "integer",
        "description": "The year the record label was founded."
      }
    },
    "required": [
      "record_label_name",
      "co_founder_details",
      "founding_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
