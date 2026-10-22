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
Turkey Open: The Turkey Open is a defunct tennis tournament that was played on the Grand Prix tennis circuit in 1975.  The event was held in Istanbul, Turkey.  Colin Dowdeswell won the singles title while Colin Dibley and Thomaz Koch partnered to win the doubles title.

Thomaz Koch: Thomaz Koch (born May 11, 1945 in Porto Alegre), is a left-handed former tennis player from Brazil, who was a quarter-finalist at the French Open, Wimbledon and the U.S. National Championships.

Fantasy sport: A fantasy sport (also known less commonly as rotisserie or roto) is a type of online game where participants assemble imaginary or virtual teams of real players of a professional sport.  These teams compete based on the statistical performance of those players' players in actual games.  This performance is converted into points that are compiled and totaled according to a roster selected by each fantasy team's manager.  These point systems can be simple enough to be manually calculated by a "league commissioner" who coordinates and manages the overall league, or points can be compiled and calculated using computers tracking actual results of the professional sport.  In fantasy sports, team owners draft, trade and cut (drop) players, analogously to real sports.

Maria Fernanda Alves: Maria Fernanda Barbato Alves (born 17 April 1983), also known as Nanda Alves, is a Brazilian tennis player.  She is currently coached by her father Carlos and former tennis player Thomaz Koch.  As of 1 March 2010, Alves is ranked World No. 262, and is the highest ranked Brazilian player.  She has enjoyed success at the ITF Circuit, winning 18 singles and 26 doubles titles so far.  Alves made her WTA Tour debut at Copa Colsanitas in 2004, and has played qualifications for all four Grand Slam events.  Partnering with Vanessa Henke, Alves took part in the 2005 Australian Open doubles event, but they lost to Daniela Hantuchová and Martina Navratilova in the first round.

Jack Sock: Jack Sock (born September 24, 1992) is an American professional tennis player who is currently ranked world No. 21 in men's singles by the Association of Tennis Professionals (ATP).  He is one of the top ranked American men in both singles and doubles on the ATP Tour.  A former junior US Open champion, Sock's singles success is highlighted by 7 ATP finals, including three titles.  His career best result came at the 2017 Indian Wells Masters, where he reached the semi-finals.

2016 China Open – Men's Doubles: Vasek Pospisil and Jack Sock were the defending champions, but Pospisil chose to play in Tokyo instead.  Sock played alongside Bernard Tomic but lost in the final to Pablo Carreño Busta and Rafael Nadal, who won 6−7, 6−2, [10−8].

Bruno Soares: Bruno Fraga Soares (] ; born February 27, 1982, in Belo Horizonte) is a professional tennis player from Brazil.  His highest singles ranking on the ATP Tour is World No. 221, which he reached in March 2004.  Primarily a doubles specialist, his career-high doubles ranking is World No. 2, which he achieved in October 2016.  After a few efforts, including a final in the 2012 US Open and the semifinals of the 2008 and 2013 French Opens, Soares finally won his first Grand Slam title at the 2016 Australian Open, partnering Jamie Murray and then followed that up with a second men's doubles title at the 2016 US Open.  He has also won three Grand Slam titles in Mixed Doubles, two at the US Open, in 2012 and 2014, and one at the Australian Open in 2016.  He was the third Brazilian tennis player to achieve this, after Maria Bueno and Thomaz Koch.

Fiorella Bonicelli: Fiorella Bonicelli (born 21 December 1951) is a retired professional tennis player from Uruguay.  During her career, she won the 1975 French Open mixed doubles title with Thomaz Koch.  She also won the 1976 French Open women's doubles title with Gail Lovera, defeating Kathleen Harter and Helga Niessen Masthoff 6–4, 1–6, 6–3.  At the Fed Cup, her singles record is 11–4, and doubles record 6–8.  During her career, she reached one Grand Slam singles quarterfinal, at the 1978 French Open, where she lost to Virginia Ruzici 6–7, 6–4, 6–8.

Khartoum International: The Khartoum International is a defunct tennis tournament that was played on the Grand Prix tennis circuit in 1976.  The event was held in Khartoum, Sudan and was played on outdoor hard courts.  Mike Estep won the singles title, defeating Thomaz Koch in the final.

High performance sport: High performance sport or elite sport is sport at the highest level of competition, with elite athletes as the competitors.  In sports administration "high performance sport", where the emphasis is on winning prestigious competitions, is distinguished from "mass sport" or "recreational sport", where the emphasis is on attracting the maximum number of participants.  High performance sport overlaps with professional sport but is not the same; for example, the English football league system and Minor League Baseball include lower divisions whose teams' members are full-time professionals; on the other hand, competitors at the Olympic Games or World Games in some minority sports may be part-time or rely on government grants.

Question: Do athletes Thomaz Koch and Jack Sock play the same professional sport?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "athletes_involved": {
      "type": "array",
      "description": "List of athletes mentioned in the question and their respective sports.",
      "items": {
        "type": "object",
        "properties": {
          "athlete_name": {
            "type": "string",
            "description": "The name of the athlete."
          },
          "sport_played": {
            "type": "string",
            "description": "The professional sport the athlete plays."
          }
        },
        "required": [
          "athlete_name",
          "sport_played"
        ],
        "additionalProperties": false
      }
    },
    "play_same_sport": {
      "type": "boolean",
      "description": "True if both athletes play the same professional sport, false otherwise."
    },
    "shared_sport": {
      "type": "string",
      "description": "The name of the professional sport they both play, if any."
    }
  },
  "required": [
    "athletes_involved",
    "play_same_sport",
    "shared_sport"
  ],
  "additionalProperties": false
}
