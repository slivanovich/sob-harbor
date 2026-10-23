{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nStrikeforce: Fedor vs. Rogers: Strikeforce/M-1 Global: Fedor vs. Rogers was a mixed martial arts event held on November 7, 2009 promoted by Strikeforce in association with M-1 Global.  It was the first MMA event on network television since the now-defunct EliteXC promotion broadcast its final event, , on CBS on October 4, 2008.  The event had a four-fight main card with a broadcasting team of Gus Johnson, Frank Shamrock and Mauro Ranallo.  The event drew an estimated 4,040,000 viewers, with a peak at 5,460,000 on CBS.\n\nInside MMA: Inside MMA was a live mixed martial arts news magazine, which aired on AXS TV, immediately following the network's live AXS TV Fights broadcasts.  Hosted by Mauro Ranallo and UFC Hall of Famer Bas Rutten, the series provided an in-depth look at the world of MMA, with live breakdowns, talk, highlights, and analysis from major MMA organizations such as the UFC, Bellator, and the World Series of Fighting.  \"Inside MMA\" debuted on AXS TV, then known as HDNET, in September 2007, and was the longest-running MMA news show on television.\n\nFloyd Mayweather Jr. vs. Conor McGregor: Floyd Mayweather Jr. vs. Conor McGregor, also known as \"The Money Fight\" and \"The Biggest Fight in Combat Sports History\", was a professional boxing match between undefeated eleven-time five-division boxing world champion Floyd Mayweather Jr. and two-division mixed martial arts (MMA) world champion and at-the-time current UFC Lightweight Champion Conor McGregor.  The match took place at the T-Mobile Arena in Paradise, Nevada, on August 26, 2017 at the light-middleweight weight class (154 lbs; 69.9 kgs).  It was scheduled for twelve rounds.\n\nShowtime Championship Boxing: Showtime Championship Boxing is a television boxing program airing on Showtime.  Debuting in March 1986, it is broadcast live on the first Saturday of every month.  \"Showtime Championship Boxing\", which is very similar to \"HBO World Championship Boxing\", features Mauro Ranallo on play-by-play, Al Bernstein as the color analyst, Jimmy Lennon (Sr. and Jr.) as announcers, and Jim Gray as reporter.\n\nMauro Sérgio Martins Viana: Mauro Sérgio Martins Viana (born 22 May 1984), known as Mauro Viana or simply \"Mauro\", is a Brazilian footballer who plays for Uberlândia as a Defender.\n\nMauro (footballer): Bruno Mauro Nunes da Silva (born 5 May 1986), more commonly known as Mauro is a retired Angolan footballer who played mainly as a winger.  Mauro was a journeyman who played in various teams in Portugal, as well as Cyprus and Greece.\n\nCarlos Mauro Pereira da Silva: Carlos Mauro Pereira da Silva (born 10 August 1978) also known as Mauro or Mauro Silva was a Brazilian footballer.\n\nAbner Mares vs. Joseph Agbeko: Abner Mares vs. Joseph Agbeko was a championship fight for the WBC Silver & IBF Bantamweight championships.  The bout was held on August 13, 2011, at Hard Rock Hotel and Casino, Las Vegas, Nevada, United States, and was televised on Showtime.  The bout was marred in controversy due to the prevalence of low blows by Mares that went unpenalized by referee Russell Mora.\n\nFloyd Mayweather Jr. vs. Robert Guerrero: Floyd Mayweather Jr. vs. Robert Guerrero, billed as May Day, was a boxing welterweight championship superfight for Mayweather's World Boxing Council (WBC) Welterweight title and vacant \"Ring\" Welterweight title.  The bout was held on May 4, 2013, in the MGM Grand Garden Arena at the MGM Grand Hotel & Casino in Las Vegas, Nevada, United States on Showtime PPV.  The bout was the first major televised fight of Mayweather's career to not be aired on HBO PPV.  The card featured some of the rising stars of Mayweather Promotions: J'Leon Love, Badou Jack, Luis Arias, Ronald Gavril and Lanell Bellows.  Mayweather won via unanimous decision with Guerrero winning the first 3 rounds, then Mayweather adjusted and won from the 4th to 12th round.\n\nMauro Ranallo: Mauro Domenico Ranallo (born December 21, 1969) is a Canadian sports announcer and commentator.  He is currently signed as a play-by-play announcer with MMA organization Bellator, professional wrestling promotion WWE (on their NXT brand) and also performs play-by-play duties for boxing broadcaster Showtime, most notably, the Floyd Mayweather Jr. vs. Conor McGregor bout.  He began announcing when he was 16 years old and is notable for his dramatic style, which involves heavy use of metaphor, puns, and an advanced vocabulary.  He has experience in Canadian football, ice hockey, professional wrestling, boxing, kickboxing, and mixed martial arts events.\n\nQuestion: Mauro Ranallo was a Showtime broadcaster for the bout that was known as what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"broadcaster_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the broadcaster.\"\n    },\n    \"event_official_name\": {\n      \"type\": \"string\",\n      \"description\": \"The official name of the boxing event.\"\n    },\n    \"event_alternative_names\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other names by which the event was known.\"\n    },\n    \"broadcasting_network\": {\n      \"type\": \"string\",\n      \"description\": \"The television network that broadcasted the event.\"\n    },\n    \"broadcasting_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the broadcaster during the event.\"\n    }\n  },\n  \"required\": [\n    \"broadcaster_name\",\n    \"event_official_name\",\n    \"event_alternative_names\",\n    \"broadcasting_network\",\n    \"broadcasting_role\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "broadcaster_name": {
        "type": "string",
        "description": "The name of the broadcaster."
      },
      "event_official_name": {
        "type": "string",
        "description": "The official name of the boxing event."
      },
      "event_alternative_names": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other names by which the event was known."
      },
      "broadcasting_network": {
        "type": "string",
        "description": "The television network that broadcasted the event."
      },
      "broadcasting_role": {
        "type": "string",
        "description": "The role of the broadcaster during the event."
      }
    },
    "required": [
      "broadcaster_name",
      "event_official_name",
      "event_alternative_names",
      "broadcasting_network",
      "broadcasting_role"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
