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
FPAI Indian Player of the Year: The FPAI Indian Player of the Year is an annual award given to an Indian player who is adjudged to have been the best of the year in Indian football.  The award has been presented since the 2009–10 season and the winner is chosen by a vote amongst the members of the players' trade union, the Football Players' Association of India.  The first winner of the award was Dempo striker Sunil Chhetri.  Anas Edathodika, the Defender of Mohun Bagan  and Indian national team has been the recent winner, for 2016–17.

Empire Award for Best Film: The Empire Award for Best Film is an Empire Award presented annually by the British film magazine "Empire" to honor the best film of the previous year.  The Empire Award for Best Film is one of five ongoing awards which were first introduced at the 1st Empire Awards ceremony in 1996 (the others being Best Actor, Best Actress, Best Director and Best British Film) with "Braveheart" receiving the award. ""  is the most recent winner in this category.  Winners are voted by the readers of "Empire" magazine.

USA Basketball Male Athlete of the Year: The USA Basketball Male Athlete of the Year is an annual award issued by USA Basketball that honors the top American male basketball performer during the year's international competition.  The most recent winner(s) are Kevin Durant and Carmelo Anthony, who were named co-players of the year in 2016 for their performances in the 2016 Olympic Games.

Empire Award for Best British Film: The Empire Award for Best British Film is an Empire Award presented annually by the British film magazine "Empire" to honor the best British film of the previous year.  The Empire Award for Best British Film is one of five ongoing awards which were first introduced at the 1st Empire Awards ceremony in 1996 (the others being Best Actor, Best Actress, Best Director and Best Film) with "Shallow Grave" receiving the award. ""  is the most recent winner in this category.  Winners are voted by the readers of "Empire" magazine.

Carmelo Anthony: Carmelo Kyam Anthony (born May 29, 1984) is an American professional basketball player for the Oklahoma City Thunder of the National Basketball Association (NBA).  Anthony attended Towson Catholic High School and Oak Hill Academy before playing college basketball at Syracuse.  In Anthony's freshman season, he led the Orangemen to their first and only National Championship and was named the NCAA Tournament's Most Outstanding Player.  Anthony then entered the 2003 NBA draft where he was selected with the third overall pick by the Denver Nuggets.

Empire Legend Award: The Empire Legend Award (also known as the Legend of Our Lifetime Award) is an honorary Empire Award presented by the British film magazine "Empire".  The Empire Legend Award was first introduced at the 17th Empire Awards in 2012 with Tim Burton receiving the award.  Ralph Fiennes is the most recent winner in this category.  At the most recent awards ceremony three honorary awards were presented: Empire Hero Award, Empire Inspiration Award and Empire Legend Award.

OHL Executive of the Year: The OHL Executive of the Year Award is given annually to the top executive in the Ontario Hockey League.  It was first awarded in 1989–90.  The most recent winner, Mike Vellucci is the first person in OHL history to be named both executive and coach of the year in the same season.

Shaun Meiklejohn: Shaun Meiklejohn (born 30 November 1961 in Pretoria, South Africa) is a South African marathon and ultra-marathon athlete, most widely known for his winning of the 1995 Comrades Marathon, the 89 km marathon between Durban & Pietermaritzburg.  Before the 2014 race winner Bongmusa Mthembu, he was the most recent winner from the race province, KwaZulu-Natal.  He has run the race a total of 27 times.

Empire Award for Best Comedy: The Empire Award for Best Comedy is an Empire Award presented annually by the British film magazine "Empire" to honor the best comedy film of the previous year.  The Empire Award for Best Comedy is one of four new Best Film ongoing awards which were first introduced at the 11th Empire Awards ceremony in 2006 (along with Best Horror, Best Sci-Fi/Fantasy and Best Thriller) with "" receiving the award. " Paddington" is the most recent winner in this category.  Winners are voted by the readers of "Empire" magazine.

Empire Inspiration Award: The Empire Inspiration Award is an honorary Empire Award presented by the British film magazine "Empire".  The Empire Inspiration Award was first introduced at the 2nd Empire Awards ceremony in 1997 with the Monty Python team receiving the award.  The award was absent from the 3rd, 8th, 12th and 14th Empire Awards ceremonies.  Christopher Nolan is the most recent winner in this category.  At the most recent awards ceremony three honorary awards were presented: Empire Hero Award, Empire Inspiration Award and Empire Legend Award.

Question: Who played at Syracuse and was the recent winner of USA basketblal mael athlethe of the year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the individual who meets the criteria."
    },
    "award_details": {
      "type": "object",
      "properties": {
        "award_name": {
          "type": "string",
          "description": "The full name of the award received."
        },
        "award_year": {
          "type": "integer",
          "description": "The year the award was received."
        },
        "is_co_winner": {
          "type": "boolean",
          "description": "Indicates if the person was a co-winner of the award."
        },
        "other_co_winners": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of other individuals who co-won the award, if any."
        }
      },
      "required": [
        "award_name",
        "award_year",
        "is_co_winner"
      ],
      "additionalProperties": false
    },
    "college_attended": {
      "type": "string",
      "description": "The name of the college where the person played."
    },
    "sport": {
      "type": "string",
      "description": "The sport the person played at college and for which they received the award."
    }
  },
  "required": [
    "person_name",
    "award_details",
    "college_attended",
    "sport"
  ],
  "additionalProperties": false
}
