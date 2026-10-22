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
David Adams (tennis): David Adams (born 5 January 1970) is a former professional tennis player from South Africa.  He turned pro in 1989.  During his career he won 19 doubles titles and finished runner-up an additional 33 times, including at the French Open in 1992.  He achieved a career-high doubles ranking of World No. 9 in February 1994.

Lucie Šafářová career statistics: This list summarizes the main career statistics of Czech professional tennis player Lucie Šafářová.  To date, Šafářová has won seven WTA singles titles and fifteen WTA doubles titles including five Grand Slam doubles titles with Bethanie Mattek-Sands at the 2015 Australian Open and French Open,; the 2016 US Open and 2017 Australian Open and French Open.  Other highlights of Šafářová's career thus far include winning the 2015 Qatar Total Open, reaching the final of the 2015 French Open and making quarterfinal and semifinal appearances at the 2007 Australian Open and 2014 Wimbledon Championships, respectively.  Šafářová achieved career high singles and doubles rankings of World No. 5 and World No. 2 on 14 September 2015 and 30 January 2017.

Fred McNair: Frederick V. McNair IV (born July 22, 1950 in Washington, D.C.) is a former professional tennis player from the United States who reached the World No. 1 doubles ranking in 1976.  That year, he teamed up with Sherwood Stewart to capture the men's doubles titles at French Open, the German Open and the Masters.  McNair was also a mixed doubles runner-up at the French Open in 1981, partnering Betty Stöve.  In 1978, he was a member of the US team that won the Davis Cup.  In nine years on the professional tour, McNair won 16 doubles titles.  His career-high singles ranking was World No. 67.

Lucie Šafářová: Lucie Šafářová (] ; born 4 February 1987) is a Czech professional tennis player from Brno.  She is currently the WTA world No. 1 doubles player.  Šafářová has won seven WTA tour singles titles, fifteen doubles titles and reached the quarterfinals of the 2007 Australian Open by upsetting defending champion Amélie Mauresmo in the fourth round.  She reached her first Grand Slam semifinal at the 2014 Wimbledon Championships and her first Grand Slam final at the 2015 French Open.  She also won the 2015 Australian Open, 2015 French Open, 2016 US Open, 2017 Australian Open and 2017 French Open women's doubles titles partnering with Bethanie Mattek-Sands.

Martin Legner: Martin Legner (born December 17, 1961 in Tyrol) is a professional Austrian wheelchair tennis player who has been ranked number one for wheelchair doubles.  Legner has won the Australian Open doubles title four times with Robin Ammerlaan since 2000, and has won eight doubles titles.  Six of them are Australian Open Titles, the other two being French Open titles.  He has won one French Open and one Australian Open singles title.  He has represented his country at every Summer Paralympics since 1992, and has competed in both singles and doubles at all of those Games.  His favorite surfaces are clay and hard court.  As of April 7, 2007 his highest singles rank was number three.  Also of that date, he was ranked number six for singles and doubles.  His wheelchair is manufactured by Kronbickler.  Legner is a fan of Bob Marley, and listens to his music aside from tennis.

Garbiñe Muguruza career statistics: This is a list of the main career statistics of Spanish professional tennis player, Garbiñe Muguruza.  To date, Muguruza has won five WTA singles titles – most significantly the 2016 French Open and the 2017 Wimbledon Championships– and five WTA doubles titles.  Other highlights of Muguruza's career thus far include reaching the final of the 2015 Wimbledon Championships, quarterfinal appearances at the French Open in 2014 and 2015; two runner-up finishes in doubles at the Madrid Open in 2014 and 2015 and a semi-final appearance in doubles at the 2014 French Open alongside Carla Suárez Navarro.

Ashleigh Barty: Ashleigh Barty (born 24 April 1996) is an Australian professional tennis player and cricketer.  Barty first gained media attention by reaching the doubles final of the 2013 Australian Open, partnered by Casey Dellacqua.  The pair also reached the finals of both Wimbledon and the US Open in 2013, making Barty one of the most successful WTA debutants in history.  In 2017, while again partnering with Dellacqua, Ashleigh finished runner-up at the French Open in the women's doubles which means that she has now made the women's doubles final in each of the four grand slams.  She also won the 2011 Wimbledon Girls' Championships title and has won three WTA doubles titles so far in her career.  In September 2014, she took a break from tennis and switched to cricket in 2015, earning a contract with the Brisbane Heat for the inaugural Women's Big Bash League.  In February 2016 she resumed her career in tennis.

Andrea Jaeger: Andrea Jaeger ( ; born June 4, 1965) is a former World No. 2 professional tennis player from the United States whose brief but highly successful tennis career ended prematurely due to major shoulder injuries.  Jaeger reached the singles final of Wimbledon in 1983 and the French Open in 1982.  She reached the singles semifinals of the Australian Open in 1982 and of the U.S. Open in 1980 and 1982.  She also won 10 singles titles.  In mixed doubles, Jaeger won the French Open with Jimmy Arias in 1981.  During her career, Jaeger won U.S. $1.4 million in prize money and millions more in endorsements.  After retirement in 1987, she has prominently dedicated her life to public service, charities, and philanthropy.  In 2006, she became "Sister Andrea" as a member of the Anglican Order of Preachers.  She is a member of the Episcopal Church and based in Santa Rosa Beach, Florida, U.S.

Samantha Stosur career statistics: This is a list of the main career statistics of professional Australian tennis player, Samantha Stosur.  To date, Stosur has won eight WTA singles titles including one Grand Slam singles title at the 2011 US Open.  She was also the runner-up at the 2010 French Open and a semi-finalist at the 2010 and 2011 WTA Tour Championships.  Stosur has also enjoyed a successful doubles career, in which she has held the World No. 1 ranking and won twenty-four WTA doubles titles including two grand slam women's doubles titles at the 2005 US Open and 2006 French Open and two year-ending championships at the 2005 and 2006 WTA Tour Championships.

Jimmy Arias: James Arias (born August 16, 1964) is a former tennis touring professional player from the United States.

Question: Who won 19 doubles titles and finished runner-up an additional 33 times, including at the French Open in 1992, David Adams or Jimmy Arias?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the tennis player who matches the description."
    },
    "doubles_titles_won": {
      "type": "integer",
      "description": "The total number of doubles titles won by the player."
    },
    "doubles_runner_up_finishes": {
      "type": "integer",
      "description": "The total number of times the player finished as a runner-up in doubles."
    },
    "notable_runner_up_event": {
      "type": "string",
      "description": "A specific Grand Slam event where the player was a runner-up, if mentioned."
    },
    "notable_runner_up_year": {
      "type": "integer",
      "description": "The year of the notable runner-up event."
    },
    "comparison_player_name": {
      "type": "string",
      "description": "The name of the other player mentioned in the question for comparison."
    },
    "comparison_player_details_available": {
      "type": "boolean",
      "description": "Indicates whether relevant career details (like doubles titles/runner-up finishes) for the comparison player were found in the context."
    }
  },
  "required": [
    "player_name",
    "doubles_titles_won",
    "doubles_runner_up_finishes",
    "notable_runner_up_event",
    "notable_runner_up_year",
    "comparison_player_name",
    "comparison_player_details_available"
  ],
  "additionalProperties": false
}
