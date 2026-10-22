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
Mixed martial arts: Mixed martial arts (MMA) is a full-contact combat sport that allows both striking and grappling, both standing and on the ground, using techniques from other combat sports and martial arts.  The first documented use of the term "mixed martial arts" was in a review of UFC 1 by television critic Howard Rosenberg in 1993.  The term gained popularity when newfullcontact.com, then one of the largest websites covering the sport, hosted and republished the article.  The question of who actually coined the term is subject to debate.

Wrestling: Wrestling is a combat sport involving grappling type techniques such as clinch fighting, throws and takedowns, joint locks, pins and other grappling holds.  The sport can either be theatrical for entertainment, or genuinely competitive.  A wrestling bout is a physical competition, between two (occasionally more) competitors or sparring partners, who attempt to gain and maintain a superior position.  There are a wide range of styles with varying rules with both traditional historic and modern styles.  Wrestling techniques have been incorporated into other martial arts as well as military hand-to-hand combat systems.

SCA armoured combat: SCA armoured combat, or informally heavy combat, is a combat sport developed by the Society for Creative Anachronism (SCA) in which participants in protective body armour either "act out" mock combats loosely inspired by forms of historical combat practiced in medieval Europe or under supervision, may approximate historically real combat using SCA approved safe weapons under the watch of marshals to maintain safety.  It is variously considered a combat sport, contact sport, or a form of martial art.

Shin-kicking: Shin-kicking, also known as hacking or purring, is a combat sport that involves two contestants attempting to kick each other on the shin in order to force their opponent to the ground.  It has been described as an English martial art.  It originated in England in the early 17th century, and was one of the most popular events at the Cotswold Olimpick Games until the Games ended in the 1850s.  It also became a popular pastime among Cornish miners.  In the 19th century the sport was also practised by British immigrants to the United States.  It was included in the 1951 revival of the Cotswold Olimpick Games, and remains one of its most popular events, run as the World Shin-kicking Championships.  The event now draws crowds of thousands of spectators.

Gary Cornish: Gary Cornish (born April 10, 1987) is a Scottish professional boxer.  Cornish has had 24 fights and lost his undefeated record in the ring to Anthony Joshua in a bout on September 12, 2015 in what was Cornish's first Commonwealth title attempt.

Combat sport: A combat sport, or fighting sport, is a competitive contact sport with one-on-one combat.  Determining the winner depends on the particular contest's rules.  In many fighting sports, a contestant wins by scoring more points than the opponent or by disabling the opponent.  Mixed Martial Arts, Boxing, Wrestling, Savate, Kickboxing, Muay Thai, Tae Kwon Do, Judo, Brazilian Jiu-jitsu Sambo and Fencing are examples of combat sports.

Anthony Joshua vs. Wladimir Klitschko: Anthony Joshua vs. Wladimir Klitschko was a professional boxing match contested between Anthony Joshua and Wladimir Klitschko.  The event took place on 29 April 2017 at Wembley Stadium in London, England, with Joshua's IBF and the vacant WBA (Super) and IBO heavyweight titles on the line.  Joshua won the match via technical knockout in the 11th round.  Klitschko announced his retirement from boxing a few months after the fight.

Anthony Joshua: As of May 2017, Joshua is ranked as the world's best heavyweight by the Transnational Boxing Rankings Board and BoxRec, and second best by "The Ring".  His knockout-to-win ratio stands at 100%.  Joshua is the second British boxer, after James DeGale, to win both a gold medal at the Olympics and a world title by a major professional sanctioning body, as well as being the first British heavyweight to do so.  He is also the second boxer, after Joe Frazier, to win a world heavyweight title whilst still reigning as Olympic champion at the top weight.

Professional wrestling: Professional wrestling (often shortened to pro wrestling or simply wrestling) is a form of performance art which combines athletics with theatrical performance.  It takes the form of events, held by touring companies, which mimic a title match combat sport.  The unique form of sport portrayed is fundamentally based on classical and "catch" wrestling, with modern additions of striking attacks, strength-based holds and throws and acrobatic maneuvers, much of these derive from the influence of various international martial arts.  An additional aspect of combat with improvised weaponry is sometimes included to varying degrees.

Amateur wrestling: Amateur wrestling is the most widespread form of sport wrestling.  There are two "international wrestling styles" performed in the Olympic Games under the supervision of United World Wrestling (UWW; formerly known as FILA, from the French acronym for International Federation of Associated Wrestling Styles): Greco-Roman and freestyle.  Freestyle is possibly derived from the English Lancashire style.  A similar style, commonly called collegiate (also known as scholastic or folkstyle), is practiced in colleges and universities, secondary schools, middle schools, and among younger age groups in the United States.  Where the style is not specified, this article refers to the international styles of competition on a mat.  In February 2013, the IOC voted to remove the sport from the 2020 Summer Olympics onwards.  On 8 September 2013, the IOC announced that wrestling would return to the Summer Olympics in 2020.  The rapid rise in the popularity of the combat sport mixed martial arts (MMA) has increased interest in amateur wrestling due to its effectiveness in the sport and it is considered a core discipline.

Question: Gary Cornish and Anthony Joshua engage in what combat sport? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "combat_sport_name": {
      "type": "string",
      "description": "The name of the combat sport."
    },
    "sport_type": {
      "type": "string",
      "description": "The specific type or classification of the sport (e.g., professional, amateur)."
    },
    "participants": {
      "type": "array",
      "description": "A list of individuals who participate in this combat sport.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the participant."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "combat_sport_name",
    "sport_type",
    "participants"
  ],
  "additionalProperties": false
}
