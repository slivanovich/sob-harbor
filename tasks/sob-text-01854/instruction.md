{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIván Calderón (boxer): Iván Calderón Marrero (born January 7, 1975) is a Puerto Rican former professional boxer who competed from 2001 to 2012.  He is a two-weight world champion, having held the WBO mini flyweight title from 2003 to 2007 (making eleven successful defenses and being recognized as super champion by the organization), and the WBO, \" Ring\" magazine, and lineal light flyweight titles from 2007 to 2010 (making six successful defenses).  Additionally, his August 2010 bout against Giovani Segura was named fight of the year by \" Ring\" magazine.  As an amateur Calderón represented Puerto Rico in international competitions, including the 2000 Olympics.\n\nJoe Calzaghe: Joseph William Calzaghe, {'1': \", '2': \", '3': \", '4': \"} ( ; born 23 March 1972) is a Welsh former professional boxer who competed from 1993 to 2008.  He is a two-weight world champion, having held the unified WBA (Super), WBC, IBF, WBO, \"Ring\" magazine, and lineal super-middleweight titles, as well as the \"Ring\" light-heavyweight title.  Calzaghe is the longest-reigning super-middleweight world champion in boxing history, having held the WBO title for over 10 years and making 21 successful defences before moving up to light-heavyweight.  As his super-middleweight and light-heavyweight reigns overlapped, he retired with the longest continual time as world champion of any active fighter.\n\nBuddy McGirt: James Walter \"Buddy\" McGirt (born January 17, 1964) is an American former professional boxer who competed from 1982 to 1997, and has since worked as a boxing trainer.  He is a two-weight world champion, having held the IBF junior welterweight title in 1988, and the WBC and lineal welterweight titles from 1991 to 1993.\n\nVirgil Hill: Virgil Eugene Hill (born January 18, 1964) is an American former professional boxer who competed from 1984 to 2007, and in 2015.  He is a two-weight world champion, having held the WBA light heavyweight title twice, from 1987 to 1997; the IBF and lineal light heavyweight titles from 1996 to 1997; and the WBA cruiserweight title twice, from 2000 to 2002 and 2006 to 2007.  As an amateur, Hill won a silver medal in the middleweight division at the 1984 Summer Olympics.  In 2013, he was inducted into the International Boxing Hall of Fame.\n\nBeibut Shumenov: Beibut Amirhanoviç Shumenov (Kyrgyz: Бейбут Амирханович Шуменов ; born 19 August 1983) is a Kazakhstani former professional boxer who competed from 2007 to 2016.  He is a two-weight world champion, having held the WBA light heavyweight title from 2010 to 2014, and the WBA (Regular) cruiserweight title from 2016 to 2017.\n\nGerry Peñalosa: Geronimo \"Gerry\" Peñalosa (born August 7, 1972) is a Filipino former professional boxer who competed from 1989 to 2010.  He is a two-weight world champion, having held the WBC and lineal super flyweight titles from 1997 to 1998, and the WBO bantamweight title from 2007 to 2009.  Originally from San Carlos City, Peñalosa currently resides in Manila.  He was trained mainly by Freddie Roach, and went on to become a boxing trainer himself after retirement.  Peñalosa's older brother, Dodie Boy Peñalosa, is also a former boxer and world champion.\n\nGuy Waters: Guy \"Arc Angel\" Waters ( (1964--) 25 1964 (age (2017)-(1964)-((11)<(01)or(11)==(01)and(30)<(25)) ) ) is an Australian professional welter/light middle/middle/super middle/light heavy/cruiserweight boxer of the 1980s, 1990s and 2000s who won the New South Wales State (Australia) light heavyweight title, Australian light heavyweight title, Oriental and Pacific Boxing Federation (OPBF) light heavyweight title, Australasian Light Heavyweight Title, World Boxing Federation (WBF) light heavyweight title, International Boxing Federation (IBF) Pan Pacific super middleweight title, Oriental and Pacific Boxing Federation (OPBF) super middleweight title, and Commonwealth light heavyweight title, and was a challenger for the WBC light heavyweight title against Dennis Andries, World Boxing Association (WBA) World light heavyweight title against Virgil Hill, World Boxing Council (WBC) cruiserweight title against Juan Carlos Gómez, and Commonwealth super middleweight title against David Starie, his professional fighting weight varied from 167+1/2 lb , i.e. super middleweight to 185+1/4 lb , i.e. cruiserweight.\n\nNigel Benn: Nigel Gregory Benn (born 22 January 1964) is a British former professional boxer who competed from 1987 to 1996.  He is a two-weight world champion, having held the WBO middleweight title in 1990, and the WBC super-middleweight title from 1992 to 1996.  Additionally he held the Commonwealth middleweight title from 1988 to 1989.  Nicknamed \"The Dark Destroyer\" for his formidable punching power and aggressive fighting style, Benn is ranked by BoxRec as the fourth best British super-middleweight boxer of all time.\n\nDariusz Michalczewski: Dariusz Michalczewski (born 5 May 1968) is a Polish-German former professional boxer who competed from 1991 to 2005.  He is a two-weight world champion, having held multiple world titles at light-heavyweight, including the WBO title from 1994 to 2003; the unified WBA, IBF, and lineal titles in 1997; and the WBO junior-heavyweight title from 1994 to 1995.\n\nMeldrick Taylor: Meldrick Taylor (born October 19, 1966) is an American former professional boxer who competed from 1984 to 2002.  He is a two-weight world champion, having held the IBF junior welterweight title from 1988 to 1990, and the WBA welterweight title from 1991 to 1992.  As an amateur, Taylor won a gold medal in the featherweight division at the 1984 Summer Olympics.\n\nQuestion: Guy Walters competed against which former professional boxer that is a two-weight world champion?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"opponent_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the boxer who competed against Guy Waters.\"\n    },\n    \"is_two_weight_world_champion\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the opponent is a two-weight world champion.\"\n    },\n    \"competition_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title_challenged\": {\n          \"type\": \"string\",\n          \"description\": \"The specific title Guy Waters challenged against this opponent.\"\n        },\n        \"organization\": {\n          \"type\": \"string\",\n          \"description\": \"The boxing organization associated with the challenged title.\"\n        }\n      },\n      \"required\": [\n        \"title_challenged\",\n        \"organization\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"opponent_name\",\n    \"is_two_weight_world_champion\",\n    \"competition_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "opponent_name": {
        "type": "string",
        "description": "The name of the boxer who competed against Guy Waters."
      },
      "is_two_weight_world_champion": {
        "type": "boolean",
        "description": "Indicates if the opponent is a two-weight world champion."
      },
      "competition_details": {
        "type": "object",
        "properties": {
          "title_challenged": {
            "type": "string",
            "description": "The specific title Guy Waters challenged against this opponent."
          },
          "organization": {
            "type": "string",
            "description": "The boxing organization associated with the challenged title."
          }
        },
        "required": [
          "title_challenged",
          "organization"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "opponent_name",
      "is_two_weight_world_champion",
      "competition_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
