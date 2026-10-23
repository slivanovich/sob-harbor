{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSue Barker: Susan Barker, OBE (born 19 April 1956 in Paignton, Devon) is an English television presenter and former professional tennis player.  During her tennis career, she won eleven WTA Tour singles titles, including one Grand Slam singles title at the 1976 French Open.  She reached a career-high singles ranking of World No. 3.  She is now one of the main sports presenters at the BBC, most notably fronting the corporation’s coverage of Wimbledon and A Question of Sport.\n\nÓscar Serrano (tennis): Óscar Serrano Gámez (born 25 May 1978, in Barcelona, Catalonia) is a former Spanish professional male tennis player.  Currently, as June 2010, Oscar Serrano is the coach of Fabio Fognini.\n\nSimone Bolelli: Simone Bolelli (born 8 October 1985; ] ) is an Italian professional tennis player.  Bolelli is a Grand Slam champion since he won the 2015 Australian Open doubles event with Fabio Fognini, becoming the first all Italian men's pair to win a Grand Slam title in the Open Era.\n\nAdam Pavlásek: Adam Pavlásek (born 8 October 1994) is a tennis player playing on the ATP Challenger Tour from the Czech Republic.  He reached his career-high ATP singles ranking of World No. 72 in January 2017.  At the start of 2015, Pavlásek replaced injured countryman Radek Štěpánek in the Hopman Cup, playing alongside Lucie Šafářová.  He made a name for himself by defeating world number 20 Fabio Fognini of Italy, Pavlásek's first ever win over a top 20 player.\n\n1975 Austrian Open (tennis): The 1975 Austrian Open was a combined men's and women's tennis tournament played on outdoor clay courts.  It was categorized as Grade B tournament and was part of the 1975 Commercial Union Assurance Grand Prix circuit.  It took place at the Tennis stadium Kitzbühel in Kitzbühel  Austria and was held from 7 July through 13 July 1975.  Adriano Panatta and Sue Barker won the singles titles.\n\n2013 International German Open: The 2013 International German Open (also known as the bet–at–home Open – German Tennis Championships 2013 for sponsorship reasons) was a men's tennis tournament played on outdoor red clay courts.  It was the 107th edition of the event known that year as the International German Open and was part of the ATP World Tour 500 series of the 2013 ATP World Tour.  It took place at the Am Rothenbaum in Hamburg, Germany, from 14 July through 22 July 2013.  Twelfth-seeded Fabio Fognini won the singles title.\n\nKavita Chahal: \"Kavita Chahal\"' (born 8 April 1985) is a 5' 9\" tall heavyweight Indian female boxer and recipient of the highest world ranking 2 from 2012 to 2014 (AIBA Ranking - 11 in 2016) from the village Nimri which resides in the Bhiwani district, Haryana.  In recognition of her achievements, the Government of India presented Chahal with the Arjuna Award in 2013.  Chahal is the first female boxer from Haryana to be presented with the Arjuna Award.  Chahal is a twice-consecutive World Championship medallist, 2 Time Gold medalist in World Police Games 2017 Los Angeles And 2013 in Northern Ireland .  4-Time Asian championship, Asian cup medallist.  With 8 gold medals, she is a record holder in women's national championship boxing.  She is a 5-time gold medallist in the Federation Cup, and 5-times Gold medalist in all india police games 2012 to 2017.  Chahal 3-time gold medallist in the Inter-zonal Super Cup championship.\n\nFabio Fognini: Fabio Fognini (] ; born 24 May 1987) is an Italian professional tennis player who is currently ranked world No. 29 in men's singles by the Association of Tennis Professionals (ATP) and the current Italian No. 1.  His career-high singles ranking is world No. 13, achieved in March 2014, and world No. 7 in doubles, achieved in July 2015.  Fognini's most successful surface is red clay, upon which he won his four ATP singles titles in Stuttgart, Hamburg, Viña del Mar and Umag, reached the quarterfinals of the 2011 French Open and the semifinals of the 2013 Monte-Carlo Masters.  Together with Simone Bolelli, Fognini won the 2015 Australian Open doubles event, becoming the first all Italian men's pair to win a Grand Slam title in the Open era.\n\nConchita Martínez: Conchita Martínez Bernat (born 16 April 1972) is a Spanish former professional tennis player.  She was the first Spanish player to win the women's singles title at Wimbledon, where she beat Martina Navratilova to win the 1994 title.  Martínez also was the singles runner-up at the 1998 Australian Open and the 2000 French Open.  She reached a highest world ranking of No. 2 in October 1995 and finished the season in the top 10 for nine years.  Martínez won 33 singles and 13 doubles titles during her 18-year career.  She is currently the captain of the Spain Fed Cup team and the Spain Davis Cup team.\n\nPaolo Lorenzi: Paolo Lorenzi (] ; born 15 December 1981 in Rome, Italy) is an Italian professional tennis player, and current Italian No. 2.  His career-high singles ranking is World No. 33.  Lorenzi is coached by Claudio Galoppini.  On August 1, 2016 he overtook Fabio Fognini becoming the new Italian #1 in the Association of Tennis Professionals ATP Ranking at the age of 34 years old and 8 months.\n\nQuestion: Has Sue Barker or Fabio Fognini been held the highest world ranking in tennis?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"highest_ranked_player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the player who achieved the highest world ranking.\"\n    },\n    \"highest_ranked_player_singles_ranking\": {\n      \"type\": \"integer\",\n      \"description\": \"The career-high singles ranking of the highest ranked player.\"\n    },\n    \"other_player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the other player in the comparison.\"\n    },\n    \"other_player_singles_ranking\": {\n      \"type\": \"integer\",\n      \"description\": \"The career-high singles ranking of the other player.\"\n    },\n    \"is_sue_barker_highest\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if Sue Barker held the highest world ranking, false otherwise.\"\n    },\n    \"is_fabio_fognini_highest\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if Fabio Fognini held the highest world ranking, false otherwise.\"\n    }\n  },\n  \"required\": [\n    \"highest_ranked_player_name\",\n    \"highest_ranked_player_singles_ranking\",\n    \"other_player_name\",\n    \"other_player_singles_ranking\",\n    \"is_sue_barker_highest\",\n    \"is_fabio_fognini_highest\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "highest_ranked_player_name": {
        "type": "string",
        "description": "The name of the player who achieved the highest world ranking."
      },
      "highest_ranked_player_singles_ranking": {
        "type": "integer",
        "description": "The career-high singles ranking of the highest ranked player."
      },
      "other_player_name": {
        "type": "string",
        "description": "The name of the other player in the comparison."
      },
      "other_player_singles_ranking": {
        "type": "integer",
        "description": "The career-high singles ranking of the other player."
      },
      "is_sue_barker_highest": {
        "type": "boolean",
        "description": "True if Sue Barker held the highest world ranking, false otherwise."
      },
      "is_fabio_fognini_highest": {
        "type": "boolean",
        "description": "True if Fabio Fognini held the highest world ranking, false otherwise."
      }
    },
    "required": [
      "highest_ranked_player_name",
      "highest_ranked_player_singles_ranking",
      "other_player_name",
      "other_player_singles_ranking",
      "is_sue_barker_highest",
      "is_fabio_fognini_highest"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
