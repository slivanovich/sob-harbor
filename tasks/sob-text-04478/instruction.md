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
'Round Springfield: "'Round Springfield" is the 22nd episode of "The Simpsons"' sixth season.  It originally aired on the Fox network in the United States on April 30, 1995.  In the episode, Bart is rushed to the hospital after eating a jagged metal Krusty-O and decides to sue Krusty the Clown.  Whilst visiting Bart, Lisa meets her old mentor, jazz musician Bleeding Gums Murphy.  She is saddened when she later learns that Murphy has died, and resolves to honor his memory.  Steve Allen (as himself) and Ron Taylor (as Bleeding Gums Murphy) guest star, each in their second appearance on the show.  Dan Higgins also returns as the writer and performer of all of Lisa and Bleeding Gums' saxophone solos.

Acute necrotizing ulcerative gingivitis: Acute necrotizing ulcerative gingivitis (ANUG; colloquially known as trench mouth) is a common, non-contagious infection of the gums with sudden onset.  The main features are painful, bleeding gums, and ulceration of inter-dental papillae (the sections of gum between adjacent teeth).  This disease, along with necrotizing (ulcerative) periodontitis (NP or NUP) is classified as a necrotizing periodontal disease, one of the seven general types of periodontitis.  The often severe gingival pain that characterizes ANUG distinguishes it from the more common chronic periodontitis which is rarely painful.  ANUG is the acute presentation of necrotizing ulcerative gingivitis (NUG), which is the usual course the disease takes.  If improperly treated or neglected, NUG may become chronic and/or recurrent.  The causative organisms are mostly anaerobic bacteria, particularly Fusobacteria and spirochete species.  Predisposing factors include poor oral hygiene, smoking, malnutrition, psychological stress and immunosuppression (sub-optimal functioning of the immune system).  When the attachments of the teeth to the bone are involved, the term NUP is used.  Treatment of ANUG is by debridement (although pain may prevent this) and antibiotics (usually metronidazole) in the acute phase, and improving oral hygiene to prevent recurrence.  Although the condition has a rapid onset and is debilitating, it usually resolves quickly and does no serious harm.  The synonym "trench mouth" arose during World War I as many soldiers developed the disease, probably because of the poor conditions and extreme psychological stress.

Moaning Lisa: "Moaning Lisa" is the sixth episode of "The Simpsons"<nowiki>'</nowiki> first season.  It originally aired on the Fox network in the United States on February 11, 1990.  The episode was written by Al Jean and Mike Reiss, and was directed by Wes Archer.  Ron Taylor guest stars in the episode as Bleeding Gums Murphy.  The episode deals with Lisa's depression and her attempts to sublimate it by playing her saxophone.  It received positive reviews from television critics.

Dan Higgins: Dan Higgins is an American saxophone and woodwind player.  He has worked with such artists as Aerosmith, Stevie Wonder, Neil Diamond, Al Jarreau, Maroon 5, Kenny Loggins, Barry Manilow, Elton John, Go West, The Temptations, Lionel Richie, Joe Cocker, Lisa Stansfield and Eros Ramazzotti.  He has over 300 motion picture soundtracks to his credit.  He is also known as the saxophone sound of Bleeding Gums Murphy from The Simpsons.

Mandibular fracture: Mandibular fracture, also known as fracture of the jaw, is a break through the mandibular bone.  In about 60% of cases the break occurs in two places.  It may result in a decreased ability to fully open the mouth.  Often the teeth will not feel properly aligned or there may be bleeding of the gums.  Mandibular fractures occur most commonly among males in their 30s.

Ron Taylor (actor): Ronald James Taylor (October 16, 1952 – January 16, 2002) was an American actor, singer and writer.  He grew up in Galveston, Texas and later moved to New York City to attend the American Academy of Dramatic Arts.  After graduating, Taylor began working in musical theater, appearing in "The Wiz" (1977), before getting his break with the 1982 off-Broadway production "Little Shop of Horrors".  Taylor voiced the killer plant Audrey II in the show, which ran for five years and over 2,000 performances.

Coumachlor: Coumachlor is a 1st genereation anticoagulant rodenticide which blocks formation of prothrombin and inhibits blood coagulation causing death by internal haemorrhage.  Although the compound is non-hazardous but toxicological properties have not been researched yet.  The chemical can be absorbed through the skin.  The symptoms of human contact can be nosebleeds, bleeding gums, bloody urine, extensive bruising in the absence of injury, fatigue, shortness of breath (dyspnea) on exertion.  The human consumption or inhalation of compound can also cause fluid in lungs (pulmonary edema).

Tisa Chang: Tisa Chang (born 5 April 1941) is a Chinese American actress and theatre director from Chongqing.  Her father was a diplomat and her family moved to New York City when she was a child.  Chang was interested in theatre and decided to study acting at the High School of Performing Arts and at Barnard College.  Soon afterwards she started her career as an actor performing in Broadway plays and musicals, including "Lovely Ladies, Kind Gentlemen" and "The Basic Training of Pavlo Hummel".  She also appeared in a few films such as "Ambush Bay" and "Greetings".

Bleeding on probing: Bleeding on probing which is also known as bleeding gums or gingival bleeding is a term used by dentists and dental hygienists when referring to bleeding that is induced by gentle manipulation of the tissue at the depth of the gingival sulcus, or interface between the gingiva and a tooth.  Bleeding on probing, often abbreviated BOP, is a sign of inflammation and indicates some sort of destruction and erosion to the lining of the sulcus or the ulceration of sulcular epithelium.  The blood comes from lamina propria after the ulceration of the lining.

Rick Pantera: Rick Pantera a.k.a. John Pantera (born July 24, 1965) is a male African-American pornographic actor performing in adult entertainment films in the 1990s.  Pantera appeared in 27 adult films and videos catering to gay male audiences.

Question: Where did the actor performing the voice of Bleeding Gums Murphy in the Simpsons grow up?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "character_voiced": {
      "type": "string",
      "description": "The name of the character voiced by the actor."
    },
    "show_name": {
      "type": "string",
      "description": "The name of the show the character appeared in."
    },
    "grew_up_location": {
      "type": "string",
      "description": "The city and state where the actor grew up."
    }
  },
  "required": [
    "actor_name",
    "character_voiced",
    "show_name",
    "grew_up_location"
  ],
  "additionalProperties": false
}
