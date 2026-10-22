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
Károly Ecser: Károly Ecser (born (1934--)22 1934 in Cegléd - April 2005 in Cegléd) was a Hungarian male weightlifter, who competed in the heavyweight class and represented Hungary at international competitions.  He won the bronze medal at the 1965 World Weightlifting Championships in the +90 kg category.  He participated at the 1964 Summer Olympics in the +90 kg event finishing fifth.  Ecser had furthermore the following podium finishes at major championships: bronze in the 1965 World Championships Unlimited class (522.5 kg), bronze in the 1961 European Championships Unlimited class (455.0 kg) silver in the 1962 European Championships Unlimited class (482.5 kg), silver in the 1964 European Championships Unlimited class (490 kg) and gold at the 1965 European Championships Unlimited class (505 kg)

Jolijn van Valkengoed: Jolijn van Valkengoed (born August 26, 1981 in Lelystad, Flevoland) is a Dutch swimmer, who is mainly specialized in breaststroke.  She is currently training in her hometown Lelystad together with her younger brother Thijs.  At the age of 24 she made her international debut at the European Championships 2006 in Budapest.  At the 2008 European Aquatics Championships in Eindhoven she won a bronze medal in the 4×100 medley relay.  She also qualified for Beijing 2008 as the breaststroke swimmer in the 4×100 medley relay.  At the short course she has been the owner of the national record in the 50 m breaststroke.

Roman Kapitonenko: Roman Kapitanenko (born January 21, 1981) is a Ukrainian amateur boxer who won the bronze medal at the European Championships 2008.  He benefitted from Vyacheslav Glazkov's decision to turn pro.  He beat Vladimir Prusa and Yousef Abdelghani before losing his semifinal 4:6 to Kubrat Pulev.

Igor Bour: Igor Bour, also known as Igor Lazăr or Igor Lazăr-Bour (born 18 December 1984) is a male weightlifter from Moldova.  He is best known for winning the title at the 2007 European Championships in the men's – 56 kg division, defeating Vitali Dzerbianiou (second) and Igor Grabucea.  At the 2008 European Championships he defeated Halil Mutlu and won gold medal with body weight, but later revealed he used metandienone.  He gave 4-year ban.  After he return, he won silver medal at the 2013 European Championships, but failed doping again.  According to the IWF rules, after the second doping violation Bour was banned for life by the IWF.

Gábor Szarvas: Gábor Szarvas (born (1943--)18 1943 in Újpest - (1992--)3 1992 in Budapest) was a Hungarian male former weightlifter, who competed in the middleweight class and represented Hungary at international competitions.  He won the silver medal at the 1969 World Weightlifting Championships and the bronze medal at the 1970 World Weightlifting Championships, both in the 75 kg category.  He participated at the 1972 Summer Olympics in the 75 kg event.  Szarvas had furthermore the following podium finishes at major championships: second in the 1969 European Championships Middleweight class (440.0 kg); second in the 1970 European Championships Middleweight class (452.5 kg); second in the 1971 European Championships Middleweight class (460.0 kg); second in the 1978 European Championships Featherweight class (275.0 kg).

2007–08 Swedish Figure Skating Championships: The 2007–08 Swedish Figure Skating Championships were held in the Scandinavium in Göteborg between December 7 and 10, 2007.  Because they were held in December, they were officially designated by the Swedish federation as the 2007 Swedish Championships, but the champions are the 2008 Swedish Champions.  Senior level (Olympic-level), junior level, and two age-group levels of Novice ("Riksmästerskap" (RM) and "UngdomsSM" (USM)) skaters competed in the disciplines of men's singles, ladies singles, and pair skating.  This event was used to help choose the Swedish teams for the 2008 European Championships, the 2008 World Junior Championships, and the 2008 World Championships.

Pamela Fischer (synchronised swimmer): Pamela Fischer (born 7 April 1988 in Lausanne) is a Swiss competitor in synchronized swimming who competed in the 2004 European Championships, 2005 World Aquatics Championships, 2006 European Aquatics Championships, 2007 World Aquatics Championships, 2008 European Aquatics Championships, 2009 World Aquatics Championships, 2010 European Aquatics Championships, 2011 World Aquatics Championships, 2012 European Aquatics Championships, 2013 World Aquatics Championships, and 2012 Summer Olympics.

Nóra Barta: Nóra Barta (born 2 April 1984 in Budapest) is a Hungarian diver.  She won the bronze medal in 3m Springboard event at the 2006 European Aquatics Championships and the silver in 1 m springboard event at the 2008 European Championships in Aquatics.

Kubrat Pulev: Kubrat Venkov Pulev (Bulgarian: Кубрат Венков Пулев ; born 4 May 1981) is a Bulgarian professional boxer.  He held the European heavyweight title twice between 2012 and 2016, and has challenged once for the unified world heavyweight title in 2014.  As an amateur he won multiple medals at international tournaments, including gold at the 2008 European Championships and bronze at the 2005 World Championships, all in the super-heavyweight division.

Tervel Pulev: Tervel Venkov Pulev (Bulgarian: Тервел Венков Пулев ) born 10 January 1983) is a Bulgarian boxer.  He is the younger brother of European Super Heavyweight champion Kubrat Pulev.  Tervel Pulev is best known for winning a bronze medal for Men's Boxing (Heavyweight division 91 kg) at the 2012 Summer Olympics in London, United Kingdom.  Pulev has signed up for the new AIBA professional league, called AIBA Pro Boxing (APB), which launches in fall 2013.

Question: What medal did Kubrat Pulev win after beating Roman Kapitonenko in the semifinal at the 2008 European Championships?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "athlete_name": {
      "type": "string",
      "description": "The name of the athlete."
    },
    "championship_name": {
      "type": "string",
      "description": "The name of the championship event."
    },
    "event_year": {
      "type": "integer",
      "description": "The year the championship took place."
    },
    "medal_won": {
      "type": "string",
      "description": "The type of medal won by the athlete."
    },
    "opponent_in_semifinal": {
      "type": "string",
      "description": "The name of the opponent in the semifinal match."
    }
  },
  "required": [
    "athlete_name",
    "championship_name",
    "event_year",
    "medal_won",
    "opponent_in_semifinal"
  ],
  "additionalProperties": false
}
