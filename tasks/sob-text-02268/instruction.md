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
Hanson Puthuff: Hanson Duvall Puthuff (August 21, 1875 – May 12, 1972) was a landscape painter and muralist, born in Waverly, Missouri.  Puthuff studied at the Art Institute of Chicago before moving to Colorado in 1889 to study at University of Denver Art School.  He traveled to Los Angeles in 1903 and for 23 years worked as a commercial artist painting billboards while painting landscapes in his leisure.  In 1926, he abandoned commercial art and devote full-time to fine art and exhibitions.  He is nationally famous for his lyric interpretations of the Southern California deserts. Puthuff died in Corona del Mar on May 12, 1972.

George Tuccaro: George Tuccaro (born May 12, 1950) was the Commissioner of the Northwest Territories.  He served in that position from May 12, 2010 until May 10, 2016.

Carlos Muñoz Pizarro: Carlos Muñoz Pizarro (September 25, 1913 – May 12, 1976) was a Chilean botanist born in the city of Coquimbo and deceased on May 12, 1976 in New York City.  He was well known for his studies of the Chilean flora, its conservation and as university professor.

Rural Solidarity: Rural Solidarity (full name "Independent Self-governing Trade Union of Individual Farmers "Solidarity"") is a trade union of Polish farmers, established in late 1980 as part of the growing Solidarity movement.  Its legalization became possible on February 19, 1981, when officials of the government of the People's Republic of Poland signed the so-called "Rzeszów - Ustrzyki Dolne Agreement" with striking farmers.  Previously, Communist government had refused farmers’ right to self-organize, which caused widespread strikes, with the biggest wave taking place in January 1981.  The Rural Solidarity was officially recognized on May 12, 1981, and, strongly backed by the Catholic Church of Poland, it claimed to represent at least half of Poland's 3.2 million smallholders.

Robbie Rogers: Robert Hampton "Robbie" Rogers III (born May 12, 1987) is an American professional soccer player who plays for LA Galaxy in Major League Soccer.  He plays as a winger and as a left back.  Rogers has also represented the United States men's national soccer team.  In February 2013, Rogers came out as gay, becoming the second male soccer player in Britain to do so after Justin Fashanu in 1990.  On May 26, 2013, he became the first openly gay man to compete in a top North American professional sports league when he played his first match for the Galaxy.

Rami Malek: Rami Said Malek (Arabic: رامي سعيد مالك‎ ‎ : "Ramī Sa‘īd Malek", ; born May 12, 1981) is an Egyptian-American actor.  He became known for the lead role of Elliot Alderson in the critically acclaimed USA Network television series "Mr. Robot", for which he won a Critics' Choice Award and the Primetime Emmy Award for Outstanding Lead Actor in a Drama Series.  He also received Golden Globe Award, Screen Actors Guild Award, and TCA Award nominations.

Maryanne Jordan: Maryanne Jordan (born May 12, 1956) is an American Democratic politician from Boise, Idaho.  She has served on the Boise City Council since 2003, and was president from 2005-2006, and 2010-2015.  In March 2015 she was appointed to the Idaho Senate by Gov. Butch Otter to succeed Elliot Werk, who resigned the previous month to take a seat on the Idaho State Tax Commission.

Andre Brown (basketball): Andre Devon Brown (born May 12, 1981) is an American professional basketball player who currently plays for Valvoline of the Mongolian National Basketball Association (MNBA).  He played college basketball for DePaul University and went on to play professionally in Europe, Asia, South America, Australia, and in the National Basketball Association and the NBA Development League.  He is also a former two-year member of the USA Basketball World Youth Games team that won a gold medal 1998 and a bronze medal in 1999.

Bracken Kearns: Bracken Kearns (born May 12, 1981) is a Canadian professional ice hockey player who currently plays under contract to the New Jersey Devils in the National Hockey League (NHL).  Kearns, who started his professional career in 2005 with the Toledo Storm in the ECHL, played 428 games in the minors before playing his first game in the NHL with the Florida Panthers.

Mr. Robot (TV series): Mr. Robot is an American drama–thriller television series created by Sam Esmail.  It stars Rami Malek as Elliot Alderson, a cybersecurity engineer and hacker who suffers from social anxiety disorder and clinical depression.  Alderson is recruited by an insurrectionary anarchist known as "Mr. Robot", played by Christian Slater, to join a group of hacktivists called "fsociety".  The group aims to destroy all debt records by encrypting the financial data of the largest conglomerate in the world, E Corp.

Question: Who plays Elliot Alderson and was born on May 12, 1981?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The full name of the actor."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character played by the actor."
    },
    "birth_date": {
      "type": "string",
      "description": "The full birth date of the actor."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the actor."
    },
    "nationality": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The nationalities of the actor."
    },
    "notable_awards_for_role": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "award_name": {
            "type": "string",
            "description": "The name of the award won."
          },
          "award_category": {
            "type": "string",
            "description": "The category of the award won."
          }
        },
        "required": [
          "award_name",
          "award_category"
        ],
        "additionalProperties": false
      },
      "description": "A list of notable awards won by the actor for the specified role."
    }
  },
  "required": [
    "actor_name",
    "character_name",
    "birth_date",
    "birth_year"
  ],
  "additionalProperties": false
}
