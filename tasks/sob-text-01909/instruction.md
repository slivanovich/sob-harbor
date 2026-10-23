{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nViacheslav Zhukov: Viacheslav Zhukov (c. 1989) is a Russian professional poker player who has won two World Series of Poker bracelets. Prior to becoming a professional poker player, Zhukov was a geologist in Russia.  he has career earnings of $940,000, $838,000 of which was earned at the World Series of Poker.\n\nTommy Angelo (poker player): Tommy Angelo (born August 25, 1958) is an Oakland, California professional poker player, writer, and coach.  Angelo was a career musician in the 1980's, performing rock and country on drums and piano.  In 1990, he became a full-time professional poker player.  Since then has since written 100 magazine articles, written and produced 18 poker training videos, and written and published three books on poker.\n\nHoward Lederer: Howard Henry Lederer (born October 30, 1963) is an American professional poker player.  He has won two World Series of Poker bracelets and holds two World Poker Tour titles.  Lederer has also contributed to several books on poker strategy and has provided commentary for poker programming.  He is known by poker fans and players as \"The Professor\" and is the older brother of professional poker player Annie Duke.\n\nHeresy (radio series): Heresy is a comedy talk show on BBC Radio 4, created and originally hosted by David Baddiel, now hosted by Victoria Coren Mitchell.  In the show, the presenter and a panel of guests commit \"heresy\" by challenging people's most deeply received opinions on a subject, in front of a studio audience.\n\nBilly Baxter (poker player): William E. Baxter, Jr. (born 1940) is an American professional poker player and sports bettor.  He has won numerous tournament titles in his career as a professional poker player, including seven World Series of Poker bracelets.\n\nAndy Frankenberger: Andy Frankenberger is a professional poker player and former equity derivatives trader from New York City.  In his first year as a professional poker player, Frankenberger was named World Poker Tour (WPT) Season IX Player of the Year.  Card Player Magazine described this as one of poker's best rookie years in a September 2011 cover story.  Frankenberger followed this up by winning back to back bracelets at the World Series of Poker in 2011 and 2012.  He has been prominently featured in financial media including The Wall Street Journal, Fox Business Network, and Bloomberg Television.\n\nVictoria Coren Mitchell: Victoria Elizabeth Coren Mitchell (born Victoria Elizabeth Coren; 18 August 1972) is an English writer, presenter and professional poker player.  Coren Mitchell writes weekly columns for \"The Observer\" and has hosted the BBC television quiz show \"Only Connect\" since 2008.\n\nDaniel Negreanu: Daniel Negreanu ( ; born July 26, 1974) is a Canadian professional poker player who has won six World Series of Poker (WSOP) bracelets and two World Poker Tour (WPT) championship titles.  The independent poker ranking service Global Poker Index (GPI) recognised Negreanu as the best poker player of the decade in 2014.\n\nDag Palovic: Dag Palovič (* 4 January 1975, Bratislava) is a Slovak professional poker player, businessman and a former TV host.  Since 1 January 2011, he is a member of PokerStars Team Pro, first and as of October 2011 only sponsored poker player from Slovakia.  He is best known for making two European Poker Tour (EPT) final tables as well as being the only player from Slovakia who has cashed in the World Series of Poker (WSOP) Main Event, finishing 120th in 2009 and 37th in 2010.  As of March 2013, he is second leading Slovak all time money list with career earnings of $909,405 and is also an author of first Slovak poker book on poker titled \"Ako sa stať poker pro\" (How to become a poker pro), co-authored by 1983 World Series Of Poker champion Tom McEvoy.  From 2000 until 2004 he was CEO and Chairman Of The Board of Directors of \"ad pepper media Slovakia, a.s.\", the daughter company of one of the world´s leading e-Adverising german-dutch agency \"ad pepper media International N.V.\" for Slovak and Czech Republic.\n\nDavid Catapano: David Catapano is an American celebrity chef, professional poker player, and reality television personality.  He is known for his mastery in Italian Cuisine and his self-developed \"Twisted Mediterranean\" style.  However, he is most notable for having appeared on a wide variety of cooking TV shows, including the long-running FoodyTV show \"Italian Style with Chef Catman\" and \"Food Network\" shows such as iron chef and chopped.  Over the years he pioneered several catchphrases, including \"My Kitchen, My rules!\" , \"Bada Bing!\"  and \"Why, No?\"  Catapano is an avid poker player and has played professionally and for large charity events.  Sometimes billed a Celebrity Poker Player because of his chef profile.\n\nQuestion: What is the birthdate of this English writer, presenter, and professional poker player, who hosts Heresy?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the person.\"\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the person in 'Day Month Year' format.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the person.\"\n    },\n    \"professions\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of professions or roles held by the person.\"\n    },\n    \"hosted_shows\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of shows or programs hosted by the person.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"birth_date\",\n    \"nationality\",\n    \"professions\",\n    \"hosted_shows\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The full name of the person."
      },
      "birth_date": {
        "type": "string",
        "description": "The birth date of the person in 'Day Month Year' format."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the person."
      },
      "professions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of professions or roles held by the person."
      },
      "hosted_shows": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of shows or programs hosted by the person."
      }
    },
    "required": [
      "person_name",
      "birth_date",
      "nationality",
      "professions",
      "hosted_shows"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
