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
Teresa Ciepły: Teresa Barbara Ciepły ("née" Wieczorek; 19 October 1937 – 8 March 2006) was a Polish sprinter and hurdler.  She was a bronze Olympic medalist in the 4×100 metre relay at the 1960 Summer Olympics.  Two years later she won gold medals in the 4 × 100 m relay (in European record time of 44.5 seconds) and the 80 m hurdles, and a bronze medal in the 100 m sprint at the 1962 European Championships.  The same year she was chosen as the Polish Sportspersonality of the year.  At the 1964 Olympics she won a gold medal in the 4 × 100 m relay, in a world record time of 43.6 seconds, and a silver in the 80 m hurdles.  Nationally Ciepły won the Polish titles in the 80 m hurdles (1961–62, 1964–1965) and in the 100 m sprint (1960–1962).

Sally Pearson: Sally Pearson, OAM (née McLellan; born 19 September 1986) is an Australian athlete.  She is the 2011 and 2017 World champion and 2012 Olympic champion in the 100 metres hurdles.  She also won a silver medal in the 100 m hurdles at the 2008 Summer Olympics and the 2013 World Championships.

Canada at the 2008 Summer Olympics: Canada, which is represented by the Canadian Olympic Committee (COC), competed at the 2008 Summer Olympics in Beijing, People's Republic of China, from August 8 to 24, 2008.  Canadian athletes have competed in every Summer Olympic Games since 1900, except the 1980 Summer Olympics which they boycotted.  Canada sent 332 athletes in 25 sports, the seventh largest team at the games and Canada's largest since 1988.  Canada did not send a team in handball, volleyball or basketball.  Kayaker and 2004 Summer Olympics gold medalist Adam van Koeverden was the flag bearer at the opening ceremonies; Karen Cockburn bore the flag at the closing.

Park Tae-hwan: Park Tae-hwan (Korean: 박태환, ] ; born September 27, 1989) is a South Korean competitive swimmer who is an Olympic gold medalist and world champion.  He has four Olympic medals, five world titles, and 20 Asian Games medals.  He won a gold medal in the 400-meter freestyle and a silver in the 200-meter freestyle events at the 2008 Summer Olympics.  He also won two silver medals at the 2012 Summer Olympics in the 200- and 400-meter freestyle.  He is the first Asian swimmer to claim a gold medal in the men's 400-meter freestyle, and the first-ever South Korean swimmer to win any Olympic medal in swimming.  He also holds 3 Asian Records, all in Men's Freestyle.  He is best known for his impressive range and versatility, as he is able to compete at international level in 100-, 200-, 400- and 1,500-meter freestyle.

Sherone Simpson: Sherone Simpson (born 12 August 1984) is a Jamaican track and field sprint athlete.  She is a gold medalist in the 4 × 100 m relay from the 2004 Olympics and silver medalist in 2005 World Championships and now is the silver medalist in the individual event at the 2008 Summer Olympics, after she tied for second with Kerron Stewart in a photo finish.

Dominic Seiterle: Dominic Seiterle (born 1975) is a Canadian rower born in Montreal, Quebec.  He is a 2008 Summer Olympics and World Rowing Championships gold medalist as a member of the 8+.  He also won three gold medals at the 2007 World Rowing Cup regattas and gold at the 2007 Henley Royal Regatta.  Previous to this, he was 2006 Canadian National Rowing Gold medalist in the single scull and came 13th at the 2000 Summer Olympics in the double sculls.

Rowdy Gaines: Ambrose "Rowdy" Gaines, IV (born February 17, 1959) is an American former competitive swimmer, U.S. Olympic Hall of Fame member, three-time Olympic gold medalist, and member of the International Swimming Hall of Fame.  He is the chief fundraiser for USA Swimming as well as a swimming analyst for television networks ESPN and NBC.  He covered the Beijing 2008 Summer Olympics, the London 2012 Summer Olympics, and the Rio 2016 Summer Olympics.

Australia at the World Championships in Athletics: Australia has participated in all the World Championships in Athletics since the beginning in 1983.  Australia is 19th on the all time medal table.  Cathy Freeman, Jana Pittman and Sally Pearson are Australia's only multiple gold medal winners, Freeman (bronze) and Pearson (silver) have also each won a place medal. .  Other multiple medalists are: Dimitri Markov (1 gold, 1 silver), (2 golds), Jared Tallent (1 silver, 2 bronzes), Kerry Saxby-Junna (1 silver, 1 bronze) and Mitchell Watt (1 silver, 1 bronze).  Australia's first World Championships medal was won by Robert De Castella in the Men's marathon in 1983.  He won gold.

Leisel Jones: Leisel Marie Jones, OAM (born 30 August 1985) is an Australian former competition swimmer and Olympic gold medallist.  A participant in the 2000 Summer Olympics – at just 15 years old – and 2004 Summer Olympics, she was part of gold-medal-winning Australian team in the women's 4×100-metre medley relay at the Athens Games in 2004 and a gold medalist for 100-meter breaststroke in the 2008 Summer Olympics in Beijing.

Sanya Richards-Ross: Sanya Richards-Ross (born February 26, 1985) is a Jamaican-American former track and field athlete who competed internationally for the United States.  At the 2012 Summer Olympics, she won gold in the 400 metres after finishing third at the 2008 Summer Olympics.  Richards-Ross has also won Olympic gold in the 4×400 meters relay at the 2004 Summer Olympics, the 2008 Summer Olympics, and the 2012 Summer Olympics.  She was the best 400m runner in the world for a decade, ranking No. 1 in the world from 2005-2009 and again in 2012.

Question: which multiple Australian gold medalist won the 100m hurdles at the 2008 Summer Olympics?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "athlete_name": {
      "type": "string",
      "description": "The name of the athlete."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the athlete."
    },
    "olympic_games_year_of_event": {
      "type": "integer",
      "description": "The year of the Summer Olympics where the event took place."
    },
    "event_name": {
      "type": "string",
      "description": "The name of the athletic event."
    },
    "medal_won_at_event": {
      "type": "string",
      "description": "The type of medal won by the athlete in the specified event and year."
    },
    "is_overall_multiple_gold_medalist": {
      "type": "boolean",
      "description": "Indicates if the athlete is recognized as an overall multiple gold medalist across their career."
    },
    "gold_medal_achievements": {
      "type": "array",
      "description": "A list of specific gold medal achievements by the athlete.",
      "items": {
        "type": "object",
        "properties": {
          "championship_type": {
            "type": "string",
            "description": "The type of championship (e.g., 'Olympic Games', 'World Championships')."
          },
          "year": {
            "type": "integer",
            "description": "The year the gold medal was won."
          },
          "event": {
            "type": "string",
            "description": "The event in which the gold medal was won."
          }
        },
        "required": [
          "championship_type",
          "year",
          "event"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "athlete_name",
    "nationality",
    "olympic_games_year_of_event",
    "event_name",
    "medal_won_at_event",
    "is_overall_multiple_gold_medalist",
    "gold_medal_achievements"
  ],
  "additionalProperties": false
}
