{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJeon Soo-kyung: Jeon Soo-kyung (born July 12, 1966) is a South Korean actress.  She is best known in musical theatre, and has starred in Korean productions of \"Mamma Mia! \", \"Chicago\", \"The Life\", \"Guys and Dolls\", \"Menopause\", and \"Kiss Me, Kate\".\n\nWay Back Home (2013 film): Way Back Home () is a 2013 South Korean drama film starring Jeon Do-yeon and Go Soo, and directed by Bang Eun-jin.  It is based on the true story of an ordinary Korean housewife who was imprisoned in Martinique for two years after being wrongfully accused of drug smuggling at a Paris airport.\n\nLovers (TV series): Lovers () is a South Korean television series starring Kim Jung-eun and Lee Seo-jin who play a plastic surgeon and a gangster who enter into an unlikely romance.  The series is based on the Lee Man-hee stage play \"Turn Around and Leave\", the same work that inspired the 1998 blockbuster film \"\" starring Jeon Do-yeon and Park Shin-yang.  It aired on SBS from November 8, 2006 to January 11, 2007 on Wednesdays and Thursdays at 21:55 for 20 episodes.\n\nYou Are My Sunshine (2005 film): You Are My Sunshine (, literally: \"You are my destiny\") is a 2005 South Korean film written and directed by Park Jin-pyo, and starring Jeon Do-yeon.  It was released in Korea on 23 September 2005.\n\nMy Prettiest Moments: My Prettiest Moments () is a South Korean single-episode television drama starring Jeon Ye-seo and Lee Jong-suk.  It aired on August 26, 2012 as part of \"Drama Special\", a weekly program on KBS2 showing short dramas (usually single episodes), with each episode having a different story, cast, director, and writer.\n\nMenopause The Musical: Written by Jeanie Linders, Menopause The Musical debuted March 28, 2001 in Orlando, Florida.  The original cast members were Shelly Browne as the Power (later Professional) Woman, Patti McGuire as the Iowa Housewife, Pammie O'Bannon as the Earth Mother and Wesley Williams as the Soap Star.  The musical follows four women shopping for lingerie at a Bloomingdale's sale sing 25 songs about chocolate cravings, hot flashes, loss of memory, nocturnal sweats, and sexual predicaments.  The lyrics parody popular music from the baby boomer era, and includes the numbers \"Stayin' Awake\" and \"Puff, My God I'm Draggin'.\"\n\nLovers in Prague: Lovers in Prague () is a 2005 South Korean television drama series starring Jeon Do-yeon, Kim Joo-hyuk, Kim Min-joon and Yoon Se-ah.  It aired on SBS from September 24 to November 20, 2005 on Saturdays and Sundays at 21:45 for 18 episodes.\n\nPrincess Aurora (TV series): Princess Aurora () is a 2013 South Korean television series starring Jeon So-min, Oh Chang-seok, Park Yeong-gyu, Son Chang-min, Oh Dae-gyu, Kim Bo-yeon, Park Hae-mi, and Kim Hye-eun.  The daily drama aired on MBC from May 20 to December 20, 2013, on Mondays to Fridays at 19:15 for 150 episodes.\n\nThe Good Wife (South Korean TV series): The Good Wife () is a South Korean television series starring Jeon Do-yeon, Yoo Ji-tae and Yoon Kye-sang.  It is a Korean drama remake of the American television series of the same title which aired on CBS from 2009 to 2016.  It replaced \"Dear My Friends\" and it broadcast on the cable network tvN on Fridays and Saturdays at 20:30 (KST) for 16 episodes from July 8 to August 27, 2016.\n\nMy Dear Enemy: My Dear Enemy (; lit.  \"One Fine Day\") is a road movie starring Jeon Do-yeon and Ha Jung-woo as two ex-lovers who reacquaint themselves while driving around Seoul.  The film takes place over one rather uneventful day, and subtle emotions and chemistry between the actors propel the narrative.  This is the fourth film by South Korean director Lee Yoon-ki.\n\nQuestion: Which musical starring Jeon Soo-kyung originally debuted March 28, 2001?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"musical_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the musical.\"\n    },\n    \"debut_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"debut_date\": {\n          \"type\": \"string\",\n          \"description\": \"The original debut date of the musical.\"\n        },\n        \"debut_location\": {\n          \"type\": \"string\",\n          \"description\": \"The original debut location of the musical.\"\n        }\n      },\n      \"required\": [\n        \"debut_date\",\n        \"debut_location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"starring_actress\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress who starred in the musical.\"\n    }\n  },\n  \"required\": [\n    \"musical_title\",\n    \"debut_information\",\n    \"starring_actress\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "musical_title": {
        "type": "string",
        "description": "The title of the musical."
      },
      "debut_information": {
        "type": "object",
        "properties": {
          "debut_date": {
            "type": "string",
            "description": "The original debut date of the musical."
          },
          "debut_location": {
            "type": "string",
            "description": "The original debut location of the musical."
          }
        },
        "required": [
          "debut_date",
          "debut_location"
        ],
        "additionalProperties": false
      },
      "starring_actress": {
        "type": "string",
        "description": "The name of the actress who starred in the musical."
      }
    },
    "required": [
      "musical_title",
      "debut_information",
      "starring_actress"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
