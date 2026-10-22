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
La Cage aux Folles (musical): La Cage aux Folles (] ) is a musical with a book by Harvey Fierstein and lyrics and music by Jerry Herman.  Based on the 1973 French play of the same name by Jean Poiret, it focuses on a gay couple: Georges, the manager of a Saint-Tropez nightclub featuring drag entertainment, and Albin, his romantic partner and star attraction, and the farcical adventures that ensue when Georges's son, Jean-Michel, brings home his fiancée's ultra-conservative parents to meet them.  "La cage aux folles" literally means "the cage of mad women".  However, "folles" is also a slang term for effeminate homosexuals (queens).

Marina Kamen: Marina Kamen (aka MARINA), is a Director/Producer/Casting Director/Vocalist/Choreographer & Musician best known for her music in the advertising industry & fitness/health/dance music communities and has a large online catalogue of workout music, treadmill workouts and audio workouts including 50 albums, 450 Original Songs and 1,200 Online Musical Audio Programs.  Marina's EBook entitled "I'mSteppin' Out!" …confessions of a Food-a-Holic has sold around the globe for the past 15 years and is available on Iamplifi, Audible and on Amazon.  Kamen won the 2005 People's Choice Award in Podcasting .  MARINA's High-nrg Fitness Brand includes Radio and Television Broadcasts, Music, albums, and a Live Show currently playing in NYC called MARINA's High-nrg Fitness LIVE! …an Interactive Musical Theatre WORKOUT Experience.  MARINA's lifelong work merging the worlds of vocalisation and dance has brought her to work with Celebrity artists including Patti Labelle, Carnie Wilson, James Earl Jones, Mandy Patinkin, Gloria Gaynor, Britney Spears, Liza Minnelli and countless others.  In 1987, Kamen and her husband, Roy Kamen, opened Kamen Entertainment Group, Inc.  Kamen's credits in Radio and television advertising have included thousands of campaigns working for Starburst, PopTarts, Mercedes, Exxon Mobile, CocaCola, Dairy Queen, and Febreeze in the 1990s, in 2004, Marina Diretcted, Produced, Cast & Choreographed Britney Spears' Twister Dance Rave Global Television Campaign for Hasbro.  Kamen also Cast, Directed,Choreographed & Produced Television spots for Jenga Tetris & Bop It.  Kamen performs a series of live performance concerts around the country.  In the late 90s, it seemed impossible because she had three young children and was over 215 pounds.  Nonetheless, Kamen started to write and produce music aimed at the dance market.  High energy shows won awards, such as her "Silent Night" performance at Webster Hall in New York City.  Kamen taught aerobics classes in the 70's and 80's, and through her performances she began using dance music to drive her workout routines.  By singing, dancing, and eating well-portioned meals, she lost over 100 pounds.  Kamen released her debut album, "Um-Lotty-Da" in 1997.  Kamen quickly earned a reputation in the New York City club scene.  Her albums and performances garnered the attention of the Dance Organization of America.  This committee steered Kamen towards positions as a director and choreographer for Atlantic Records, Columbia Records, The Naras Foundation which Hosts The Grammy Awards.By the year 2000, Kamen had combined her previous experiences and started to sell her fitness music within the fitness community.  With her innovative approach and inspirational message, Kamen became a well-known persona in the world of Musical Fitness.  Kamen has produced material and live presentations for clients including QVC/Direct, Dynamix, Equinox Gyms, Jazzercise, Strive Enterprise with Bill Kazmier (ESPN), and Jackie Chan's CableFlex.  She has appeared on British TV on "Reborn in the USA," produced and televised from New York City by the producers of "American Idol."  Kamen has been covered in the NY Times, Daily News and Family Circle Magazine.  She can be seen on programing from The Discovery Health Network, PBS and Nickelodeon (The N), ShopNBC, The Tyra Banks Show & ABC NEWS.  Marina is also Hosting a Web Broadcast show entitled "MARINA's High-nrg Fitness Musical Health Talk" at http://www.musicalhealthtalk.com.  Ms. Kamen attended The Manhattan School of Music & Interlochen Arts Academy majoring in voice, violin, and composition.  Marina trained in dance with The American Ballet Theatre, Luigi & Frank Hatchett.  Marina also thanks her longtime friend in dance Francis Roach for his openness and dance talent over the years in addition to carrying out the teachings of dance Icon Luigi.  His work has helped to train thousands of dancers around the world.

I Will Survive (Billie Jo Spears album): I Will Survive is the 14th album by Billie Jo Spears an American country artist (born Billie Jean Spears in Beaumont, Texas, United States, January 14, 1937 – December 14, 2011) released in May 1979 on the United Artists label.  The title track, "I Will Survive", was a cover of the chart topper for Gloria Gaynor in 1978.  Although the album didn't quite make the top 40 three singles released from it did.  These were:-

Experience Gloria Gaynor: Experience Gloria Gaynor is the second album by Gloria Gaynor, released in 1975 on MGM Records.  The album charted in the US Billboard at #64 in the US Pop chart, and at #32 in the US R&B chart.  The album failed to chart in the UK, the single "How High The Moon" was issued in the UK and peaked at #33.

The Power of Gloria Gaynor: The Power of Gloria Gaynor, also known as "The Power", or "The Power of Love", is the twelfth studio album by Gloria Gaynor, released in 1986, which is composed mostly of cover versions of other popular songs from the 1970s and 1980s, and is her only album to be released on Stylus Records.  It was originally only released in the UK.  The album was issued on record, compact disc and cassette, each containing bonus tracks of re-recorded versions of a few of Gaynor's biggest hits in a medley and a remixed version of "Don't You Dare Call It Love".

I Will Survive (TV series): I Will Survive is an Australian talent show-themed television series that premiered on Network Ten on 21 August 2012.  The premise of the show is to search for a new, unknown talent to perform in the Broadway production of the musical "Priscilla, Queen of the Desert".  Due to the Broadway theatre production closing in June 2012, the prize has been amended to another performance on Broadway, along with a $250,000 cash prize.  The title of the show is derived from the title of a song in the production, "I Will Survive", originally sung by Gloria Gaynor.  "I Will Survive" is hosted by actor and singer Hugh Sheridan and features judges Jason Donovan, who played Tick in the West End theatre production of the show, and Stephan Elliott, the director of the film "The Adventures of Priscilla, Queen of the Desert".

Gloria Gaynor (album): Gloria Gaynor is the tenth studio album by Gloria Gaynor and her only to be released on Atlantic Records after her contract with Polydor Records expired.  The lead single release was a cover of The Supremes' "Stop in the Name of Love", followed by the singles "America" and "Tease Me".  The album failed to garner much attention in either the U.S. or in Europe.

Gloria Gaynor's Park Avenue Sound: Gloria Gaynor's Park Avenue Sound is the fifth album by Gloria Gaynor.  It was released in 1978 on Polydor Records.

I Am Gloria Gaynor: I Am Gloria Gaynor is the eleventh studio album by Gloria Gaynor, released in 1984 by Chrysalis Records.  The most notable song on the album was Gloria Gaynor's cover of "I Am What I Am" from the musical "La Cage Aux Folles".  It reached #82 on the Billboard Hot R&B/Hip-Hop Songs charts.

¡Celia Cruz: Azúcar!: ¡Celia Cruz: Azúcar!  (English: Celia Cruz: Sugar! )  was a tribute special held in honor of Cuban performer Celia Cruz.  It was hosted by American singer Marc Anthony and Cuban-American singer Gloria Estefan.  It featured musical performances by various Latin music and Anglo performers including Victor Manuelle, Paulina Rubio, José Feliciano, Milly Quezada, Los Tri-O, Estefan, Patti Labelle, Arturo Sandoval, Ana Gabriel, Gilberto Santa Rosa, Tito Nieves, Albita, Johnny Pacheco, Alicia Villareal, Olga Tañón, Mikey Perfecto, José Alberto "El Canario", Rosario, Luis Enrique, Anthony and Gloria Gaynor.  This was Cruz's final public appearance, before her death in July 2003.  The tribute concert raised $145,000 for the Celia Cruz Foundation.

Question: Gloria Gaynor's cover of "I Am What I Am" is from a musical that it's title translates to what in English ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musical_title_original": {
      "type": "string",
      "description": "The original title of the musical."
    },
    "song_covered": {
      "type": "string",
      "description": "The title of the song covered by Gloria Gaynor."
    },
    "musical_title_english_translation": {
      "type": "string",
      "description": "The literal English translation of the musical's title."
    }
  },
  "required": [
    "musical_title_original",
    "song_covered",
    "musical_title_english_translation"
  ],
  "additionalProperties": false
}
