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
Angelė Rupšienė: Angelė Rupšienė (née Jankūnaitė; born 27 June 1952 in Vilnius, Lithuanian SSR) is a retired Lithuanian professional basketball player, who most notably played for BC Kibirkštis Vilnius.  She won two gold medals in the 1976 Montreal Olympic games and 1980 Moscow Olympic games, three gold medals during European Championship and two gold medals during World Championship, playing for Soviet Union national basketball team.

Jonas Jacobsson: Jonas Jacobsson (born 22 June 1965) is a Swedish sport shooter who has won several gold medals at the Paralympic Games.  He has participated in nine consecutive Summer Paralympics from 1980 to 2012, winning a total of seventeen gold, two silver, and nine bronze medals.  In 1996, he won two gold medals in the air rifle 3×40 and English match events and a bronze in the air rifle prone at the Atlanta Paralympics.  At the 2000 Summer Paralympics, he took two gold medals in the free rifle 3×40 and free rifle prone events and two bronzes in air rifle standing and air rifle prone events.  Four years later, at the Athens Games, he competed in the same four events and won the gold medal in all of them.

Rebecca Adlington: Rebecca Adlington, OBE (born 17 February 1989) is an English former competitive swimmer who specialised in freestyle events in international competition.  She won two gold medals at the 2008 Summer Olympics in the 400-metre freestyle and 800-metre freestyle, breaking the 19-year-old world record of Janet Evans in the 800-metre final.  Adlington was Britain's first Olympic swimming champion since 1988, and the first British swimmer to win two Olympic gold medals since 1908.  She won bronze medals in both the women's 400-metre and 800-metre freestyle events in the 2012 Summer Olympics in London.

Zhao Yunlei: Zhao Yunlei (born August 25, 1986) is a mixed and women's doubles badminton athlete from China.  She graduated with a BA from Huazhong University of Science and Technology.  She is the first and only badminton player to have ever won two Gold medals in the same Olympic edition, winning in both the Mixed and Women's Doubles categories in 2012.  Zhao joins the ranks with nine other players with two Olympic Gold Medals, the highest number of Gold Medals won by any badminton athlete.  Through her performance at the 2014 and 2015 BWF World Championships, she became the first player to win two consecutive gold medals in two consecutive BWF World Championships.

Paul Ziert: Paul Ziert is a former University of Oklahoma gymnastics coach.  Ziert recruited Bart Conner to the school.  In 1977 and 1978, Ziert's teams won the NCAA Men's Gymnastics championship.

Johan Grøttumsbråten: Johan Hagbart Pedersen Grøttumsbraaten (12 February 1899 – 24 January 1983) was a Norwegian skier who competed in Nordic combined and cross-country.  Dominating both events in the 1920s and early 1930s, he won several medals in the early Winter Olympics.  Most notably, he won two gold medals at the 1928 Winter Olympics, and as one of the only two entrants to win two gold medalists from St. Moritz, was the most successful athlete there, along with Clas Thunberg of Finland.  He previously won three medals (one silver, two bronzes) at the inaugural Winter Olympics held in Chamonix in 1924, and went on to defend his Olympic Nordic Combined at the 1932 Winter Olympics.

Vicki Draves: Victoria Manalo Draves (December 31, 1924 – April 11, 2010) was an American competition diver who won gold medals in both platform and springboard diving in the 1948 Summer Olympics in London.  Draves became the first woman to be awarded gold medals for both the ten-meter platform and the three-meter springboard.  Additionally, Draves became the first American woman to win two gold medals in diving.  She was born in San Francisco.

Sim Kwon-ho: Sim Kwon-Ho (Hangul: 심권호, Hanja: 沈權虎; born October 10, 1972 in Seongnam, South Korea) is a retired South Korean Greco Roman wrestler.  He won gold medals at the 1996 and 2000 Olympic Games, and is the only South Korean wrestler to win two gold medals in the Olympics.

Bart Conner: Bart Conner (born March 28, 1958) is a retired American Olympic gymnast.  As a member of the men's gymnastics team at the 1984 Summer Olympic Games, Conner won two gold medals.  He currently owns and operates the Bart Conner Gymnastics Academy in Norman, Oklahoma, along with his wife, Romanian Olympic gold medalist Nadia Comăneci.  In addition, both Comăneci and Conner are highly involved with the Special Olympics.

Terence Anderson (sport shooter): Terence "Terry" M. Anderson (born c. 1946) is a retired Australian-born American sports shooter who specialized in the 25 meter rapid fire pistol event.  He won the national championships in Australia in 1969 and 1971, in New Zealand in 1971–1973 and in the United States in 1975, 1977, 1979, 1993, 1997, 1999, 2000.  Internationally he won three gold medals and a silver medal at the 1972 Asian Championships.  Won two gold medals setting the Hemisphere record at the 1977 Championships of the Americas.  Pan Am Games silver medal at the 1979 Pan Am Games, two gold medals, the Pan Am and world record at the 1983 Pan Am Games and four gold medals at the 1995 Pan American Games.  He was selected to the 1980 Olympic team, but missed the games due to their boycott by the United States and selected to the 1996 Olympic Team in Atlanta.

Question: What year did the man who Paul Ziert recruited to the University of Oklahoma win two gold medals?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "recruited_athlete": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "sport": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "sport"
      ],
      "additionalProperties": false
    },
    "recruiting_coach": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "university": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "university"
      ],
      "additionalProperties": false
    },
    "medal_achievement": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer"
        },
        "event_type": {
          "type": "string"
        },
        "gold_medals_count": {
          "type": "integer"
        }
      },
      "required": [
        "year",
        "event_type",
        "gold_medals_count"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "recruited_athlete",
    "recruiting_coach",
    "medal_achievement"
  ],
  "additionalProperties": false
}
