{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTrend type forecast: A trend type forecast (TTF) also known simply as a trend, is an aviation weather forecast written by a real person on location at a major airport or military base.  A TTF is a professionally considered forecast for weather over a two-hour period, and is based on an actual weather report, such as a METAR or SPECI and appended to the end of it.\n\nShort Weather Cipher: The Short Weather Cipher (German: \"Wetterkurzschlüssel\" ), also known as the weather short signal book, was a cipher, presented as a codebook, that was used by the radio telegraphists aboard U-boats of the German Navy (Kriegsmarine) during World War II.  It was used to condense weather reports into a short 7-letter message, which was enciphered by using the naval Enigma and transmitted by radiomen to intercept stations on shore, where it was deciphered by Enigma and the 7-letter weather report was reconstructed.\n\nWeather Report Girl: Weather Report Girl (お天気お姉さん , Otenki Onēsan ) , also known as Weather Woman, is a two-episode anime yuri erotic OVA comedy series originally released in Japan in August 1994 by Toho and released in the U.S. on VHS in September 1996 and DVD August 2005 by The Right Stuf International.  It is based on a softcore erotic manga by Tetsu Adachi.\n\nThe Zawinul Syndicate (band): The Zawinul Syndicate was a band (active from 1988 to 2007) that has been influenced by and formed around Austrian jazz-rock musician Joe Zawinul.  The band evolved out of a former band of Zawinul called Weather Report.  The band adhered to Zawinul's roots in jazz.  Their style could be described as a combination of unusual grooves, driving and swinging rhythms and many borrowings from different music cultures.\n\nTale Spinnin': Tale Spinnin' is the sixth album by Weather Report, recorded and released in 1975, featuring the addition of Leon \"Ndugu\" Chancler on the drums.  Ndugu was recruited after Josef Zawinul heard him play with Carlos Santana.  Weather Report was recording next door to Ndugu in the studio, and Chancler was asked to join them for a recording session.  That session ended up lasting a week and produced \"Tale Spinnin\"'.  After the record, Ndugu was asked to join the band as a permanent member, but declined in favor of continuing to work with Carlos Santana.\n\nManolo Badrena: Manolo Badrena (born March 17, 1952 in San Juan, Puerto Rico) is a percussionist most noted for his work with Weather Report from 1976 to 1977.  He has made contributions to over 100 recordings that span jazz, world music, pop, and Latin music.  Badrena has played with The Zawinul Syndicate, the Rolling Stones, Mezzoforte, Joni Mitchell, Spyro Gyra, Art Blakey, Bill Evans, Steve Khan, Carla Bley, Talking Heads, Blondie, Michael Franks, Ahmad Jamal, Hugo Fattoruso, and others.\n\nEric Gravatt: Eric Kamau Grávátt (born March 6, 1947) is a jazz drummer from Philadelphia.  He has played with McCoy Tyner, Joe Henderson, Weather Report, Byard Lancaster, Dom Um Romão.  He was a member of Weather Report from 1972–1974.\n\nDom Um Romão: Dom Um Romão (3 August 1925 – 27 July 2005) was a Brazilian jazz drummer and percussionist.  Noted for his expressive stylings with the fusion band Weather Report, Romão recorded with varied artists such as Cannonball Adderley, Paul Simon, Antonio Carlos Jobim, Jorge Ben, Sergio Mendes and Brasil '66 and Tony Bennett.  He died in Rio de Janeiro shortly after suffering a stroke.  He was the percussionist Tom Jobim brought to the studio for the legendary album Jobim recorded with Frank Sinatra in 1967 for Reprise \"Francis Albert Sinatra & Antonio Carlos Jobim\"\n\nVictor Bailey (musician): Victor Bailey (March 27, 1960 – November 11, 2016) was an American bass guitar player.  He was the bassist for Weather Report during their final years from 1982 to 1986, and launched a solo career in 1988.  As a musician, Bailey was known for his signature scat-bass solos.\n\nJoni Mitchell: Roberta Joan \"Joni\" Mitchell, CC (née Anderson; born November 7, 1943) is a Canadian singer-songwriter and painter.  \"Rolling Stone\" called her \"one of the greatest songwriters ever\", and AllMusic has stated, \"When the dust settles, Joni Mitchell may stand as the most important and influential female recording artist of the late 20th century\".  Drawing from folk, pop, rock and jazz, Mitchell's songs often reflect social and environmental ideals as well as her feelings about romance, confusion, disillusionment and joy.\n\nQuestion: The man who played with the Canadian singer-songwriter and is noted for his work with Weather Report is known as what type of musician?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"musician_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the musician identified.\"\n    },\n    \"musician_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of musician.\"\n    },\n    \"noted_band_affiliation\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"band_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the band the musician is noted for working with.\"\n        },\n        \"start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The start year of the musician's work with the band.\"\n        },\n        \"end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The end year of the musician's work with the band.\"\n        }\n      },\n      \"required\": [\n        \"band_name\",\n        \"start_year\",\n        \"end_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"collaborator_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the collaborator.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the collaborator.\"\n        },\n        \"occupations\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of occupations for the collaborator.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"occupations\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"musician_name\",\n    \"musician_type\",\n    \"noted_band_affiliation\",\n    \"collaborator_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "musician_name": {
        "type": "string",
        "description": "The name of the musician identified."
      },
      "musician_type": {
        "type": "string",
        "description": "The type of musician."
      },
      "noted_band_affiliation": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band the musician is noted for working with."
          },
          "start_year": {
            "type": "integer",
            "description": "The start year of the musician's work with the band."
          },
          "end_year": {
            "type": "integer",
            "description": "The end year of the musician's work with the band."
          }
        },
        "required": [
          "band_name",
          "start_year",
          "end_year"
        ],
        "additionalProperties": false
      },
      "collaborator_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the collaborator."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the collaborator."
          },
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of occupations for the collaborator."
          }
        },
        "required": [
          "name",
          "nationality",
          "occupations"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "musician_name",
      "musician_type",
      "noted_band_affiliation",
      "collaborator_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
