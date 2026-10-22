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
Lelisa Desisa: Lelisa Desisa Benti (born 14 January 1990) is an Ethiopian long-distance runner who specialises in road running competitions.  He gained his first international medal at the 2009 African Junior Athletics Championships, where he took the 10,000 metres gold medal.

Mack Horton: Mackenzie "Mack" Horton {'1': ", '2': ", '3': ", '4': "} (born 25 April 1996) is an Australian freestyle swimmer.  He is an Olympic gold medallist, World Championships medallist, and Commonwealth Games medallist.  At the 2016 Olympic Games in Rio de Janeiro, Brazil, he finished first in the 400m freestyle, winning his first gold medal and became the first male swimmer from the state of Victoria to do so in the Games' history.

Cosmas Rono Kipkorir: Cosmas Rono Kipkorir (born 12 December 1984) is a male Kenyan middle-distance runner who specializes in the 800 metres.  At age category level, he was the silver medallist in the event at the World Youth Championships in Athletics in 2001 and the gold medallist at the 2003 African Junior Athletics Championships.

Oluwatobiloba Amusan: Oluwatobiloba Ayomide Amusan (born April 23, 1997) is a Nigerian sprinter.  She claimed gold in the 100 metres hurdles event at the 2015 African Junior Athletics Championships in Addis Ababa.  In 2015, while making her All-Africa Games debut, she won gold in the 100 metres hurdles event at the 2015 All-Africa Games.  Her team mate, Lindsay Lindley was third.  She was also a silver medallist at the 2013 African Youth Championships in Warri.

2013 African Junior Athletics Championships: The 2013 African Junior Athletics Championships was the eleventh edition of the biennial, continental athletics tournament for African athletes aged 19 years or younger.  It was held at the Germain Comarmond Stadium in Bambous, Mauritius from 29 August – 1 September.  A total of 223 athletes from 29 nations competed.  Neither pole vault event was held, due to a lack of entries, and the decathlon and heptathlon competitions were also not contested.

Dawit Wolde: Dawit Wolde (born 19 May 1991) is an Ethiopian middle distance runner who specialises in the 1500 metres.  A medallist at the World Youth Championships and the African Junior Athletics Championships, he has represented Ethiopia at the African Championships in Athletics and the All-Africa Games.  He was chosen to compete at the 2012 Summer Olympics.  His 1500 m personal best is 3:33.82 minutes.

Caster Semenya: Mokgadi Caster Semenya Bronze OIB (born 7 January 1991) is a South African middle-distance runner and 2016 Olympic gold medallist.  Semenya won gold in the women's 800 metres at the 2009 World Championships with a time of 1:55.45 and at the 2017 World Championships in her new personal best, 1:55.16.  Semenya also won silver medals at the 2011 World Championships and the 2012 Summer Olympics, both in the 800 metres.  She was the winner of the gold medal in the 800 metre event at the 2016 Summer Olympics.

2015 African Youth Athletics Championships: The 2015 African Youth Athletics Championships was the second edition of the biennial athletics competition for African athletes aged fifteen to seventeen, It was held in Reduit, Mauritius from 23–26 April.  Mauritius had hosted the 2013 African Junior Athletics Championships two years earlier.  A total of 38 events, 18 by boys and 20 by girls, were contested at the competition.

Folashade Abugan: Folashade Abigeal Abugan (born December 17, 1990) is a female Nigerian sprinter who specializes in the 400 metres.  She was the 400 m bronze medalist at the 2007 All-Africa Games and improved to the silver medal at the 2008 African Championships, where she set a personal best time of 50.89 seconds.  She won gold medals at the 2008 World Junior Championships in Athletics and the 2009 African Junior Athletics Championships.

2009 African Junior Athletics Championships: The 2009 African Junior Athletics Championships were held in Bambous, Mauritius from 30 July to 2 August.  There were 40 events in total, of which 20 were contested by male athletes and 20 by female athletes.  Multiple gold medallists Caster Semenya and Amaka Ogoegbunam broke championships records, but also created controversy at the 2009 World Championships in Athletics later that year.  Semenya was asked to take a gender test and Ogoegbunam tested positive for anabolic steroids.

Question: The 2009 African Junior Athletics Championships were held in Bambous, Mauritius, which multiple gold medallist, a South African middle-distance runner and 2016 Olympic gold medallist, broke championships records?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "athlete_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the athlete."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the athlete."
        },
        "specialization": {
          "type": "string",
          "description": "The athletic specialization of the athlete."
        },
        "olympic_gold_medal_year": {
          "type": "integer",
          "description": "The year the athlete won an Olympic gold medal."
        }
      },
      "required": [
        "name",
        "nationality",
        "specialization",
        "olympic_gold_medal_year"
      ],
      "additionalProperties": false
    },
    "championship_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the championship event."
        },
        "year": {
          "type": "integer",
          "description": "The year the championship was held."
        },
        "location": {
          "type": "string",
          "description": "The location where the championship was held."
        }
      },
      "required": [
        "name",
        "year",
        "location"
      ],
      "additionalProperties": false
    },
    "action_performed": {
      "type": "string",
      "description": "The specific action performed by the athlete at the championship."
    }
  },
  "required": [
    "athlete_details",
    "championship_details",
    "action_performed"
  ],
  "additionalProperties": false
}
