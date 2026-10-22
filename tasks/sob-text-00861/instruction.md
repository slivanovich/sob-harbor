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
Florence Griffith Joyner: Florence Delorez Griffith Joyner (December 21, 1959 – September 21, 1998), also known as Flo-Jo, was an American track and field athlete.  She is considered the fastest woman of all time based on the fact that the world records she set in 1988 for both the 100 m and 200 m still stand.  During the late 1980s she became a popular figure in international track and field because of her record-setting performances and flashy personal style.

Elaine Thompson: Elaine Thompson (born 28 June 1992) is a Jamaican track and field sprinter.  She rose to prominence as part of the gold medal-winning team in the 4x100 metres relay at the 2015 World Championships, where she also won a silver medal in the 200 metres.  At the 2016 Olympic Games in Rio de Janeiro, Thompson completed a rare sprint double when she won gold in the 100m (with a time of 10.71 s) and the 200m (21.78 s), becoming the first female sprinter to do so since Florence Griffith Joyner at the Seoul Olympics in 1988.  Thompson currently ranks as the fifth-fastest woman ever in the 200 metres event and tied fourth-fastest in the 100 metres.

Jesse Owens Memorial Stadium: Jesse Owens Memorial Stadium is a 10,000-capacity stadium located in Columbus, Ohio, United States.  The stadium is home of the Ohio State Buckeyes men's and women's lacrosse teams as well as the soccer and track and field teams.  The stadium opened for soccer in the fall of 2001.  It also hosts the OHSAA boys and girls track and field State Tournament.  It is named after former OSU athlete, Jesse Owens.  Jesse Owens (September 12, 1913 – March 31, 1980) was an American track and field athlete and four-time Olympic gold medalist as a black man in the 1936 Games in Nazi Germany.

Chioma Ajunwa: Chioma Ajunwa-Opara, MON (born 25 December 1970) – also known as Chioma Ajunwa – is a Nigerian former athlete who specialised in the long jump.  After various setbacks in her career she achieved fame when she became the first athlete in her country to win an Olympic gold medal at the 1996 Summer Olympics in Atlanta, and to date remains Nigeria's only individual Olympic gold medalist.  Chioma Ajunwa is the first black African woman to win an Olympic gold medal in a field event.  Ajunwa is also an officer with the Nigerian Police Force.

Brandon Richards: Brandon Richards (born February 6, 1967) is an American Track and Field athlete.  He was the national high school record holder in the pole vault and a son of double Olympic Gold Medalist in the pole vault, Bob Richards.  He is the third of four of Richards' sons who all excelled at the pole vault—Bob Jr. finished second in 1968 and Tom won the CIF California State Meet in the pole vault.

List of career achievements by Michael Johnson: This page details the career achievements of American track & field athlete Michael Johnson.  Over the course of his career, Johnson consistently dominated his events, winning almost every time he took to the track.  He set numerous world and Olympic records in short distance track, both as an individual and as a member of relay teams.  His domination of the 400 meter race is unprecedented in the history of track and field, making him arguably the greatest 400 m runner of all time.  For approximately one decade, Michael Johnson held the world records in the 200 meters, 400 meters and indoor 400 meters, as well as the world's best time in the 300 meters and the world record for the 4 by 400 meter relay.  He is still a world record holder for the 4 x 400 meter relay.  In 2004, Johnson was voted into the United States Track & Field Hall of Fame.  At the ceremony, his record-setting 200-meter performance at the 1996 Summer Olympics was deemed the greatest track and field moment in the past 25 years.  Johnson is generally considered one of the greatest and most consistent sprinters in the history of track and field.

Michael Norman (sprinter): Michael Norman, Jr. (born December 3, 1997) is an American track and field athlete who competes in the 100 meters, 200 meters, and 400 meters.  He graduated from Vista Murrieta High School in Murrieta, California in 2016.  He currently attends University of Southern California.  He broke the NFHS record in the 400 meters with a time of 45.19 seconds at the 2015 CIF California State Meet held at Buchanan High School in Clovis, California on June 6, 2015.  His time is the fastest 400 meters run by a U.S. high school athlete against other high school-aged athletes, along with Aldrich Bailey who also ran 45.19 seconds in Lubbock, Texas on April 28, 2012.  The time, however, is not the fastest 400 meters ever run by a U.S. high school-aged athlete according to the List of United States High School National Records in Track and Field.  The time of 44.69 seconds set by Darrell Robinson is the fastest.  However, it was set at a non-NFHS sanctioned meet, therefore only being acknowledged as a National Record by Track & Field News.  Norman's NFHS record is currently awaiting NFHS ratification.  On June 30, 2015, Norman was named the Gatorade Player of the Year for his achievements in Track and Field.  He is only the 2nd non-senior to win the Gatorade Player of the Year award in the 30-year history of the program and the first male sprinter to win the honors as a non-senior.

Al Joyner: Alfrederick "Al" Joyner (born January 19, 1960) is an American former athlete and now coach.  He was born in East St. Louis, Illinois.  He is the 1984 Olympic gold medalist in the triple jump.  He was also the husband of three-time Olympic gold medalist and world 100 m and 200 m record holder Florence Griffith Joyner and is the brother of three-time Olympic gold medalist and world heptathlon record holder Jackie Joyner-Kersee.

Tom Patsalis: Tom Patsalis (December 6, 1921 – July 29, 2014) was an American track and field athlete.  He has set 26 World Records in his career, a career that was still active in his late 80s.  As of 2014 he is the World Record holder in the M60 Long Jump, set in 1982 and thus a record he has held for more than three decades.  As of 2014, only one jumper has come within .2 m (0 ft floor(((.2)*3.28084)−(floor((.2)*3.28084)) *12) in) .  He is also the American record holder in the Long Jump for the M60 age division, has an as yet unrecognized mark that has been pending since 1977 (though recognized by the California Track News chief statistician at the time, Percy Knox) still 7 inches superior to the listed American record and is the American record holder in the Triple Jump in the M60 and M65 age divisions.  He was selected to the Masters division of the National Track and Field Hall of Fame in 2003.

Dawn Harper-Nelson: Dawn Harper-Nelson (born May 13, 1984) is an American track and field athlete who specializes in the 100-meter hurdles.  She was the gold medalist in the event at the 2008 Beijing Olympic Games and the silver medalist in the 2012 London Olympic Games and the 2017 World Championships.  Dawn Harper is the first American 100-meter hurdler to ever win gold at an Olympics and medal in the following Olympics.  She is trained by Bob Kersee, husband of Jackie Joyner-Kersee, six time Olympic medalist also from her hometown of East St. Louis, Illinois.

Question: Alfrederick "Al" Joyner, is an American former athlete and now coach,he was also the husband of Olympic gold medalist, and record holder Florence Griffith Joyner, also known as Flo-Jo, was an American track and field athlete, she's considered the fastest woman of all time, based on the fact that the world records she set, in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "athlete_name": {
      "type": "string",
      "description": "The full name of the athlete."
    },
    "athlete_nickname": {
      "type": "string",
      "description": "The nickname of the athlete."
    },
    "sport": {
      "type": "string",
      "description": "The sport the athlete competes in."
    },
    "record_setting_year": {
      "type": "integer",
      "description": "The year the world records were set."
    },
    "events": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of events for which world records were set."
    }
  },
  "required": [
    "athlete_name",
    "sport",
    "record_setting_year",
    "events"
  ],
  "additionalProperties": false
}
