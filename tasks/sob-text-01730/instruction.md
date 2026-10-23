{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDefinitive INXS: Definitive INXS is a two-CD compilation of Australian rock band INXS released in 2002.  It has almost the same track listing as \"The Best of INXS\".  The compilation features most of their hit singles, as well as two previously unreleased tracks, \"Salvation Jane\" and \"Tight\".  \"Salvation Jane\" is an outtake taken from the \"X\" sessions in 1990.  The 2002 remaster of \"X\" features the song's original demo.  \"Tight\" was written by songwriter and multi-instrumentalist Andrew Farriss and recorded by the band during the sessions for \"Welcome to Wherever You Are\" in 1992.  The song was reworked by the remaining members of INXS in 2002 after the death of vocalist Michael Hutchence in 1997.  The compilation also features a cover of Steppenwolf's \"Born to Be Wild\", which was specially recorded for the April 1993 launch of Virgin Radio in the UK and was first included on the Japanse release of \"Full Moon, Dirty Hearts\".\n\nINXS (album): INXS is Australian rock band INXS's first album.  It was released on Deluxe Records in Australia on 13 October 1980.  The band recorded the album in midnight to dawn sessions during 1979 to 1980 after performing, on average, two gigs a day at local pubs around Sydney.  All tracks were credited to band members, Garry Gary Beers (bass guitar and double bass); brothers Andrew (keyboards and guitar), Jon (drums, keyboards) and Tim Farriss (lead guitar); Michael Hutchence (lead vocals); and Kirk Pengilly (guitar, saxophone and backing vocals).  The album was co-produced by the band and Duncan McGuire (ex-Ayers Rock).  It spawned the single, \"Just Keep Walking\" (September 1980), which became their first Australian Top 40 hit.  \"INXS\" peaked in the Top 30 of the related Kent Music Report Albums Chart.  The album did not appear internationally until 1984.\n\nBeautiful Girl (INXS song): \"Beautiful Girl\" was the fifth, internationally released single from the 1992 album \"Welcome to Wherever You Are\", by Australian rock band INXS.  The song was written by Andrew Farriss who was inspired to write this by the birth of his baby daughter.  In an interview by Debbie Kruger the INXS keyboardist explained: \"I was writing lyrics like \"Baby Don't Cry\" and \"Beautiful Girl\" and lyrics just about how wonderful it is to have something else in your life besides yourself to worry about and think about.\"\n\nINXS: INXS ( ) were an Australian rock band, formed as The Farriss Brothers in 1977 in Sydney, New South Wales.  They began playing covers in Western Australian pubs and clubs, occasionally playing some of their original music.  Mainstays were main composer and keyboardist Andrew Farriss, drummer Jon Farriss, guitarists Tim Farriss and Kirk Pengilly, bassist Garry Gary Beers and main lyricist and vocalist Michael Hutchence.  For twenty years, INXS was fronted by Hutchence, whose \"sultry good looks\" and magnetic stage presence made him the focal point of the band.  Initially known for their new wave/pop style, the band later developed a harder pub rock style that included funk and dance elements.\n\nKiss the Dirt (Falling Down the Mountain): \"Kiss the Dirt (Falling Down the Mountain)\" is a song by the Australian rock band INXS.  It was written by Andrew Farriss and Michael Hutchence and included as the third track on the 1985 album \"Listen Like Thieves\".\n\nFreedom Deep: \"Freedom Deep\" is the fourth, and final, single from the 1993 album \"Full Moon, Dirty Hearts\", by Australian rock band INXS.  The song was written by Andrew Farriss and Michael Hutchence.\n\nReen Nalli: Reen Nalli is an American music executive.  She is the current president of A&R Consultants.  She has worked with the likes of INXS, Blue October, and India.Arie.\n\nJon Farriss: Jonathan James Farriss (born 10 August 1961, Perth, Western Australia) is the drummer, and founding member, of the Australian rock band INXS.\n\nPlease (You Got That ...): \"Please (You Got That ...)\" is the second single from the 1993 album \"Full Moon, Dirty Hearts\", by Australian rock band INXS.  The song was written by Andrew Farriss and Michael Hutchence and featured guest vocals from legendary American R&B Artist Ray Charles.\n\nNot Enough Time: \"Not Enough Time\" is the third single from the 1992 album \"Welcome to Wherever You Are\", it was released simultaneously with \"Baby Don't Cry\" (Europe and Australia) but only in the US and Japan, by Australian rock band INXS.  The song was written by Andrew Farriss and Michael Hutchence, the music in Sydney and the lyrics in Paris, France.\n\nQuestion: Reen Nalli is an American music executive, she has worked with the likes of INXS, who were an Australian rock band, formed as The Farriss Brothers, in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the entity being discussed.\"\n    },\n    \"entity_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of entity (e.g., band, person, album).\"\n    },\n    \"formation_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"formed_as\": {\n          \"type\": \"string\",\n          \"description\": \"The original name under which the entity was formed.\"\n        },\n        \"formation_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the entity was formed.\"\n        },\n        \"formation_location\": {\n          \"type\": \"string\",\n          \"description\": \"The location where the entity was formed.\"\n        }\n      },\n      \"required\": [\n        \"formed_as\",\n        \"formation_year\",\n        \"formation_location\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"entity_name\",\n    \"entity_type\",\n    \"formation_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_name": {
        "type": "string",
        "description": "The name of the entity being discussed."
      },
      "entity_type": {
        "type": "string",
        "description": "The type of entity (e.g., band, person, album)."
      },
      "formation_details": {
        "type": "object",
        "properties": {
          "formed_as": {
            "type": "string",
            "description": "The original name under which the entity was formed."
          },
          "formation_year": {
            "type": "integer",
            "description": "The year the entity was formed."
          },
          "formation_location": {
            "type": "string",
            "description": "The location where the entity was formed."
          }
        },
        "required": [
          "formed_as",
          "formation_year",
          "formation_location"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "entity_name",
      "entity_type",
      "formation_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
