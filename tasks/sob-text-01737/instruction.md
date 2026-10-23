{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Big Break I: The Big Break I was the first round of \"The Big Break\", the Golf Channel's reality television program.  The show's premise is to award an aspiring professional golfer exemptions into selected events or full-season exemptions on certain tours.  The series debuted on October 6, 2003.\n\nThe Big Break III: Ladies Only: The Big Break III: Ladies Only is the third installment of The Golf Channel's reality series, \"The Big Break\".  This installment first aired on February 8, 2005.  The show was filmed in October 2004 at the Kingsmill Resort and Spa just outside Williamsburg, Virginia.  The winner of this edition would receive exemptions into two LPGA events and a celebrity tournament (the American Century Championship) in 2005, \"not\" all of which aired on The Golf Channel.  Also, a leading golf retailer, Golf Galaxy, was offering $5,000 so that the winning player could purchase whatever they need for the LPGA events, such as new clubs or other accessories.  The first of those three tournaments was the Michelob ULTRA Open at Kingsmill, held at the golf resort where the show was filmed.  The Michelob ULTRA Open is commonly referred to as the LPGA's \"fifth major,\" much like The Players Championship is for the PGA Tour.\n\nThe Big Break V: Hawaii: The Big Break V: Hawaii was the fifth edition of The Golf Channel's reality television competition program, \"The Big Break\".  The show's premise is to award aspiring golf professionals exemptions into event on major tours, eliminating one contestant each week through a series of challenges until only one player is left.\n\nThe Big Break VII: Reunion at Reunion: The Big Break VII: Reunion at Reunion featured sixteen competitors from previous seasons of \"The Big Break\" returning to compete for PGA, Champions and LPGA Tour exemptions at the Reunion Resort & Club in Orlando, Florida.  The series premiered on The Golf Channel on February 25, 2007 and was won by Tommy \"Two Gloves\" Gainey, who originally competed on \"\".\n\nBig Break Atlantis: Big Break Atlantis was the 17th edition of the Golf Channel's reality show, The Big Break.  It was contested at the Paradise Island Golf Course on Paradise Island, The Bahamas.  It premiered on May 14, 2012.\n\nKirstie Alley: Kirstie Louise Alley (born January 12, 1951) is an American actress, comedian and spokesmodel.  Her big break came in 1982 playing Lieutenant JG Saavik in the science fiction film \"\".\n\nMarta Kauffman: Marta Fran Kauffman (born September 21, 1956) is an American writer and TV producer, best known as the co-creator of the popular sitcom \"Friends\", alongside David Crane.  Both Kauffman and Crane were also executive producers of the show, along with Kevin Bright.  Kauffman and Crane also produced \"Veronica's Closet\", starring Kirstie Alley, and \"Jesse\", starring Christina Applegate.  From 2005–2006 she was an executive producer on \"Related\".  Both writers were the creators of the 1990 HBO series \"Dream On\".  Marta Kauffman also studied Acting at The Neighborhood Playhouse School of the Theater in New York City.\n\nBig Break Ireland: Big Break Ireland was the 16th edition of the Golf Channel reality show, The Big Break.  It was contested in the K Club in Straffan, County Kildare, Ireland.  It premiered on September 20, 2011.  The eventual winner of the show was Mark Murphy, who won $50,000 and two exemptions to European Tour events, the Trophée Hassan II and the Irish Open.\n\nThe Big Break VI: Trump National: The Big Break VI: Trump National was the sixth edition of The Golf Channel's popular reality television series, \"The Big Break\".  The show awards exemptions into selected events on major professional golf tours.\n\nFull Swing (game show): Full Swing was a game show that combined general knowledge questions and the game of golf which aired on BBC1 for one series from 25 May to 27 July 1996.  The programme was hosted by Jimmy Tarbuck with voice overs by Rosemarie Ford.  The show was inspired by (and produced by the team behind) the BBC's popular \"Big Break\", which featured snooker (and in turn, was influenced by ITV's long-running darts quiz, \"Bullseye\").  However, unlike the long-running \"Big Break\", \"Full Swing\" did not catch on and only ran for one series.\n\nQuestion: Where was the big break of the star of Veronica's Closet in playing?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"star_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the star whose big break is being identified.\"\n    },\n    \"show_starring_role\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the show where the star had a starring role.\"\n    },\n    \"big_break_role\": {\n      \"type\": \"string\",\n      \"description\": \"The specific role that constituted the star's big break.\"\n    },\n    \"big_break_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the star's big break occurred.\"\n    }\n  },\n  \"required\": [\n    \"star_name\",\n    \"show_starring_role\",\n    \"big_break_role\",\n    \"big_break_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "star_name": {
        "type": "string",
        "description": "The name of the star whose big break is being identified."
      },
      "show_starring_role": {
        "type": "string",
        "description": "The name of the show where the star had a starring role."
      },
      "big_break_role": {
        "type": "string",
        "description": "The specific role that constituted the star's big break."
      },
      "big_break_year": {
        "type": "integer",
        "description": "The year the star's big break occurred."
      }
    },
    "required": [
      "star_name",
      "show_starring_role",
      "big_break_role",
      "big_break_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
