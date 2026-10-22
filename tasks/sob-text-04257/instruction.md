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
Christopher Martin (trumpeter): Christopher Martin is an American trumpet player who was named the principal trumpet of the New York Philharmonic in May 2016 and began his tenure there in September 2016. He has also served as Principal trumpet of the Chicago Symphony Orchestra (2005-2016) and the Atlanta Symphony Orchestra, and as Associate Principal of the Philadelphia Orchestra.  During his time in Chicago, Martin gave the world premieres of several trumpet concerti, notably Christopher Rouse's Heimdall's Trumpet in 2012.

David S. Sampson: David Sampson (born January 26, 1951, Charlottesville, Virginia) is a composer and professional trumpet player.  He was Composer-in-Residence with the Colonial Symphony Orchestra from 1998 through 2007.  He is a recipient a 2014 New Jersey State Council on the Arts Individual Artist Fellowship.  His major works include The War Prayer for soloists, chorus and orchestra commissioned by the National Endowment for the Arts and premiered by Princeton Pro Musica; Hommage JFK commissioned by the National Symphony Orchestra; Monument commissioned by the Barlow Foundation for the Akron and Memphis symphony orchestras; Turns for Cello and Orchestra commissioned by the Bergen Foundation and cellist Paul Tobias and premiered with the New Jersey Symphony Orchestra; Triptych for trumpet and orchestra commissioned by the International Trumpet Guild and premiered by Raymond Mase at the Aspen Music Festival and with the American Composers Orchestra at Carnegie Hall; Dectet commissioned by the Chicago Chamber Musicians; Elements commissioned by the Elements Quartet; Strata commissioned by the NEA and the American Brass Quintet; Jersey Rain commissioned by the NEA and the Geraldine R. Dodge Foundation and premiered by Harmonium and Masterworks Choruses and the Colonial Symphony.

Manfred Moch: Manfred Moch was a German trumpet player.  He made a name for himself in the 1960s as the featured solo trumpet player for the Bert Kaempfert orchestra, contributing memorable and melodic solos to many of Kaempfert’s hits; such songs included “Bye Bye Blues”, “Strangers In The Night”, “L-O-V-E” and “Sweet Maria”.  His association with Kaempfert ended in 1968 over a pay dispute, but by the late 1970s he was again playing sessions and concerts with Kaempfert, although not as a soloist.  Moch was also a long-time member of the James Last Orchestra during the 1960s and 1970s, and continued to play for Last as a session musician after leaving the touring band.  In addition, Moch was a member of the NDR (Nordeutscher Rundfunk, or North German Radio) Big Band from the 1960s until the 1990s.  He was also active as a session player in Hamburg, playing for many other popular German recording artists.  During the late 1960s, Moch recorded some trumpet duet albums with fellow Last/Kaempfert bandmate Heinz Habermann, which were released on the Decca label under the name The Tattoos.

Paul Neebe: Paul Neebe is an American classical trumpeter who performs widely as a soloist, orchestral musician, and chamber player.  He currently serves as principal trumpet of the Roanoke Symphony Orchestra, Wintergreen Festival Orchestra, and formerly of the Charlottesville University Symphony Orchestra in Virginia.  He released "Te Deum" in 2003, a CD released on the German label MDG that features solo trumpet and organ, and "American Trumpet Concertos" in 2006, a CD released on Albany Records that consists entirely of worldwide premieres with the Slovak Radio Symphony Orchestra.  His chamber work can be heard on "Walter Ross: Brass Trios", a CD released on DCD Records.  Neebe garnered semi-finalist honors at the First International Trumpet Festival Competition in Moscow.  He has performed several times for the Goethe Institute Cultural Program in Rothenburg, Germany, and regularly gives solo recitals across the United States and Germany.  Neebe has served as Trumpet Mentor at the National Music Festival since its inception.

A Trumpeter's Lullaby: A Trumpeter's Lullaby is a short composition for solo trumpet and orchestra, written by American composer Leroy Anderson in 1949.  The two and a half minute piece was premiered on May 9, 1950, by the Boston Pops Orchestra with Arthur Fiedler conducting and French-born American Roger Voisin as trumpet soloist.  It was composed at the request of Voisin, who was principal trumpeter of the Boston Pops Orchestra at the time.  It was first recorded on June 18, 1950, with Fiedler conducting Roger Voisin and the Boston Pops.  Three months later it was recorded with Anderson himself conducting and James F. Burke as trumpet soloist.  The first stereo recording was made in October 1956 with Frederick Fennell conducting the Eastman-Rochester Pops Orchestra, recorded in one take without rehearsal.  The (uncredited) soloist was Sidney Mear.

Bert Kaempfert: Berthold Heinrich Kämpfert, (16 October 1923 – 21 June 1980), better known as Bert Kaempfert, was a German orchestra leader, music producer, and songwriter.  He made easy listening and jazz-oriented records and wrote the music for a number of well-known songs, including "Strangers in the Night" and "Moon Over Naples".

Merri Franquin: Merri Jean Baptiste Franquin (b. 19 October 1848, Lançon, Bouches-du-Rhône, France, d. 1934) was a French trumpeter, cornetist, and flugelhornist who was professor of trumpet at the Paris Conservatory from 1894 until 1925.  Franquin was a teacher of both Georges Mager (1885–1950) who was principal trumpet of the Boston Symphony Orchestra from 1919 until 1950, and Eugene Foveau (1886–1957) who became professor of cornet at the Paris Conservatory in 1925.  His collaboration with Romanian composer Georges Enescu (1881–1955) led to the composition in 1906 of "Légende", one of the great twentieth-century works for solo trumpet and piano.  Franquin's book, "Methode Complète de la Trompette Moderne de Cornet a Pistons et de Bugle", has been an influential teaching aid for many trumpet players, notably Maurice André.  Franquin's most notable accomplishment while at the Paris Conservatory was his push for the C Trumpet to replace the low F trumpet as a more versatile orchestral instrument.  A more modern form of this instrument was introduced to American symphony orchestras by Georges Mager, and it remains very much in popular use in the United States.

Ray Cummins (guitarist): Ray started playing music at the early age of 5.  This took place in Northern Kentucky.  His first instrument was a 12 bass accordion.  By the time he was in the fourth grade, he had studied piano and accordion and had graduated to a 120 bass accordion.  By the fifth grade he started playing the trumpet.  By the sixth grade he was playing first chair trumpet in the elementary band.  In the seventh grade he was the only seventh grader playing in the high school band.  By this time he realized he wanted to become a trumpet player like Al Hirt.  He learned to play many of Al Hirt's songs by ear and one of his favorites was "Walkin".  Ray noticed that this song was produced by Chet Atkins and written by Jerry Reed but he was not familiar with them at that time.  By the tenth grade he was just starting to study trumpet at the Cincinnati Conservatory of Music from the first chair trumpet player of the Cincinnati Symphony.

Lennart Axelsson (musician): Lennart Axelsson (born July 11, 1941) is a Swedish trumpet player who has spent a good part of his career in Germany.  Born and raised in Sweden, he began his career in a Swedish armed forces band.  Disillusioned with military life, he quit to become a full-time musician, playing with various jazz bands in Sweden.  In the early 1970s, he moved to Zürich, Switzerland to take a job in the big band of Swiss radio station Schweizer Radio DRS.  In 1974, he joined the James Last Orchestra.  He was one of the featured trumpet soloists on Last's 1975 album "In The Mood For Trumpets", along with Rick Kiefer and Ack van Rooyen; this was notable as Last's record company Polydor usually did not credit the individual personnel on Last's studio recordings.  In 1979, Axelsson left the Last band and joined the NDR (Norddeutscher Rundfunk, or North German Radio) big band, where he eventually became the featured trumpet soloist.  He retired from the NDR band in 2005.

Henry Glover: Henry Bernard Glover (May 21, 1921 – April 7, 1991) was an American songwriter, arranger, record producer and trumpet player.  In the music industry of the time, Glover was one of the most successful and influential black executives.  He gained eminence in the late 1940s, primarily working for the independent (and white-owned) King label.  His duties included operating as a producer, arranger, songwriter (occasionally utilising the alias of Henry Bernard), engineer, trumpet player, talent scout, A&R man, studio constructor, while later in his career he became an owner of his own label.  Glover worked with country, blues, R&B, pop, rock, and jazz musicians, and he helped King Records to become one of the largest independent labels of its time.

Question: Manfred Moch was a German trumpet player, he made a name for himself in the 1960s as the featured solo trumpet player for an orchestra of which German orchestra leader, music producer, and songwriter?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "trumpet_player_name": {
      "type": "string",
      "description": "The name of the trumpet player."
    },
    "orchestra_leader": {
      "type": "object",
      "properties": {
        "common_name": {
          "type": "string",
          "description": "The common name of the orchestra leader."
        },
        "full_name": {
          "type": "string",
          "description": "The full name of the orchestra leader."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the orchestra leader."
        },
        "profession": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Professions of the orchestra leader."
        }
      },
      "required": [
        "common_name",
        "full_name",
        "nationality",
        "profession"
      ],
      "additionalProperties": false
    },
    "role_in_orchestra": {
      "type": "string",
      "description": "The role of the trumpet player in the orchestra."
    },
    "time_period": {
      "type": "string",
      "description": "The time period when the trumpet player was notable in this role."
    }
  },
  "required": [
    "trumpet_player_name",
    "orchestra_leader",
    "role_in_orchestra",
    "time_period"
  ],
  "additionalProperties": false
}
