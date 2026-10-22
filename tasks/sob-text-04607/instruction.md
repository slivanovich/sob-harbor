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
Martan Mann: Martan Mann is an American jazz pianist and educator living in Boulder Creek, California.  He performs with the Martan Mann Trio, the Martan Mann & Mannkind (contemporary jazz band) and has performed with George Young and Dmitri Matheny.  A graduate of San Jose State University, San Francisco State University, Hawaii Pacific College, and the University of Hawaii, he is a musical director at Capitola Theater in Capitola, California and is on the board of directors for the Jazz Society of Santa Cruz, California.  Jazz educational books include "Jazz Improvisation for the Classical Pianist" (1989), "New Age Improvisation for the Classical Pianist" (1994), and "Improvising blues piano" (1997).  He is also the author of an jazz educational DVD, "Jazz Skills for Piano".

Scotty Barnhart: William "Scotty" Barnhart (born October 27, 1964) is an American jazz trumpeter.  A two-time Grammy winner, he has played since 1993 as a featured soloist with Count Basie Orchestra.  In September 2013, Barnhart was announced as the new director of the Basie Orchestra.  He has multiple recordings with pianist Marcus Roberts, as well as recordings with Tony Bennett, Diana Krall, Ray Charles, and Tito Puente.  A solo CD, released with Unity Music, is titled "Say It Plain" and features Clark Terry, Ellis and Wynton Marsalis, Marcus Roberts, Jamie Davis and Etienne Charles; it achieved number 3 in the Jazz Charts.  Also active as an educator and clinician, he is author of "The World of Jazz Trumpet - A Comprehensive History and Practical Philosophy" (published by Hal Leonard).  He is a professor in the College of Music at Florida State University.

Count Basie: William James "Count" Basie (August 21, 1904 – April 26, 1984) was an American jazz pianist, organist, bandleader, and composer.  His mother taught him to play the piano and he started performing in his teens.  Dropping out of school, he learned to operate lights for vaudeville and to improvise accompaniment for silent films at a local movie theater in his home town of Red Bank, New Jersey.  By age 16, he increasingly played jazz piano at parties, resorts and other venues.  In 1924, he went to Harlem, where his performing career expanded; he toured with groups to the major jazz cities of Chicago, St. Louis and Kansas City.  In 1929 he joined Bennie Moten's band in Kansas City, and played with them until Moten's death in 1935.

Dick Hyman: Richard "Dick" Hyman (born March 8, 1927) is an American jazz pianist and composer.  Over a 60-year career, he has functioned as a pianist, organist, arranger, music director, electronic musician, and, increasingly, as a composer.  He will be a National Endowment for the Arts Jazz Masters fellow in 2017.

Dara Tucker: Dara Tucker is an American jazz singer and composer.  Tucker has released four studio albums; "All Right Now" (2009), "Soul Said Yes" (2011) "The Sun Season" (2014) and "Oklahoma Rain" (2017), as well as a limited-release, live performance album, "Dara Tucker Live" in 2013.  Dara was named, "Jazz Vocalist of the Year" at the 2016 and 2017 Nashville Industry Music Awards.  .  In 2017, the second single from "Oklahoma Rain, "Radio," was named, "Song of the Year" at Nashville Industry Music Awards, and "Oklahoma Rain" won "Jazz Album of the Year."  Tucker has performed internationally with her jazz ensemble since 2009.  Dara was featured on the Tavis Smiley Show in 2015, and opened for Gregory Porter in 2016.  She won the silver medal in the "American Traditions Vocal Competition" in 2017.  She has shared the stage with jazz musicians such as organist Dr. Lonnie Smith, 7-string guitarist Charlie Hunter, and pianist Johnny O'Neal at The Blue Note in New York City, The San Jose Jazz Festival, Smoke Jazz and Supper Club in NYC, Sculler's in Boston, MA, The Oklahoma Jazz Hall of Fame, and Snug Harbor in New Orleans, LA.  In November 2016, she shared the stage with Vince Gill and the Time Jumpers .  She has recorded with guitarist Peter Bernstein, guitarist Charlie Hunter, pianist Helen Sung, trombonist Alan Ferber, saxophonist John Ellis and drummer Donald Edwards.

Alice Coltrane: Alice Coltrane ("née" McLeod, August 27, 1937 – January 12, 2007), also known by her adopted Sanskrit name Turiyasangitananda or Turiya Alice Coltrane, was an American jazz pianist, organist, harpist, singer, composer, swamini, and the second wife of jazz saxophonist and composer John Coltrane.  One of the few harpists in the history of jazz, she recorded many albums as a bandleader, beginning in the late 1960s and early 1970s for Impulse!  Records and Universal Distribution.

Mike Williams (trumpeter): Mike Williams is an American jazz and big band trumpeter residing in Lapeer, Michigan.  He is most noted as the lead trumpeter for the Count Basie Orchestra, an esteemed chair which he has held without interruption for more than 21 years.  Mike can be heard on numerous Count Basie Orchestra recordings (some of them Grammy Award winners), including the recent ""Basie Is Back"" (recorded live in Japan) and the Grammy nominated ""Ray Sings, Basie Swings,"" on which he was a featured soloist.  As a member of the Basie Band, he has performed in all 50 states and 40 countries with such notable names as Dizzy Gillespie, Billy Eckstine, Frank Sinatra, Ella Fitzgerald, Sarah Vaughan, George Benson, Tony Bennett and Diane Schuur.

Back with Basie: Back with Basie (subtitled More Hit Performances of the '60s) is an album released by pianist, composer and bandleader Count Basie featuring tracks recorded in 1962 (with one from 1960) and originally released on the Roulette label.

Black Jazz Records: Black Jazz Records was a jazz record company and label founded in Oakland, California by pianist Gene Russell (December 2, 1932 - May 3, 1981) and percussionist Dick Schory.  The label was created to promote the talents of young African American jazz musicians and singers, and released twenty albums between 1971 and 1975.  Some of the more notable artists to record for Black Jazz Records were Cleveland Eaton, former bassist for Count Basie and Ramsey Lewis, and pianist Doug Carn, whose four albums were the most successful of any Black Jazz artist.  Carn's wife at the time, Jean Carn, sang on his albums; she changed her name to Jean Carne and went on to have a successful solo career as an R & B singer.  Singer Kellee Patterson gained notoriety as the first black Miss Indiana in 1971, before recording her debut album, "Maiden Voyage", with Black Jazz Records in 1973.  The label was distributed and financed by Ovation Records, a country and western label based in Chicago, which was also founded by Schory.  Black Jazz Records was considered at the time to be the first jazz label started by an African American since brothers John and Reb Spikes started Sunshine Records in 1921.

Donald &quot;Tee&quot; Carson: Donald Tecumseh "Tee" Carson (born in Washington, D.C.) was an American jazz pianist who played in Count Basie's big band after Basie died in 1984.

Question: When was the American jazz pianist and organist died who's album is Back with Basie?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musician_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the jazz musician."
        },
        "primary_roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Key musical roles of the musician."
        },
        "birth_date": {
          "type": "string",
          "description": "The birth date of the musician."
        },
        "death_date": {
          "type": "string",
          "description": "The death date of the musician."
        }
      },
      "required": [
        "name",
        "primary_roles",
        "birth_date",
        "death_date"
      ],
      "additionalProperties": false
    },
    "album_details": {
      "type": "object",
      "properties": {
        "album_title": {
          "type": "string",
          "description": "The title of the album associated with the musician."
        },
        "release_year_context": {
          "type": "integer",
          "description": "The year mentioned in the context regarding the album's recording or release."
        },
        "original_label": {
          "type": "string",
          "description": "The original record label for the album."
        }
      },
      "required": [
        "album_title",
        "release_year_context",
        "original_label"
      ],
      "additionalProperties": false
    },
    "question_answer": {
      "type": "string",
      "description": "The specific date answering the question about the musician's death."
    }
  },
  "required": [
    "musician_details",
    "album_details",
    "question_answer"
  ],
  "additionalProperties": false
}
