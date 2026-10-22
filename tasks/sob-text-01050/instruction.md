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
Chino Hills High School: Chino Hills High School, abbreviated CHHS, is located in Chino Hills, California and is a public comprehensive high school serving a student body from three cities in the Chino Valley Unified School District.  The school was established in 2001 and is located in the City of Chino Hills, which is in the southwest corner of San Bernardino County.  The City of Chino Hills was incorporated in 1991, and is now a community of 76,131.  Chino Valley Unified School District serves over 29,000 students in Chino, Chino Hills, and south Ontario, slightly down from 30,659 three years ago.  After years of rampant growth, enrollment has somewhat stabilized.  The district employs over 2,400 people, and supports thirty-five schools including four comprehensive high schools and one continuation school.

Palomares League: Palomares League is a high school athletic league in Southern California.  It is a member of the CIF Southern Section, serving the eastern San Gabriel Valley and Chino Hills in San Bernardino County.  The 2014-15 school year will be its inaugural season.  Several of these schools were previously in what was known as the Sierra League.

Woodland Hills High School: Woodland Hills High School is a large, suburban public high school providing grades 9-12 for the Woodland Hills School District located in Churchill, Pennsylvania.  It services the communities of Braddock, Braddock Hills, Chalfant, Churchill, East Pittsburgh, Edgewood, Forest Hills, North Braddock, Rankin, Swissvale, Turtle Creek, and Wilkins Township.  In April 2014, Principal Dan Stephens retired and an interim principal was appointed.  In 2013, Woodland Hills High School enrollment was reported as 1,244 pupils in 9th through 12th grades, with 69% of pupils were eligible for the federal free or reduced-price lunch due to family poverty.  Additionally, 16.6% of pupils receiving special education services, while 9.8% of pupils were identified as gifted.  The school employed teachers.  Per the PA Department of Education 100% of the teachers were rated "Highly Qualified" under the federal No Child Left Behind Act.  The school is a Title I school.

LaVar Ball: LaVar Ball (born October 23, 1968) is an American businessman and media personality, who attracted widespread public and media attention in 2017 after making a series of incredible claims concerning the careers of himself and his sons.  He is the father of basketball players Lonzo of the Los Angeles Lakers, UCLA freshman LiAngelo, and Chino Hills High School basketball player LaMelo.  A former basketball and American football player, LaVar is the founder and CEO of the sports apparel company Big Baller Brand.

Chino Valley Unified School District (California): The Chino Valley Unified School District is a school district in San Bernardino County, California, United States.  It serves the cities of Chino, Chino Hills, and the southwestern portion of Ontario, though originally it served only Chino when it was founded in 1860.  It now encompasses 88 sqmi and serves about 32,000 students from grades kindergarten up to 12th grade.  CVUSD serves four high schools, five junior high schools, twenty-one elementary schools, one continuation school, and an adult school.

Laguna Hills High School: Laguna Hills High School is a public high school located in Laguna Hills, California which serves the Saddleback Valley Unified School District.  The school has the smallest student enrollment of the district’s four schools at approximately 1,600 students.  The mascot for Laguna Hills is the Hawk, and the official colors are brown and gold.  220 credits are required to graduate from Laguna Hills High School.  89% of LHHS grads are accepted at 2 or 4-year colleges.

Ruben S. Ayala High School: Senator Ruben S. Ayala Senior High School, often abbreviated as Ayala High School or AHS, is located in Chino Hills, California and is one of the four comprehensive high schools in the Chino Valley Unified School District.  The school was established in 1990 and named after California state senator Ruben S. Ayala.  It received the 2011 California Distinguished School award and the 2015 California Gold Ribbon School Award.

Granite Hills High School (El Cajon, California): Granite Hills High School is a California Distinguished School, public and comprehensive high school located in El Cajon, California and serves students in grades nine through twelve.  Opened in 1960, Granite Hills is one of thirteen high schools in the Grossmont Union High School District.  GHHS is the home of the Eagles.  Granite Hills High School has been an IB World School since July 2001.

LaMelo Ball: LaMelo Ball (born August 22, 2001) is an American basketball player who attends Chino Hills High School in Chino Hills, California.  A junior point guard, he has repeatedly drawn attention from national sports media.  Ball verbally committed to play basketball for UCLA at age 13.  He is the brother of Los Angeles Lakers rookie Lonzo Ball and UCLA basketball freshman LiAngelo Ball.  His father LaVar grew into a media personality in 2017.

Calaveras Hills High School: Calaveras Hills High School (CHHS) is one of the two high schools of Milpitas, California.  Calaveras Hills High School works with students who need an alternative form of education.  Calaveras Hills High is referred to as "Cal Hills" by students and the community.  Cal Hills is the most successful alternative school in the state.  Test scores for the STAR test rose hundreds of points from 500+ to 714.  Cal Hills often has a waiting list to get into the program.

Question: LaMelo Ball, is an American basketball player who attends Chino Hills High School in Chino Hills, California, his father is an American businessman and media personality, who attracted widespread public and media attention in which year, after making a series of incredible claims concerning the careers of himself and his sons?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the basketball player."
    },
    "school_attended": {
      "type": "string",
      "description": "The name of the high school the player attends."
    },
    "school_location": {
      "type": "string",
      "description": "The city and state where the high school is located."
    },
    "father_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the father."
        },
        "occupation": {
          "type": "string",
          "description": "The occupation of the father."
        },
        "year_gained_media_attention": {
          "type": "integer",
          "description": "The year the father attracted widespread public and media attention."
        },
        "reason_for_attention": {
          "type": "string",
          "description": "The reason for the father gaining media attention."
        }
      },
      "required": [
        "name",
        "occupation",
        "year_gained_media_attention",
        "reason_for_attention"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "school_attended",
    "school_location",
    "father_details"
  ],
  "additionalProperties": false
}
