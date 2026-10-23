{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLeslie Arden: Leslie Arden is a Canadian musical theatre composer, lyricist and librettist.  She is best known for her work \"The House of Martin Guerre\" (co-book by Anna Theresa Cascio) produced by Theatre Plus (1993), the Goodman Theatre (1996) in Chicago and the Canadian Stage Company (1997).  Her musical \"The Boys are Coming Home\" was part of the American Music Theatre Project at North Western University and was showcased by the National Alliance of Musical Theatre in New York City.  Theatre critic Richard Ouzanian says she is \"the creator of some of the most sophisticated work on our stages\".  The Toronto Star has commented that her work is “beautifully crafted” and USA Today states she is a “major talent”.  She also wrote the Chalmers Award-winning \"The Happy Prince\".  She collaborated with esteemed Canadian playwright Norm Foster for her latest musical \"Ned Durango\".  It had its world premiere at Theatre Orangeville in May 2011.\n\nTriple-A Plowed Under: Triple-A Plowed Under is a Living Newspaper play produced by the Federal Theatre Project in 1936.  Written by Arthur Arent from research by the editorial staff of the Federal Theatre Project and directed by Joseph Losey, it focused on the Agricultural Adjustment Act of 1933 and the plight of Dust Bowl farmers.  The production premiered at the Biltmore Theatre on March 14, 1936 and ran until May 2, 1936.\n\nTony Award: The Antoinette Perry Award for Excellence in Broadway Theatre, more commonly known as Tony Award, recognizes the excellence in live Broadway theatre.  The awards are presented by the American Theatre Wing and The Broadway League at an annual ceremony in New York City.  The awards are given for Broadway productions and performances, and an award is given for regional theatre.  Several discretionary non-competitive awards are also given, including a Special Tony Award, the Tony Honors for Excellence in Theatre, and the Isabelle Stevenson Award.  The awards are named after Antoinette \"Tony\" Perry, co-founder of the American Theatre Wing.\n\nOne-Third of a Nation: One Third of a Nation is a Living Newspaper play produced by the Federal Theatre Project in 1938.  Written by Arthur Arent from research by the editorial staff of the Federal Theatre Project, it focused on the problem of housing in the United States and the growth of slums in New York City.  The play was produced in New York and in nine additional cities, where it was adapted to specific community conditions.  It was adapted as a feature film in 1939, and revived on the New York stage in 2011.\n\n44th Street Theatre: The 44th Street Theatre was a Broadway theatre located at 216 West 44th Street in New York City from 1912 to 1945.  It opened and operated for three years as the Weber and Fields' Music Hall.  Its rooftop theatre, the Nora Bayes Theatre, presented many productions of the Federal Theatre Project in the mid 1930s.  Its basement club became the famed Stage Door Canteen during World War II.\n\nOld Broadway Theatre: The Broadway Theatre (September 27, 1847 – April 2, 1859), called the Old Broadway Theatre since its demise, was at 326–30 Broadway, between Pearl and Anthony (now Worth) Streets in Manhattan.  With over 4000 seats, it was the largest theater ever built in New York when it opened.  During its brief existence, many prominent performers of the era appeared on its stage.  It presented plays, opera, ballet, hippodrama, and circus performances in a space that was reconfigured several times.  The operators always struggled to make money, however, and after twelve years the Broadway Theatre was replaced by a more profitable building, for the textile trade.\n\nFederal Theatre Project: The Federal Theatre Project (1935–39) was a New Deal program to fund theatre and other live artistic performances and entertainment programs in the United States during the Great Depression.  It was one of five Federal Project Number One projects sponsored by the Works Progress Administration.  It was created not as a cultural activity but as a relief measure to employ artists, writers, directors and theater workers.  It was shaped by national director Hallie Flanagan into a federation of regional theatres that created relevant art, encouraged experimentation in new forms and techniques, and made it possible for millions of Americans to see live theatre for the first time.  The Federal Theatre Project ended when its funding was canceled after strong Congressional objections to the left-wing political tone of a small percentage of its productions.\n\nBroadway Theatre (53rd Street): The Broadway Theatre (formerly Universal's Colony Theatre, B.S. Moss' Broadway Theatre, Earl Carroll's Broadway Theatre, and Ciné Roma) is a Broadway theatre located in midtown Manhattan.  It has a large seating capacity of 1,761, and unlike most Broadway theaters, it is actually located on Broadway, at number 1681.\n\nAnn Reinking: Ann Reinking (born November 10, 1949) is an American actress, dancer, and choreographer.  Her extensive work in musical theater includes starring in Broadway productions of \"Coco\" (1969), \"Over Here! \" (1974), \"Goodtime Charley\" (1975), \"A Chorus Line\" (1976), \"Chicago\" (1977), \"Dancin'\" (1978) and \"Sweet Charity\" (1986).  In the 1996 revival of \"Chicago\", she reprised the role of Roxie Hart and was also the choreographer, winning the Tony Award for Best Choreography.  For the 2000 West End production of \"Fosse\", she won the Olivier Award for Best Theatre Choreographer.  She has also appeared in the films \"All That Jazz\" (1979), \"Annie\" (1982), and \"Micki & Maude\" (1984).\n\nBroadway Theater Project: The Broadway Theatre Project is an intensive training program for both high school and college-aged students that want to hone their skills in the industry of musical theatre.  It was founded by Tony Award winner Ann Reinking, under the name The Musical Theatre Project of Tampa.  Students accepted into the program are referred to as \"apprentices\" and divided into groups reflecting their dance experience, vocal/acting experience, and age for more individualized training.  Classes are taken every day of the project, typically from 8:30am to 5:00pm with an hour lunch break, and block rehearsals for numbers within the final showcase are from 6:00pm to 10:00pm.  Students not in block rehearsal continue with group classes for that time period.\n\nQuestion: The founder of The Broadway Theatre Project played the role of \"Roxie\" in what musical?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"founder_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the founder of The Broadway Theatre Project.\"\n    },\n    \"founded_project_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the project founded by the person.\"\n    },\n    \"role_played\": {\n      \"type\": \"string\",\n      \"description\": \"The specific role the founder played in the musical.\"\n    },\n    \"musical_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the musical in which the role was played.\"\n    },\n    \"production_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year of the production where the role was played.\"\n        },\n        \"production_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of production (e.g., revival).\"\n        },\n        \"additional_contribution\": {\n          \"type\": \"string\",\n          \"description\": \"Any other significant contribution made by the founder in this production.\"\n        },\n        \"award_received\": {\n          \"type\": \"string\",\n          \"description\": \"Any award received for their work in this specific production.\"\n        }\n      },\n      \"required\": [\n        \"year\",\n        \"production_type\",\n        \"additional_contribution\",\n        \"award_received\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"founder_name\",\n    \"founded_project_name\",\n    \"role_played\",\n    \"musical_title\",\n    \"production_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "founder_name": {
        "type": "string",
        "description": "The name of the founder of The Broadway Theatre Project."
      },
      "founded_project_name": {
        "type": "string",
        "description": "The name of the project founded by the person."
      },
      "role_played": {
        "type": "string",
        "description": "The specific role the founder played in the musical."
      },
      "musical_title": {
        "type": "string",
        "description": "The title of the musical in which the role was played."
      },
      "production_details": {
        "type": "object",
        "properties": {
          "year": {
            "type": "integer",
            "description": "The year of the production where the role was played."
          },
          "production_type": {
            "type": "string",
            "description": "The type of production (e.g., revival)."
          },
          "additional_contribution": {
            "type": "string",
            "description": "Any other significant contribution made by the founder in this production."
          },
          "award_received": {
            "type": "string",
            "description": "Any award received for their work in this specific production."
          }
        },
        "required": [
          "year",
          "production_type",
          "additional_contribution",
          "award_received"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "founder_name",
      "founded_project_name",
      "role_played",
      "musical_title",
      "production_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
