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
Greg Smith (Paralympian): Gregory Stephen "Greg" Smith, OAM (born 19 August 1967) is an Australian Paralympic athlete and wheelchair rugby player who won three gold medals in athletics at the 2000 Summer Paralympics, and a gold medal in wheelchair rugby at the 2012 Summer Paralympics, where he was the flag bearer at the opening ceremony.

Lee Cox (athlete): Lee Cox (born 7 April 1981) is an Australian Paralympic athlete with a vision impairment.  He was born in the Victorian town of Hamilton.  At the 1996 Pacific School Games, he won two gold medals in the 400 m and discus events and four silver medals in the 100 m, 200 m, long jump and triple jump events, and in 1997 he was named Most Outstanding Junior Athlete by the Australian Blind Sports Federation.  He participated in the 1999 FESPIC Games, winning two silver medals in the 400 m and triple jump events and a bronze medal in the long jump event.  At the 2000 Sydney Games, he won a silver medal in the men's Pentathlon – P13 event.  At the time of the games he was living in New South Wales.

Marit Bjørgen: Marit Bjørgen (born 21 March 1980) is a Norwegian cross-country skier and six times Olympic champion from Midtre Gauldal, Norway.  She is ranked first in the all-time Cross-Country World Cup rankings with 106 individual victories.  Bjørgen is also the most successful sprinter in Cross-Country World Cup history, with twenty-nine victories.  One of her most notable achievements was becoming the most successful athlete at the 2010 Winter Olympics by winning five medals, including three gold medals.  She also won three gold medals at the 2014 Winter Olympics.  With her 2014 medals, she became, alongside Raisa Smetanina and Stefania Belmondo, the most medaled female Winter Olympian.  However, she has more gold medals amongst her 10 Olympic medals than either of them.  She is well known for her endurance, fitness, technical strength, mental toughness, and also her finishing sprints.  She excels equally in both classic and skate style skiing, and does well through all distances from the sprint events to the long distance ones.

James Turner (athlete): James Michael Turner {'1': ", '2': ", '3': ", '4': "} (born 22 May 1996) is an Australia Paralympic athlete and soccer player with cerebral palsy.  He has represented Australia as part of the Australia Paralympic soccer team, the ParaRoos, and was its player of the year in 2013.  At the 2016 Summer Paralympics, he won the Men's 800 m T36 in a world record time of 2:02.39.  At the 2017 World Para Athletics Championships in London, England, he won three gold medals including the 200 m T36 in a world record.

Jouko Grip: Jouko Grip (born January 10, 1949 in Pälkäne) is a Paralympic athlete who has won medals in both the Summer and Winter Games.  Most of his medals were in Nordic skiing.  He is Finnish and has polio in his left hand.  In 2006 he was inducted into the Paralympic Hall of Fame.  He competed at the Summer Paralympics twice, in 1984 and 1988, and participated in track and field athletics both times, winning two gold medals in the 400 and 1500 metre races in 1984.  He competed in seven consecutive Winter Paralympics, from 1980 to 2002, and won a total of ten gold and five silver medals.  Two of his winter gold medals were won in the biathlon and the remainder of his winter medals were from cross-country skiing.

Ellie Cole: Ellie Victoria Cole, {'1': ", '2': ", '3': ", '4': "} (born 12 December 1991) is an Australian Paralympic swimmer and wheelchair basketball player.  After having her leg amputated due to cancer, she trained in swimming as part of her rehabilitation program and progressed more rapidly than instructors had predicted.  She began competitive swimming in 2003 and first competed internationally at the 2006 IPC Swimming World Championships, where she won a silver medal.  Since then, she has won medals in the Pan Pacific Swimming Championships, the Commonwealth Games, the Paralympic Games, the IPC Swimming World Championships, and various national championships.  At the 2012 London Paralympics, she won four gold and two bronze medals.  After the Games, she underwent two shoulder reconstructions and made a successful return to swimming at the 2015 IPC Swimming World Championships winning five medals including three gold medals.  She represented Australia at the 2016 Rio de Janeiro Paralympics, winning two gold medals, three silver and a bronze.

Casey Redford: Casey Redford is a Paralympic swimming competitor from Australia.  A Victorian Institute of Sport scholarship holder, she won three gold medals at the 1999 FESPIC Games, and a bronze medal at the 2000 Summer Paralympics in Sydney in the Women's 100 m backstroke S9 event.

FESPIC Games: The FESPIC Games or the Far East and South Pacific Games for the Disabled, was a multi-sports games in Asia and the South Pacific region.

Sanaa Benhama: Sanaa Benhama (born 9 June 1982) is a Paralympic athlete from Morocco competing mainly in category T13 sprint events.  She has competed at two Summer Paralympics, most notably at the 2008 Summer Paralympics in Beijing, China where she won three gold medals dominating the sprint field in her class.

Wayne Patchett: Wayne John Patchett is an Australian Paralympic athlete.  At the 1976 Toronto Games, he won a gold medal in the Men's Discus 1A event and a silver medal in the Men's Shot Put 1A event.  At the 1980 Arnhem Games, he won three gold medals in the Men's Club Throw 1A, Men's Discus 1A, and Men's Shot Put 1A events.  In 2000, he received an Australian Sports Medal.

Question: A Paralympic athlete from which country won three gold medals at a multi-sports games in Asia and the South Pacific region in 1999?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "athlete_name": {
      "type": "string",
      "description": "The name of the Paralympic athlete."
    },
    "country": {
      "type": "string",
      "description": "The country the athlete represented."
    },
    "games_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the multi-sports games."
        },
        "year": {
          "type": "integer",
          "description": "The year the games took place."
        },
        "gold_medals_won": {
          "type": "integer",
          "description": "The number of gold medals won by the athlete at these games."
        }
      },
      "required": [
        "name",
        "year",
        "gold_medals_won"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "athlete_name",
    "country",
    "games_details"
  ],
  "additionalProperties": false
}
