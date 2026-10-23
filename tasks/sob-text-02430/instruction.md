{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBlack Rose (UK band): Black Rose are an English heavy metal band from Teesside in the north east of England.  They formed in 1976 under the name ICE but changed it to Black Rose in 1980 and were one of many British bands considered part of the new wave of British heavy metal movement.  The original line up was Steve Bardsley (lead vocals/guitar), Kenny Nicholson (guitar), Marty Rajn (bass) and Mark Eason (drums).  Over the next nine years the band went through various line up changes and released quite a few records including two albums: \"Boys Will Be Boys\" (1984) and \"Walk It How You Talk It\" (1986) before splitting up in 1989.  The band then reformed in 2006 and released their newest album \"Cure for Your Disease\" in 2010.\n\nWelcome to Hell: Welcome to Hell is the debut studio album by English heavy metal band Venom.  It was released in December 1981, through Neat Records, at the culmination of the new wave of British heavy metal movement.  The music of \"Welcome to Hell\" is often described as speed metal, but it had a great influence on the then-emerging thrash metal style, and crystallised the elements of what later became known as death metal and black metal.\n\nSaxon (band): Saxon are an English heavy metal band formed in 1977, in South Yorkshire.  As one of the leaders of the new wave of British heavy metal, they had eight UK Top 40 albums in the 1980s including four UK Top 10 albums and two Top 5 albums.  The band also had numerous singles in the UK Singles Chart and chart success all over Europe and Japan, as well as success in the US.  During the 1980s Saxon established themselves as one of Europe's biggest metal acts.  The band tours regularly and have sold more than 15 million albums worldwide.  They are considered one of the classic metal acts and have influenced many bands such as Metallica, Mötley Crüe, Pantera, Sodom.\n\nDiamond Head (band): Diamond Head are an English heavy metal band formed in 1976 in Stourbridge, England.  The band is recognised as one of the leading members of the new wave of British heavy metal movement and is acknowledged by thrash metal bands such as Metallica and Megadeth as an important early influence.\n\nArtch: Artch is a heavy metal band from Sarpsborg in Norway.  Initially formed in 1983 by guitarist Cato André Olsen and bass player Bernt Jansen, in 1984 guitarist Geir Nilssen, drummer Jørn Jamissen and vocalist Lars Fladeby all joined the band but they had formerly been with a local rock group called Oxygen.  Espen Hoff replaced Mr. Fladeby as lead singer in 1985 but he died in a motorcycle accident later that same year and was replaced by Eiríkur Hauksson in 1986.  Artch released two albums on USA label Metal Blade that got great reviews, especially in the English heavy metal press, but sales were disappointing.  Drummer Jamissen left the band in 1991 and was replaced by Gudmund Bolsgård.  They reformed in 2000 after a prolonged period of inactivity.\n\nJaguar (band): Jaguar are an English heavy metal band, formed in Bristol, England, in December 1979.  They had moderate success throughout Europe and Asia in the early 1980s, during the heyday of the new wave of British heavy metal movement.\n\nBlack Metal (Venom album): Black Metal is the second album by English heavy metal band Venom.  It was released in November 1982, during the great flourishing of metal music in the UK that was the new wave of British heavy metal, and is considered a major influence on the thrash metal, death metal and black metal scenes that emerged in the 1980s and early 1990s.\n\nVenom (band): Venom are an English heavy metal band formed in 1979 in Newcastle upon Tyne.  Coming to prominence towards the end of the new wave of British heavy metal, Venom's first two albums—\"Welcome to Hell\" (1981) and \"Black Metal\" (1982)—are considered a major influence on thrash metal and extreme metal in general.  Venom's second album proved influential enough that its title was used as the name of an extreme metal subgenre: black metal.\n\nThe Iron Maidens: The Iron Maidens is an American heavy metal band from Los Angeles, California.  Formed in 2001 as an all-female tribute act to English heavy metal band Iron Maiden.  Considered the \"World's Only Female Tribute to Iron Maiden,\" the band currently consists of vocalist Kirsten Rosenberg, bassist Wanda Ortiz, drummer Linda McDonald, guitarist Courtney Cox, and guitarist Nikki Stringfield,\n\nCall Me (EP): Call Me is an EP by heavy metal band Diamond Head and was released in 1982 by MCA.  It was a single A-side featuring \"Call Me\", with \"Dead Reckoning\" as the B-Side.  The French release was only available on 7\".\n\nQuestion: Call Me is an EP by an English heavy metal band that was formed in 1976 in what part of England?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"ep_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the EP mentioned in the question.\"\n    },\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band that released the EP.\"\n    },\n    \"band_origin\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the band was formed.\"\n        },\n        \"city_or_region\": {\n          \"type\": \"string\",\n          \"description\": \"The specific city or region in England where the band was formed.\"\n        },\n        \"formation_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the band was formed.\"\n        }\n      },\n      \"required\": [\n        \"country\",\n        \"city_or_region\",\n        \"formation_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"ep_title\",\n    \"band_name\",\n    \"band_origin\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "ep_title": {
        "type": "string",
        "description": "The title of the EP mentioned in the question."
      },
      "band_name": {
        "type": "string",
        "description": "The name of the band that released the EP."
      },
      "band_origin": {
        "type": "object",
        "properties": {
          "country": {
            "type": "string",
            "description": "The country where the band was formed."
          },
          "city_or_region": {
            "type": "string",
            "description": "The specific city or region in England where the band was formed."
          },
          "formation_year": {
            "type": "integer",
            "description": "The year the band was formed."
          }
        },
        "required": [
          "country",
          "city_or_region",
          "formation_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "ep_title",
      "band_name",
      "band_origin"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
