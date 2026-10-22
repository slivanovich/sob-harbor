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
2015 Apia International Sydney – Women's Doubles: Tímea Babos and Lucie Šafářová were the defending champions, but chose not to participate together.  Babos played alongside Kristina Mladenovic, but lost in the semifinals to Raquel Kops-Jones and Abigail Spears.  Šafářová teamed up with Belinda Bencic, but lost in the first round to Kimiko Date-Krumm and Karolína Plíšková. <br>

2017 Miami Open – Women's Doubles: Bethanie Mattek-Sands and Lucie Šafářová were the defending champions, but lost in the second round to Andreja Klepač and María José Martínez Sánchez.

Conchita Martínez: Conchita Martínez Bernat (born 16 April 1972) is a Spanish former professional tennis player.  She was the first Spanish player to win the women's singles title at Wimbledon, where she beat Martina Navratilova to win the 1994 title.  Martínez also was the singles runner-up at the 1998 Australian Open and the 2000 French Open.  She reached a highest world ranking of No. 2 in October 1995 and finished the season in the top 10 for nine years.  Martínez won 33 singles and 13 doubles titles during her 18-year career.  She is currently the captain of the Spain Fed Cup team and the Spain Davis Cup team.

Lucie Šafářová career statistics: This list summarizes the main career statistics of Czech professional tennis player Lucie Šafářová.  To date, Šafářová has won seven WTA singles titles and fifteen WTA doubles titles including five Grand Slam doubles titles with Bethanie Mattek-Sands at the 2015 Australian Open and French Open,; the 2016 US Open and 2017 Australian Open and French Open.  Other highlights of Šafářová's career thus far include winning the 2015 Qatar Total Open, reaching the final of the 2015 French Open and making quarterfinal and semifinal appearances at the 2007 Australian Open and 2014 Wimbledon Championships, respectively.  Šafářová achieved career high singles and doubles rankings of World No. 5 and World No. 2 on 14 September 2015 and 30 January 2017.

2014 Family Circle Cup – Doubles: Kristina Mladenovic and Lucie Šafářová were the defending champions, but Mladenovic chose not to participate this year.  Šafářová played alongside Květa Peschke, but they lost in the first round to Chan Hao-ching and Chan Yung-jan.

2016 Rogers Cup – Women's Doubles: Bethanie Mattek-Sands and Lucie Šafářová were the defending champions, but decided not to compete together.  Mattek-Sands played alongside Heather Watson, but lost in the quarterfinals to Andreja Klepač and Katarina Srebotnik.  Šafářová teamed up with Tímea Babos, but lost in the first round to Kateryna Bondarenko and Olga Savchuk.

Lucie Šafářová: Lucie Šafářová (] ; born 4 February 1987) is a Czech professional tennis player from Brno.  She is currently the WTA world No. 1 doubles player.  Šafářová has won seven WTA tour singles titles, fifteen doubles titles and reached the quarterfinals of the 2007 Australian Open by upsetting defending champion Amélie Mauresmo in the fourth round.  She reached her first Grand Slam semifinal at the 2014 Wimbledon Championships and her first Grand Slam final at the 2015 French Open.  She also won the 2015 Australian Open, 2015 French Open, 2016 US Open, 2017 Australian Open and 2017 French Open women's doubles titles partnering with Bethanie Mattek-Sands.

2016 Porsche Tennis Grand Prix – Doubles: Bethanie Mattek-Sands and Lucie Šafářová were the defending champions, but Mattek-Sands chose not to participate this year.  Šafářová played alongside Sabine Lisicki, but lost in the semifinals to Martina Hingis and Sania Mirza. <br>

2016 Australian Open – Women's Doubles: Bethanie Mattek-Sands and Lucie Šafářová were the defending champions, but Šafářová withdrew before the tournament due to a bacterial infection.  Mattek-Sands played alongside Sabine Lisicki, but lost in the second round to Anastasia and Arina Rodionova.

2017 US Open – Women's Doubles: Bethanie Mattek-Sands and Lucie Šafářová were the defending champions, but Mattek-Sands was unable to compete due to injury.  Šafářová played alongside Barbora Strýcová, but lost in the semifinals to Lucie Hradecká and Kateřina Siniaková.

Question: Who won more doubles titles, Conchita Martínez or Lucie Šafářová?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_comparison": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "player_name": {
            "type": "string"
          },
          "doubles_titles_won": {
            "type": "integer",
            "minimum": 0
          }
        },
        "required": [
          "player_name",
          "doubles_titles_won"
        ],
        "additionalProperties": false
      }
    },
    "player_with_most_doubles_titles": {
      "type": "string"
    },
    "most_doubles_titles_count": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": [
    "player_comparison",
    "player_with_most_doubles_titles",
    "most_doubles_titles_count"
  ],
  "additionalProperties": false
}
