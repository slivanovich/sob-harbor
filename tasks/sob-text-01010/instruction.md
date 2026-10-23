{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nStewart Sukuma: Luis Pereira (born in 1963), known as Stewart Sukuma, is a Mozambican singer.  His stage name – Stewart Sukuma – means 'Rise Up' in Zulu and 'Push' in Swahili.  He was born in Cuamba, Niassa Province in Mozambique.  Coming from a modest family he soon realised his passion for music and in 1977 he moved to the capital Maputo, where he learned how to play percussion, guitar and piano.  In 1982 he joined a music group as a vocalist.  He won the Mozambican prize for music – Ngoma – in 1983 and soon became one of the most played singers in the national radio stations of Mozambique, being described as \"Mozambique's most popular male vocalist\".  His major works include songs such as Felizminha, Xitchuketa Marrabenta, Sumanga, Male and Why and he sings in languages including Portuguese, English, Swahili, Echwabo, Coti, and Tsonga.\n\nRonny Thorsen: Ronny Thorsen (born 3 January 1978 in Kristiansand, Vest-Agder, Norway) is a Norwegian vocalist most notable for being the harsh vocalist, lyricist, and formerly the only constant member of the band Trail of Tears, until he left the band in 2013.  He has also been a session vocalist for the bands Blood Red Throne and Scariot and was a guest for the band Tristania.  For the 2005 Napalm Awards for Napalm Records, Ronny Thorsen placed third in the categories of Artist of the Year and Best Male Vocalist.\n\nMike Mattison: Mike Mattison is an American musician and vocalist of the Grammy Award-winning blues rock/soul group, the Tedeschi Trucks Band, as well as lead vocalist and co-founder of the blues rock trio Scrapomatic.  Mattison's vocal sound has been described as \"strong,\" with an \"expressive blues voice\".  As lead vocalist of Scrapomatic, he picked up a nomination for Minnesota Music Awards best male vocalist, and both he and co-founder Paul Olsen were also nominated for best R&B Group.  Mattison was previously the lead vocalist of the Grammy Award winning Derek Trucks Band and has been a main songwriter of all three bands.  He is also an active essayist who publishes on music and poetry.  Since 2013 Mattison and Ernest Suarez have edited “Hot Rocks: Songs and Verse,” an ongoing feature in Five Points: A Journal of Literature and Art.\n\nRydell &amp; Quick: Rydell & Quick is a Swedish rock band featuring male vocalist Christer Rydell and female vocalist and saxophonist Malin Quick.  Rydell had formed a band with Peer Stappe, Rydell Rip Offs, playing locally, while Quick performed with big bands.  The band was originally formed in 1989 after Quick joined Rydell's band on stage with her instrument.  The band has toured extensively around Sweden and since 1999 are sponsored by Harley-Davidson.  The band also features two drummers Berndt Baumgartner and Peer Stappe and the bass player Jonas Bonnier.  The band has released two albums, \"R.O.C.K.O.H.O.L.I.C\" (2006) and \"R.O.A.D.T.R.I.P.\"(2012).  Their first album was described as \" catchy, feel-good, melodic hard rock\".  Both are from the Västra Götaland area of Sweden and live in Borås.\n\nChrigel Glanzmann: Christian \"Chrigel\" Glanzmann (born January 1, 1975) is the male lead vocalist in the folk metal band Eluveitie.  He also plays mandola, whistles, and bagpipes in Branâ Keternâ.  He was born in Basel, Switzerland, as Christian Oliver Ivan Glanzmann.\n\nEluveitie: Eluveitie ( ) is a Swiss folk metal band from Winterthur, Zurich, founded in 2002 by Chrigel Glanzmann.  The project's first EP, \"Vên\", was released in 2003.  \"Vên\" was a studio project of Glanzmann's, but its success led to the recruitment of a full band.  The band then released a full-length album, \"Spirit\", in June 2006.  In November 2007, Eluveitie was signed by Nuclear Blast.  The group rose to fame following the release of their first major-label album, \"Slania\", in February 2008.  The album peaked at number 35 in the Swiss charts and number 72 in the German charts.\n\nDa Mouth: Da Mouth () was a Taiwanese hip hop band made up of MC40, DJ Chung Hua, male vocalist Harry, and female vocalist Aisa.  They were formed in 2007 and disbanded in 2016.  They are considered the Asian The Black Eyed Peas due to the group's diversity.  The band's Chinese band name directly translates into \"big mouth\".  Their English band name is derived from the concatenation of the Chinese character for \"big\" 大, which when romanized using pinyin becomes \"dà\", and the translation of the second half of their Chinese band name.  They released their self-titled debut album \"Da Mouth\" on 16 November 2007.\n\nNightwish discography: The discography of the Finnish symphonic metal band Nightwish consists of eight studio albums, one extended play, four live albums, seven compilations, thirteen music videos and twenty one singles.  The band was formed in 1996 by songwriter and keyboardist Tuomas Holopainen, guitarist Emppu Vuorinen, and former vocalist Tarja Turunen; Nightwish's current line-up has six members although Turunen has been replaced by Anette Olzon, and the original bassist, Sami Vänskä, has been replaced by Marco Hietala, who also took over the male vocalist part.  Olzon left the band in 2012 and was replaced by Floor Jansen.\n\nUndish: Undish was a Christian gothic metal band from Oborniki, Poland, formed in 1991.  Undish is led by female vocalist Ada Szarata as well as a male vocalist named Robert Baum who is also handling the drums.  After the release of their first album, \"...Acta Est Fabula\", on Massacre Records, they toured Europe in August 1997 together with Saviour Machine and Theatre of Tragedy, and performed at Wacken Open Air.  Their second album, \"Letters from the Earth\", was released on Morbid Noizz Productions.  The band was planning to record a third album entitled \"A Gift of Flying\" in 2003 but its release was delayed until 2005 when it was released on CL Productions.\n\nMarco Hietala: Marko Tapani \"Marco\" Hietala (born 14 January 1966) is a Finnish heavy metal vocalist, bass guitarist and songwriter.  Internationally, he is most known as the current bass guitarist, male vocalist and secondary composer to Tuomas Holopainen, of the symphonic metal band Nightwish.  He is also the vocalist and bassist as well as composer and lyricist for the heavy metal band Tarot.\n\nQuestion: This band was founded in 2002 by a male vocalist who was born where?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band.\"\n    },\n    \"founding_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the band was founded.\"\n    },\n    \"founder_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"founder_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the band's founder.\"\n        },\n        \"founder_role\": {\n          \"type\": \"string\",\n          \"description\": \"The primary role of the founder in the band.\"\n        },\n        \"birth_location\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"city\": {\n              \"type\": \"string\",\n              \"description\": \"The city where the founder was born.\"\n            },\n            \"country\": {\n              \"type\": \"string\",\n              \"description\": \"The country where the founder was born.\"\n            }\n          },\n          \"required\": [\n            \"city\",\n            \"country\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"founder_name\",\n        \"founder_role\",\n        \"birth_location\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"band_name\",\n    \"founding_year\",\n    \"founder_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "band_name": {
        "type": "string",
        "description": "The name of the band."
      },
      "founding_year": {
        "type": "integer",
        "description": "The year the band was founded."
      },
      "founder_details": {
        "type": "object",
        "properties": {
          "founder_name": {
            "type": "string",
            "description": "The name of the band's founder."
          },
          "founder_role": {
            "type": "string",
            "description": "The primary role of the founder in the band."
          },
          "birth_location": {
            "type": "object",
            "properties": {
              "city": {
                "type": "string",
                "description": "The city where the founder was born."
              },
              "country": {
                "type": "string",
                "description": "The country where the founder was born."
              }
            },
            "required": [
              "city",
              "country"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "founder_name",
          "founder_role",
          "birth_location"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "band_name",
      "founding_year",
      "founder_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
