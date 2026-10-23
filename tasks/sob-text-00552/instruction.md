{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSchool Daze: School Daze is a 1988 American musical comedy drama film, written and directed by Spike Lee, and starring Larry Fishburne, Giancarlo Esposito, and Tisha Campbell-Martin.  Based in part on Spike Lee's experiences at Atlanta's Morehouse College, Spelman College, Morris Brown College and Clark Atlanta University, it is a story about fraternity and sorority members clashing with other students at a historically black college during homecoming weekend.  It also touches upon issues of colorism and hair texture bias within the African-American community.  The second feature film by Spike Lee, \"School Daze\" was released on February 12, 1988 by Columbia Pictures.\n\nAmerican Movie: American Movie is a 1999 documentary film directed by Chris Smith.  The film chronicles the real 1996–97 making of \"Coven\", an independent horror film directed by filmmaker Mark Borchardt.  Produced for the purpose of raising capital for another film that Borchardt intends to make, the epic \"Northwestern,\" \"Coven\" suffers from numerous setbacks, including poor financing, a lack of planning, Borchardt's burgeoning alcoholism, and the ineptitude of the friends and family Borchardt hires as his production team.  The documentary follows Borchardt's filmmaking process from script to screen, and is interspersed with footage from both developing projects.  \"American Movie\" was produced by Sarah Price and edited by Jun Diaz and Barry Poltermann.\n\nOrleans Levee Board: From 1890 through 2006, the Orleans Levee Board was the body of commissioners that oversaw the Orleans Levee District (OLD) which supervised the levee and floodwall system in Orleans Parish, Louisiana.  The role of the OLD has changed over time.  Prior to Hurricane Betsy in 1965, the OLD developed land and sold it to raise money to build and improve levees.  After 1965, Congress directed the Army Corps of Engineers to be responsible for design and construction of the hurricane flood protection system enveloping New Orleans.\n\nIf God Is Willing and da Creek Don't Rise (film): If God Is Willing and da Creek Don't Rise is a 2010 documentary film directed by Spike Lee, as a follow-up to his 2006 HBO documentary film, \"\".  The film looks into the proceeding years since Hurricane Katrina struck the New Orleans and Gulf Coast region, and also focuses on the 2010 BP oil spill in the Gulf of Mexico and its effect on the men and women who work along the shores of the gulf.  Many of the participants in \"Levees\" were also featured in this documentary.\n\nJamie Meltzer: Jamie Meltzer is an American movie and documentary film director.  He has made \"True Conviction\", \"\"Off the Charts: The Song-Poem Story\"\", \"\"Welcome to Nollywood\"\", \"\"La Caminata\"\" (a short film), and the feature-length documentary film \"\"Informant\"\".  He teaches documentary film production in the Art Department of Stanford University, as part of the MFA Program in Documentary Film.\n\nDinerral Shavers: Dinerral \"Dick\" Shavers (born c. 1981, died 28 December 2006) was a jazz drummer and educator from New Orleans, Louisiana.  Shavers was best known musically as a founding member of the Hot 8 Brass Band.  He also taught at a local high school and created music programs for poor local youths.  He appeared in the Spike Lee film \"When the Levees Broke\" discussing the devastation of his family home in the Lower 9th Ward.\n\nPutting the River in Reverse: Putting the River in Reverse is a 2006 documentary film about the first major recording session in New Orleans, United States, following Hurricane Katrina.  It features Elvis Costello and Allen Toussaint.  It was directed by Matthew Buzzell and premiered at the 2006 Full Frame Documentary Film Festival.  It also played at the 2006 Tribeca Film Festival.\n\nHexing a Hurricane: Hexing a Hurricane is a 2006 documentary film about the effect of Hurricane Katrina on New Orleans.  It has been billed as the \"First Katrina documentary\" released by a New Orleanian.  The film is directed by Jeremy Campbell and distributed by the National Film Network.  The film's score was orchestrated by New Orleans artist Eric Laws.\n\nWhen the Levees Broke: When the Levees Broke: A Requiem in Four Acts is a 2006 documentary film directed by Spike Lee about the devastation of New Orleans, Louisiana following the failure of the levees during Hurricane Katrina.  It was filmed in late August and early September 2005, and premiered at the New Orleans Arena on August 16, 2006 and was first aired on HBO the following week.  The television premiere aired in two parts on August 21 and 22, 2006 on HBO.  It has been described by Sheila Nevins, chief of HBO's documentary unit, as \"one of the most important films HBO has ever made.\"  The title is a reference to the blues tune, \"When the Levee Breaks\", by Kansas Joe McCoy and Memphis Minnie, about the Great Mississippi Flood of 1927.\n\nKobe Doin' Work: Kobe Doin' Work is a 2009 documentary film directed by Spike Lee.  It focuses on Kobe Bryant during one day of the 2007–08 Los Angeles Lakers season.  Bryant granted filmmaker Spike Lee and 30 cameras unprecedented access to his life for one day.  \"Kobe: Doin' Work\" premiered on ESPN on May 16, 2009.\n\nQuestion: What s a 2006 documentary film directed by Spike Lee about the devastation of New Orleans, American Movie or When the Levees Broke ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_criteria\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year specified in the question.\"\n        },\n        \"director_name\": {\n          \"type\": \"string\",\n          \"description\": \"The director's name specified in the question.\"\n        },\n        \"subject_keywords\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Keywords describing the subject matter specified in the question.\"\n        },\n        \"film_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of film specified in the question (e.g., documentary).\"\n        }\n      },\n      \"required\": [\n        \"release_year\",\n        \"director_name\",\n        \"subject_keywords\",\n        \"film_type\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"candidate_films\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"title\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the candidate film.\"\n          },\n          \"director\": {\n            \"type\": \"string\",\n            \"description\": \"The director of the candidate film.\"\n          },\n          \"release_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The release year of the candidate film.\"\n          },\n          \"is_documentary\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the film is a documentary.\"\n          },\n          \"is_about_new_orleans_devastation\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the film is about the devastation of New Orleans.\"\n          }\n        },\n        \"required\": [\n          \"title\",\n          \"director\",\n          \"release_year\",\n          \"is_documentary\",\n          \"is_about_new_orleans_devastation\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"A list of films presented as choices in the question, with their attributes.\"\n    },\n    \"identified_film\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film that matches all criteria.\"\n        },\n        \"director\": {\n          \"type\": \"string\",\n          \"description\": \"The director of the identified film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the identified film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"director\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"question_criteria\",\n    \"candidate_films\",\n    \"identified_film\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_criteria": {
        "type": "object",
        "properties": {
          "release_year": {
            "type": "integer",
            "description": "The release year specified in the question."
          },
          "director_name": {
            "type": "string",
            "description": "The director's name specified in the question."
          },
          "subject_keywords": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Keywords describing the subject matter specified in the question."
          },
          "film_type": {
            "type": "string",
            "description": "The type of film specified in the question (e.g., documentary)."
          }
        },
        "required": [
          "release_year",
          "director_name",
          "subject_keywords",
          "film_type"
        ],
        "additionalProperties": false
      },
      "candidate_films": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string",
              "description": "The title of the candidate film."
            },
            "director": {
              "type": "string",
              "description": "The director of the candidate film."
            },
            "release_year": {
              "type": "integer",
              "description": "The release year of the candidate film."
            },
            "is_documentary": {
              "type": "boolean",
              "description": "True if the film is a documentary."
            },
            "is_about_new_orleans_devastation": {
              "type": "boolean",
              "description": "True if the film is about the devastation of New Orleans."
            }
          },
          "required": [
            "title",
            "director",
            "release_year",
            "is_documentary",
            "is_about_new_orleans_devastation"
          ],
          "additionalProperties": false
        },
        "description": "A list of films presented as choices in the question, with their attributes."
      },
      "identified_film": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film that matches all criteria."
          },
          "director": {
            "type": "string",
            "description": "The director of the identified film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the identified film."
          }
        },
        "required": [
          "title",
          "director",
          "release_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "question_criteria",
      "candidate_films",
      "identified_film"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
