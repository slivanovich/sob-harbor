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
Just Got Paid, Let's Get Laid: Just Got Paid, Let's Get Laid is an EP by the electropop group Millionaires released in 2009 by Decaydance (it was later released independently by the group).  This is the group's second EP and contains three songs from their first EP, released a year prior.  The girls promoted the EP on the Warped Tour 2009 where they sold a limited number of CD copies.  Two music videos were made, one for the single "Just Got Paid, Let's Get Laid" and another for the song "Alcohol".

East Is East (1999 film): East Is East is a 1999 British comedy-drama film written by Ayub Khan-Din and directed by Damien O'Donnell.  It is set in Salford, Lancashire, in 1971, in a mixed-ethnicity British household headed by Pakistani father George (Om Puri) and an English mother, Ella (Linda Bassett).

Frances Barber: Frances Barber (born Frances J Brookes, 13 May 1957) is an English actress.  She received Olivier Award nominations for her work in the plays, "Camille" (1985), and "Uncle Vanya" (1997).  Her numerous television credits include "The Street" (2009), "Doctor Who" (2011), and "Silk" (2012–14), while her film appearances include "Prick Up Your Ears" (1987), "Sammy and Rosie Get Laid" (1987), "Soft Top Hard Shoulder" (1992), and the upcoming, "Film Stars Don't Die in Liverpool" (2017).

Manuel Garcia-Rulfo: Manuel García-Rulfo (born February 25, 1981) is a Mexican actor.  He is best known for roles in films such as "Bless Me, Ultima" and "Cake", as well as the television program "".  He headlined as one of the titular characters in the 2016 remake "The Magnificent Seven".

Beauty and the Beast (2017 film): Beauty and the Beast is a 2017 American musical romantic fantasy film directed by Bill Condon from a screenplay written by Stephen Chbosky and Evan Spiliotopoulos, and co-produced by Walt Disney Pictures and Mandeville Films.  The film is based on Disney's 1991 animated film of the same name, itself an adaptation of Jeanne-Marie Leprince de Beaumont's eighteenth-century fairy tale.  The film features an ensemble cast that includes Emma Watson and Dan Stevens as the titular characters with Luke Evans, Kevin Kline, Josh Gad, Ewan McGregor, Stanley Tucci, Audra McDonald, Gugu Mbatha-Raw, Ian McKellen, and Emma Thompson in supporting roles.

La luz de mis ojos: La luz de mis ojos is a Colombian musical comedy-drama telenovela directed by Jorge Alí Triana for RCN Televisión.  The series is written by Gerardo Pinzón and Claudia Rojas.  It stars Laura de León and Édgar Vittorino as the titular characters.

Sammy and Rosie Get Laid: Sammy and Rosie Get Laid is a 1987 film directed by Stephen Frears, with a screenplay by Hanif Kureishi.

Damien Starkey: Damien Joel Starkey (born October 20, 1982) is an American producer, songwriter, composer, and multi-instrumentalist.  He has played many roles in several bands, served as a vocalist for Society Red and Burn Season, bassist for Puddle of Mudd, and he also owns a company called Give 2 Get Music Group in which he is a music supervisor and composer for TV and film music.  Damien has scored and wrote music for several TV shows and movies including American Reunion, Nitro Circus Movie, Freeheld, Pawn Stars, Bar Rescue, and Undercover Boss.  As a producer he has written for and produced many notable artists including platinum selling bands Saliva, Daughtry and Avril Lavigne.  Damien also is a managing partner in the music technology company Songlinkr.

Ayub Khan-Din: Ayub Khan Din (born 1961) is a British Pakistani actor perhaps best known for his role of Sammy in Hanif Kureishi's film "Sammy and Rosie Get Laid" in (1987) and as the writer of the BAFTA, BIFA and London Film Critics Circle award-winning film "East Is East", based on the original 1996 play that was nominated for an Olivier Award in 1998.  In 2008 his new comedy play "Rafta, Rafta..." won the Olivier Award that year.  He also wrote the film sequel "West Is West" released in 2010.

Millionaires discography: The discography of the Millionaires consists of one studio album, three extended plays, one mixtape and five singles.  The group released their debut EP, "Bling Bling Bling! ", in July 2008, followed by their second EP "Just Got Paid, Let's Get Laid" in June 2009.  Their third extended play, "Cash Only", was preceded by the single "Stay the Night", released with B-Unique Records, which charted at #12 on the UK Top World Dance Charts.  After the departure of member Dani Gore, the now-duo released a free mixtape, "Your Girl Does Party" in May 2012, followed by their debut studio album "Tonight" in March 2013.  Various songs remain unreleased with no confirmed release date, such as "Hush Little Boyfriend", "That's How We Party", "Rich Girls", "Not Everyone's A Millionaire", "Hairspray", "Candy Paint", "Beatbox", a song featured on Ashley Purdy's Instagram.  As well as two unreleased features one on a song rumored to be "Fuck Me I'm Famous" dubbed "Team Fierce" alongside Jeffree Star and Blood on the Dance Floor and Young Scrap's song "Phantom".

Question: Directed by Damien O'Donnell, what 1999 movie was written by one of the titular characters of "Sammy and Rosie Get Laid"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the movie."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the movie."
    },
    "director": {
      "type": "string",
      "description": "The director of the movie."
    },
    "writer_details": {
      "type": "object",
      "properties": {
        "writer_name": {
          "type": "string",
          "description": "The name of the writer."
        },
        "writer_role_in_other_film": {
          "type": "string",
          "description": "The role the writer played in the specified other film."
        },
        "other_film_title": {
          "type": "string",
          "description": "The title of the other film where the writer had a titular role."
        }
      },
      "required": [
        "writer_name",
        "writer_role_in_other_film",
        "other_film_title"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "movie_title",
    "release_year",
    "director",
    "writer_details"
  ],
  "additionalProperties": false
}
