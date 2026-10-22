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
Baltimore's Marching Ravens: Baltimore's Marching Ravens are the official marching band of the Baltimore Ravens American football team.  They were founded as the Baltimore Colts' Marching Band on September 7, 1947 and have continuously operated ever since, supporting three separate football franchises.  The band first supported the original Baltimore Colts from 1947 to 1950, but continued to operate even after the franchise disbanded in 1950.  After a new Baltimore Colts franchise was installed in 1953, the band became associated with the newly founded team.  The band endured a second relocation when the Colts moved to Indianapolis in the middle of the night in 1984, leaving Baltimore without a team for eleven years.  The band became attached to a third franchise when the Cleveland Browns relocated to Baltimore in 1996 and became the Ravens.  They are one of two official marching bands in the NFL, the other being the Washington Redskins Marching Band.

Oregon State University Marching Band: With over 250 members, the Oregon State University Marching Band, ("OSUMB"), is the marching band of Oregon State University, known as the ""Spirit and Sound of OSU"."  It was founded in 1891 making it the oldest band in the Pac-12.  The Oregon State University Marching Band is the primary athletic band at Oregon State.  In addition to the Oregon State University Marching Band, other athletic bands include Basketball Band, Rhythm & Beavs, Rhythm & Beavs: Travel Band, the Away Game Pep Band (for select away games), Alumni Band (the band that covers any games occurring prior to the start of the school term), Gymnastics Band (the ensemble that performs at home gymnastic meets; this ensemble also include alumni members), and Bar Band (a small ensemble that tours local bars on the day before a home football game).  All band members are required to participate in marching band before they may be eligible to participate in any of the other bands Oregon State offers.

The Pride of the Sunshine: The University of Florida Fightin' Gator Marching Band, also known as The Pride of the Sunshine, is the official marching band for the University of Florida.  They perform at every Florida Gators home football game at Ben Hill Griffin Stadium and also at various other events such as pep rallies, parades, and the annual Orange and Blue spring scrimmage game.  A full band usually travels to one away game a year while at other games a small/medium-sized pep band will attend.  Members of the Gator Band, as well as other University of Florida students, are encouraged to join other ensembles such as concert band, jazz band, basketball band, and volleyball band.  The majorettes (twirlers) for the marching band are called the Gatorettes.  The color guard is called the Florida Visual Ensemble.

Marian University Marching Band: The Marian University Marching Band, is the official marching band of Marian University in Indianapolis, Indiana.  The marching band is the largest student organization on campus and the university's largest for-credit course.  Under the leadership of Dr. Sid Hearn, the Marian University Marching Band took the field for the first time on September 19, 2009.

Band camp: A band camp typically refers to a high school, college, or university marching band summer camp.  Band camp is often mandatory for members of the band, and constitutes the majority of the preparation a marching band makes before its marching season (learning how to march, learning "sets" on the field, memorizing show songs).  A high school marching band may travel to a college or university for band camp for use of its facilities (dormitories, fieldhouses, fields) and services, or it may stay at the school.  The time at band camp is used for focused rehearsals and time for bonding between band members.The colorguard also learns and rehearses with the marching band.

Cavalier Marching Band: The Cavalier Marching Band (CMB) is the premier marching ensemble at the University of Virginia.  Under the direction of Dr. William E. Pease, the first full-time marching band director in University of Virginia history, the Cavalier Marching Band made its debut on September 11, 2004 after a considerable donation was made by University of Virginia benefactors Carl and Hunter Smith to found the band in 2003.  Currently in its eleventh season, the band is composed of over 330 of the University of Virginia's best and brightest student musicians, with representatives from over 80 different majors from all 7 of the undergraduate schools.  Whenever describing the composition of the members of the band, Pease typically states that almost none are music majors but almost a third hold leadership positions, thus emphasizing the virtue of student-self-governance, an ideal widely emphasized at the University of Virginia.  On September 2, 2011, the Cavalier Marching Band moved into the Hunter Smith Band Building within the College of Arts & Sciences.

Mustang Band: The Cal Poly Mustang Band, also known as The Pride of the Pacific, is the official marching band of California Polytechnic State University in the city of San Luis Obispo, California.  Although the band is not a competitive marching band they serve as a school spirit organization.  The band functions in two different forms throughout the year.  In the fall the band marches as The Mustang Marching Band and during Cal Poly's winter quarter they function as a pep band.  The band attends many athletic events during the year to encourage the school's athletic teams and audience support/involvement.  The marching band is well-known around campus as an exciting and spirited group that brings pep, passion, and tradition to every performance.  The marching band is conducted by three directors: Andrew McMahan (Director of Bands), Christopher Woodruff (Associate Director), and Len Kawamoto (Assistant Director).

Sound of the South Marching Band: The Sound of the South is the official marching band of Troy University.  The marching band was established in 1939 and has been referred to by its current name since 1965.  The band was named by John M. Long soon after he was hired as band director.  The band, now boasting over 300 members on a regular basis, has enjoyed major success in performing at hundreds of marching band competitions, dozens of different college and professional football venues, and follows the football team to almost every away game.  The band's "trademark" piece that is played before every performance of the band is called "The Fanfare" and was written by John M. Long in 1965.

Frank Roman: Frank Roman (March 3, 1877 in Italy – December 19, 1928 in Atlanta, Georgia) was a musician, composer, and band director of the Georgia Tech Yellow Jacket Marching Band at the Georgia Institute of Technology from 1913 to 1929.  He is most known for his arrangement of Georgia Tech's fight song, Ramblin' Wreck from Georgia Tech, which he copyrighted in 1919.

Georgia Tech Yellow Jacket Marching Band: The Georgia Tech Yellow Jacket Marching Band (also known as the Marching Yellow Jackets) is the official marching band of the Georgia Institute of Technology.  Founded in 1908 by a group of 14 students, the Georgia Tech Band is one of the school's oldest student organizations.

Question: What Marching band is the official marching band of the Georgia Institute of Technology and directed by Frank Roman?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the marching band."
    },
    "university_affiliation": {
      "type": "string",
      "description": "The university the marching band is officially associated with."
    },
    "director_info": {
      "type": "object",
      "properties": {
        "director_name": {
          "type": "string",
          "description": "The name of the band director."
        },
        "director_start_year": {
          "type": "integer",
          "description": "The year the director started their tenure."
        },
        "director_end_year": {
          "type": "integer",
          "description": "The year the director ended their tenure."
        }
      },
      "required": [
        "director_name",
        "director_start_year",
        "director_end_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "band_name",
    "university_affiliation",
    "director_info"
  ],
  "additionalProperties": false
}
