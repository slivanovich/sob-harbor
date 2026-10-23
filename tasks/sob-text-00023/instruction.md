{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPhilippine Hot 100: The Philippine Hot 100 is the music industry standard record chart in the Philippines for singles and published weekly by \"Billboard Philippines\".  The charts combine overall rankings of both top-performing local and international songs.  They are compiled by Nielsen Music through ranking songs based on online streaming from Apple Music, Spotify and YouTube and digital downloads from iTunes.\n\nCool Kids (Echosmith song): \"Cool Kids\" is the debut single song by American indie pop band Echosmith from their 2013 debut studio album, \"Talking Dreams\".  The song was written by Echosmith, Jeffery David, and Jesiah Dzwonek.  It was produced by Mike Elizondo, with additional production on the radio edit by Rob Cavallo.  \"Cool Kids\" was originally released on 31 May 2013 as the iTunes Store Single of the Week and officially impacted United States radio the following year.  The song subsequently became a sleeper hit, peaking at number 13 on the \"Billboard\" Hot 100 and receiving airplay on US modern rock, hot adult contemporary, and contemporary hit radio stations.  The song is a playable track in Guitar Hero Live.\n\nIrish Albums Chart: The Irish Albums Chart is the Irish music industry standard albums popularity chart issued weekly by the Irish Recorded Music Association and compiled on its behalf by Chart-Track.  Chart rankings are based on sales, which are compiled through over-the-counter retail data captured electronically each day from retailers' Point of sale systems and certain digital retailers.  All major record stores and over forty independents submit data for the charts, accounting for over 80% of the market, according to Chart-Track.  A new chart is compiled and released to the public by the Irish Recorded Music Association on Friday at noon.  Each chart is dated with the \"week-ending\" date of the previous Thursday (i.e., the day before issue).\n\nIndustry Standard Coding Identification: Industry Standard Coding Identification (ISCI, also known as Industry Standard Commercial Identification) was a standard created to identify commercials that aired on TV in the United States, for ad agencies and advertisers from 1970 until 2004 (it was replaced by Ad-ID in 2005).\n\nPhilippine Top 20: The Philippine Top 20 is the music industry standard record chart in the Philippines for local singles and published weekly by \"Billboard Philippines\".  The charts only rank the top-performing local songs by Filipino artists.  They are compiled by Nielsen Music through ranking songs based on online streaming from Apple Music, Spotify and YouTube and digital downloads from iTunes.\n\nCanadian Hot 100: The Canadian Hot 100 is a music industry record chart in Canada for singles, published weekly by \"Billboard\" magazine.  The Canadian Hot 100 was launched on the issue dated June 16, 2007, and is currently the standard record chart in Canada; a new chart is compiled and officially released to the public by \"Billboard\" on Tuesdays.\n\nBillboard Hot 100: The \"Billboard\" Hot 100 is the music industry standard record chart in the United States for singles, published weekly by \"Billboard\" magazine.  Chart rankings are based on sales (physical and digital), radio play, and online streaming.\n\nGaon Digital Chart: The Gaon Digital Chart is the music industry standard record chart in South Korea for singles, provided by the Korea Music Content Industry Association and published weekly by the Gaon Music Chart.  The chart provides rankings on a weekly, monthly, and yearly basis, which are based on an aggregate of downloads, streaming and background music.  In addition to rank ranking all songs, it also supplies separate rankings for domestic and international releases.  It started tracking sales in 2009, which were published the following February.  It is compiled from online data provided by web-based music providers Bugs, Genie, KakaoMusic, Melon, Mnet, Naver Music, Olleh Music, and Soribada.\n\nIrish Singles Chart: The Irish Singles Chart (Irish: \"Cairt Singil na hÉireann\") is Ireland's music industry standard singles popularity chart issued weekly by the Irish Recorded Music Association and compiled on behalf of the IRMA by Chart-Track.  Chart rankings are based on sales, which are compiled through over-the-counter retail data captured electronically each day from retailers' EPOS systems.  Currently all major record stores and over forty independents submit data for the charts, accounting for over 80% of the market, according to Chart-Track.  A new chart is compiled and officially released to the public by the Irish Recorded Music Association on Friday at noon.  Each chart is dated with the \"week-ending\" date of the previous Thursday (i.e. the day before issue).  The singles chart was first published on 1 October 1962, and covered the top ten singles of the previous week by record label shipments.\n\nEchosmith: Echosmith is an American, Corporate indie pop band formed in February 2009 in Chino, California.  Originally formed as a quartet of siblings, the band currently consists of Sydney, Noah and Graham Sierota, following the departure of eldest sibling Jamie in late 2016.  Echosmith started first as \"Ready Set Go!\"  until they signed to Warner Bros.  Records in May 2012.  They are best known for their hit song \"Cool Kids\", which reached number 13 on the \"Billboard\" Hot 100 and was certified double platinum by the RIAA with over 1,200,000 sales in the United States and also double platinum by ARIA in Australia.  The song was Warner Bros.  Records' fifth-biggest-selling-digital song of 2014, with 1.3 million downloads sold.  The band's debut album, \"Talking Dreams\", was released on October 8, 2013.\n\nQuestion: which  music industry standard record chart in the United States  is Cool Kids  at number 13 \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the song.\"\n        },\n        \"peak_position\": {\n          \"type\": \"integer\",\n          \"description\": \"The highest position the song reached on the chart.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"peak_position\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"chart_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the music chart.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the chart is standard.\"\n        },\n        \"is_industry_standard\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the chart is considered an industry standard.\"\n        },\n        \"chart_scope\": {\n          \"type\": \"string\",\n          \"description\": \"The type of music releases the chart tracks (e.g., singles, albums).\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"country\",\n        \"is_industry_standard\",\n        \"chart_scope\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer_chart_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the music industry standard record chart in the United States where the song peaked at the specified position.\"\n    }\n  },\n  \"required\": [\n    \"song_details\",\n    \"chart_details\",\n    \"final_answer_chart_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the song."
          },
          "peak_position": {
            "type": "integer",
            "description": "The highest position the song reached on the chart."
          }
        },
        "required": [
          "title",
          "peak_position"
        ],
        "additionalProperties": false
      },
      "chart_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the music chart."
          },
          "country": {
            "type": "string",
            "description": "The country where the chart is standard."
          },
          "is_industry_standard": {
            "type": "boolean",
            "description": "Indicates if the chart is considered an industry standard."
          },
          "chart_scope": {
            "type": "string",
            "description": "The type of music releases the chart tracks (e.g., singles, albums)."
          }
        },
        "required": [
          "name",
          "country",
          "is_industry_standard",
          "chart_scope"
        ],
        "additionalProperties": false
      },
      "final_answer_chart_name": {
        "type": "string",
        "description": "The name of the music industry standard record chart in the United States where the song peaked at the specified position."
      }
    },
    "required": [
      "song_details",
      "chart_details",
      "final_answer_chart_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
