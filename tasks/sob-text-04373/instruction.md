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
Kuo Po-cheng: Kuo Po-cheng () (born January 15, 1978) is a Taiwanese professional pool player, nicknamed "the Little Monster".  Kuo finished first runner-up to Wu Chia-ching in the 2005 World Nine-ball Championship held in Kaohsiung, Taiwan.  He was also runner-up to Francisco Bustamante in the 2010 World Nine-ball Championship held in Doha, Qatar.

Daryl Peach: Daryl Peach (born 8 March 1972 in Castleford, West Yorkshire, England) is an English professional pocket billiards (pool) player, who now resides in Blackpool, England.  Nicknamed "The Dazzler," he defeated the Philippines' Roberto Gomez in 2007 in Manila, Philippines to become the first Englishman to win the WPA World Nine-ball Championship.  The event was broadcast live in its entirety on Sky Sports, and was held at the infamous Araneta Colosseum, the very same arena where Mohamed Ali fought Joe Frazier in the "Thriller in Manila" fight.  In front of more than 7,000 spectators, Peach held his composure under adverse conditions due to the extremely partisan crowds, beating amongst others, 4 Filipino Giants on his way to lifting the coveted title, including the defending champion, Ronnie Alcano, Francisco Bustamente, and Roberto Gomez.  Peach held the title until 2010, where the tournament was held in Doha, Qatar, which was won by Francisco Bustamante.

Matchroom Sport: Matchroom Sport is a sport event promotions company led by the founder and owner English entrepreneur Barry Hearn and his son Eddie.  It first came to attention in the sports of snooker and boxing and is also involved in pool, bowling, golf (see PGA EuroPro Tour), fishing, darts, ping pong, and poker and as of late 2016 gymnastics.  The company is based in Brentwood, Essex.

Lee Kun-fang: Lee Kun-fang () (born 1968) is a Taiwanese professional pool player.  He came close to winning his first world title at the 1997 WPA World Nine-ball Championship, but the American cue artist Johnny Archer defeated him in the final match.  In 1998, Lee won the International Challenge of Champions, defeating Takahashi Kunihiko, a former world champion from Japan.  He finished runner-up at the 1997 Philippines World Pool Championship.

Jharome Peña: Jharome Peña is a Filipino professional pool player.  During the WPA World Nine-ball Championship in 2006, he advanced to the round of 32, but was then eliminated by former world snooker champion Steve Davis of Great Britain.

2007 WPA Men's World Nine-ball Championship: The 2007 WPA Men's World Nine-ball Championship (billed in the host country as 2007 Philippines World Pool Championship) was the 18th annual international nine-ball pool tournament for men sanctioned by the World Pool-Billiard Association (WPA).  It was held at the Araneta Coliseum in Quezon City, Metro Manila, Philippines from 3–11 November 2007.  It was the second consecutive time the tournament has been held in the Philippines.

2010 WPA World Nine-ball Championship: The 2010 WPA World Nine-ball Championship (a.k.a. the World Pool Championship 2010) was the professional nine-ball pocket billiards (pool) championship, sanctioned by the World Pool-Billiard Association (WPA) and organised by Matchroom Sport.  It was held from 29 June through 5 July in Doha, Qatar, hosted by the Qatar Billiards and Snooker Federation.  Qualifying tournaments were held from 25 through 29 June in the same city.

Darren Appleton: Darren "Dynamite" Appleton (born 8 February 1976) is an English pool player.  He won the first WPA World Ten-ball Championship in 2008 against Wu Jia-qing, the former world champion in both nine-ball and eight-ball from Taiwan.  With the victory, he became the second male player from Britain to win a world championship after Daryl Peach who won the world nine-ball title a year earlier.

WPA World Nine-ball Championship: The WPA World Nine-ball Championship is an annual, international, professional nine-ball pool (pocket billiards) tournament, founded in 1990, sanctioned by the World Pool-Billiard Association (WPA), and principally sponsored and organised by Matchroom Sport (who provide the event's official website, under the less specific name World Pool Championship).  It is divided into men's, women's and wheelchair Divisions.  Since 2010, it is held in Doha, Qatar.

2011 WPA World Nine-ball Championship: The 2011 WPA World Nine-ball Championship (a.k.a. the World Pool Championship 2011) was the professional nine-ball pocket billiards (pool) championship, sanctioned by the World Pool-Billiard Association (WPA) and organised by Matchroom Sport.  It was held from 25 June through 1 July in Doha, Qatar, hosted by the Qatar Billiards and Snooker Federation.  Qualifying tournaments were held from 21 to 23 June, with the Al Sadd Sports Club hosting both qualifying and final tournaments.

Question:  The 2011 WPA World Nine-ball Championship was organized by a sport event promotions company based in which city ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "event_name": {
      "type": "string",
      "description": "The name of the WPA World Nine-ball Championship event."
    },
    "organizer_company": {
      "type": "string",
      "description": "The name of the company that organized the event."
    },
    "organizer_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the organizing company is based."
        },
        "county_or_region": {
          "type": "string",
          "description": "The county or region where the organizing company is based."
        }
      },
      "required": [
        "city",
        "county_or_region"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "event_name",
    "organizer_company",
    "organizer_location"
  ],
  "additionalProperties": false
}
