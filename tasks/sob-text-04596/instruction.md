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
Mental Overdrive: Mental Overdrive is the primary solo moniker of Per Martinsen (born 31 July 1966), one of Norway's most prolific and influential techno musicians.  His tracks have ranged from hardcore rave techno to vibrant space-disco, and he's always maintained a healthy balance of humor and braininess.  Active since 1990, he began his career releasing several 12" EPs of aggressive, rave-ready hardcore techno on revered Belgian label R&S, including 12000 AD (1990), The Second Coming (1991), Move!  (as Confusion Club, 1991), and The Love EP (1992).  In 1994, Martinsen began releasing atmospheric techno singles as part of Illumination, his duo with Nicholas Sillitoe.  The next year, Mental Overdrive released the single "Disto Disco," which featured a B-side ("Faith") co-written by R&S artist Outlander, best known for the 1991 classic "Vamp."  The A-side appeared on Mental Overdrive's full-length debut Plugged, released on Martinsen's own Love OD Communications.  The album showed a notable progression in his music, maintaining its rough, distorted hardcore techno sound while adding more cerebral elements, placing it closer to Warp's Artificial Intelligence series.  Martinsen displayed his sense of humor with 1996's Unplugged, a limited conceptual release containing silent "versions" of the tracks on Plugged.  083 In 1997, Mental Overdrive signed to Virgin and released About Jazz, a significantly more house/disco-influenced EP than his previous work.  This was followed by full-length Ad Absurdum, which continued in a more light-hearted and funky direction than his previous releases.  He took a few years off from releasing Mental Overdrive recordings, instead devoting time to Frost (his more pop-focused electronic duo with his wife Aggie Peterson) and Illumination, which released two albums on RCA.  Following the 2003 release of Mental Overdrive's Me EP on Love OD, he signed to Norwegian label Smalltown Supersound and released full-length 083, which featured the single "Diskodans."  In 2005, the label compiled his early R&S material on CD as The Phuture That Never Happened.  Two years later, Mental Overdrive's single "Spooks" appeared on Prins Thomas' Full Pupp label.  The song appeared on his next Smalltown full-length, You Are Being Manipulated, which was released in 2008.  The album was perfectly at home with the label's other left-field dance artists like Bjørn Torske and Kim Hiorthøy, while maintaining the unique Mental Overdrive sound.  Martinsen continued releasing Mental Overdrive singles on Full Pupp and Love OD, and contributed to Rune Lindbæk's Meanderthals project.  In 2012, he released Man with a Movie Camera, an EP featuring music he'd composed for a 1996 screening of the Russian silent film of the same name, which also featured pieces by Biosphere which would later appear on the 2001 remaster of his classic album Substrata.  Mental Overdrive returned to his Love OD label for 2013 full-length Cycls, as well as 2014's Everything Is Connected, which compiled a few previously released EPs.  In 2016, Full Pupp sublabel Rett I Fletta released a new version of Plugged consisting of alternate takes sourced from the original DAT tapes.  (Paul Simpson for allmusic.com)

Erin McDougald: Erin McDougald is a Chicago-based jazz vocalist, bandleader, composer-lyricist and producer.  McDougald is known for her innovative arrangements of jazz standards and phrasing which many critics compare to Chicago-born jazz song stylist, the late Anita O'Day.  Her company, Flapper Girl Productions, has served as th record label for two of McDougald's albums ("Blue Prelude", 2000, and "Meeting Place", 2006).  She has produced four critically acclaimed recordings as leader since 2000, and is the creator the FGP JazzSeries in Chicago, which brings a live audience into a recording studio environment so they may be part of the recording process and part of the actual recording through audience reactions and applause.  This idea was developed from James Wagner's original "Strobe Sessions" in Wicker Park.  She has performed with jazz luminaries Dave Liebman, Nicholas Payton, Ira Sullivan, Rodney Green, Howard Levy, Orlando Sanchez-Soto, Roy Hargrove, Von Freeman, Carlos Henriquez, Harold Mabern and others.

Derrick May (musician): Derrick May (born April 6, 1963), also known as Mayday and Rhythm Is Rhythm, is an electronic musician from Belleville, Michigan, United States.  May is credited with pioneering techno music in the 1980s along with collaborators Juan Atkins and Kevin Saunderson, commonly known as the Belleville Three.

Ko Nak-choon: Ko Nak-choon (born 10 April 1963) is a South Korean fencer.  He competed in the individual and team foil events at the 1988 Summer Olympics.

Osama Al-Khurafi: Osama Al-Khurafi (born 24 April 1963) is a Kuwaiti fencer.  He competed in the individual and team épée events at the 1980 and 1984 Summer Olympics.

Leviathan (2014 film): Leviathan (Russian: Левиафан , "Leviafan") is a 2014 Russian drama film directed by Andrey Zvyagintsev, co-written by Zvyagintsev and Oleg Negin, and starring Aleksei Serebryakov, Elena Lyadova, and Vladimir Vdovichenkov.  According to Zvyagintsev, the story of Marvin Heemeyer in the United States inspired him and it was adapted into a Russian setting, but critics compare the story to the more similar biblical story of Naboth's Vineyard, where a King vies for his subjects' land and is motivated by his Queen to obtain it in a sly manner.  The character development of the protagonist parallels another biblical figure, Job.  The producer Alexander Rodnyansky has said: "It deals with some of the most important social issues of contemporary Russia while never becoming an artist's sermon or a public statement; it is a story of love and tragedy experienced by ordinary people".  Critics noted the film as being formidable, dealing with quirks of fate, power and money.

The Advent: The pair began recording together in 1990; their first activity was an engineering job for Fade to Black (aka Jay Denham), but later they debuted on vinyl with their first single, recorded for inclusion on a sampler by Network Records.  The official debut of The Advent came in 1994, just after Ferreira signed to Internal Records (also the home of Orbital).  He convinced McBean to join him in the recording of a series of crucially limited singles, then the debut album "Elements of Life" in late 1995.  Critics championed the duo's energetic update of original techno renegades like Derrick May and Kevin Saunderson, and The Advent followed with the remix album "Shaded Elementz" one year later.  Their second full album "New Beginning" was released 28 April 1997, though Internal Records dropped the duo soon after its release.  After transferring to the Metalbox division of Northwest/BMG, The Advent returned later that year with another remix album titled "Kombination Phunk", which alternated remixes with several original productions.

Mano Solo: Mano Solo (24 April 1963 – 10 January 2010), born Emmanuel Cabut, was a French singer.  He was born in Châlons-sur-Marne on 24 April 1963 to the illustrator Cabu and Isabelle Monin, co-founder of the ecology-related magazine, "La Gueule ouverte".

Shōgo Suzuki: Shōgo Suzuki (鈴木 省吾 , Suzuki Shōgo , born 12 April 1963) is a Japanese actor and narrator.  He began his career narrating television commercials and instructional videos for corporations.  He debuted as a voice actor in Square-Enix's "Final Fantasy VII Advent Children".

Anne Minter: Anne Minter (born 3 April 1963) is a former tennis player from Australia, who competed for her native country at the 1988 Summer Olympics in Seoul.  She was an Australian Institute of Sport scholarship holder.  She won four singles titles on the WTA Tour: 1987 Taipei, Singapore; 1988 Puerto Rico; 1989 Taipei.  Minter was a quarterfinalist at the Australian Open in 1988, beating fourth seed Pam Shriver in the R16 when the tournament moved to the hard court surface at Melbourne Park.  She twice reached the R16 at Wimbledon, upsetting ninth seed Hana Mandlíková in the third round in 1988.  She reached her highest individual ranking in her professional career on 4 July 1988, when she became the 23rd top player in the world.  On 19 March 1990 she reached her highest doubles ranking or 68.  Her playing career spanned 11 years from 1981 until 1992.  Minter's win-loss record for singles stands at 258–245.

Question: In addition to the individual born in April 1963, what other artist did critics compare The Advent's energetic update of original techno to?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "the_advent_music_description": {
      "type": "string",
      "description": "Description of The Advent's music that was subject to comparison."
    },
    "compared_artists": {
      "type": "array",
      "description": "List of artists The Advent's music was compared to.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the artist."
          },
          "birth_date": {
            "type": "string",
            "description": "Birth date of the artist, if available."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    },
    "other_compared_artist_name": {
      "type": "string",
      "description": "The name of the other artist mentioned in the comparison, besides the one born in April 1963."
    }
  },
  "required": [
    "the_advent_music_description",
    "compared_artists",
    "other_compared_artist_name"
  ],
  "additionalProperties": false
}
