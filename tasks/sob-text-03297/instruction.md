Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Andy Murray: Sir Andrew Barron Murray, {'1': ", '2': ", '3': ", '4': "} (born 15 May 1987) is a British professional tennis player from Scotland currently ranked world no. 3 in men's singles.  Murray represents Great Britain in his sporting activities and is a three-time Grand Slam tournament winner, two-time Olympic champion, Davis Cup champion and the winner of the 2016 ATP World Tour Finals.

2010 Rogers Cup – Men's Singles: Andy Murray became the first player since Andre Agassi in 1995 to successfully defend the title.  He beat Roger Federer 7-5, 7-5 in the final.  It was also the first time in the tournament's history that the top four seeds reached the semifinals.

2014 Rogers Cup – Men's Singles: The 2014 Rogers Cup – Men's Singles was the main men's event of the 2014 Rogers Cup tennis tournament played in Toronto, Canada from August 2 through August 10, 2014.

2013 Rogers Cup – Women's Singles: The 2013 Rogers Cup – Singles was the tennis singles event of the 112th female edition of the Rogers Cup; a WTA Premier 5 tournament held in Toronto, Canada.  The tournament was held at the Rexall Centre in Toronto, from 3 – 11 August.

Fernando Verdasco: Fernando Verdasco Carmona (] ; (born 15 November 1983) is a Spanish professional tennis player.  His career-high singles ranking is world No. 7, achieved in April 2009.  Verdasco started playing tennis at four years of age and had a full-time coach when he was eight.  As of 2009, Verdasco has been working in Las Vegas with Andre Agassi and his team, including Darren Cahill (Agassi's former coach) and Gil Reyes (Agassi's fitness coach).

Agassi Tennis Generation: Agassi Tennis Generation is a tennis sports game, developed by Aqua Pacific and published by DreamCatcher Interactive for the PC, PlayStation 2 and Game Boy Advance.  It was originally released for PC on August 12, 2002.  The game features former tennis player Andre Agassi.

2010 Rogers Cup – Men's Singles Qualifying: This article shows the Qualifying Draw for the 2010 Rogers Cup.

2011 Rogers Cup: The 2011 Canada Masters (also known as the 2011 Rogers Cup presented by National Bank and the 2011 Rogers Cup for sponsorship reasons) was a tennis tournament played on outdoor hard courts in Canada.  It was the 122nd edition of the Canada Masters (110th for the women), and was part of the ATP World Tour Masters 1000 of the 2011 ATP World Tour, and of the Premier Series of the 2011 WTA Tour.  The women's and legends event was held at the Rexall Centre in Toronto, Ontario, Canada and the men's event took place at the Uniprix Stadium in Montreal, Quebec, Canada, from August 8 to August 14.

2010 Rogers Cup: The 2010 Canada Masters (also known as the 2010 Rogers Cup presented by National Bank and the 2010 Rogers Cup for sponsorship reasons) was a tennis tournament played on outdoor hard courts in Canada.  It was the 121st edition of the Canada Masters for the men (the 109th edition for the women), and was part of the ATP Masters Series of the 2010 ATP World Tour, and of the Premier Series of the 2010 WTA Tour.  The men's event was held at the Rexall Centre in Toronto, Ontario, Canada, from August 7 through August 15, 2010.  The women's event was held at the Uniprix Stadium in Montreal, Quebec, Canada, from August 13 through August 23, 2010.  It was scheduled to end August 22 but some of the matches were postponed to August 23 due to rain.

Gil Reyes (tennis): Gil Reyes (born 1952) is an American fitness trainer who spent seventeen years as the strength and conditioning trainer for retired tennis player Andre Agassi, from 1989 until Agassi's retirement in 2006.  He was also considered one of Agassi's closest friends and confidants.

Question: What British tennis player from Scotland became the first player since Andre Agassi to successfully defend the 2010 Rogers Cup – Men's Singles?  

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the tennis player."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the player."
    },
    "origin_region": {
      "type": "string",
      "description": "The specific region or country of origin within their nationality."
    },
    "tournament_details": {
      "type": "object",
      "properties": {
        "tournament_name": {
          "type": "string",
          "description": "The name of the tournament."
        },
        "year": {
          "type": "integer",
          "description": "The year the tournament took place."
        },
        "event_type": {
          "type": "string",
          "description": "The specific event type within the tournament (e.g., Men's Singles)."
        }
      },
      "required": [
        "tournament_name",
        "year",
        "event_type"
      ],
      "additionalProperties": false
    },
    "achievement_description": {
      "type": "string",
      "description": "A description of the player's achievement in the tournament."
    },
    "comparison_player": {
      "type": "string",
      "description": "The name of the player who previously achieved the same feat, setting a comparison point."
    }
  },
  "required": [
    "player_name",
    "nationality",
    "origin_region",
    "tournament_details",
    "achievement_description",
    "comparison_player"
  ],
  "additionalProperties": false
}
