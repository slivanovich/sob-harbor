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
Andrew Murray (Guyanese boxer): Andrew "The Eagle" Murray (1 July 1971 — 26 January 2002 (aged 30)) born in Georgetown was a Guyanese professional welter/light middle/middleweight boxer of the 1990s and 2000s who won the World Boxing Council (WBC) FECARBOX welterweight title, World Boxing Association (WBA) Fedelatin welterweight title, and Commonwealth welterweight title, and was a challenger for the World Boxing Association (WBA) World welterweight title against Ike Quartey, World Boxing Union (WBU) welterweight title against Michele Piccirillo, and World Boxing Organization (WBO) North American Boxing Organization (NABO) light middleweight title against Fathi Missaoui, his professional fighting weight varied from 145 lb , i.e. welterweight to 156 lb , i.e. middleweight.  Andrew Murray was trained by Emanuel Steward, and was the Vice-President of the Guyana Amateur Boxing Board and was training several young boxers, and he had coached Hugo Lewis to the Guyanese super featherweight title on 26 December 2001.  Andrew Murray died in a traffic collision on the Soesdyke-Linden Highway early in the morning of Sunday 27 January 2002, he had been in Linden promoting a fight card and was on his way back to Georgetown.

Ralph Charles: Ralph Charles (born 5 February 1943) is an English amateur welterweight and professional light welter/welter/light middle/middleweight boxer of the 1960s and '70s who as an amateur won the Amateur Boxing Association of England (ABAE) 1959 Junior Class-A title against Kenneth "Ken"/"Kenny" J. Cooper  (Warley ABC), boxing out of West Ham Boys & ABC, won the Amateur Boxing Association of England (ABAE) 1960 Junior Class-B title against J. Harwood (National Association of Boys Clubs), boxing out of West Ham Boys & ABC, and was runner-up for the 1963 Amateur Boxing Association of England welterweight title, against Johnny Pritchett (Bingham & District ABC), boxing out of West Ham ABC, and as a professional won the British Boxing Board of Control (BBBofC) Southern Area welterweight title, BBBofC British welterweight title, European Boxing Union (EBU) welterweight title, and Commonwealth welterweight title, and was a challenger for the World Boxing Council (WBC) welterweight title, and World Boxing Association (WBA) World welterweight title against José Nápoles, his professional fighting weight varied from 140 lb , i.e. light welterweight to 157 lb , i.e. middleweight.

Fatai Onikeke: Fatai "Kid Dynamite" Onikeke ( (1983--) 02 1983 (age (2017)-(1983)-((11)<(04)or(11)==(04)and(30)<(02)) ) ) is a Nigerian/Australian professional light welter/welterweight boxer of the 2000s and 2010s who won the Nigerian welterweight title, African Boxing Union (ABU) welterweight title, World Boxing Foundation (WBFo) Intercontinental light welterweight title, International Boxing Federation (IBF) Pan Pacific light welterweight title, and Commonwealth welterweight title, and was a challenger for the World Boxing Organization (WBO) Africa light welterweight title, WBFo light welterweight title, and World Boxing Organization (WBO) Oriental light welterweight title against Lance Gostelow , his professional fighting weight varied from 138+1/2 lb , i.e. light welterweight to 146+1/2 lb , i.e. welterweight.

Adrien Broner: Adrien Jerome Broner (born July 28, 1989) is an American professional boxer.  He is a former four-weight world champion, having held the WBO junior lightweight title from 2011 to 2012; the WBC lightweight title from 2012 to 2013; the WBA welterweight title in 2014; and the WBA light welterweight title from 2015 to 2016.

Bunny Grant: George Leslie "Bunny" Grant (born 29 September 1940) is a Jamaican professional feather/super feather/light/light welter/welterweight/light middleweight boxer of the 1950s, '60s and '70s who won the Jamaican lightweight title, Jamaican welterweight title, Central American light welterweight Title, Latin American junior welterweight title, and British Commonwealth lightweight title, and was a challenger for the World Boxing Council (WBC) light welterweight title and World Boxing Association (WBA) World light welterweight title against Eddie Perkins, Commonwealth welterweight title against Clyde Gray, his professional fighting weight varied from 125+1/2 lb , i.e. featherweight to 152+1/2 lb , i.e. light middleweight.  Bunny Grant was managed by Jacques Deschamps, and Pancho Rankine (circa 1962), and trained by Harry Wiley (circa 1962).

Alex de Jesús: Alexander "Alex" de Jesús (February 2, 1983 – April 3, 2016) was a Puerto Rican professional boxer.  As an amateur, de Jesús represented the island of Puerto Rico in international events, including the 2003 Pan American Games, the 2002 Central American and Caribbean Games and the 2004 Summer Olympics.  Early in his career, he won seven regional titles: the World Boxing Organization Latino lightweight title, World Boxing Council Caribbean Boxing Federation lightweight title, World Boxing Association Fedecaribe Lightweight title, WBO Latino light welterweight title, WBA Fedecaribe Welterweight title, WBC Latino light welterweight title and the WBA Fedebol light welterweight title.

Saleh Khoulef: Saleh Khoulef (born March 30, 1975) is an Egyptian boxer., He competed in the light welterweight division at the 2000 Summer Olympics.  During the competition, he defeated Ukraine's Vyacheslav Senchenko in the second round, but was eliminated in the subsequent round.

Jeff Malcolm: Jeff "Flash" Malcolm (born 9 May 1956 in Cowra, New South Wales), is an Australian professional boxer who fought from 1971 until 2002.  He won the Australian light welterweight title, New South Wales (Australia) State lightweight title, Australasian light welterweight title, South Pacific light welterweight title, Queensland (Australia) State welterweight title, International Boxing Council (IBC) welterweight title, South Pacific welterweight title, World Boxing Federation (WBF) Intercontinental welterweight title, WBF welterweight title, Pan Asian Boxing Association (PABA) welterweight title, World Boxing Association (WBA) Fedelatin welterweight title, PABA light middleweight title, and Commonwealth light welterweight title.  He was also a challenger for the South Seas light welterweight title against Pat Leglise, Australian welterweight title against Wilf Gentzen, and World Boxing Organization (WBO) welterweight title against Manning Galloway.  His professional fighting weight varied from 135 lb , i.e. lightweight to 165+1/4 lb , i.e. super middleweight.  He was inducted into the Australian National Boxing Hall of Fame in 2007.

Hector Thompson: Hector Thompson (born 24 June 1949 in Kempsey, New South Wales) is an Australian professional light/light welter/welter/light middleweight boxer of the 1970s and '80s who won the New South Wales (Australia) State lightweight title, Australian light welterweight title, Australasian lightweight title, Australasian light welterweight title, South Pacific welterweight title, and Commonwealth light welterweight title (three times), and was a challenger for the World Boxing Association (WBA) World lightweight title against Roberto Durán, and World Boxing Association (WBA) World light welterweight title against Antonio Cervantes, his professional fighting weight varied from 132 lb , i.e. lightweight to 152 lb , i.e. light middleweight.  He was inducted into the Australian National Boxing Hall of Fame in 2005.

Vyacheslav Senchenko: Vyacheslav Senchenko (Ukrainian: В'ячеслав Сенченко , ] ; born 12 April 1977) is a Ukrainian professional boxer who held the WBA welterweight title from 2009 to 2012.

Question: Egyptian boxer, Saleh Khoulef, defeated the Ukrainian professional boxer who held the WBA welterweight title from when to when?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "egyptian_boxer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "ukrainian_boxer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "title_held": {
          "type": "string"
        },
        "title_reign_start_year": {
          "type": "integer"
        },
        "title_reign_end_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "title_held",
        "title_reign_start_year",
        "title_reign_end_year"
      ],
      "additionalProperties": false
    },
    "relationship": {
      "type": "string",
      "description": "Describes the relationship between the two boxers in the context of the question."
    }
  },
  "required": [
    "egyptian_boxer",
    "ukrainian_boxer",
    "relationship"
  ],
  "additionalProperties": false
}
