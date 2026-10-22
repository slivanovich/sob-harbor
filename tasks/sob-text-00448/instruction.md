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
Dan Henderson: Daniel Jeffery Henderson (born August 24, 1970) is an American former mixed martial artist and Olympic wrestler, who last competed as a middleweight in the Ultimate Fighting Championship.  He was the last Strikeforce Light Heavyweight Champion and was the last Welterweight (80 kg ) and Middleweight (95 kg ) champion of Pride Fighting Championships.  Additionally, Henderson was the Brazil Open '97 Tournament Champion, the UFC 17 Middleweight Tournament Champion, the Rings: King of Kings 1999 Tournament Champion and the Pride Weltwerweight Grand Prix Tournament Champion.  During his career, Henderson also challenged for the UFC Middleweight Championship (2x), the UFC Light Heavyweight Championship and the Strikeforce Middleweight Championship.  He was the first mixed martial artist to concurrently hold two titles in two different weight classes in a major MMA promotion.  At the time of his retirement after UFC 204, he was the oldest fighter on the UFC roster.  Known to be one of the greatest mixed martial artists of all time having defeated a total of seventeen MMA world champions across four major MMA promotions (UFC, PRIDE FC, Strikeforce, and RINGS).

Bertrand Amoussou-Guenou: Bertrand Amoussou-Guenou (born May 29, 1966) is a retired French mixed martial artist and judoka.  He is a trainer for his younger brother Karl of "Team Amoussou" and, following official recognition of mixed martial arts in France, became the president of the national sanctioning body, the Commission National de Mixed Martial Arts, in January 2008.  On 1 October 2013, Amoussou assumed the position of president of the International Mixed Martial Arts Federation (IMMAF).

Akihiko Adachi: Akihiko Adachi (安達 明彦 , Adachi Akihiko ) is a Japanese light heavyweight mixed martial artist.  Adachi was born in Sapporo, Hokkaido, Japan.  He fought as a professional mixed martial artist from Paraesta Matsudo in Matsudo, Chiba Prefecture beginning in 2000.  Adachi was the top amateur Shooto light heavyweight in 2002, and was named the Shooto cruiserweight rookie of the year in 2003.  Adachi's last bout was in 2006 and he formally retired from mixed martial arts in 2008.

Marc Roberts (singer-songwriter): Marc Roberts is a singer-songwriter and radio broadcaster.  He is originally from Crossmolina, County Mayo, and now based in Galway.  Prior to 1997, he fronted his own band doing own original work and American country classics.  In May of that year, Roberts represented Ireland in the Eurovision Song Contest with "Mysterious Woman", finishing in second place.  His debut single reached number two on the Irish Singles Chart.

Ray Mercer: Raymond Anthony "Ray" Mercer (born April 4, 1961) is an American former professional boxer, kickboxer, and mixed martial artist.  In boxing he competed from 1989 to 2008, and held the WBO heavyweight title from 1991 to 1992.  As an amateur he won a gold medal in the heavyweight division at the 1988 Summer Olympics.  As a mixed martial artist, Mercer is known for scoring an upset one-punch knockout victory over former UFC heavyweight champion Tim Sylvia in 2009.

Mohammed &quot;The Hawk&quot; Shahid: Mohammed Shahid (born July 8, 1989) is an entrepreneur and a mixed martial artist from Bahrain.  He is the CEO of KHK MMA and the President of the Bahrain based mixed martial arts organisation, Brave Combat Federation owned and supported by His Highness Sheikh Khalid bin Hamad Al Khalifa.  Mohammed Shahid was the first mixed martial artist from Bahrain to compete in global MMA events.  He was assigned a managerial role to develop mixed martial arts in Bahrain as the CEO of KHK MMA.  Bahrain established a national team alongside bringing global talent to facilitate the growth of MMA in Bahrain.

Lee Hasdell: Lee Hasdell (born 13 December 1966) is a British martial artist, promoter and former professional kickboxer and mixed martial artist.  Hasdell is considered by many as a true pioneer of UK mixed martial arts, as he was the main driving force and innovator in the 1990s.  Hasdell promoted the first professional Mixed martial arts events in the United Kingdom and has helped develop many of the standards within the British MMA scene of today.

Baboo Da Silva: Mauricio "Baboo" Da Silva (born November 28, 1967) is a Brazilian kyokushin kaikan full contact karate practitioner and former professional kickboxer and mixed martial artist.  He is a professional coach and trainer of K-1 and MMA (Mixed Martial Arts), who has trained a number of world class fighters including Francisco Filho (martial artist), Glaube Feitosa, Andrews Nakahara, Ewerton Teixeira, Ray Sefo, Aleksandr Pitchkounov, Takumi Sato, Jan Soukup, Kou Tasei (aka Hong Tae Seong), Jan Nortje, Doug Viney, Mighty Mo (kickboxer) and Akebono Taro.  From 1998 to 2004 he worked as the trainer and sparring partner for Francisco Filho.  He lived in Tokyo, Japan from 2005 to December 2010 and trained fighters from the IKO1 Kyokushin - Team Ichigeki and other fighters from visiting teams at the Ichigeki Plaza.  He fought in the K-1 PREMIUM 2003 Dynamite!!  and also in the Ichigeki events in Japan.

Marc Roberts (footballer): Marc Roberts (born 26 July 1990) is an English footballer who plays as a defender for Championship club Birmingham City.  Roberts began his career in non-league football, with Wakefield, Worksop Town, Buxton and FC Halifax Town, and was capped for England C, the team that represents England at semi-professional level.  He joined League One club Barnsley in 2015, helped them gain promotion to the Championship, and captained the team.  He signed for Birmingham in July 2017.

Marc Roberts (sports agent): Marc Roberts (born September 20, 1959, Newark, New Jersey) was a Division I basketball player at American University in Washington, D.C., before starting a career as a sports agent.  He has represented NFL players such as Antonio Freeman, Tyronne Drakeford, O.J. McDuffie, Jerry Porter, and Tyrone Wheatley, NBA players Bobby Jackson, Johnny Newman, and Derek Anderson, and World Champion boxers "Merciless" Ray Mercer, Shannon Briggs, Tracy Harris Patterson, Danell Nicholson, Charles Murray and Alex Trujillo.  He was one of the five sports agents consulted in making the film "Jerry Maguire".

Question: Which mixed martial artist was represented by Marc Roberts?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "agent_name": {
      "type": "string",
      "description": "The name of the sports agent."
    },
    "agent_profession": {
      "type": "string",
      "description": "The profession of the individual who represented the athlete."
    },
    "represented_athlete": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the athlete represented by the agent."
        },
        "primary_sport": {
          "type": "string",
          "description": "The primary sport of the athlete as identified in the question."
        },
        "other_sports_competed_in": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other sports the athlete competed in professionally."
        }
      },
      "required": [
        "name",
        "primary_sport",
        "other_sports_competed_in"
      ],
      "additionalProperties": false
    },
    "relationship_type": {
      "type": "string",
      "description": "Describes the relationship between the agent and the athlete."
    }
  },
  "required": [
    "agent_name",
    "agent_profession",
    "represented_athlete",
    "relationship_type"
  ],
  "additionalProperties": false
}
