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
La Hora Lunática: La Hora Lunática (The Crazy Hour) was a daily one-hour live TV show aired on Telemundo.  It was the first TV show to win in its time slot over its strongest competitor, "Univisión".  The show featured the talents of "Humberto Luna", Mario Ramírez Reyes "El Comodín", "Hugo Armando" & Jackie Torres who welcomed Tito Puente, "Celia Cruz", Marc Anthony, "Julio Iglesias", "Antonio Aguilar", "Vicky Carr" & many more international stars.  The show also featured the talents of Belkis Proenza, Miguel Angel MasJuan, Luis Enrique De Los Cobos, Lucio Arroyo and singer Sylvia Flores.  Jackie Torres produced the show from 1995 until 1996 when she welcomed Mario Proenza as the new producer.

Pāvels Gumennikovs: Pāvels Gumennikovs (born January 1, 1986) is a Latvian film director, actor, writer, and producer.  He started his film career in China, where he directed his first film "Kaleidoscope" (2010) that won him a best young director and best film award in Chinese Young Film director Festival.  After that he directed a movie "I love You Riga" that become 3rd highest grossing in a country and was one of the 2 films considered to be nomination for Oscar.  It was the runner out at the end for Oscar nomination (2011) that become one of the most successful movies in Latvia and were screened in cinemas around the country and participated in European Film Festivals, after that he directed a critique very well received TV show "Yes Boss" (2012), that was proclaimed as best made show in Latvia for great acting and directing.  It was a revolutionary TV Show for Latvia, as it was first TV Show shoot in outside locations with scale of Hollywood TV Show production.  The TV Show was shown on Muz-TV channel and TV5 and was seen by 300,000 people online.

Eva Murati: Eva Murati (born 25 May 1995) is an Albanian actress and TV host.  Starting her career at the age of 15, she made herself known in Albanian showbiz through different commercials and modeling jobs.  Eva hosted her first TV program "Antilope" in 2013 and then she co-hosted with Adi Krasta "Duartrokitje", both of them at Agon Channel.  She then moved to Vizion Plus in 2016 where she hosted Miss Universe Albania and "VIP Zone".  She is currently hosting the UEFA Champions League Show and "Sports Week" at Tring Digital.  Murati debuted in film in "The Outlaw" in 2013.  She then starred in 2017 in "Ti mund të më quash Xhon".  In 2016 she starred in the TV series "Skanderbeg".  Her most recent project is "Kangur Tv Show" which is currently filming.

Garry Marshall: Garry Kent Marshall (November 13, 1934 – July 19, 2016) was an American actor, director, producer, writer, and voice artist best known for creating "Happy Days" and its various spin-offs, developing Neil Simon's 1965 play "The Odd Couple" for television, and directing "Pretty Woman", "Runaway Bride", "Valentine's Day", "New Year's Eve", "Mother's Day", ""The Princess Diaries", and "".  He provided the voice of Buck Cluck in "Chicken Little".

Chase Parker: Chase Parker (born April 22, 1994) is an American child actor who was born in San Bernardino County, California.  He is the grandson of actress Eleanor Parker and nephew of Paul Day Clemens, Jr.  Chase Parker started acting when he was only 2 years old, and his TV debut was for an Arby's commercial.  Then, in 1998 he acted in his first TV show, "General Hospital" as a younger version of Nikolas Cassadine.  In 1999, he played as Benjy Evans in "Sunset Beach" and guest starred in "7th Heaven" as a younger version of Matt.  He finished at The Woodlands High School.

Star King (TV series): Star King (Hangul: 놀라운 대회 스타킹 ; Hanja: 놀라운大會 스타킹 ) is a South Korean television show which first aired on January 13, 2007 on the SBS network.  "Star King" is the first TV show in Korea to run both online and on television simultaneously.  The last episode of “Star King” aired on August 9, 2016.

Fat Albert Rotunda: Fat Albert Rotunda is the eighth album by jazz keyboardist Herbie Hancock, released in 1970.  It also was the first album that Hancock had on the Warner Bros.  Records label, since leaving Blue Note Records.  The music was originally done for the TV special "Hey, Hey, Hey, It's Fat Albert", which later inspired "Fat Albert and the Cosby Kids" TV show.  "Fat Albert Rotunda", along with "Mwandishi" and "Crossings" was reissued in one set as "Mwandishi: The Complete Warner Bros.  Recordings" in 1994.

Hey, Landlord: Hey, Landlord is an American sitcom that appeared on NBC during the 1966-1967 season, sponsored by Procter & Gamble in the 8:30-9pm Eastern time period on Sunday nights.  It is notable for its casting director Fred Roos, who later became a producer for Francis Ford Coppola.  Roos discovered the counterculture sketch group The Committee in San Francisco and cast all members in bit parts in "Hey, Landlord."  It also served as the first TV show for prolific writer-director-producer Garry Marshall ("Happy Days", "Laverne and Shirley").

Ippadikku Rose: Ippadikku Rose (Tamil: இப்படிக்கு ரோஸ் ; English: Yours truly, Rose ) is a Tamil talk show aired on Vijay TV.  The show hosted by Rose.  The talk show deals with current affairs touching a wide variety of social issues including traditions, taboos, rebels and culture.  This is the first TV show in India hosted by a transgender person.  The show is telecast at every Thursday at 11:PM IST.

Billy Baxter (song): "Billy Baxter" is the third single by Australian rock group Paul Kelly and the Dots which was released on 20 October 1980, ahead of the related album, "Talk" (March 1981).  It was written by band members Paul Kelly and Chris Langman.  It peaked at No. 38 on the Australian Kent Music Report Singles Chart.  The song was produced by Joe Camilleri (from Jo Jo Zep & The Falcons) for Mushroom Records.  In early November the group performed the track on national pop music TV show, "Countdown" – it was Kelly's first TV appearance.  The song's subject, Billy Baxter, is an Australian musician and was a long term member of "Coodabeens Footy Show" on ABC Radio National.

Question: What was the middle name of the man whose first TV show was "Hey, Landlord"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_full_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "person_middle_name": {
      "type": "string",
      "description": "The middle name of the person."
    },
    "first_tv_show_name": {
      "type": "string",
      "description": "The name of the person's first TV show."
    },
    "person_roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Roles of the person in the entertainment industry."
    }
  },
  "required": [
    "person_full_name",
    "person_middle_name",
    "first_tv_show_name",
    "person_roles"
  ],
  "additionalProperties": false
}
