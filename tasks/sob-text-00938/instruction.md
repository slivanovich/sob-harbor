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
Kevin Randleman: Kevin Christopher Randleman (August 10, 1971 – February 11, 2016) was an American mixed martial arts fighter and a former UFC Heavyweight Champion.  Randleman's background was in collegiate wrestling, and he competed in the heavyweight and light heavyweight classes.  Randleman had fought in the UFC, PRIDE, WVR, and Strikeforce.  He was previously associated with Mark Coleman's Team Hammer House, before training at Randy Couture's gym in Las Vegas, Nevada.

Philip Sahagun: Philip Sahagun is a martial arts champion in both forms and fighting.  With a background in American Kenpo, Kickboxing, Wushu and Shaolin Kung Fu, Philip is a 7-time National Weapons Champion and a 3-Time International Martial Arts Council Grand Champion.  Philip has been a semi-finalist on America's Got Talent, as well as a contestant on two of China’s top-rated reality competitions, Kung Fu Star and Jackie Chan’s Disciple.  In 2008 & 2009 He toured as a martial arts ‘Ninja’ performer for Tina Turner’s 50th Anniversary World Tour.  He has taught martial arts extensively and represented America twice at the World Traditional Wushu Festival in China where he won both gold and silver medals for the U.S. Team.  In 2010 he founded the group "Kung Fu Heroes" an international martial arts team whose mission is to unite individuals seeking to become "Heroes" and positive role models in local and worldwide communities and currently resides as a head teacher at South Coast Martial Arts in Costa Mesa.

Xtreme Couture Mixed Martial Arts: Xtreme Couture Mixed Martial Arts is an American mixed martial arts training organization headed by former UFC Champion and former co-founder of Team Quest, Randy Couture.  Xtreme Couture was founded with the flagship gym in Las Vegas.  Since then, the franchise has spread to other cities in the United States and Canada.  Xtreme Couture Las Vegas is one of the largest gyms (over 24000 sqft ), most recognized brands and MMA gyms in the world where many past and current top MMA fighters train.

Ron Waterman: Ron Waterman (born November 23, 1965) is an American mixed martial artist, professional wrestler, and celebrity member of the Team Impact motivational group.  He holds notable victories over Valentijn Overeem, Ricco Rodriguez, Kevin Randleman, and Mario Rinaldi.  He was the only WEC Super Heavyweight Champion.

Nova União (mixed martial arts): Nova União (] ) is a Brazilian Jiu-Jitsu (BJJ) academy and mixed martial arts team located in Rio de Janeiro, Brazil.  Their BJJ black belts have participated in BJJ, submission grappling and MMA competitions all over the world.  BJ Penn's victory at the Mundials marked the first time a non-Brazilian native won gold in the black belt category.  Since 2008 Nova União has become a familiar name in the Mixed Martial Arts scene as a result of stabling the former #1 ranked featherweight fighter in the world, Jose Aldo, as well as Renan Barão, the former UFC Bantamweight champion, and another top ten ranked featherweight in Marlon Sandro.  Nova União is one of the top professional MMA training camps.

Team Hammer House: Team Hammer House is a mixed martial arts team operating out of Columbus, Ohio, made up of mostly former NCAA wrestlers.  While Hammer House focuses on amateur wrestling they do have cross training deals with notable fighters and camps such as Matt Serra, Pat Miletich and Xtreme Couture Mixed Martial Arts.  Founded by former UFC champion Mark Coleman, Team Hammer House has attracted such mixed martial arts fighters as Kevin Randleman and Phil Baroni.

Carlos Barreto (fighter): Carlos Barreto (born July 22, 1968 in Rio de Janeiro is a retired Brazilian mixed martial arts fighter who was trained by the legendary Carlson Gracie.  A veteran of both the UFC and Pride Fighting Championships, Barreto holds notable wins over Ben Rothwell, Kevin Randleman and Dan Bobish.  He won the IVC Heavyweight Championship in 1999.

Mixed Martial Arts Pakistan: Mixed Martial Arts Pakistan (or PAK MMA) is the premiere mixed martial arts (MMA) and martial arts promotion based in Pakistan that was created in December 2007 by Bashir Ahmad to promote martial arts (and martial sports such as boxing and wrestling) styles in Pakistan with a particular focus on mixed martial arts competition.

Kenichi Yamamoto (mixed martial artist): Kenichi Yamamoto (山本 喧一 , Yamamoto Ken'ichi ) is a Japanese mixed martial artist and professional wrestler.  Known for his pro wrestling career in UWF International, Yamamoto also competed against some of the best MMA fighters of his era in RINGS, Pride and the UFC, taking on Kevin Randleman, Genki Sudo and Pat Miletich, among others.

Derrick Lewis (fighter): Born and raised as one of seven siblings, the second oldest, by a single mother in New Orleans, Louisiana, Lewis was troubled growing up and was often involved in street fighting.  In 1999, Lewis and his family relocated to Houston, Texas due to his mother being in an abusive relationship.  At the age of 17, Lewis began training in boxing and was preparing for his first amateur fight when the gym unexpectedly shut down.  Two weeks after graduating from high school, Lewis was charged with aggravated assault, and was placed on probation.  Two years later, while attending Kilgore College on a full scholarship for football, Lewis violated his probation and was sentenced to five years in prison, but ended up serving three and a half.  A week after being released, Lewis was introduced to mixed martial arts by a friend and, while working as a tow-truck driver, continued with boxing under the tutelage of George Foreman.  However, after dominating in his first professional mixed martial arts fight, Lewis decided to focus on mixed martial arts.

Question: Before training in Las Vegas, Kevin Randleman was working with a mixed martial arts team operating out of which city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "fighter_name": {
      "type": "string",
      "description": "The name of the fighter in question."
    },
    "previous_team_name": {
      "type": "string",
      "description": "The name of the mixed martial arts team the fighter was previously associated with."
    },
    "team_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the team operates from."
        },
        "state": {
          "type": "string",
          "description": "The state where the team operates from."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "fighter_name",
    "previous_team_name",
    "team_location"
  ],
  "additionalProperties": false
}
